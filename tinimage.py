"""Main module."""

import numpy
import sys
from PIL import Image


def make_magic_image(input_image, output_image):
    """
    Create magic image with input_image in output_image.

    :param input_image:  name of trasformable image in working directory
    :param output_image: name for output image
    """
    pattern_div = 8

    try:
        depth_map = Image.open(input_image).convert("RGB")
        depth_data = depth_map.load()
    except FileNotFoundError:
        print('No such file or directory: ' + input_image)
        return

    out_img = Image.new("L", depth_map.size)
    out_data = out_img.load()

    pattern_width = int(depth_map.size[0] / pattern_div)
    pattern = numpy.random.randint(0, 256, (pattern_width, depth_map.size[1]))

    for x in range(depth_map.size[0]):
        for y in range(depth_map.size[1]):

            if x < pattern_width:
                out_data[x, y] = int(pattern[x, y])
            else:
                shift = int(depth_data[x, y][0] / pattern_div)
                out_data[x, y] = out_data[x - pattern_width + shift, y]

    out_img.save(output_image)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("You must indicate image for transormation.")
        print("Use one of the next command:")
        print("python3 tinimage.py image_for_transform.png")
        print("python3 tinimage.py image_for_transform.png output_image.png")
        exit()
    elif len(sys.argv) == 2:
        input_image = sys.argv[1]
        output_image = 'out.png'
    elif len(sys.argv) == 3:
        input_image = sys.argv[1]
        output_image = sys.argv[2]
    else:
        print("Too much arguments!")
        exit()
    make_magic_image(input_image, output_image)
