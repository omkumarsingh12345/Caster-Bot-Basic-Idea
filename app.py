Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import cv2
... 
... cap = cv2.VideoCapture("gameplay.mp4")
... 
... while cap.isOpened():
...     success, frame = cap.read()
...     if not success:
...         break
... 
...     # Show current frame
...     cv2.imshow("Gameplay", frame)
... 
...     # Press Q to quit
...     if cv2.waitKey(25) & 0xFF == ord('q'):
...         break
... 
... cap.release()
... cv2.destroyAllWindows()
