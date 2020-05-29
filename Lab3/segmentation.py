'''За сликите дадени во директориумите database и query (вкупно 40 на број) применете некој од алгоритмите за сегментација на слика со цел да добиете црно-бели слики со јасно издвоени лист и позадина.

Коментирајте ги добиените резултати! Дали избраниот алгоритам точно ги сегментира дадените слики?'''

import cv2
from os import listdir
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    path = "/home/kmartin62/PycharmProjects/AI/Digital image processing/Lab3/images/"
    pictures = [f for f in listdir(path)]
    kernel = np.ones((6, 6), np.uint8)

    for picture in pictures:
        img = cv2.imread(path + picture, 0)

        blur = cv2.GaussianBlur(img, (5, 5), 0)

        ret, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        img_erosion = cv2.erode(th, kernel, iterations=1)

        f = plt.figure()
        f.add_subplot(1, 3, 1)
        plt.title("Original")
        plt.imshow(img)
        f.add_subplot(1, 3, 2)
        plt.title("OTSU Threshold")
        plt.imshow(th)
        f.add_subplot(1, 3, 3)
        plt.title("Erosion")
        plt.imshow(img_erosion)
        plt.show()

