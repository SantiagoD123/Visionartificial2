"Ejercicio 1"

import cv2 as cv
import numpy as np

S = 100
im = np.zeros([100,100])


def im_1():
    im = np.zeros([100,100])
    for i in range(5):
        im[i,i] = 255
    print(im)

    cv.imshow("Imagen2.png", im)
    cv.waitKey(0)

im_1()