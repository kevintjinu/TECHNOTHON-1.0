import numpy as np
from matplotlib import pyplot as plt
import cv2
import time

hb_count = 128
hb_values = [0]*hb_count
hb_times = [time.time()]*hb_count

# Matplotlib graph surface
fig = plt.figure()
ax = fig.add_subplot(111)

def get_vals(crop_img):

    global hb_values, hb_times

    hb_values = hb_values[1:] + [np.average(crop_img)]
    hb_times = hb_times[1:] + [time.time()]

    #print("HT = ",hb_times)
    print("HV = ",hb_values)

    # Draw matplotlib graph to numpy array
    ax.plot(hb_times, hb_values)
    fig.canvas.draw()
    img_plot = np.fromstring(fig.canvas.tostring_rgb(),
                                dtype=np.uint8, sep='')
    img_plot = img_plot.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.cla()

    return crop_img, img_plot, hb_values