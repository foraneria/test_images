import sys
from io import BytesIO
from json import dumps, loads

import requests
from PIL import Image

from logger import logger


def transform_image_from_url_to_image_object(image_link: str) -> (Image.Image, dict):
    """
    This method opens file by url link and returns Image object
    :param image_link: string
    :return: Image.Image
    """
    response = send_request(image_link)
    file = BytesIO(response.content)
    image = Image.open(file)
    return image, dict(response.headers)


def send_request(url: str) -> requests.Response:
    """
    Use requests library and add logging in it
    :type url: string
    :return: requests.Response
    """
    logger.info(f'\nSend request:\n'
                f'Method: GET \n'
                f'URL: {url}:')
    response = requests.request(method='GET', url=url)
    _body = _reduce_response(response.text)
    logger.info(f'\nReceived response:\n'
                f'Status: {response.status_code}\n'
                f'Headers: {dumps(dict(response.headers))}\n'
                f'Body: {_body}\n')
    return response


def _reduce_response(data: str) -> str:
    """
    Reduce response in log in case it is more than 200 kb
    :param text: str
    :return: text
    """
    try:
        data = dumps(loads(data))
    except ValueError:
        pass
    size = sys.getsizeof(data)
    if size > 2 * 10 ** 4:
        start = data[:10 ** 1]
        end = data[-(10 ** 1):]
        data = f'{start}\n...\n<Response was {size} bytes. Log was reduced>\n...\n{end}'
    return data
