import image_checker
from image_helper import transform_image_from_url_to_image_object


def test_image():
    image_url = 'https://id-live-02.slatic.net/p/2/apple-iphone-6-64gb-grey-1489001408-3555482-9891707b8ccac025b674b86ea61870bd-product.jpg'
    image, headers = transform_image_from_url_to_image_object(image_url)
    image_checker.check_metadata(image)
    image_checker.check_icc_profile(image)
    image_checker.check_image_size(image, (340, 340))
    image_checker.check_headers(headers)
