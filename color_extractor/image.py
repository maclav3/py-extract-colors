import numpy as np
import webcolors
from PIL import Image as im

_resample_size = (256, 256)


class Image:
    def __init__(self, input):
        self._image = im.open(input)
        # downsample the image first
        self._image.thumbnail(_resample_size)
        _pix = np.array(self._image)
        # flatten the image, we don't care about x,y
        self._pix = _pix.reshape((_pix.shape[0] * _pix.shape[1], 3))

    def histogram(self, partitions=3, nbins=5):
        # counts how many pixels fall in which bin
        bins_count = np.ndarray((partitions, partitions, partitions, 1))
        # maps each pixel to a bin
        pix_to_bin = np.ndarray((self._pix.shape[0], 3), dtype=np.int)
        for i, p in enumerate(self._pix):
            # indices of the bin
            r, g, b = np.floor(p / 256 * partitions)
            r, g, b = int(r), int(g), int(r)
            bins_count[r, g, b] += 1
            pix_to_bin[i] = (r, g, b)

        # check out which bins have the least pixels
        indices = bins_count.flatten().argsort()
        # sort from least to most
        indices = np.flipud(indices)
        # choose at most nbins largest bins
        indices = indices[:nbins]

        # save indices of the bins that have the most pixels
        highest_bins = []
        for i in indices:
            highest_bins.append(np.unravel_index(i, bins_count.shape[:-1]))

        # indices of matching pixels for each of the highest bins
        pixels_by_bin = [np.where((pix_to_bin == bin_index).all(axis=1)) for bin_index in highest_bins]

        # extract the average color of each bin
        colors = []
        for bin in pixels_by_bin:
            pixels = np.take(self._pix, bin, axis=0)
            # skip empty bins
            if not pixels.any():
                continue
            colors.append([int(c) for c in np.average(pixels, axis=1)[0]])

        # convert to #rrggbb
        return tuple([webcolors.rgb_to_hex(color) for color in colors])


if __name__ == '__main__':
    from sys import argv

    img = Image(argv[1])

    print(img.histogram())
