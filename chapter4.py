
#Constructing Basic Shapes in OpenCv
# Import required packages:
import cv2
import numpy as np
import matplotlib.pyplot as plt
#import constant
import math
import datetime
# Getting red color:
#print("red: '{}'".format(constant.RED))
#OR use this
'''
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
YELLOW = (0, 255, 255)
MAGENTA = (255, 0, 255)
CYAN = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (220, 220, 220)
'''
#testing_colors
'''
#define a show_with_matplotlib function with 2 paramter (the image,the image title)
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]
    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()

# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

#we have created an image of size 500 500, with the 3
#channels (we want a color image) and a uint8 type (8-bit unsigned integers)
#We have created it with a black background:
image = np.zeros((500, 500, 3), dtype="uint8")

# So we want another background color and we do the following:
image[:] = colors['light_gray']

# We draw all the colors to test the dictionary
# We draw some lines each one in one color. To get the color use 'colors[key]'
separation = 40
for i in colors:
    # Draw a line using the function cv2.line():
    cv2.line(image, (0, separation), (500, separation), colors[i], 20)
    separation += 50

# Show image:
show_with_matplotlib(image, 'Dictionary with some predefined colors')
'''
#Drawing shapes part1:
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 400 x 400 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set the background to black using np.zeros():
image = np.zeros((400, 400, 3), dtype="uint8")

# If you want another background color you can do the following:
image[:] = colors['light_gray']

# Show image:
show_with_matplotlib(image, '')

# 1. We are going to see how cv2.line() works:
#img = line(img, pt1, pt2, color, thickness=1, lineType=8, shift=0)
#lineType: It is the type of the shape boundary. OpenCV provides three types of line
#cv2.LINE_4: This means four-connected lines
#cv2.LINE_8: This means eight-connected lines
#cv2.LINE_AA: This means an anti-aliased line
#shift: This indicates the number of fractional bits in connection with the
###coordinates of some points defining the shape
cv2.line(image, (0, 0), (400, 400), colors['rand'], 3)
cv2.line(image, (0, 400), (400, 0), colors['blue'], 3)
cv2.line(image, (200, 0), (200, 400), colors['red'], 10)
cv2.line(image, (0, 200), (400, 200), colors['yellow'], 10)


# Show image:
show_with_matplotlib(image, 'cv2.line()')

# Clean the canvas to draw again:
image[:] = colors['light_gray']

# 2. We are going to see how cv2.rectangle() works:
#img = rectangle(img, pt1, pt2, color, thickness=1, lineType=8, shift=0)
cv2.rectangle(image, (10, 50), (60, 300), colors['green'],5)
cv2.rectangle(image, (80, 50), (130, 300), colors['blue'], -1)
cv2.rectangle(image, (150, 50), (350, 100), colors['red'], -1)
cv2.rectangle(image, (150, 150), (350, 300), colors['cyan'], 10)

# Show image:
show_with_matplotlib(image, 'cv2.rectangle()')

# Clean the canvas to draw again:
image[:] = colors['light_gray']

# 3. We are going to see how cv2.circle() works:
#img = circle(img, center, radius, color, thickness=1, lineType=8, shift=0)
cv2.circle(image, (50, 50), 20, colors['green'], 3)
cv2.circle(image, (100, 100), 30, colors['blue'], -1)
cv2.circle(image, (200, 200), 40, colors['magenta'], 10)
cv2.circle(image, (300, 300), 40, colors['cyan'], -1)

# Show image:
show_with_matplotlib(image, 'cv2.circle()')
'''
#Drawing shapes part2:
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 20 x 20 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set the background to black using np.zeros():
image = np.zeros((20, 20, 3), dtype="uint8")

# If you want another background color you can do the following:
image[:] = colors['light_gray']

# We are going to see how cv2.line() works modifying the parameter lineType:
cv2.line(image, (5, 0), (20, 15), colors['yellow'], 1, cv2.LINE_4)
cv2.line(image, (0, 0), (20, 20), colors['red'], 1, cv2.LINE_AA)
cv2.line(image, (0, 5), (15, 20), colors['green'], 1, cv2.LINE_8)

# Show image:
show_with_matplotlib(image, 'LINE_4    LINE_AA    LINE_8')
'''
#Drawing shapes part3:
'''
#The signature for the cv2.clipLine() function is as follows as follows:

def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 300 x 300 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set background to black using np.zeros():
image = np.zeros((300, 300, 3), dtype="uint8")
#1. We are going to see how cv2.clipLine() works
# Draw a rectangle and a line:
cv2.line(image, (0, 0), (300, 300), colors['green'], 3)
cv2.rectangle(image, (100, 100), (200, 200), colors['blue'], 3)

# We call the function cv2.clipLine():
#retval, pt1, pt2 = clipLine(imgRect, pt1, pt2)
ret, p1, p2 = cv2.clipLine((100, 100,200,200), (100, 100), (200, 200))

# cv2.clipLine() returns False if the line is outside the rectangle
# And returns True otherwise
if ret:
    cv2.line(image, p1, p2, colors['yellow'], 3)
# Show image:
show_with_matplotlib(image, 'cv2.clipLine()')
'''
#Drawing arrows
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 300 x 300 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set background to black using np.zeros():
image = np.zeros((300, 300, 3), dtype="uint8")
image[:] = colors['light_gray']

