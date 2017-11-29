from hashlib import md5

from PIL import Image
from hamcrest import assert_that, equal_to, empty, is_not


def check_metadata(image_file: Image):
    """
    For decreasing image size better to delete unnecessary metadata
    :param image_file: JpegImageFile, WebPImageFile
    """
    exif = image_file._getexif()
    assert_that(exif, equal_to(None), 'EXIF (metadata) must be empty for a smaller image file size')


def check_image_progressive(image_file: Image):
    """
    For Jpeg file better to have progressive image. It is more user friendly because it gives reasonable preview after
    receiving only a portion of the data
    :param image_file: Pil.Image
    """
    profile_progressive = image_file.info.get('progressive', '')
    assert_that(profile_progressive, equal_to(1),
                f"""JPEG should be progressive after saving. Its image_extension is {image_file.format} and 
                profile progressive is {profile_progressive}""")


def check_icc_profile(image_file: Image):
    """
    icc_profile is a set of data that characterizes a color input or output device, or a color space.
    For web sRGB profile is a default profile, also,
    in case when icc_profile are not explicitly set device (monitor) use sRGB
    So, for correct work and decreasing image size need to convert icc_prodile to sRGB and clear this data
    :param image_file: PIL.Image
    """
    color_profile = image_file.info.get('icc_profile', '')
    assert_that(color_profile, empty(), 'Color profile should be empty, it is: {}'.format(color_profile))


def check_image_size(image_file: Image, size: tuple):
    assert_that(image_file.size, equal_to(size))


def check_headers(headers: dict):
    assert_that(headers.get('Content-Length'), is_not(None))
    assert_that(headers.get('Content-Type'), equal_to('image/jpeg'))


def check_image_md5(old_image_data: bytes, new_image_data: bytes):
    old_md5 = md5(old_image_data).hexdigest()
    new_md5 = md5(new_image_data).hexdigest()
    assert_that(old_md5, not equal_to(new_md5))
