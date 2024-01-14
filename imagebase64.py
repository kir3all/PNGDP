import base64
import io


class ImageBase64():
    def __init__(self, htmldata = None) -> None:
        self.tag = "data:image/png;base64,"
        self.data = b""
        self.rawdata = ""
        if htmldata:
            data_array = htmldata.split(",")
            self.tag = data_array[0] + ","
            self.rawdata = data_array[1]


    def process(self):
        self.data = base64.b64decode(self.rawdata)


    def get(self):
        return io.BytesIO(self.data)
    

    def set(self, data):
        self.data = data


    def gettag(self):
        return self.tag + base64.b64encode(self.data).decode("utf-8")



if __name__ == "__main__":
    from filelib import FileLib
    n = FileLib()
    n.read("1.png")
    data = n.get().getvalue()
    n64 = ImageBase64()
    n64.set(data)
    tmp_tag = n64.gettag()
    print(tmp_tag[:50] + "..." + tmp_tag[-5:])

    img_tag = "data:image/png;base64,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"
    m = ImageBase64(img_tag)
    m.process()
    assert m.gettag() == img_tag, "images differs!"
    nf = FileLib()
    nf.set(m.get().getvalue())
    nf.save("from_b64.png")



