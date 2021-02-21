# -*- coding: utf-8 -*-

import pytesseract

def convert_ltrb_to_yolo(l, t, r, b):
    width = r - l
    height = b - t
    X_centre = int(l + width / 2) / 400
    Y_centre = int(t + height / 2) / 150
    width = width / 400
    height = height / 150

    return (X_centre, Y_centre, width, height)


def get_yolo_points(img):
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    n_boxes = len(data['level'])
    for i in range(n_boxes):

        if (data['text'][i].lower() in ['hello,', 'wello,', 'helo', 'hell,', 'helle,', 'hello.', 'hel,']):
            l, t = data['left'][i] - 1, data['top'][i] - 1
        if (data['text'][i].lower() in ['world!', 'worle!', 'wore!', 'were!', 'wartd!', 'word!', 'worl']):
            r, b = data['left'][i] + data['width'][i] - 1, data['top'][i] + data['height'][i] + 1

    return convert_ltrb_to_yolo(l, t, r, b)
