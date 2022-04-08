
import cv2
import numpy as np
import matplotlib.pyplot as plt
#import constant
import math
import datetime

#Section 2: Image Processing in OpenCV
#Image Processing Techniques
#First: Splitting and merging channels in OpenCV
# cv2.split() and cv2.merge() 
'''
def show_with_matplotlib(color_img, title, pos):
    img_RGB = color_img[:, :, ::-1]
    ax = plt.subplot(3, 6, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')
image = cv2.imread('color_spaces.png')
# create a figure() object with appropriate size and title:
plt.figure(figsize=(13, 5))
plt.suptitle("Splitting and merging channels in OpenCV", fontsize=18, fontweight='bold')
# Show the BGR image:
show_with_matplotlib(image, "BGR - image", 1)
# Split the image into its three components (blue, green and red):
(b, g, r) = cv2.split(image)
# Show all the channels from the BGR image:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR - (B)", 2)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR - (G)", 2 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR - (R)", 2 + 6 * 2)

# Merge the three channels again to build a BGR image:
image_copy = cv2.merge((b, g, r))

# Show the BGR image:
show_with_matplotlib(image_copy, "BGR - image (copy)", 1 + 6)

# You should remember that cv2.split() is a time consuming operation
# Therefore, you should only use it if it is strictly necessary
# Otherwise, you can use numpy functionality to work with specific channels
# Another way of getting one component (in this case, the blue one)
# is using numpy idexing:
b_copy = image[:, :, 0]

# We make a copy of the loaded image:
image_without_blue = image.copy()

# From the BGR image, we "eliminate" (set to 0) the blue component (channel 0):
image_without_blue[:, :, 0] = 0

# From the BGR image, we "eliminate" (set to 0) the green component (channel 1):
image_without_green = image.copy()
image_without_green[:, :, 1] = 0

# From the BGR image, we "eliminate" (set to 0) the red component (channel 2):
image_without_red = image.copy()
image_without_red[:, :, 2] = 0

# Show all the channels from the BGR image:
show_with_matplotlib(image_without_blue, "BGR without B", 3)
show_with_matplotlib(image_without_green, "BGR without G", 3 + 6)
show_with_matplotlib(image_without_red, "BGR without R", 3 + 6 * 2)

# Split the 'image_without_blue' image into its three components (blue, green and red):
(b, g, r) = cv2.split(image_without_blue)

# Show all the channels from the BGR image without the blue information:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR without B (B)", 4)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR without B (G)", 4 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR without B (R)", 4 + 6 * 2)

# Split the 'image_without_green' image into its three components (blue, green and red):
(b, g, r) = cv2.split(image_without_green)

# Show all the channels from the BGR image without the green information:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR without G (B)", 5)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR without G (G)", 5 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR without G (R)", 5 + 6 * 2)

# Split the 'image_without_red' image into its three components (blue, green and red):
(b, g, r) = cv2.split(image_without_red)

# Show all the channels from the BGR image without the red information:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR without R (B)", 6)
show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR without R (G)", 6 + 6)
show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR without R (R)", 6 + 6 * 2)

# Show the created image:
plt.show()
'''
#Second
#Geometric transformations of images

