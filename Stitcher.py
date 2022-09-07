from matplotlib import image
import numpy as np
import cv2

class Stitcher:

    def stitch(self, images, ratio=0.75, reprojThresh=4.0, showMatches=False):
        
        (imageB, imageA) = images
        (kpsA, featuresA) = self.detectAndDescribe(imageA)
        (kpsB, featuresB) = self.detectAndDescribe(imageB)

        M = self.matchKeypoints(kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh)
        
        if M is None:
            return None

        (matches, H, status) = M
        result = cv2.warpPerspective(imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))

        self.cv_show('result', result)

        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB

        # self.cv_show('result', result)

        # if showMatches:
        #     # pass
        #     # vis = self.drawMatches(imageA, imageB, kpsA, kpsB, matches)
        #     vis = cv2.drawMatchesKnn(imageA, kpsA[0], imageB, kpsB[1], matches, None, flags=2)

        return result

    # def drawMatches(imageA, imageB, kpsA, kpsB, matches):
    #     image = cv2.drawMatchesKnn(imageA, kpsA, imageB, kpsB, matches, None, flags=2)
    #     return image

    def cv_show(self, strName, image):
        cv2.imshow(strName, image)


    def detectAndDescribe(self, image):
         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

         descriptor = cv2.SIFT_create()

         (kps, features) = descriptor.detectAndCompute(gray, None)

         kps = np.float32([kp.pt for kp in kps])

         return (kps, features)

    def matchKeypoints(self, kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh):
        
        # 建立暴力匹配机制
        matcher = cv2.BFMatcher()

        # 使用KNN检测来自AB图的SIFT特征匹配对， K=2
        rawMatches = matcher.knnMatch(featuresA, featuresB, 2)

        matches = []

        for m in rawMatches:
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))


        if len(matches) > 4:
            ptsA = np.float32([kpsA[i] for (_, i) in matches])
            ptsB = np.float32([kpsB[i] for (i, _) in matches])

            (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, reprojThresh)

            return (matches, H, status)
