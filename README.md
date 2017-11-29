# test_images repository #
## Set of images for testing ##

In test_data you found images which were separated into 3 groups:
* in positive image folder: 
```
- different formats (jpg, gif, png), 
- different color profiles (RGB, CMYK and etc),
- different proportions (square, horizontal, vertical)
```
All these images should be successful for uploading 

* special image folder:
```
- webp format
- files without an extension in the name
- files with the wrong extension in the name
- large files (more than 1000 pixels on one side)
- png with the transparent layer
```
This cases should be also successful in image uploading but may contain difficulties for image service 

* negative image folder:
```bazaar
- wrong format
- empty files
```
All these images are not images actually and it uploading should return error code

## Checker ##
In file image_checker you can find checks for image:
- size
- icc_profile
- progressive for jpeg
- meta data checks

This checks use Pillow library for get image data

## To run test ## 
Test uses pytest framework

### For the first run ###
- use python 3.6.x
- if you use virtualenv, activate it
- install requirements 
```
pip install -r requirements.txt 
```
### run test ### 
- activate virtualenv and call from terminal
```
source venv/bin/activate
py.test test.py 
```
or use PyCarm to run test 