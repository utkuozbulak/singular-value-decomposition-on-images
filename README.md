# Singular Value Decomposition on Images

I was curious about singular value decompositions and its effects on images and decided to start this tiny side project. I decomposed a grayscale image (**cat!**) and an rgb image (**dog!**) in Python and re-composed the images from their decomposed matrices part by part(matrix by matrix). Below are results of this experiment.

## Code

The code to recreate the decompositions/re-compositions are in the src folder. I only ended up using numpy and scipy packages for this project.

## Data

Two images are in /data/ folder. Sample outputs of summed up decompositions are in /data/sample_decomposition_results/. 

**Grayscale Cat**

![cat](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/grayscale_cat.jpg "Grayscale_cat")

**RGB Dog**

![dog](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/rgb_dog.jpg "RGB_dog")

## Singular Value Decomposition Explanation


If we say the result of a singular value decomposition is `U, S, V = svd(some_matrix)` then the resulting values U, S and V are matrices. 

The matrix U is composed of eigenvectors of the matrix `A* *transpose*(A)`

The matrix V is composed of eigenvectors of the matrix `*transpose*(A) *A`

The matrix S is composed of eigenvalus of those matrices. ( ps. eigenvalues of `A* *transpose*(A)` and `*transpose*(A) *A` are the same )

If we do the multiplication U\*S\*V we get the intial matrix (the image). Now let's look at from a different way, the matrices U and V are composed of vectors and S is composed of eigenvalues of those vectors. Let's assume we have `N` many eigenvalues/vectors. If we multiply them individually and sum them all up, that is also equal to image itself, instead of doing matrix multiplication we are just doing scalar(s)-vector(u)-vector transpose(v) multiplication and result is also a matrix.

How will those matrices(images) look like ? 

What happens if we sum up some of those matrices (sub-images) but not all ?

## Results

### Grayscale Cat
For grayscale cat there are 400 decomposed matrices, below are some of the examples of decomposed matrices.

**Grayscale Cat, Decomposed Matrix 0**

![Grayscale_cat_decomposed_matrix_0](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/cat_0.png "Grayscale_cat_decomposed_matrix_0")


**Grayscale Cat, Decomposed Matrix 1**

![Grayscale_cat_decomposed_matrix_1](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/cat_1.png "Grayscale_cat_decomposed_matrix_1")


**Grayscale Cat, Decomposed Matrix 2**

![Grayscale_cat_decomposed_matrix_2](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/cat_2.png "Grayscale_cat_decomposed_matrix_2")

...and 397 more like this, now if we sum those matrices

**Grayscale Cat, top 5 Decomposed Matrices summed**

![cat_top_5](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/cat_top5_decomposed_matrices.png "cat_top_5")

**Grayscale Cat, top 10 Decomposed Matrices summed**

![cat_top_10](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/cat_top10_decomposed_matrices.png "cat_top_10")

**Grayscale Cat, top 20 Decomposed Matrices summed**

![cat_top_20](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/cat_top20_decomposed_matrices.png "cat_top_20")

**Grayscale Cat, top 100 Decomposed Matrices summed**

![cat_top_100](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/cat_top100_decomposed_matrices.png "cat_top_100")

**Grayscale Cat Original Image**

![cat](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/grayscale_cat.jpg "Grayscale_cat")

### RGB Dog
For grayscale cat there are 399 decomposed matrices, below are some of the examples of decomposed matrices.

**RGB Dog, Decomposed Matrix 0**

![RGB_dog_decomposed_matrix_0](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/dog_0.png "RGB_dog_decomposed_matrix_0")


**RGB Dog, Decomposed Matrix 1**

![RGB_dog_decomposed_matrix_1](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/dog_1.png "RGB_dog_decomposed_matrix_1")


**RGB Dog, Decomposed Matrix 2**

![RGB_dog_decomposed_matrix_2](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/dog_2.png "RGB_dog_decomposed_matrix_2")

...and 396 more like this, now if we sum those matrices

**RGB Dog, top 5 Decomposed Matrices summed**

![dog_top_5](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/dog_top5_decompositions.png "dog_top_5")

**RGB Dog, top 10 Decomposed Matrices summed**

![dog_top_10](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/dog_top10_decompositions.png "dog_top_10")

**RGB Dog, top 20 Decomposed Matrices summed**

![dog_top_20](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/dog_top20_decompositions.png "dog_top_20")

**RGB Dog, top 100 Decomposed Matrices summed**

![dog_top_100](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/sample_decomposition_results/dog_top100_decompositions.png "dog_top_100")

**RGB Dog Original Image**

![dog](https://raw.githubusercontent.com/utkuozbulak/singular-value-decomposition-on-images/master/data/rgb_dog.jpg "RGB_dog")

