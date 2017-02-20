import numpy as np
from img_functions import save_single_img, get_zoomed_image, append_channels


def decompose(image_matrix):
    """
    # Get decomposed matrices, USVtranspose
    """
    U, S, V = np.linalg.svd(image_matrix, full_matrices=True)
    reshaped_u = reshape_matrix(U)
    return reshaped_u, S, V


def reshape_matrix(matrix):
    """
    # Transpose of sorts, was needed because of the way arrays are stored
    # Different than MATLAB
    """
    reshaped_matrix = []
    for i in range(0, len(matrix[0])):
        vector = matrix[:,i]
        reshaped_matrix.append(vector)
    reshaped_matrix = np.array(reshaped_matrix)
    return reshaped_matrix


def vector_vector_transpose_multiplication(vector1, vector2):
    """
    # Generates matrix
    """
    result_matrix = []
    for item in vector1:
        single_vector = item * vector2
        single_vector = np.array(single_vector)
        result_matrix.append(single_vector)
    result_matrix = np.array(result_matrix)
    return result_matrix


def decomposed_matrix_multiplication(vector1, scalar, vector2):
    """
    # Generates a single matrix from vector vector transpose and scalar multiplication
    """
    matrix = vector_vector_transpose_multiplication(vector1, vector2)
    matrix = scalar * matrix
    return matrix


def generate_decomposed_matrices(U,S,V):
    """
    # Generates all sub decomposition matrices from a SVD
    """
    decomposed_matrices = []
    for i in range(0,len(S)):
        single_matrix = decomposed_matrix_multiplication(U[i], S[i], V[i])
        decomposed_matrices.append(single_matrix)
    return decomposed_matrices


def save_sample_grayscale_decomposition(folder_name, decomposed_list, first_n_decompositions):
    """
    # Saves a sample decomposition for grayscale images
    """
    image_height = decomposed_list[0].shape[0]
    image_width = decomposed_list[0].shape[1]
    summed_image = np.zeros((image_height, image_width))
    for index,item in enumerate(decomposed_list[:first_n_decompositions:]):  # First n decompositions
        image = get_zoomed_image(item, 100)  # No zoom
        save_single_img(folder_name, str(index), image)
        summed_image = summed_image + item
    summed_image = get_zoomed_image(summed_image, 100)  # No zoom
    save_single_img(folder_name, 'summed_image', summed_image)


def save_sample_rgb_decomposition(folder_name, red_decomposed_list, green_decomposed_list,
                                  blue_decomposed_list, first_n_decompositions):
    """
    # Saves a sample for rgb images
    """
    image_height = red_decomposed_list[0].shape[0]
    image_width = red_decomposed_list[0].shape[1]
    summed_image = np.zeros((3, image_height, image_width))
    for index,item in enumerate(red_decomposed_list[:first_n_decompositions:]):  # First n decompositions
        reconstructed_image = append_channels(red_decomposed_list[index], green_decomposed_list[index], blue_decomposed_list[index])
        image = get_zoomed_image(reconstructed_image, 100)  # No zoom
        save_single_img(folder_name, str(index), image)
        summed_image = summed_image + reconstructed_image
    summed_image = get_zoomed_image(summed_image, 100)  # No zoom
    save_single_img(folder_name, 'summed_image', summed_image)
