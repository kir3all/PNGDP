import io
from checker import Checker
import colour
from colour_demosaicing import (
    ROOT_RESOURCES_EXAMPLES,
    demosaicing_CFA_Bayer_bilinear,
    demosaicing_CFA_Bayer_Malvar2004,
    demosaicing_CFA_Bayer_Menon2007,
    mosaicing_CFA_Bayer)
from PIL import Image
import numpy as np

class CfaFilter(Checker):
    def __init__(self, data) -> None:
        super().__init__(data)
    

    def check(self):
        my_image = Image.open(self.data).convert('RGB')
        CFA = mosaicing_CFA_Bayer(my_image)
        # colour.plotting.plot_image(
        #     CFA,
        #     text_kwargs={'text': 'Lighthouse - CFA - RGGB'})
        my_result = colour.cctf_encoding(demosaicing_CFA_Bayer_bilinear(CFA))
        # colour.plotting.plot_image(
        #     my_result,
        #     text_kwargs={'text': 'Lighthouse - R914108 - Kodak'})
        img_byte_arr = io.BytesIO()
        Image.fromarray(my_result, mode="RGB").save(img_byte_arr, format='PNG')
        self.result = img_byte_arr.getvalue()
        



if __name__ == "__main__":
    from filelib import FileLib
    n = FileLib()
    n.read("1.png")
    data = n.get()
    p = CfaFilter(data)
    p.check()
    n.set(p.get())
    n.save()