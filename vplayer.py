from tkinter import *
import cv2
from ffpyplayer.player import MediaPlayer


root = Tk()

root.mainloop()

path = 'c:\\Users\\ompra\\Videos\\'\
       '%5BHindi%5D_Deleting_A_Local_Remote_Branch_In_Git_-_Git_and_GitHub_Tutorials_for_'\
       'beginners_%2311(1080p).mp4'

val = ''
cap = MediaPlayer(path)
cap1 = cv2.VideoCapture(path)

while val != 'eof':
    frame, val = cap.get_frame()
    ret, frame1 = cap1.read()
    cv2.imshow('Video', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if val != 'eof' and frame is not None:
        vid, t = frame

cap1.release()
cv2.destroyAllWindows()
