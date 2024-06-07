from PIL import Image
from math import sqrt

# Render the image with the colors
# Input:
# - image: image to color
# - nb_cases: number of cases to colorize the image
# - color_list: list of colors used
# - tab_colors_in_image: list of colors in the image
# - image_name: name of the image
# Output:
# - 1 if the image has been saved
# - 0 if the image has not been saved
def render(image, nb_cases, color_list, tab_colors_in_image, image_name):
    # ---- Load image
    try:
        if isinstance(image, str):
            image = Image.open(image)
    except FileNotFoundError:
        print('Image not found')
        return 0
    
    pixels = image.load()
    width, height = image.size
    columns = int(sqrt(nb_cases))
    rows = int(sqrt(nb_cases))

    # ---- Calculate the average color of each case and color the case with the average color
    for i in range(0, rows):
        for j in range(0, columns):
            color = color_list[tab_colors_in_image[int(j * columns + i)]]
            for x in range(i * int(width/rows), (i + 1) * int(width/rows)):
                for y in range(j * int(height/columns), (j + 1) * int(height/columns)):
                    if x >= width or y >= height:
                        break
                    pixels[x, y] = (color[0], color[1], color[2])

    # ---- Save the image
    image.save('colorized_' + image_name)
    return 1