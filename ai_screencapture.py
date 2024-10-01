import mss
import pyautogui
import  cv2 as cv
import numpy as np
import time
import math
import multiprocessing as mp


class ScreenCaptureAgent:
    def __init__(self) -> None:
        self.img = None
        self.capture_process = None
        self.fps = None
        self.enable_cv_preview = True
  
        self.w, self.h = pyautogui.size()
        print("Screen Resolution:   " + "w: " + str(self.w)  +   "   h:  " +   str(self.h)) 
    def start_capture(self):
        self.monitor = {"top": 0, "left": 0, "width": self.w, "height": self.h}
       
       
       
    def capture_screen(self):
        fps_report_time= time.time()
        fps_report_delay = 5
        n_frames = 1
        with mss.mss() as sct:
            while True:
                self.img = sct.grab(monitor=self.monitor)
                self.img = np.array(self.img)


            if self.enable_cv_preview:
                small = cv.resize(self.img, (0, 0), fx=0.5, fy=0.5)
                cv.imshow("Computer Vision", small)
                cv.waitKey(1)
    
                elapsed_time = time.time() - fps_report_time

                if elapsed_time >= fps_report_delay:
                    self.fps = (n_frames / elapsed_time)
                    print(f"FPS: {self.fps:.2f}")
                n_frames += 1
             

cv.destroyAllWindows()