# -*- coding: utf-8 -*-

# Importing required libraries

from PIL import Image, ImageDraw, ImageFont
import os
import pytesseract
import tensorflow as tf
from tf.keras.models import load_model

from Dictionaries import *

import numpy as np


class Predict(object):


	def __init__(self):

		self.model = load_model('label_classifier.hdf5')

	def find_label(self,image):
		"""Summary

        Args:
            image (TYPE): Image of Hello World


        Returns:
            x,y,w,h,type,conf: Returns values in json format a list of identified fonts, coordinates and confidene.
        """

		data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

		list_boxes = []
		for i in range(len(data['level'])):
			if data['text'][i] != '':
				list_boxes.append((data['text'][i], data['left'][i], data['top'][i], data['width'][i], data['height'][i]))

		final_dict = {'detected_fonts': []}
		if len(list_boxes) % 2 == 0:
			for i in range(int(len(list_boxes) / 2)):
				chunk_coords = list_boxes[2 * i][1], list_boxes[2 * i][2], list_boxes[2 * i + 1][1] + list_boxes[2 * i + 1][3], \
							   list_boxes[2 * i][2] + max(list_boxes[2 * i][4], list_boxes[2 * i + 1][4])
				im1 = Image.new('RGB', (400, 150), color=(255, 255, 255))
				im1.paste(img.crop(chunk_coords).resize((190, 28)), (20, 20))
				im1 = im1.resize((384, 384))
				im1 = np.expand_dims(im1, axis=0)
				output = self.model.predict(im1).argmax(axis=-1)[0]
				confidence = self.model.predict(im1)[0][output]

				final_dict['detected_fonts']\
					.append(dict_return(chunk_coords[0], chunk_coords[1],
										chunk_coords[2] - chunk_coords[0],
										chunk_coords[3] - chunk_coords[1],
										Reverse_Font_Mapping[output], confidence))

		return final_dict

