from PIL import Image
from PIL.ExifTags import TAGS

filename = "testing.png"
newfilename = filename[:-4] + "new.png"
exifdata = filename.getexif()

for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()

with Image.open(filename) as img:
    if img != None:
        img.save(newfilename)
    else:
        image_without_exif = Image.new(filename.mode, filename.size)
        image_without_exif.putdata(data)
        image_without_exif.save(newfilename)

        width, height = filename.size
        newfilename = filename.resize(width + 1, height + 1)
        newfilename = image_without_exif
                                      