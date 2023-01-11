# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from random import *
import time
before = time.time()
array = []
for i in range(24):
    random_number = randrange(1, 25)
    while random_number in array:
        random_number = randrange(1, 25)
    array.append(random_number)
    after = time.time()
print("Avec boucle while et in:")
print(array)
print(after - before)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def random_rec(nbelement, min, max):
    before = time.time()
    array = []
    for i in range(nbelement):
        random_number = randrange(min, max+1)
        array.append(random_number)
        def remove_duplicates(array):
            for i in range(len(array)):
                for j in range(len(array)):
                    if i != j and array[i] == array[j]:
                        array[j] = randrange(min, max+1)
                        remove_duplicates(array)
        remove_duplicates(array)

    print("Avec boucle while sans ")
    print(array)
    print(after - before)

#random_rec(100, 1, 100)

pixelsPerChar  =  [(32,0),(33,37),(34,51),(35,98),(36,87),(37,88),(38,71),(39,25),(40,42),
(41,48),(42,44),(43,46),(44,26),(45,24),(46,15),(47,44),(48,80),(49,49),(50,72),(51,69),
(52,71),(53,74),(54,84),(55,50),(56,93),(57,83),(58,30),(59,44),(60,50),(61,39),(62,52),
(63,56),(64,98),(65,83),(66,92),(67,71),(68,78),(69,87),(70,77),(71,83),(72,85),(73,52),
(74,62),(75,94),(76,55),(77,105),(78,100),(79,82),(80,73),(81,102),(82,88),(83,86),
(84,62),(85,82),(86,74),(87,109),(88,88),(89,67),(90,74),(91,47),(92,43),(93,47),(94,32),
(95,28),(96,15),(97,78),(98,88),(99,66),(100,91),(101,82),(102,62),(103,81),(104,72),
(105,42),(106,51),(107,77),(108,45),(109,87),(110,60),(111,67),(112,80),(113,85),
(114,50),(115,70),(116,58),(117,64),(118,61),(119,78),(120,75),(121,65),(122,61),
(123,49),(124,36),(125,48),(126,28),(127,0),(128,0),(129,0),(130,0),(131,0),(132,0),
(133,0),(134,0),(135,0),(136,0),(137,0),(138,0),(139,0),(140,0),(141,0),(142,0),(143,0),
(144,0),(145,0),(146,0),(147,0),(148,0),(149,0),(150,0),(151,0),(152,0),(153,0),(154,0),
(155,0),(156,0),(157,0),(158,0),(159,0),(160,0),(161,0),(162,0),(163,0),(164,0),(165,0),
(166,0),(167,0),(168,0),(169,0),(170,0),(171,0),(172,0),(173,0),(174,0),(175,0),(176,0),
(177,0),(178,0),(179,0),(180,0),(181,0),(182,0),(183,0),(184,0),(185,0),(186,0),(187,0),
(188,0),(189,0),(190,0),(191,0),(192,0),(193,0),(194,0),(195,0),(196,0),(197,0),(198,0),
(199,0),(200,0),(201,0),(202,0),(203,0),(204,0),(205,0),(206,0),(207,0),(208,0),(209,0),
(210,0),(211,0),(212,0),(213,0),(214,0),(215,0),(216,0),(217,0),(218,0),(219,0),(220,0),
(221,0),(222,0),(223,0),(224,0),(225,0),(226,0),(227,0),(228,0),(229,0),(230,0),(231,0),
(232,0),(233,0),(234,0),(235,0),(236,0),(237,0),(238,0),(239,0),(240,0),(241,0),(242,0),
(243,0),(244,0),(245,0),(246,0),(247,0),(248,0),(249,0),(250,0),(251,0),(252,0),(253,0),
(254,0)]
pixelsPerChar.sort(key=lambda y: y[1])
maxPixelsPerChar = 109
from PIL import Image
import numpy as np
path = "/Users/enzolagadec/Desktop/image.jpeg"
image = np.asarray(Image.open(path), dtype='int32')

#
# ## acii art from image
# def ascii_art_from_image(image, pixelsPerChar):
#     image = np.asarray(Image.open(path), dtype='int32')
#     for i in range(len(image)):
#         for j in range(len(image[i])):
#             for k in range(image[i][j]):
#                 print(k)
#     return image
# print(ascii_art_from_image(path, pixelsPerChar))


xBloc = 5
yBloc = 10
diviseurMoyenneBloc = (xBloc * yBloc)*3

image = np.asarray(Image.open(path), dtype='int32')
print(image)
newImage = []
for x in range(270//xBloc):
    ligne = []
    for y in range(260//yBloc):
        somme = 0
        moyenne = 0
        for i in range(y*yBloc, y*yBloc + yBloc):
            for j in range(x*xBloc, x*xBloc + xBloc):
                for loop in range(3):
                    somme += image[i][j][loop]
        moyenne = somme/diviseurMoyenneBloc
        ligne.append(moyenne)
    newImage.append(ligne)
print(len(newImage)*len(newImage[0]))

finalImage = ''
for y in range(260//yBloc):
    for x in range(270//xBloc):
        pix = newImage[x][y]
        if pix < 50 :
            finalImage+= chr(81)
        elif pix < 100:
            finalImage+= chr(67)
        elif pix < 150:
            finalImage += chr(124)
        elif pix <200:
            finalImage += chr(96)
        else:
            finalImage += chr(32)
    finalImage += '\n'
f = open('imageTexte.txt', 'w')
a = f.write(finalImage)
f.close()

