from ast import main
from tkinter.tix import Tree
from Stitcher import Stitcher

import cv2

imageA = cv2.imread("0_left.png")
imageB = cv2.imread("2_right.png")

stitcher = Stitcher()
result = stitcher.stitch([imageA, imageB], showMatches=True)


# cv2.imshow("ImageA", imageA)
# cv2.imshow("ImageB", imageB)

# cv2.imshow("keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


def evaluatedebugWalk(self):
        filepath = QFileDialog.getExistingDirectory(self, "Open Image Dir", QDir.currentPath())
        print("filePath:", filepath)
        fileleft = ''
        fileright = ''
        for root , dirs, files in os.walk(filepath):
            if files is not NULL:
                for file in files:
                    if file.startswith("0_"):
                        fileleft = os.path.join(root, file)
                        print("fileleft = ", fileleft)
                    elif file.startswith("2_"):
                        fileright = os.path.join(root, file)
                        print("fileright = ", fileright)
                print(files)
                dirpath = fileleft.split("/")[-1]
                tmpfolder = os.path.exists(TMP_PATH + dirpath)
                if not tmpfolder:
                    os.makedirs(TMP_PATH + dirpath)
                self.work.leftImagePath = self.getImagePath(fileleft, dirpath + "/0_left")
                self.work.rightImagePath = self.getImagePath(fileright, dirpath + "/2_right")
                self.showImage(self.leftLabel, self.work.leftImagePath)
                self.showImage(self.rightLabel, self.work.rightImagePath)
                self.work.debugPath = TMP_PATH + dirpath
                self.work.evaluate()

if __main__ == main():
    