def show_with_matplotlib(img, title):
    img_RGB = img[:, :, ::-1]
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
image = cv2.imread('lena_image.png')
show_with_matplotlib(image, 'Original image')
# 1. Scaling or resizing
# Resize the input image using cv2.resize()
# Resize using the scaling factor for each dimension of the image
# In this case the scaling factor is 0.5 in every dimension
''''''The five interpolation methods provided with OpenCV are 
1)cv2.INTER_NEAREST (nearest neighbor interpolation)
2)cv2.INTER_LINEAR (bilinear interpolation)
3)cv2.INTER_AREA (resampling using pixel area relation)
4)cv2.INTER_CUBIC (bicubic interpolation)
5)cv2.INTER_LANCZOS4 (sinusoidal interpolation)''''''
dst_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# Get the height and width of the image:
height, width = image.shape[:2]
# You can resize also the image specifying the new size:
dst_image_2 = cv2.resize(image, (width * 2, height * 2), interpolation=cv2.INTER_LINEAR)
# We see the two resized images:
show_with_matplotlib(dst_image, 'Resized image')
show_with_matplotlib(dst_image_2, 'Resized image 2')
#2)Translating an image
#In order to translate an object, you need to create the 2 x 3 transformation matrix
#by using the NumPy array with float values providing the translation in both the
#x and y directions in pixels, as shown in the following code:
M = np.float32([[1, 0, 200], [0, 1, 30]])
# Once this transformation Matrix is created, we can pass it to the function cv2.warpAffine():
dst_image = cv2.warpAffine(image, M, (width, height))
show_with_matplotlib(dst_image, 'Translated image (positive values)')
#Note that the translation can be also negative, as shown in the following code:
M = np.float32([[1, 0, -200], [0, 1, -30]])
dst_image = cv2.warpAffine(image, M, (width, height))
show_with_matplotlib(dst_image, 'Translated image (negative values)')
#3. Rotation
# To rotate the image we make use of the function  cv.getRotationMatrix2D() to build the 2x3 rotation matrix:
# In this case, we are going to rotate the image 180 degrees (upside down):
M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 180, 1)
dst_image = cv2.warpAffine(image, M, (width, height))

# Show the center of rotation and the rotated image:
cv2.circle(dst_image, (round(width / 2.0), round(height / 2.0)), 5, (255, 0, 0), -1)
show_with_matplotlib(dst_image, 'Image rotated 180 degrees')

# Now, we are going to rotate the image 30 degrees changing the center of rotation
M = cv2.getRotationMatrix2D((width / 1.5, height / 1.5), 30, 1)
dst_image = cv2.warpAffine(image, M, (width, height))

# Show the center of rotation and the rotated image:
cv2.circle(dst_image, (round(width / 1.5), round(height / 1.5)), 5, (255, 0, 0), -1)
show_with_matplotlib(dst_image, 'Image rotated 30 degrees')

# 4. Affine Transformation
# In an affine transformation we first make use of the function cv2.getAffineTransform()
# to build the 2x3 transformation matrix, which is obtained from the relation between three points
# from the input image and their corresponding coordinates in the transformed image.

# A copy of the image is created to show the points that will be used for the affine transformation:
image_points = image.copy()
cv2.circle(image_points, (135, 45), 5, (255, 0, 255), -1)
cv2.circle(image_points, (385, 45), 5, (255, 0, 255), -1)
cv2.circle(image_points, (135, 230), 5, (255, 0, 255), -1)

# Show the image with the three created points:
show_with_matplotlib(image_points, 'before affine transformation')

# We create the arrays with the aforementioned three points and the desired positions in the output image:
pts_1 = np.float32([[135, 45], [385, 45], [135, 230]])
pts_2 = np.float32([[135, 45], [385, 45], [150, 230]])

# We get the 2x3 tranformation matrix based on pts_1 and pts_2 and apply cv2.warpAffine():
M = cv2.getAffineTransform(pts_1, pts_2)
dst_image = cv2.warpAffine(image_points, M, (width, height))

# Show the image:
show_with_matplotlib(dst_image, 'Affine transformation')

# 5. Perspective transformation
# A copy of the image is created to show the points that will be used for the perspective transformation:
image_points = image.copy()
cv2.circle(image_points, (450, 65), 5, (255, 0, 255), -1)
cv2.circle(image_points, (517, 65), 5, (255, 0, 255), -1)
cv2.circle(image_points, (431, 164), 5, (255, 0, 255), -1)
cv2.circle(image_points, (552, 164), 5, (255, 0, 255), -1)

# Show the image:
show_with_matplotlib(image_points, 'before perspective transformation')

# cv2.getPerspectiveTransform() needs four pairs of points
# (coordinates of a quadrangle in both the source and output image)
# We create the arrays for these four pairs of points:
pts_1 = np.float32([[450, 65], [517, 65], [431, 164], [552, 164]])
pts_2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# To correct the perspective (also known as perspective transformation) you need to create the transformation matrix
# making use of the function cv2.getPerspectiveTransform(), where a 3x3 matrix is constructed:
M = cv2.getPerspectiveTransform(pts_1, pts_2)

