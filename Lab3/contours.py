'''Во секоја од добиените слики по сегментацијата применете алгоритам за детекција на контури и пронајдете ја контурата која го дефинира листот. '''


import cv2
from os import listdir

if __name__ == '__main__':
    path = "/home/kmartin62/PycharmProjects/AI/Digital image processing/Lab3/output_images/"
    pictures = [f for f in listdir(path)]

    for picture in pictures:
        img = cv2.imread(path + picture)
        edged = cv2.Canny(img, 30, 200)

        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
