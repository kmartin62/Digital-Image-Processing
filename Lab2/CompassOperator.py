'''Имплементирајте Compass оператор за детекција на рабови.

(a) Пресметајте и прикажете го резултатот на секој од филтрите.

(b) Пресметајте и прикажете го резултатот добиен со комбинација на сите филтри. Тестирајте со различни вредности за прагот.
'''

import cv2
import numpy as np

filter1 = ([1, 1, 0], [1, 0, -1], [0, -1, -1])
filter2 = ([1, 1, 1], [0, 0, 0], [-1, -1, -1])
filter3 = ([0, 1, 1], [-1, 0, 1], [-1, -1, 0])
filter4 = ([-1, 0, 1], [-1, 0, 1], [-1, 0, 1])
filter5 = ([-1, -1, 0], [-1, 0, 1], [0, 1, 1])
filter6 = ([-1, -1, -1], [0, 0, 0], [1, 1, 1])
filter7 = ([0, -1, -1], [1, 0, -1], [1, 1, 0])
filter8 = ([1, 0, -1], [1, 0, -1], [1, 0, -1])

def performKernel(src, filter):
    filteredImg = cv2.filter2D(src, -1, np.array(filter, dtype="float32"))
    filteredImg = abs(filteredImg)
    filteredImg = filteredImg / np.amax(filteredImg[:])

    return filteredImg

path = "/home/kmartin62/PycharmProjects/AI/Digital image processing/Lab2/"
image = cv2.imread(path + "Lenna.png", 0)
# image = cv2.GaussianBlur(image, (5, 5), 0)
image = np.float32(image)

filteredImg1 = performKernel(image, filter1)
filteredImg2 = performKernel(image, filter2)
filteredImg3 = performKernel(image, filter3)
filteredImg4 = performKernel(image, filter4)
filteredImg5 = performKernel(image, filter5)
filteredImg6 = performKernel(image, filter6)
filteredImg7 = performKernel(image, filter7)
filteredImg8 = performKernel(image, filter8)


edgeSum = np.maximum.reduce([filteredImg1, filteredImg2, filteredImg3, filteredImg4, filteredImg5,
                             filteredImg6, filteredImg7, filteredImg8])

ret, thresh = cv2.threshold(edgeSum, 0.15, 1, cv2.THRESH_BINARY)

# cv2.imshow("1", filteredImg1)
# cv2.imshow("2", filteredImg2)
# cv2.imshow("3", filteredImg3)
# cv2.imshow("4", filteredImg4)
# cv2.imshow("5", filteredImg5)
# cv2.imshow("6", filteredImg6)
# cv2.imshow("7", filteredImg7)
# cv2.imshow("8", filteredImg8)
#
cv2.imshow("EdgeSum", thresh)

cv2.waitKey(0)