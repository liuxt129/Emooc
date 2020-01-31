import time
import cv2
import shutil
import os

def capture_image(total_time, interval):
    folder_path = os.path.join('images/')
    shutil.rmtree(folder_path, ignore_errors=True)
    os.mkdir(folder_path)

    cap = cv2.VideoCapture(0)
    t = 0
    image_num = total_time//interval + 1

    while t < image_num:
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        cv2.imshow('frame', rgb)
        out1 = cv2.imwrite('images/'+str(t)+'.jpg', frame)
        t += 1
        time.sleep(interval-0.3)
        
    cap.release()
    cv2.destroyAllWindows()
