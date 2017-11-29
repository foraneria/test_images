import image_checker
from image_helper import transform_image_from_url_to_image_object, transform_image_to_binary
from unique_image import unique_image_by_metadata, unique_image_by_size, unique_image_by_draw

image_url = 'https://id-live-02.slatic.net/p/2/apple-iphone-6-64gb-grey-1489001408-3555482-9891707b8ccac025b674b86ea61870bd-product.jpg'


def test_image_properties():
    image, headers = transform_image_from_url_to_image_object(image_url)
    image_checker.check_metadata(image)
    image_checker.check_icc_profile(image)
    image_checker.check_image_size(image, (340, 340))
    image_checker.check_headers(headers)


def test_image_unique_meta_jpg():
    image, _ = transform_image_from_url_to_image_object(image_url)
    binary_data = transform_image_to_binary(image)
    transformed_binary_data = unique_image_by_metadata(image)
    image_checker.check_image_md5(binary_data, transformed_binary_data)


def test_image_unique_size():
    image, _ = transform_image_from_url_to_image_object(image_url)
    binary_data = transform_image_to_binary(image)
    transformed_binary_data = unique_image_by_size(image)
    image_checker.check_image_md5(binary_data, transformed_binary_data)


def test_image_unique_draw_timestamp():
    image, _ = transform_image_from_url_to_image_object(image_url)
    binary_data = transform_image_to_binary(image)
    transformed_binary_data = unique_image_by_draw(image)
    image_checker.check_image_md5(binary_data, transformed_binary_data)
