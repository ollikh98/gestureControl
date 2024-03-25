import cv2
import mediapipe.tasks.python.vision as mpVision
import mediapipe as mp
import time
import math

class HandTracker():
    def __init__(self, mode='LIVE_STREAM', numHands=2,detectConf = 0.5, presenceConf = 0.5 , trackConf = 0.5):
        self.mode = mode
        self.numHands = numHands
        self.detectConf = detectConf 
        self.trackConf = trackConf
        self.presenceConf = presenceConf
    
        self.hands = mpVision.HandLandmarker(self.mode,self.numHands,self.detectConf,self.presenceConf, self.trackConf)
        
    def findHands(self,frame,draw=True):
        imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
def main():
    cap = cv2.VideoCapture(0)
    
    hands = HandTracker()
    
    while True:
        success, frame = cap.read()
        
        
        
# class GestureTracker()
#     self.gestures = mpVision.GestureRecognizer(self.mode,self.numHands,self.detectConf,self.presenceConf, self.trackConf)
        
        
        
        
        