# 2. We are going to see how cv2.arrowedLine() works:
#cv2.arrowedLine(img, pt1, pt2, color, thickness=1, lineType=8, shift=0, tipLength=0.1)
cv2.arrowedLine(image, (250, 50), (100, 50), colors['red'], 3, 8, 0, 0.1)
cv2.arrowedLine(image, (50, 120), (200, 120), colors['green'], 3, cv2.LINE_AA, 0, 0.3)
cv2.arrowedLine(image, (50, 200), (200, 200), colors['blue'], 3, 8, 0, 0.3)

# Show image:
show_with_matplotlib(image, 'cv2.arrowedLine()')'''
#Drawing ellipses:
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 300 x 300 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set background to black using np.zeros():
image = np.zeros((300, 300, 3), dtype="uint8")
image[:] = colors['light_gray']
#cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=1, lineType)
cv2.ellipse(image, (80, 80), (60, 100), 0, 0, 360, colors['rand'], 5)
cv2.ellipse(image, (80, 200), (80, 40), 0, 0, 360, colors['green'], 3)
cv2.ellipse(image, (80, 200), (10, 60), 0, 0, 360, colors['blue'], 3)
cv2.ellipse(image, (50, 200), (10, 40), 0, 0, 180, colors['yellow'], 3)
cv2.ellipse(image, (200, 100), (50, 250), 0, 0, 270, colors['cyan'], 3)
cv2.ellipse(image, (150, 250), (60, 30), 0, 0, 360, colors['magenta'], 3)
cv2.ellipse(image, (250, 74), (200, 40), 45, 0, 360, colors['gray'], 3)

# Show image:
show_with_matplotlib(image, 'cv2.ellipse()')'''
#Drawing polygons
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 300 x 300 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set background to black using np.zeros():
image = np.zeros((300, 300, 3), dtype="uint8")
image[:] = colors['light_gray']
#cv2.polylines(img, pts, isClosed, color, thickness=1, lineType=8, shift=0)
# These points define a triangle:
pts = np.array([[250, 5], [220, 80], [280, 80]], np.int32)
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
# Print the shapes: this line is not necessary, only for visualization:
print("shape of pts '{}'".format(pts.shape))
# Draw this polygon with True option:
cv2.polylines(image, [pts], True, colors['green'], 3)

# These points define a triangle:
pts = np.array([[250, 105], [220, 180], [280, 180]], np.int32)
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
# Print the shapes:
print("shape of pts '{}'".format(pts.shape))
# Draw this polygon with False option:
cv2.polylines(image, [pts], False, colors['green'], 3)

# These points define a pentagon:
pts = np.array([[20, 90], [60, 60], [100, 90], [80, 130], [40, 130]], np.int32)
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
# Print the shapes:
print("shape of pts '{}'".format(pts.shape))
# Draw this polygon with True option:
cv2.polylines(image, [pts], True, colors['blue'], 3)

# These points define a pentagon:
pts = np.array([[20, 180], [60, 150], [100, 180], [80, 220], [40, 220]], np.int32)
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
# Print the shapes:
print("shape of pts '{}'".format(pts.shape))
# Draw this polygon with False option:
cv2.polylines(image, [pts], False, colors['blue'], 5)

# These points define a rectangle:
pts = np.array([[150, 100], [200, 100], [200, 150], [150, 150]], np.int32)
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
# Print the shapes:
print("shape of pts '{}'".format(pts.shape))
# Draw this polygon with False option:
cv2.polylines(image, [pts], True, colors['yellow'], 3)

