from PIL import Image
from math import sqrt, inf
import numpy as np
from sklearn.cluster import KMeans

# Calculate the closest color to a given color
# Input:
# - color: color to compare
# - tab_colors: list of colors to compare
# Output:
# - closest: closest color
# - index_min: index of the closest color in the list
def closest_color(color, tab_colors):
    min_distance = inf
    index_min = 0
    for i in range(len(tab_colors)):
        distance = 0
        for j in range(3):
            distance += (color[j] - tab_colors[i][j])**2
        if distance < min_distance:
            min_distance = distance
            index_min = i
            closest = tab_colors[i]
    return closest, index_min

# Calculate the predominant color of an image
# Input:
# - image: image to analyze
# - nb_colors: number of colors to find
# Output:
# - kmeans.cluster_centers_: table of predominant colors
def predominant_color(image, nb_colors):
    image_np = np.array(image)
    pixels_np = image_np.reshape(-1, 3)
    kmeans = KMeans(n_clusters = nb_colors)
    kmeans.fit(pixels_np)
    return kmeans.cluster_centers_

# Return the list of colors used and the list of colors in the image
# Input:
# - image: image to color
# - nb_cases: number of cases to colorize the image
# - nb_colors: number of colors to use
# Output:
# - color_list: list of colors used
# - tab_colors_in_image: list of colors in the image
def colors(image, nb_cases, nb_colors):

    pixels = image.load()
    width, height = image.size
    columns = int(sqrt(nb_cases))
    rows = int(sqrt(nb_cases))

    tab_averages = [[0, 0, 0] for i in range(columns * rows)]

    # ---- Calculate the average color of each case
    for i in range(0, rows):
        for j in range(0, columns):
            average = [0, 0, 0]

            # ---- Calculate the average color of the case
            for x in range(i * int(height/rows), (i + 1) * int(height/rows)):
                for y in range(j * int(width/columns), (j + 1) * int(width/columns)):
                    if x >= width or y >= height:
                        break
                    average[0] += pixels[x, y][0]
                    average[1] += pixels[x, y][1]
                    average[2] += pixels[x, y][2]

            average[0] = int(average[0] / (width/columns) / (height/rows))
            average[1] = int(average[1] / (width/columns) / (height/rows))
            average[2] = int(average[2] / (width/columns) / (height/rows))
            tab_averages[i * columns + j] = average

    color_list = []
    tab_colors_in_image = [0 for i in range(columns * rows)]

    predominant_colors = predominant_color(image, nb_colors)

    # calculate the distance between the average color of each case and the dominant colors
    for k in range(nb_colors):
        color_list.append(closest_color(predominant_colors[k], tab_averages)[0])

    for i in range(0, rows):
        for j in range(0, columns):
            color, index = closest_color(tab_averages[i * columns + j], color_list)
            tab_colors_in_image[j * columns + i] = index
    
    return color_list, tab_colors_in_image