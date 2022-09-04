from tkinter.tix import Tree
from Stitcher import Stitcher

import cv2

imageA = cv2.imread("left_01.jpg")
imageB = cv2.imread("right_01.jpg")

stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)


cv2.imshow("ImageA", imageA)
cv2.imshow("ImageB", imageB)

cv2.imshow("keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()