# These points define a rectangle:
pts = np.array([[150, 200], [200, 200], [200, 250], [150, 250]], np.int32)
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
# Print the shapes:
print("shape of pts '{}'".format(pts.shape))
# Draw this polygon with False option:
cv2.polylines(image, [pts], False, colors['yellow'], 3)

# Show image:
show_with_matplotlib(image, 'cv2.polylines()')'''
#Shift parameter in drawing functions
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]
    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()

# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}
def draw_float_circle(img, center, radius, color, thickness=1, lineType=8, shift=4):
    """Wrapper function to draw float-coordinate circles"""
    factor = 2 ** shift
    center = (int(round(center[0] * factor)), int(round(center[1] * factor)))
    radius = int(round(radius * factor))
    cv2.circle(img, center, radius, color, thickness, lineType, shift)
#Create a canvas
image = np.zeros((800, 800, 3), dtype="uint8")
image[:] = colors['black']
draw_float_circle(image, (299, 299), 250, colors['red'], 5, 8, 0)
draw_float_circle(image, (299.9, 299.9), 100, colors['green'], 5, 8, 1)
draw_float_circle(image, (299.99, 299.99), 150, colors['light_gray'], 5, 8, 2)
draw_float_circle(image, (299.999, 299.999), 50, colors['yellow'], 5, 8, 3)
show_with_matplotlib(image, 'cv2.circle()')
'''
#Writing text
'''
#we can write text using cv2.putText()
# We draw some text on the image:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]
    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
image = np.zeros((800, 800, 3), dtype="uint8")
image[:] = colors['black']
#img = cv.putText( img, text, org, fontFace, fontScale, color, thickness=1, lineType= 8)
cv2.putText(image, 'momo', (50, 300), cv2.FONT_HERSHEY_SIMPLEX,6,colors['red'],2)
cv2.putText(image, 'ali', (10, 500), cv2.FONT_HERSHEY_SIMPLEX,10,colors['rand'],2)
cv2.putText(image, 'the one', (10, 700), cv2.FONT_HERSHEY_SIMPLEX,5,colors['blue'],5)
# Show image:
show_with_matplotlib(image, 'cv2.putText()')
'''
#All the available fonts in OpenCV are 
'''
FONT_HERSHEY_SIMPLEX = 0
FONT_HERSHEY_PLAIN = 1
FONT_HERSHEY_DUPLEX = 2
FONT_HERSHEY_COMPLEX = 3
FONT_HERSHEY_TRIPLEX = 4
FONT_HERSHEY_COMPLEX_SMALL = 5
FONT_HERSHEY_SCRIPT_SIMPLEX = 6
FONT_HERSHEY_SCRIPT_COMPLEX = 7
'''
#EX:how to draw all OpenCV fonts
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# Dictionary containing some strings to output:
fonts = {0: "FONT HERSHEY SIMPLEX", 1: "FONT HERSHEY PLAIN", 2: "FONT HERSHEY DUPLEX", 3: "FONT HERSHEY COMPLEX",
         4: "FONT HERSHEY TRIPLEX", 5: "FONT HERSHEY COMPLEX SMALL ", 6: "FONT HERSHEY SCRIPT SIMPLEX",
         7: "FONT HERSHEY SCRIPT COMPLEX"}

# Dictionary containing the index for each color:
index_colors = {0: 'blue', 1: 'green', 2: 'red', 3: 'yellow', 4: 'magenta', 5: 'cyan', 6: 'black', 7: 'dark_gray'}

# We create the canvas to draw: 650 x 650 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set background to black using np.zeros():
image = np.zeros((650, 650, 3), dtype="uint8")

# If you want another background color you can do the following:
image[:] = colors['white']

# Write the text using all the OpenCV fonts:
position = (10, 30)
for i in range(0, 8):
    print("i index value: '{}' text: '{}' + color: '{}' = '{}'".format(i, fonts[i].lower(), index_colors[i],colors[index_colors[i]]))
    cv2.putText(image, fonts[i], position, i, 1.1, colors[index_colors[i]], 2, cv2.LINE_4)
    position = (position[0], position[1] + 40)
    cv2.putText(image, fonts[i].lower(), position, i, 1.1, colors[index_colors[i]], 2, cv2.LINE_4)
    position = (position[0], position[1] + 40)
