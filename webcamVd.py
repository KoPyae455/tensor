import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def main():
    cap = cv.VideoCapture(0)

    print("width" + str(cap.get(3)))
    print("height" + str(cap.get(4)))
    cap.set(3,640)
    cap.set(4,480)

    if cap.isOpened():
        ret,frame = cap.read()
    else:
        ret = False

    while(ret):
        ret,frame = cap.read()
        cv.imshow("live video", frame)

        k = cv.waitKey(1)
        if k == 27:
            break

    cv.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()