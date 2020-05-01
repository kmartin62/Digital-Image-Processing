'''
Имплементирајте ги функциите:

- Range compression (слајдот број 7 од презентацијата со име Оператори на ниво на пиксели во слика). Функцијата како влезени аргументи треба да има слика над која ќе се направи трансформацијата и параметарот C. 
'''

import cv2
import math

def range_compression(img, c):
    m, n = img.shape[0], img.shape[1]  # Zemi ja goleminata na matricata m x n za slikata

    for i in range(0, m):  # Vrti za site x, y vo matricata dobiena od slikata
        for j in range(0, n):
            tmp = img[i, j]
            tmp = [c * math.log10(1 + elem) for elem in tmp] #zameni go sekoj piksel so c*log10(piksel+1)
            img[i, j] = tmp  # zameni img[i, j] so tmp
    return img

img = cv2.imread('zelda.pgm')

img1 = range_compression(img, 100)
cv2.imshow("img", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


