import cv2
import numpy as np

# def detectAndDescribe(image, method=None):
#     """
#     Compute key points and feature descriptors using an specific method
#     """
#     # assert method is not None, "You need to define a feature detection method. Value
#     # detect and extract features from the image
#     if method == 'sift':
#         # descriptor = cv2.xfeatures2d.SIFT_create()
#         descriptor = cv2.SIFT_create()
#     elif method == 'surf':
#         descriptor = cv2.xfeatures2d.SURF_create()
#         # cv2.SURF_create()
#         # descriptor = cv2.SURF_create()
#     elif method == 'brisk':
#         descriptor = cv2.BRISK_create()
#     elif method == 'orb':
#         descriptor = cv2.ORB_create()
#     # get keypoints and descriptors
#     (kps, features) = descriptor.detectAndCompute(image, None)
#     return (kps, features)



# def createMatcher(method,crossCheck):
#     # "Create and return a Matcher Object"
#     if method == 'sift' or method == 'surf':
#         bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=crossCheck)
#     elif method == 'orb' or method == 'brisk':
#         bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=crossCheck)
#     return bf

# # Apply panorama correction
# width = trainImg.shape[1] + queryImg.shape[1]
# height = trainImg.shape[0] + queryImg.shape[0]
# result = cv2.warpPerspective(trainImg, H, (width, height))
# result[0:queryImg.shape[0], 0:queryImg.shape[1]] = queryImg
# plt.figure(figsize=(20,10))
# plt.imshow(result)
# plt.axis('off')

# 12 plt.show()


def knnmatch(file1, file2):
    ###
    # 读取图像
    imageA= cv2.imread(file1)
    imageB = cv2.imread(file2)


    #  转换为gray
    gray1 = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # 构建sift 对象，求特征点和特征向量
    sift = cv2.SIFT_create()

    kpsA, dpA = sift.detectAndCompute(gray1, None)
    kpsB, dpB = sift.detectAndCompute(gray2, None)
    # 构建bfmatcher 对象
    bf = cv2.BFMatcher()

    # 用knnmatch方法匹配关键点
    matches = bf.knnMatch(dpA, dpB, 2)

    good_matches = []
    # 手动去除不可靠匹配
    for m in matches:
        if len(m) == 2 and m[0].distance < 0.9 * m[1].distance:
            good_matches.append((m[0].queryIdx, m[0].trainIdx))


    #可靠的匹配转换数据类型
    kps1 = np.float32([kp.pt for kp in kpsA ]) #  求出所有关键点的坐标
    kps2 = np.float32([kp.pt for kp in kpsB ])

    # kps1 = np.float32([kps1[a[0]] for a in good_matches])  #  求出所有可靠关键点的坐标
    # kps2 = np.float32([kps2[a[1]] for a in good_matches])

    # image = cv2.drawMatchesKnn(imageA, kps1, imageB, kps2, good_matches, None, flags=2)
    # image = cv2.drawMatchesKnn(imageA, kpsA, imageB, kpsB, good_matches, None, flags=2)

    kps1 = np.float32([kps1[a[0]] for a in good_matches])  #  求出所有可靠关键点的坐标
    kps2 = np.float32([kps2[a[1]] for a in good_matches])

    # 求转换矩阵
    M, status = cv2.findHomography(kps2, kps1, cv2.RANSAC, 3.0)

    # 图像拼接
    result = cv2.warpPerspective(imageB, M, (imageA.shape[1] + imageB.shape[1], imageB.shape[0]))
    result[0:imageA.shape[0], 0:imageA.shape[1]] = imageA

    cv2.imwrite('result.png', result)

    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ###
if __name__ == '__main__':
    knnmatch('0_left.png', '2_right.png')
