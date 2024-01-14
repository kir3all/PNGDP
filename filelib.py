from pathlib import Path
import io, random

class FileLib():
    def __init__(self):
        # self.descr = None
        self.filename = None
        self.data = None


    def read(self, filepath):
        if filepath is None:
            raise Exception('Bad arguments')
        mypath = Path(filepath)
        if (mypath.exists() and mypath.is_file()) == False:
            raise Exception('Not a file')
        self.filename = mypath.name
        self.data = mypath.read_bytes()


    def save(self, filename = None):
        if filename is not None:
            new_name = Path(filename)
        else:
            while True:
                suffix = "-" + random.randbytes(2).hex()
                tmp_name = Path(self.filename)
                new_name = Path(tmp_name.stem + suffix + tmp_name.suffix)
                if not new_name.exists():
                    break
        new_name.write_bytes(self.data)


    def set(self, data):
        self.data = data


    def get(self):
        return io.BytesIO(self.data)


if __name__ == "__main__":
    n = FileLib()
    n.read("1.png")
    print(len(n.get().getvalue()))
    n.save()