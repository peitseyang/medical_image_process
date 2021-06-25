import itertools
import threading
import time
from time import sleep
import sys
import numpy as np
import png
import pydicom
import matplotlib.pyplot as plt
import os
import cv2
from PIL import Image


done = False
def animate():
    for c in itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠴', '⠦', '⠧', '⠇', '⠏']):
        if done:
            break
        sys.stdout.write('\r' + c + ' ')
        sys.stdout.flush()
        sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

INPUT_FOLDER = './raw_data/'
OUTPUT_FOLDER = './process_data/'
all_dicom_file = os.listdir(INPUT_FOLDER)
all_dicom_file.remove('.DS_Store')

print('converting dicom file...')
for dicom_file in all_dicom_file:
    path = os.path.join(INPUT_FOLDER, dicom_file)
    destination = os.path.join(OUTPUT_FOLDER, dicom_file + '.png')

    ds = pydicom.dcmread(path)
    # print(ds)
    
    data = ds.pixel_array
    scaled_img = cv2.convertScaleAbs(data-ds.WindowCenter[0], alpha=(255.0 /ds.WindowWidth[0]))
    scaled_img = 255 - scaled_img
    cv2.imwrite(destination, scaled_img)
        
print('success')
done = True