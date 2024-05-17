import warnings
warnings.filterwarnings('ignore')
import webcolors
from colorthief import ColorThief

def color_extract(image):
    colorthif=ColorThief(image)
    colors = colorthif.get_palette(color_count=5)
    return colors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(image):
    requested_colours = color_extract(image)
    closest_name = []
    
    try:
        for requested_colour in requested_colours:
            #closest_name.append(webcolors.rgb_to_name(requested_colour)) 
            closest_name.append(closest_colour(requested_colour))
    except ValueError:
        for requested_colour in requested_colours:
            closest_name.append(closest_colour(requested_colour))
    return closest_name

