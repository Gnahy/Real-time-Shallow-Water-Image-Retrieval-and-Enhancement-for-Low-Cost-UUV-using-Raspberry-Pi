import os
import numpy as np
import cv2
#import natsort

from RefinedTramsmission import Refinedtransmission
from getAtomsphericLight import getAtomsphericLight
from getRGBDarkChannel import getDarkChannel
from getTM import getTransmission
from sceneRadiance import sceneRadianceRGB

np.seterr(over='ignore')
if __name__ == '__main__':
    pass

folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/Physical/RoWS"
# folder = "C:/Users/Administrator/Desktop/Databases/Dataset"
path = folder + "/InputImages"
files = os.listdir(path)
files =  natsort.natsorted(files)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)
        img = cv2.imread(folder +'/InputImages/' + file)
        blockSize = 9
        
        RGB_Darkchannel = getDarkChannel(img, blockSize)
        AtomsphericLight = getAtomsphericLight(RGB_Darkchannel, img)
        print('AtomsphericLight', AtomsphericLight)
        transmission = getTransmission(img, AtomsphericLight, blockSize)
        print('transmission',transmission)
        print('np.mean(transmission)',np.mean(transmission))
        transmission = Refinedtransmission(transmission, img)
        sceneRadiance = sceneRadianceRGB(img, transmission, AtomsphericLight)
        # # print('AtomsphericLight',AtomsphericLight)
        #
        #
        #
        cv2.imwrite('OutputImages/' + prefix + '_RoWS_TM.jpg', np.uint8(transmission* 255))
        cv2.imwrite('OutputImages/' + prefix + '_RoWS.jpg', sceneRadiance)


import time
img = cv2.imread("deepBlue.jpg")
start_time = time.time()
height = len(img)
width = len(img[0])

blockSize = 9
        
RGB_Darkchannel = getDarkChannel(img, blockSize)
AtomsphericLight = getAtomsphericLight(RGB_Darkchannel, img)
print('AtomsphericLight', AtomsphericLight)
transmission = getTransmission(img, AtomsphericLight, blockSize)
print('transmission',transmission)
print('np.mean(transmission)',np.mean(transmission))
transmission = Refinedtransmission(transmission, img)
execution_time = time.time()-start_time
sceneRadiance = sceneRadianceRGB(img, transmission, AtomsphericLight)


execution_time1 = time.time()-start_time

cv2.imwrite('RoWS_TM_deepBlue.jpg', np.uint8(transmission * 255))
cv2.imwrite('RoWS_deepBlue.jpg', sceneRadiance)