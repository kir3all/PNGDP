from PIL import Image
from PIL.ExifTags import TAGS
imagename = "testingnew.png"
# read the image data using PIL
image = Image.open(imagename)
exifdata = image.getexif()
# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()

image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)
    
image_without_exif.save(NAME)