from asyncio.windows_events import NULL
from Stitcher import Stitcher
import cv2

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import sys

# 读取拼接图片
# imageA = cv2.imread("left_01.png")
# imageB = cv2.imread("right_01.png")
# src = cv2.resize(imageA, (imageA.shape[1]//4, imageA.shape[0]//4))
# tar = cv2.resize(imageB, (imageB.shape[1]//4, imageB.shape[0]//4))

# 把图片拼接成全景图
stitcher = Stitcher()
# (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# 显示所有图片
# cv2.imshow("Image A", imageA)
# cv2.imshow("Image B", imageB)
# cv2.imshow("Keypoint Matches", vis)
# cv2.imshow("Result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

class knnmatch:
    def main():
        pass

class UI_Image(QWidget):
    def __init__(self, parent=None):
        super(UI_Image, self).__init__(parent)
        self.evaluatedebugWalk()



    
    def evaluatedebugWalk(self):
            filepath = QFileDialog.getExistingDirectory(self, "Open Image Dir", QDir.currentPath())
            print("filePath:", filepath)
            fileleft = ''
            fileright = ''
            for root , dirs, files in os.walk(filepath):
                if len(files) > 0:
                    for file in files:
                        if file.startswith("0_"):
                            fileleft = os.path.join(root, file)
                            print("fileleft = ", fileleft)
                        elif file.startswith("2_"):
                            fileright = os.path.join(root, file)
                            print("fileright = ", fileright)
                    imageA = cv2.imread(fileleft)
                    imageB = cv2.imread(fileright)
                    # src = cv2.resize(imageA, (imageA.shape[1]//4, imageA.shape[0]//4))
                    # tar = cv2.resize(imageB, (imageB.shape[1]//4, imageB.shape[0]//4))
                    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
                    cv2.imshow("Keypoint Matches", vis)
                    cv2.imshow("Result", result)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m_ui = UI_Image()
    m_ui.show()
    sys.exit(app.exec_())