from exif import Image
from checker import Checker

class ExifDeleter(Checker):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.image = None

    
    def check(self):
        self.image = Image(self.data)
        if self.image.has_exif:
            print(dir(self.image))
            self.delete_exif()
        else:
            print('No EXIF')

    def delete_exif(self):
        self.image.delete_all()
        self.result = self.image.get_file()


if __name__ == "__main__":
    from filelib import FileLib
    n = FileLib()
    n.read("Canon_40D.jpg")
    data = n.get()
    p = ExifDeleter(data)
    p.check()
    n.set(p.get())
    n.save()