import numpy as np
import cv2

def func(path):
    frame = cv2.imread(path)
    frame = cv2.resize(frame, (128, 128))
    converted2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBoundary = np.array([0, 40, 30], dtype="uint8")
    upperBoundary = np.array([43, 255, 254], dtype="uint8")
    skinMask = cv2.inRange(converted, lowerBoundary, upperBoundary)
    skinMask = cv2.addWeighted(skinMask, 0.5, skinMask, 0.5, 0.0)
    skinMask = cv2.medianBlur(skinMask, 5)

    skin = cv2.bitwise_and(converted2, converted2, mask=skinMask)
    img2 = cv2.Canny(skin, 60, 60)
    img2 = cv2.resize(img2, (256, 256))

    sift = cv2.SIFT_create()
    kp, des = sift.detectAndCompute(img2, None)

    if des is None:
        des = np.array([])

    return des
def func2(path):
    frame = cv2.imread(path)
    frame = cv2.resize(frame, (128, 128))
    converted2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerBoundary = np.array([0, 40, 30], dtype="uint8")
    upperBoundary = np.array([43, 255, 254], dtype="uint8")
    skinMask = cv2.inRange(converted, lowerBoundary, upperBoundary)
    skinMask = cv2.addWeighted(skinMask, 0.5, skinMask, 0.5, 0.0)
    skinMask = cv2.medianBlur(skinMask, 5)

    skin = cv2.bitwise_and(converted2, converted2, mask=skinMask)
    img2 = cv2.Canny(skin, 60, 60)
    img2 = cv2.resize(img2, (256, 256))

    orb = cv2.ORB_create()
    kp, des = orb.detectAndCompute(img2, None)

    if des is None:
        des = np.array([])

    return des
