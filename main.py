import cv2

webcam = cv2.VideoCapture(0)
webcam1 = cv2.VideoCapture(2)

if not webcam.isOpened() or not webcam1.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened() and webcam1.isOpened():
    status, frame = webcam.read()
    status1, frame1 = webcam1.read()

    if status and status1:
        cv2.imshow("Cam0", frame)
        cv2.imshow("Cam1", frame1)
        cv2.moveWindow("Cam0", 0, 0)
        cv2.moveWindow("Cam1", 960, 0)
        cv2.resizeWindow("Cam0", 960, 1000)
        cv2.resizeWindow("Cam1", 960, 1000)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
webcam1.release()
cv2.destroyAllWindows()