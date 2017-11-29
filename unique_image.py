import random
from datetime import datetime

import piexif
from PIL import Image, ImageDraw, ImageFont

from image_helper import transform_image_to_binary


def unique_image_by_metadata(image: Image) -> bytes:
    """
    Only for jpeg images
    Gif image do not have _getexif() method
    For png analogically use
    img.save(output, "PNG", pnginfo=PngImagePlugin.PngInfo())
    :param image:
    :return:
    """
    exif_dict = _get_image_metadata(image)
    # 37510 in ExifIFD is UserComment field
    exif_dict['Exif'][37510] = 'test_string'.encode()
    exif_bytes = piexif.dump(exif_dict)
    binary_data = transform_image_to_binary(image, exif=exif_bytes)
    return binary_data


def _get_image_metadata(image: Image) -> dict:
    image_exif = image.info.get('exif')
    if image_exif is not None:
        return piexif.load(image_exif)
    return {'0th': {}, '1st': {}, 'thumbnail': None, 'Exif': {}, 'Interop': {}, 'GPS': {}}


def unique_image_by_size(image: Image) -> bytes:
    new_sizes = (random.randint(image.height // 2, image.height), random.randint(image.width // 2, image.width))
    image.resize(new_sizes, Image.ANTIALIAS)
    binary_data = transform_image_to_binary(image)
    return binary_data


def unique_image_by_draw(image: Image) -> bytes:
    """
    Set font_path like font_path = '/fonts/calibri.ttf' or use defult
    In case real font you can change size
    font = ImageFont.truetype(font_path, 30)
    :param image:
    :return:
    """
    draw = ImageDraw.Draw(image)
    # Default font is "better than nothing font". It doesn't allow to change font size
    font = ImageFont.load_default()
    time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
    # (150, 150) - left corner to start text
    draw.text((150, 150), time, font=font, fill='red')
    binary_data = transform_image_to_binary(image)
    return binary_data
