import numpy as np
from matplotlib import pyplot as plt
import cv2
import time
from detect import values
from flask import Flask, app, render_template, Response

app = Flask(__name__)

cap = cv2.VideoCapture(0)

def gen_frames():  
    while True:
        success, frame = cap.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



'''class VideoCamera(object):
    def __init__(self):
        self.heartbeat_values_list, self.heartbeat_value = values()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        return self.heartbeat_value'''

heartbeat_values_list , heartbeat_value = values()        

map_list = []
temp_list = []
temp = 0

for i in heartbeat_values_list:
    if i > 15 and i < 200:
        map_list.append(round(i,2))

for i in range(len(map_list)):
    temp = temp + 1
    temp_list.append(temp)

plt.plot(temp_list,map_list)
plt.xlabel('Time(seconds)')
plt.ylabel('Heart rate(bpm)')
#figg.savefig('my_plot.png')
plt.savefig('my_plot.png')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  index = open("templates/index.html").read().format(Pulse_rate = heartbeat_value)
  return index                                        

@app.route('/video_feed/')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/graph/')
def graph():
    img = r'C:\Users\KEVIN JINU\Desktop\Hack\TECHNOTHON 1.0\Dolo-650\python\my_plot.png'
    return img

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)                                         