import scipy.misc
from svd import (decompose,
                 generate_decomposed_matrices,
                 save_sample_grayscale_decomposition,
                 save_sample_rgb_decomposition)
from img_functions import get_image_channels


GRAYSCALE_CAT = '../data/grayscale_cat.jpg'
RGB_DOG = '../data/rgb_dog.jpg'


if __name__ == "__main__":
    # Read images
    grayscale_cat_as_matrix = scipy.misc.imread(GRAYSCALE_CAT)
    rgb_dog_as_matrix = scipy.misc.imread(RGB_DOG)
    dog_red_channel, dog_green_channel, dog_blue_channel = get_image_channels(rgb_dog_as_matrix)

    # SVD - Decomposed images
    # An example decomposition - Grayscale cat - single channel
    U,S,V = decompose(grayscale_cat_as_matrix)  # Get the decomposition
    decomposed_list = generate_decomposed_matrices(U, S, V)  # Decomposed list,
    save_sample_grayscale_decomposition('grayscale_cat', decomposed_list, 15)
    # Saves sample results of this grayscale decomposition
    # 15 is the amount of decompositions, play with this number
    # to change amount of decomposed matrices

    # An example decomposition - RGB Dog - decompose on separated channels
    U_red, S_red, V_red = decompose(dog_red_channel)  # Get red decomposition
    U_green, S_green, V_green = decompose(dog_green_channel)  # Get green decomposition
    U_blue, S_blue, V_blue = decompose(dog_blue_channel)  # Get blue decomposition
    # Generate decomposed matrices
    red_decomposed_list = generate_decomposed_matrices(U_red, S_red, V_red)
    green_decomposed_list = generate_decomposed_matrices(U_green, S_green, V_green)
    blue_decomposed_list = generate_decomposed_matrices(U_blue, S_blue, V_blue)
    # Save sample results
    save_sample_rgb_decomposition('rgb_dog', red_decomposed_list, green_decomposed_list, blue_decomposed_list, 30)
    # Saves sample results of this rgb decomposition
    # 30 is the amount of decompositions, play with this number
    # to change amount of decomposed matrices
