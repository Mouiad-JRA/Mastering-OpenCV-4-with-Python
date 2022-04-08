# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:01:17 2020

@author: Mouiad
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
'''
#	The	function	cv2.imread()	is	used	to	read	an	image	from	the	the	working	directory 
#	Alternatively,	you	should	provide	a	full	path	of	the	image:	
#	Load	OpenCV	logo	image	(in	this	case	from	the	working	directoy): img	=	cv2.imread('logo.png')
img	=	cv2.imread('logo.png')
#	To	get	the	dimensions	of	the	image	use	img.shape
#	img.shape	returns	a	tuple	of	number	of	rows,	columns	and	channels	(if	a	colour	image)
#	If	image	is	grayscale,	img.shape	returns	a	tuple	of	number	of	rows	and	columns.
#	So,it	can	be	used	to	check	if	loaded	image	is	grayscale	or	color	image. 
#	Get	the	shape	of	the	image:
dimensions	=	img.shape
#(img.size	is	equal	to	the	multiplication of	height	×	width	×	channels)
total_number_of_elements=	img.size()
#  	the	image datatype	is	uint8	(unsigned	char),	because	values	are	in	the	[0	-	255]	range
#	Image	datatype	is	obtained	by	img.dtype.
#	img.dtype	is	very	important	because	a	large	number	of	errors	is	caused	by	invalid	datatype. 
#	Get	the	image	datatype: 
image_dtype	=	img.dtype
#	The	function	cv2.imshow()	is	used	to	display	an	image	in	a	window 
#	The	first	argument	of	this	function	is	the	window	name 
#	The	second	argument	of	this	function	is	the	image	to	be	shown.
#	Each	created	window	should	have	different	window	names. 
#	Show	original	image: 
cv2.imshow("original	image",	img)
#	The	function	cv2.waitKey(),	which	is	a	keyboard	binding	function,	waits	for	any	keyboard	event.'
#	This	function	waits	the	value	indicated	by	the	argument	(in	milliseconds).	
#	If	any	keyboard	event	is	produced	in	this	period	of	time,	the	program	continues	its	execution 
#	If	the	value	of	the	argument	is	0,	the	program	waits	indefinitely	until	a	keyboard	event	is	produced 
cv2.waitKey(0)
# to get the value of the pixel (x=40,	y=6) In	case	of	BGR	image,
#it	returns	an	array	of	(Blue,	Green,	Red)	values.  Get	the	value	of	the	pixel	(x=40,	y=6): 
(b,	g,	r)	=	img[6,	40]
#	to	get	only	the	blue value	of	the	pixel	(x=40,	y=6),	we	would	use	the	following	code:
#we	will	use	row,	column,	and	the index	of	the	desired	channel	for	 indexing
b	=	img[6,	40,	0]
##	The	pixel	values	can	be	also	modified	in	the	same	way	-	(b,	g,	r)	format:
img[6,	40]	=	(0,	0,	255)
#to	deal	with	a	certain	region	 rather	than	one 	pixel:
#	In	this	case,	we	get	 the	top 	left	corner 	of	the 	image: 
top_left_corner	=	img[0:50,	0:50]
#The	top_left_corner	variable	is	another	image	(smaller	than	img),	but	we	can	play with	it	in	the	same	way.
'''
###############################################################################
'''
#Accessing	and	manipulating	pixels	in OpenCV	with	grayscale	images
#we	will	use	the	cv2.imread()	function	to	read	an	image
#the second	argument	is	needed	because	we	want	to	load	the	image	in	grayscale
gray_img	=	cv2.imread('logo.jpg',	cv2.IMREAD_GRAYSCALE)
dimensions	=	gray_img.shape#we will get two values 	like this:(99,	82).
#	In	grayscale images,	only	one	 value 	is	obtained 	called  the	intensity 	of	the 	pixel.
#	Get	 the	value	of	the 	pixel	(x=40,	y=6)
i	=	gray_img[6,	40]
#	You	 can	modify 	the 	pixel	values	 of 	the 	image	in	the	 same	way.
#	Set	 the	pixel	to	black(0)
gray_img[6,	40]	=	0
'''
###############################################################################
'''
#BGR	order	in	OpenCV
#	Load	image	using	cv2.imread:
img_OpenCV	=	cv2.imread('logo.jpg')
# Split	the 	loaded	 image	 into	its 	three	channels	(b,	g,	r):
b,	g,	r	=	cv2.split(img_OpenCV)
#	Merge	again	the	 three	 channels	 but	 in	 the	 RGB	format: 
img_matplotlib	=	cv2.merge([r,	g,	b])
#Now 	we	have	two 	images	(img_OpenCV	and 	img_matplotlib)
#	Show	both	images	(img_OpenCV	and	img_matplotlib)	using	matplotlib 
#	This	will	show	the	image	in	wrong	color:
plt.subplot(1,2,1)
plt.imshow(img_OpenCV)
#	This	will	show	the	image	in	true	color:
plt.subplot(1,2,2) 
plt.imshow(img_matplotlib) 
plt.show()
cv2.imshow('img_OpenCV',img_OpenCV)
cv2.waitKey(0)
cv2.imshow('img_matplotlib',img_matplotlib)
cv2.waitKey(0)
#if	we	want	to	show	the	two	images	in	the	same	window
# To stack horizontally (img_OpenCV to the left of img_matplotlib):
img_concats = np.concatenate((img_OpenCV, img_matplotlib), axis=1)
cv2.imshow('concatenate',img_concats)
cv2.waitKey(0)
#	if	you	want	to	get	one	channel	of	the	image,	instead	of	using cv2.split()	
# to	get	the	desired	channel,	you	can	use	NumPy	indexing
# Using numpy capabilities to get the channels and two build the RGB image
# Get the three channels (instead of using cv2.split):
B = img_OpenCV[:, :, 0]
G = img_OpenCV[:, :, 1]
R = img_OpenCV[:, :, 2]
#Or # Transform the image BGR to RGB using Numpy capabilities in	a	single 	instruction:
img_RGB = img_OpenCV[:, :, ::-1]
# Now, we show the RGB image:
cv2.imshow('img RGB (wrong color)', img_RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
###############################################################################
#Exercice:

#	Suppose	that	you 	have	loaded	 an 	image	in	img How to check if img is color or grayscale
'''
# load OpenCV logo image:
img = cv2.imread('logo.jpg')
# Get the shape of the image:
dimensions = img.shape
# Color images: length == 3
# Grayscale images: length == 2
# Check the length of dimensions
if len(dimensions) < 3:
    print("grayscale image!")
if len(dimensions) == 3:
    print("color image!")
# Load the same image but in grayscale:
gray_img = cv2.imread('logo.jpg', cv2.IMREAD_GRAYSCALE)
# Get again the img.shape properties:
dimensions = gray_img.shape
# Check the length of dimensions
if len(dimensions) < 3:
    print("grayscale image!")
if len(dimensions) == 3:
    print("color image!")
'''
###############################################################################