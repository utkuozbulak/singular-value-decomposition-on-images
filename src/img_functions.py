import os
import numpy as np
from scipy.misc import toimage, imresize


DECOMPOSITION_OUTPUT_DIR = '../data/decomposition/'


def display_img(data):
    i = toimage(data[1])
    i.show()


def get_zoomed_image(image_as_list ,zoom_ratio):
    resized_list = imresize(image_as_list, zoom_ratio)
    resized_img = toimage(resized_list)
    return resized_img


def save_single_img(folder_name, file_name, img):
    file_path = DECOMPOSITION_OUTPUT_DIR + folder_name + '//'
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    img.save(file_path + '/' + file_name + '.png')


def get_image_channels(image_as_list):
    red_channel = image_as_list[:,:,0]
    green_channel = image_as_list[:,:,1]
    blue_channel = image_as_list[:,:,2]
    return (red_channel, green_channel, blue_channel)


def append_channels(red_channel, green_channel, blue_channel):
    image = []
    image.append(red_channel)
    image.append(green_channel)
    image.append(blue_channel)
    rgb_image = np.array(image)
    return rgb_image