# Show image:
show_with_matplotlib(image, 'cv2.putText() using all OpenCV fonts')
'''
#text_drawing_bounding_box :('_'):
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]
    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 400 x 1200 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set background to black using np.zeros():
image = np.zeros((400, 1200, 3), dtype="uint8")

# If you want another background color you can do the following:
image[:] = colors['light_gray']

# Assign parameters to be used in the drawing functions:
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2.5
thickness = 5
text = 'momo'
circle_radius = 10

# We get the size of the text:
ret, baseline = cv2.getTextSize(text, font, font_scale, thickness)

# We get the text width and text height from ret:
text_width, text_height = ret

# We center the text in the image:
text_x = int(round((image.shape[1] - text_width) / 2))
text_y = int(round((image.shape[0] + text_height) / 2))

# Draw this point for reference:
cv2.circle(image, (text_x, text_y), circle_radius, colors['green'], -1)

# Draw the rectangle (bounding box of the text):
cv2.rectangle(image, (text_x, text_y + baseline), (text_x + text_width - thickness, text_y - text_height),
              colors['blue'], thickness)

# Draw the circles defining the rectangle:
cv2.circle(image, (text_x, text_y + baseline), circle_radius, colors['red'], -1)
cv2.circle(image, (text_x + text_width - thickness, text_y - text_height), circle_radius, colors['cyan'], -1)

# Draw the baseline line:
cv2.line(image, (text_x, text_y + int(round(thickness / 2))), (text_x + text_width - thickness, text_y +
                                                               int(round(thickness / 2))), colors['yellow'], thickness)
# Write the text centered in the image:
cv2.putText(image, text, (text_x, text_y), font, font_scale, colors['black'], thickness)

# Show image:
show_with_matplotlib(image, 'cv2.getTextSize() + cv2.putText()')
'''
#Drawing dynamic shape
'''
#cv2.setMouseCallback(windowName, onMouse, param=None)
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# This is the mouse callback function:
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("event: EVENT_LBUTTONDBLCLK")
        cv2.circle(image, (x, y), 10, colors['magenta'], -1)
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.rectangle(image, (x,y), (x+10,y+10),colors['blue'], -1)
        print("event: EVENT_MOUSEMOVE")
    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")
    if event == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")

# We create the canvas to draw: 600 x 600 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set the background to black using np.zeros():
image = np.zeros((600, 600, 3), dtype="uint8")
# We create a named window where the mouse callback will be established:
cv2.namedWindow('Image mouse')
# We set the mouse callback function to 'draw_circle':
cv2.setMouseCallback('Image mouse', draw_circle)
while True:
    # Show image 'Image mouse':
    cv2.imshow('Image mouse', image)
    # Continue until 'q' is pressed:
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Destroy all generated windows:
cv2.destroyAllWindows()'''
#Drawing both text and shapes
'''
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}


# This is the mouse callback function:
def draw_text():
    # We set the position to be used for drawing text:
    menu_pos = (10, 500)
    menu_pos2 = (10, 525)
    menu_pos3 = (10, 550)
    menu_pos4 = (10, 575)

    # Write the menu:
    cv2.putText(image, 'Double left click: add a circle', menu_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(image, 'Simple right click: delete last circle', menu_pos2, cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255))
    cv2.putText(image, 'Double right click: delete all circle', menu_pos3, cv2.FONT_HERSHEY_SIMPLEX, 0.7,  (255, 255, 255))
    cv2.putText(image, 'Press \'q\' to exit', menu_pos4, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))


# mouse callback function
def draw_circle(event, x, y, flags, param):
    """Mouse callback function"""
    global circles
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Add the circle with coordinates x,y
        print("event: EVENT_LBUTTONDBLCLK")
        circles.append((x, y))
    if event == cv2.EVENT_RBUTTONDBLCLK:
        # Delete all circles (clean the screen)
        print("event: EVENT_RBUTTONDBLCLK")
        circles[:] = []
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Delete last added circle
        print("event: EVENT_RBUTTONDOWN")
        try:
            circles.pop()
        except (IndexError):
            print("no circles to delete")
    if event == cv2.EVENT_MOUSEMOVE:
        print("event: EVENT_MOUSEMOVE")
    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")
    if event == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")


# Structure to hold the created circles:
circles = []

# We create the canvas to draw: 600 x 600 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set the background to black using np.zeros():
image = np.zeros((600, 600, 3), dtype="uint8")

# We create a named window where the mouse callback will be established:
cv2.namedWindow('Image mouse')

# We set the mouse callback function to 'draw_circle':
cv2.setMouseCallback('Image mouse', draw_circle)

# We draw the menu:
draw_text()

# We get a copy with only the text printed in it:
clone = image.copy()

while True:

    # We 'reset' the image (to get only the image with the printed text):
    image = clone.copy()

    # We draw now only the current circles:
    for pos in circles:
        # We print the circle (filled) with a  fixed radius (30):
        cv2.circle(image, pos, 30, colors['blue'], -1)

    # Show image 'Image mouse':
    cv2.imshow('Image mouse', image)

    # Continue until 'q' is pressed:
    if cv2.waitKey(400) & 0xFF == ord('q'):
        break

# Destroy all generated windows:
cv2.destroyAllWindows()'''
#capture mouse events with matplotlib to draw a circle
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]
    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 400 x 400 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set the background to black using np.zeros():
