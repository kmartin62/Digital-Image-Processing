'''
Имплементирајте ги функциите:

- Contrast stretching (слајдот број 5 од презентацијата со име Оператори на ниво на пиксели во слика). Функцијата треба да прима како влезни аргументи слика над која ќе се направи трансформацијата и координати на две точки од кривата (референтните вредности од примерот не ги земајте во предвид)
'''

import cv2

def contrast_stretch(img, points):
    m, n = img.shape[0], img.shape[1] #Zemi ja goleminata na matricata m x n za slikata
    x1 = points[0][0]
    y1 = points[0][1]

    x2 = points[1][0]
    y2 = points[1][1]

    slope1 = y1 / x1 #Presmetaj go naklonot na pravata pomegju prvite dve tocki t.e presmetaj alfa
    slope2 = (y2 - y1) / (x2 - x1) #Naklonot na pravata kaj vtorite docki t.e presmetaj beta
    slope3 = (255 - y2) / (255 - x2) #Naklonot na pravata kaj tretite tocki t.e presmetaj gama

    inter1 = y1 - slope2 * x1 #Presmetaj gi tockite kaj sto se secat x i y. Vo primerot so prezentacijata ova e y1
    inter2 = y2 - slope3 * x2 #y2

    for i in range(0, m): #Vrti za site x, y vo matricata dobiena od slikata
        for j in range(0, n):
            tmp = img[i, j]
            tmp = [
                elem * slope1 if elem <= x1 #Ako pikselot e pomal od prvata x tocka, mnozi so prviot naklon
                else elem * slope2 + inter1 if elem > x1 and elem <= x2 #So vtoriot
                else elem * slope3 + inter2 #So tretiot
                for elem in tmp]
            img[i, j] = tmp #zameni gi soodvetnite vrednosti za img [i,j] (pikselite) so novodobienite izmnozeni od tmp

    return img #vrati ja slikata


img = cv2.imread('zelda.pgm')

img1 = contrast_stretch(img, [[50, 30], [150, 200]])

cv2.imshow("img1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


