# from nis import match
import matplotlib.pyplot as plt
import numpy as np
import cv2

def cv_show(strName, image):
    cv2.imshow(strName, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

imageA = cv2.imread("0_left.png",0)
imageB = cv2.imread("2_right.png",0)
# cv_show('A',imageA)
# cv_show('B',imageB)

sift = cv2.SIFT_create()

kp1, desc1 = sift.detectAndCompute(imageA, None)
kp2, desc2 = sift.detectAndCompute(imageB, None)

bf = cv2.BFMatcher(crossCheck = True)

matches = bf.match(desc1,desc2)
matches = sorted(matches, key=lambda x:x.distance)

print("len(matches) = ", len(matches))
print(matches[:1])

img3 = cv2.drawMatches(imageA, kp1, imageB, kp2, matches[:15],None, flags=2)  # 一对一匹配

cv_show('img3',  img3)

# 一对多匹配

# kbf = cv2.BFMatcher()
# Kmatches = kbf.knnMatch(desc1,desc2,k=2)
# # Kmatches = kbf.match(desc1,desc2)
# good=[]

# # for m in Kmatches:
# #     for n in Kmatches:
# #         # if (m != n and m.distance < n.distance * 0.75):
# #         if m.distance < n.distance * 0.75:
# #             good.append([m])
#             # pass
# for m,n in Kmatches:
#     if m.distance < 0.75 * n.distance:
#         good.append([m])
# img3Knn = cv2.drawMatchesKnn(imageA, kp1, imageB, kp2, good[:20], None, flags=2)
# cv_show('img3Knn', img3Knn)