image = np.zeros((400, 400, 3), dtype="uint8")

# If you want another background color you can do the following:
image[:] = colors['light_gray']


def update_img_with_matplotlib():
    """Updates an image using matplotlib capabilities"""

    # Convert BGR to RGB image format:
    img_RGB = image[:, :, ::-1]

    # Display the image:
    plt.imshow(img_RGB)

    # Redraw the Figure because the image has been updated:
    figure.canvas.draw()


# We define the event listener for the 'button_press_event':
def click_mouse_event(event):
    # (event.xdata, event.ydata) contain the float coordinates of the mouse click event:
    cv2.circle(image, (int(round(event.xdata)), int(round(event.ydata))), 30, colors['red'], cv2.FILLED)
    # Call 'update_image()' method to update the Figure:
    update_img_with_matplotlib()
# We create the Figure:
figure = plt.figure()
figure.add_subplot(111)

# To show the image until a click is performed:
update_img_with_matplotlib()

# 'button_press_event' is a MouseEvent where a mouse botton is click (pressed)
# When this event happens the function 'click_mouse_event' is called:
figure.canvas.mpl_connect('button_press_event', click_mouse_event)
# Display the figure:
show_with_matplotlib(image, "momo")'''
#draw a watch
'''
def array_to_tuple(arr):
    return tuple(arr.reshape(1, -1)[0])
# Dictionary containing some colors
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 640 x 640 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set background to black using np.zeros()
image = np.zeros((640, 640, 3), dtype="uint8")

# If you want another background color you can do the following:
image[:] = colors['rand']

# Coordinates to define the origin for the hour markings:
hours_orig = np.array(
    [(620, 320), (580, 470), (470, 580), (320, 620), (170, 580), (60, 470), (20, 320), (60, 170), (169, 61), (319, 20),
     (469, 60), (579, 169)])

# Coordinates to define the destiny for the hour markings:
hours_dest = np.array(
    [(600, 320), (563, 460), (460, 562), (320, 600), (180, 563), (78, 460), (40, 320), (77, 180), (179, 78), (319, 40),
     (459, 77), (562, 179)])

# We draw the hour markings:
for i in range(0, 12):
    cv2.line(image, array_to_tuple(hours_orig[i]), array_to_tuple(hours_dest[i]), colors['black'], 3)

# We draw a big circle, corresponding to the shape of the analog clock
cv2.circle(image, (320, 320), 310, colors['red'], 8)

# We draw the rectangle containig the text and the text "Mastering OpenCV 4 with Python":
cv2.rectangle(image, (150, 175), (490, 270), colors['white'], -1)
cv2.putText(image, "Mastering OpenCV 4", (150, 200), 1, 2, colors['black'], 1, cv2.LINE_AA)
cv2.putText(image, "with Python", (210, 250), 1, 2, colors['black'], 1, cv2.LINE_AA)

# We make a copy of the image with the "static" information
image_original = image.copy()