# Then, apply cv2.warpPerspective(), where the source image is transformed applying
# the specified matrix and with a specified size:
dst_image = cv2.warpPerspective(image, M, (300, 300))

# Show the image:
show_with_matplotlib(dst_image, 'perspective transformation')
# 6. Cropping
# A copy of the image is created to show the points that will be used for the cropping example:
image_points = image.copy()

# Show the points and lines connecting the points:
cv2.circle(image_points, (230, 80), 5, (0, 0, 255), -1)
cv2.circle(image_points, (330, 80), 5, (0, 0, 255), -1)
cv2.circle(image_points, (230, 200), 5, (0, 0, 255), -1)
cv2.circle(image_points, (330, 200), 5, (0, 0, 255), -1)
cv2.line(image_points, (230, 80), (330, 80), (0, 0, 0))
cv2.line(image_points, (230, 200), (330, 200), (0, 0, 0))
cv2.line(image_points, (230, 80), (230, 200), (0, 0, 255))
cv2.line(image_points, (330, 200), (330, 80), (0, 0, 255))

# Show the image with the points and lines:
show_with_matplotlib(image_points, 'Before cropping')

# For cropping, we make use of numpy slicing:
dst_image = image[80:200, 230:330]

# Show the image:
show_with_matplotlib(dst_image, 'Cropping image')
#Comparing different kernels using cv2.filter2D()
def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(3, 4, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


# Create the dimensions of the figure and set title:
plt.figure(figsize=(12, 6))
plt.suptitle("Comparing different kernels using cv2.filter2D()", fontsize=14, fontweight='bold')

# Load the original image:
image = cv2.imread('cat-face.png')

# We try different kernels
# Identify kernel (does not modify the image)
kernel_identity = np.array([[0, 0, 0],
                            [0, 1, 0],
                            [0, 0, 0]])

# Try different kernels for edge detection:
kernel_edge_detection_1 = np.array([[1, 0, -1],
                                    [0, 0, 0],
                                    [-1, 0, 1]])

kernel_edge_detection_2 = np.array([[0, 1, 0],
                                    [1, -4, 1],
                                    [0, 1, 0]])

kernel_edge_detection_3 = np.array([[-1, -1, -1],
                                    [-1, 8, -1],
                                    [-1, -1, -1]])

# Try different kernels for sharpening:
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

kernel_unsharp_masking = -1 / 256 * np.array([[1, 4, 6, 4, 1],
                                              [4, 16, 24, 16, 4],
                                              [6, 24, -476, 24, 6],
                                              [4, 16, 24, 16, 4],
                                              [1, 4, 6, 4, 1]])

# Try different kernels for smoothing:
kernel_blur = 1 / 9 * np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])

gaussian_blur = 1 / 16 * np.array([[1, 2, 1],
                                   [2, 4, 2],
                                   [1, 2, 1]])

# Try a kernel for embossing:
kernel_emboss = np.array([[-2, -1, 0],
                          [-1, 1, 1],
                          [0, 1, 2]])

# Try different kernels for edge detection:
sobel_x_kernel = np.array([[1, 0, -1],
                           [2, 0, -2],
                           [1, 0, -1]])

sobel_y_kernel = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]])

outline_kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])

# Apply all the kernels:
original_image = cv2.filter2D(image, -1, kernel_identity)
edge_image_1 = cv2.filter2D(image, -1, kernel_edge_detection_1)
edge_image_2 = cv2.filter2D(image, -1, kernel_edge_detection_2)
edge_image_3 = cv2.filter2D(image, -1, kernel_edge_detection_3)
sharpen_image = cv2.filter2D(image, -1, kernel_sharpen)
unsharp_masking_image = cv2.filter2D(image, -1, kernel_unsharp_masking)
blur_image = cv2.filter2D(image, -1, kernel_blur)
gaussian_blur_image = cv2.filter2D(image, -1, gaussian_blur)
emboss_image = cv2.filter2D(image, -1, kernel_emboss)
sobel_x_image = cv2.filter2D(image, -1, sobel_x_kernel)
sobel_y_image = cv2.filter2D(image, -1, sobel_y_kernel)
outline_image = cv2.filter2D(image, -1, outline_kernel)

