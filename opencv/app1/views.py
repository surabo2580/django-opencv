from django.shortcuts import render, HttpResponse
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from app1 import views



class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        (self.grabbed,self.frame) = self.video.read()
        threading.thread(target=self.update,args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed.self.frame) + self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'content-type:image/jpeg\r\n\r\n'+ frame + b'\r\n\r\n')

@gzip.gzip_page
def Home(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam),content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request,'app1.html')

