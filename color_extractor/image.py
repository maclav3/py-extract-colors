from typing import Tuple

import numpy as np
from PIL import Image as im


class Image:
    def __init__(self, input):
        self._image = im.open(input)
        self._pix = np.array(self._image)

    def main_colors(self) -> Tuple[str]:
        return ('#000000',)
