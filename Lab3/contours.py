'''Во секоја од добиените слики по сегментацијата применете алгоритам за детекција на контури и пронајдете ја контурата која го дефинира листот. '''

import cv2
from os import listdir
import numpy as np

if __name__ == '__main__':
    path = "/home/kmartin62/PycharmProjects/AI/Digital image processing/Lab3/output_images/"
    output_path = "/home/kmartin62/PycharmProjects/AI/Digital image processing/Lab3/contours/"
    pictures = [f for f in listdir(path)]
    kernel = np.ones((1, 1), np.uint8)

    for picture in pictures:
        img = cv2.imread(path + picture)
        img = cv2.dilate(img, kernel, kernel)
        edged = cv2.Canny(img, 30, 200)

        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = []

        for cnt in contours:
            if cv2.arcLength(cnt, closed=True) >= 50:
                cnts.append(cnt)

        cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
        cv2.imwrite(output_path + picture, img)

        # cv2.imshow("img", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