# Show all the images:
show_with_matplotlib(original_image, "identity kernel", 1)
show_with_matplotlib(edge_image_1, "edge detection 1", 2)
show_with_matplotlib(edge_image_2, "edge detection 2", 3)
show_with_matplotlib(edge_image_3, "edge detection 3", 4)
show_with_matplotlib(sharpen_image, "sharpen", 5)
show_with_matplotlib(unsharp_masking_image, "unsharp masking", 6)
show_with_matplotlib(blur_image, "blur image", 7)
show_with_matplotlib(gaussian_blur_image, "gaussian blur image", 8)
show_with_matplotlib(emboss_image, "emboss image", 9)
show_with_matplotlib(sobel_x_image, "sobel x image", 10)
show_with_matplotlib(sobel_y_image, "sobel y image", 11)
show_with_matplotlib(outline_image, "outline image", 12)

"""
Comparing different methods for smoothing images
"""
def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(3, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


# Create a figure() object with appropriate size and title
plt.figure(figsize=(12, 6))
plt.suptitle("Smoothing techniques", fontsize=14, fontweight='bold')

image = cv2.imread('cat-face.png')

# We create the kernel for smoothing images
# In this case a (10,10) kernel is created
kernel_averaging_10_10 = np.ones((10, 10), np.float32) / 100

# Additionally, if you know the values, you can put them directly in the kernel:
# kernel_averaging_5_5 = np.ones((5, 5), np.float32)/25
kernel_averaging_5_5 = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04],
                                 [0.04, 0.04, 0.04, 0.04, 0.04]])

print("kernel: {}".format(kernel_averaging_5_5))

# The function cv2.filter2D() applies an arbitrary linear filter to the provided image:
smooth_image_f2D_5_5 = cv2.filter2D(image, -1, kernel_averaging_5_5)
smooth_image_f2D_10_10 = cv2.filter2D(image, -1, kernel_averaging_10_10)

# The function cv2.blur() smooths an image using the normalized box filter
smooth_image_b = cv2.blur(image, (10, 10))

# When the parameter normalize (by default True) of cv2.boxFilter() is equals to True,
# cv2.filter2D() and cv2.boxFilter() perform the same operation:
smooth_image_bfi = cv2.boxFilter(image, -1, (10, 10), normalize=True)

# The function cv2.GaussianBlur() convolves the source image with the specified Gaussian kernel
# This kernel can be controlled using the parameters ksize (kernel size),
# sigmaX(standard deviation in the x direction of the gaussian kernel) and
# sigmaY (standard deviation in the y direction of the gaussian kernel)
smooth_image_gb = cv2.GaussianBlur(image, (9, 9), 0)

# The function cv2.medianBlur(), which blurs the image with a median kernel:
smooth_image_mb = cv2.medianBlur(image, 9)

# The function cv2.bilateralFilter() can be applied to the input image in order to apply a bilateral filter:
smooth_image_bf = cv2.bilateralFilter(image, 5, 10, 10)
smooth_image_bf_2 = cv2.bilateralFilter(image, 9, 200, 200)

# Plot the images:
show_with_matplotlib(image, "original", 1)
show_with_matplotlib(smooth_image_f2D_5_5, "cv2.filter2D() (5,5) kernel", 2)
show_with_matplotlib(smooth_image_f2D_10_10, "cv2.filter2D() (10,10) kernel", 3)
show_with_matplotlib(smooth_image_b, "cv2.blur()", 4)
show_with_matplotlib(smooth_image_bfi, "cv2.boxFilter()", 5)
show_with_matplotlib(smooth_image_gb, "cv2.GaussianBlur()", 6)
show_with_matplotlib(smooth_image_mb, "cv2.medianBlur()", 7)
show_with_matplotlib(smooth_image_bf, "cv2.bilateralFilter() - small values", 8)
show_with_matplotlib(smooth_image_bf_2, "cv2.bilateralFilter() - big values", 9)

# Show the created image:
plt.show()

# Show the Figure:
plt.show()