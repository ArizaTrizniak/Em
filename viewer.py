import sys
from pyembroidery import convert
from PIL import Image


def display_pes_file(pes_file_path):
    convert(pes_file_path, "tmp.png")
    image = Image.open("tmp.png")
    image.show()


def main():
    filename = sys.argv[1]
    display_pes_file(filename)


main()
