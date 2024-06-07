#!/usr/bin/env python
# ---- Imports ----
import argparse
from PIL import Image
from math import sqrt

from color import colors
from rendered import render
# -----------------

# ---- Main ----
def main():
    # ---- Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('image', type=str, help='Image to color')
    parser.add_argument('nb_cases', type=int, help='Number of cases to colorize the image')
    parser.add_argument('nb_colors', type=int, help='Number of colors to use')

    args = parser.parse_args()

    # ---- Load image
    path = args.image
    image_name = path.split('/')[-1]
    # Check if the number of cases is a square
    nb_cases = args.nb_cases
    if sqrt(nb_cases).is_integer() == False:
        print('The number of cases must be a square')
        return
    
    # Check if the number of colors is less than the square root of the number of cases
    nb_colors = args.nb_colors
    if nb_colors > nb_cases:
        print('The number of colors must be less than the number of cases')
        return

    # Try to open the image
    try:
        image = Image.open(path)
    except FileNotFoundError:
        print('Image not found')
        return

    # ---- Main
    color_list, tab_colors_in_image = colors(image, nb_cases, nb_colors)
    if render(image, nb_cases, color_list, tab_colors_in_image, image_name) != 1:
        print('Error during rendering')
        return

if __name__ == '__main__':
    main()