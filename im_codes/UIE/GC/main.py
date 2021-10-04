
import os
import numpy as np
import cv2
#import natsort
#import xlwt
#from skimage import exposure

from sceneRadianceGC import RecoverGC

np.seterr(over='ignore')
if __name__ == '__main__':
    pass
folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/NonPhysical/GC"
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
        # img = cv2.imread('InputImages/' + file)
        img = cv2.imread(folder + '/InputImages/' + file)
        sceneRadiance = RecoverGC(img)
        print('sceneRadiance',sceneRadiance)
        cv2.imwrite('OutputImages/' + prefix + '_GC.jpg', sceneRadiance)

#import time
#img = cv2.imread("chloro.jpg")
#start_time = time.time()
#sceneRadiance = RecoverGC(img)
#execution_time = time.time()-start_time
#cv2.imwrite('GC_chloro.jpg', sceneRadiance)
