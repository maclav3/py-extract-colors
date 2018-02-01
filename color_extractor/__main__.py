import argparse

import sys

from color_extractor.image import Image


def main():
    parser = argparse.ArgumentParser(
        description='An util to extract main colors from an image'
    )

    parser.add_argument('image', type=argparse.FileType('r'), help='''The input file''')
    args = parser.parse_args()

    im = Image(args.image)
    sys.stdout.write(im.main_colors())


main()
