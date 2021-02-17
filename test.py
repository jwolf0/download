import cv2
import apriltag
print("cv2 version=",cv2.__version__)

#flipmethod = 0 leaves camera as is, flipmethod = 2 flips horizontal axis
camSet='nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1, format=NV12 ! nvvidconv flip-method=2 ! video/x-raw, width=800, height=600, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
while True:
    _, frame = cam.read()
    cv2.imshow('my_cam', frame)
    cv2.moveWindow('my_cam', 0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()