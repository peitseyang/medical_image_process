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
# print(all_dicom_file)
all_dicom_file.remove('.DS_Store')

print('converting dicom file...')
for dicom_file in all_dicom_file:
    path = os.path.join(INPUT_FOLDER, dicom_file)
    destination = os.path.join(OUTPUT_FOLDER, dicom_file + '.png')

    ds = pydicom.dcmread(path)
    data = ds.pixel_array
    plt.imshow(data)

    shape = data.shape

    # Convert to float to avoid overflow or underflow losses.
    image_2d = data.astype(float)

    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0

    # Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)

    # Write the PNG file
    with open(destination, 'wb') as png_file:
        w = png.Writer(shape[1], shape[0], greyscale=True)
        w.write(png_file, image_2d_scaled)
        
print('success')
done = True