# Now, we draw the "dynamic" information:
while True:
    # Get current date:
    date_time_now = datetime.datetime.now()
    # Get current time from the date:
    time_now = date_time_now.time()
    # Get current hour-minute-second from the time:
    hour = math.fmod(time_now.hour, 12)
    minute = time_now.minute
    second = time_now.second

    print("hour:'{}' minute:'{}' second: '{}'".format(hour, minute, second))

    # Get the hour, minute and second angles:
    second_angle = math.fmod(second * 6 + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    hour_angle = math.fmod((hour * 30) + (minute / 2) + 270, 360)

    print("hour_angle:'{}' minute_angle:'{}' second_angle: '{}'".format(hour_angle, minute_angle, second_angle))

    # Draw the lines corresponding to the hour, minute and second needles
    second_x = round(320 + 310 * math.cos(second_angle * 3.14 / 180))
    second_y = round(320 + 310 * math.sin(second_angle * 3.14 / 180))
    cv2.line(image, (320, 320), (second_x, second_y), colors['rand'], 2)

    minute_x = round(320 + 260 * math.cos(minute_angle * 3.14 / 180))
    minute_y = round(320 + 260 * math.sin(minute_angle * 3.14 / 180))
    cv2.line(image, (320, 320), (minute_x, minute_y), colors['green'], 8)

    hour_x = round(320 + 220 * math.cos(hour_angle * 3.14 / 180))
    hour_y = round(320 + 220 * math.sin(hour_angle * 3.14 / 180))
    cv2.line(image, (320, 320), (hour_x, hour_y), colors['white'], 10)

    # Finally, a small circle, corresponding to the point where the three needles joint, is drawn:
    cv2.circle(image, (320, 320), 10, colors['red'], -1)

    # Show image:
    cv2.imshow("clock", image)

    # We get the image with the static information:
    image = image_original.copy()

    # A wait of 500 milliseconds is performed (to see the displayed image)
    # Press q on keyboard to exit the program:
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

# Release everything:
cv2.destroyAllWindows()
'''
#EX1:
#Create a diagonal line starting at (0,0) and ending at (512,512).
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 300 x 300 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set background to black using np.zeros():
image = np.zeros((700, 700, 3), dtype="uint8")
#1. We are going to see how cv2.clipLine() works
# Draw a rectangle and a line:
cv2.line(image, (0, 0), (700, 700), colors['green'], 3)
#cv2.rectangle(image, (100, 100), (200, 200), colors['blue'], 3)

# We call the function cv2.clipLine():
#retval, pt1, pt2 = clipLine(imgRect, pt1, pt2)
ret, p1, p2 = cv2.clipLine((0, 0,512,512), (0, 0), (512, 512))

# cv2.clipLine() returns False if the line is outside the rectangle
# And returns True otherwise
if ret:
    cv2.line(image, p1, p2, colors['red'], 3)
# Show image:
show_with_matplotlib(image, 'cv2.clipLine()')
'''
#EX2:
#Render the text Hello OpenCV using the parameters you want.
'''
#we can write text using cv2.putText()
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]
    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
image = np.zeros((800, 800, 3), dtype="uint8")
image[:] = colors['black']
#img = cv.putText( img, text, org, fontFace, fontScale, color, thickness=1, lineType= 8)
cv2.putText(image, 'Hello', (50, 200), cv2.FONT_HERSHEY_SIMPLEX,6,colors['red'],5)
cv2.putText(image, 'Open', (10, 500), cv2.FONT_HERSHEY_SIMPLEX,10,colors['green'],5)
cv2.putText(image, 'CV', (10, 700), cv2.FONT_HERSHEY_SIMPLEX,5,colors['blue'],5)
# Show image:
show_with_matplotlib(image, 'cv2.putText()')
'''
#EX3:
#Draw a polygon (with the shape of a circle) using 12 points
'''
def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]
    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

image = np.zeros((700, 700, 3), dtype="uint8")
#cv2.polylines(img, pts, isClosed, color, thickness=1, lineType=8, shift=0)


# These points define a pentagon:
pts = np.array(
    [(600, 320), (563, 460), (460, 562), (320, 600), (180, 563), (78, 460), (40, 320), (77, 180), (179, 78), (319, 40),
     (459, 77), (562, 179)])
# Reshape to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))
# Print the shapes:
print("shape of pts '{}'".format(pts.shape))
# Draw this polygon with True option:
cv2.polylines(image, [pts], True, colors['blue'], 3)
# Show image:
show_with_matplotlib(image, 'cv2.polylines()')'''

#EX4:
#Draw a rectangle using the mouse events with CV events when a double left-click is performed.
'''
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}
# This is the mouse callback function:
def draw_text():
    # We set the position to be used for drawing text:
    menu_pos = (10, 500)
    menu_pos2 = (10, 525)
    menu_pos3 = (10, 550)
    menu_pos4 = (10, 575)
    # Write the menu:
    cv2.putText(image, 'Double left click: add a rectangle', menu_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(image, 'Simple right click: delete last rectangle', menu_pos2, cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 255, 255))
    cv2.putText(image, 'Double right click: delete all rectangles', menu_pos3, cv2.FONT_HERSHEY_SIMPLEX, 0.7,  (255, 255, 255))
    cv2.putText(image, 'Press \'q\' to exit', menu_pos4, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))

# mouse callback function
def draw_rectangle(event, x, y, flags, param):
    """Mouse callback function"""
    global rectangles
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Add the rectangle with coordinates x,y
        print("event: EVENT_LBUTTONDBLCLK")
        rectangles.append((x, y))
    if event == cv2.EVENT_RBUTTONDBLCLK:
        # Delete all rectangles (clean the screen)
        print("event: EVENT_RBUTTONDBLCLK")
        rectangles[:] = []
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Delete last added rectangles
        print("event: EVENT_RBUTTONDOWN")
        try:
            rectangles.pop()
        except (IndexError):
            print("no circles to delete")
    if event == cv2.EVENT_MOUSEMOVE:
        print("event: EVENT_MOUSEMOVE")
    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")
    if event == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")


# Structure to hold the created circles:
rectangles = []

# We create the canvas to draw: 600 x 600 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set the background to black using np.zeros():
image = np.zeros((600, 600, 3), dtype="uint8")

# We create a named window where the mouse callback will be established:
cv2.namedWindow('Image mouse')

# We set the mouse callback function to 'draw_rectangle':
cv2.setMouseCallback('Image mouse', draw_rectangle)

# We draw the menu:
draw_text()

# We get a copy with only the text printed in it:
clone = image.copy()

while True:

    # We 'reset' the image (to get only the image with the printed text):
    image = clone.copy()

    # We draw now only the current rectangle:
    for i,j in rectangles:

        cv2.rectangle(image, (i,j),(i+10,j+10), colors['blue'], -1)

    # Show image 'Image mouse':
    cv2.imshow('Image mouse', image)
    # Continue until 'q' is pressed:
    if cv2.waitKey(400) & 0xFF == ord('q'):
        break
# Destroy all generated windows:
cv2.destroyAllWindows()'''
#EX5:
#Draw a rectangle using the mouse events with Matplotlib events when a double left-click is performed.
'''
# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}
image = np.zeros((400, 400, 3), dtype="uint8")
def update_img_with_matplotlib():
    # Convert BGR to RGB image format
    img_RGB = image[:, :, ::-1]
    # Display the image:
    plt.imshow(img_RGB)
    # Redraw the Figure because the image has been updated:
    figure.canvas.draw()
# We define the event listener for the 'button_press_event':
def click_mouse_event(event):
    """Event listener for the 'button_press_event'"""
    # Check if a double left click is performed:
    if event.dblclick and event.button == 1:
        # (event.xdata, event.ydata) contain the float coordinates of the mouse click event:
        cv2.rectangle(image, (int(round(event.xdata)), int(round(event.ydata))),
                      (int(round(event.xdata)) + 100, int(round(event.ydata)) + 50), colors['blue'], cv2.FILLED)
    # Call 'update_image()' method to update the Figure:
    update_img_with_matplotlib()


# We create the Figure:
figure = plt.figure()
figure.add_subplot(111)

# To show the image until a click is performed:
update_img_with_matplotlib()

# 'button_press_event' is a MouseEvent where a mouse botton is click (pressed)
# When this event happens the function 'click_mouse_event' is called:
figure.canvas.mpl_connect('button_press_event', click_mouse_event)
# Display the figure:
plt.show()'''
#EX6:
#meme image with opencv
''''
image=cv2.imread("lenna.png")
cv2.putText(image, 'Hello World', (25,100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),2)
cv2.putText(image, 'Good Bye World',(25,200), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 0, 255),2)
cv2.imshow("Very basic meme generator",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#OR with matplotlib
'''
def show_with_matplotlib(img, title):
    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]
    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()
# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}
# We load the image 'lenna.png':
image = cv2.imread("lenna.png")
# Write some text (up):
cv2.putText(image, 'Hello World', (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 0.8, colors['green'], 1, cv2.LINE_AA)
# Write some text (down):
cv2.putText(image, 'Goodbye World', (10, 200), cv2.FONT_HERSHEY_TRIPLEX, 0.8, colors['red'], 1, cv2.LINE_AA)
# Show image:
show_with_matplotlib(image, 'very basic meme generator')
'''
