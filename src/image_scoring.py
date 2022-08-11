import os
import numpy as np
from PIL import Image

class ImageScoring:
    def __init__(self,filePath):
        self.filePath = filePath
        self.imageList = self.importImages(filePath)
    
    #Method for reading images from a file path
    def importImages(self,filePath):
        imageList = []

        if os.path.isfile(filePath):
            img = Image.open(filePath)
            imageList.append(img)
            #img.close()            
        else:
            files = os.listdir(filePath)
            for item in files:
                img = Image.open(filePath+item)
                imageList.append(img)
                #img.close()

        return imageList

    #Method for writing images to a file path
    def exportImages(self,filePath,fileType,quality):
        for index,image in enumerate(self.imageList):

            imgName = "Image_Export"+str(index)+"."
            image.save(filePath+imgName+fileType.lower(),fileType,quality)
    
    def closePath(self):
        for image in self.imageList:
            image.close()

    #Method for resizing images
    def resize(self,sizeX=500,sizeY=500,quality=80,antialias=True):
        for index,image in enumerate(self.imageList):

            if antialias:
                imResize = image.resize((sizeX,sizeY), Image.ANTIALIAS)
            else:
                imResize = image.resize((sizeX,sizeY))

            self.imageList[index] = imResize

    #Method for symmetry scoring on images
    def symmetryScore(self, axis):
        symmetryScoreList = []

        for image in self.imageList:
            pixelArray = np.array(image, dtype=np.uint8)
            pixelRows,pixelCols,channels = pixelArray.shape

            if axis == 0:
                middle = (pixelCols/2)-1


            elif axis == 1:
                middle = (pixelRows/2)-1


            symmetryScoreList.append(1)

        return symmetryScoreList

    #Methods for brightness scoring on images
    def brightnessScore(self):
        brightnessScoreList = []

        for image in self.imageList:
            currBrightScore = 0
            brightnessScoreList.append(currBrightScore)
        
        return brightnessScoreList

    #Methods for contrast scoring on images
    def contrastScore():
        return

    #Method for intensity centroid score on images
    def intensityCentroidScore():
        return

'''

def main():
    pathImport = '/home/peterjr/Pictures/TestImages/TestImage.jpg'
    imageScore = ImageScoring(pathImport)
    pathSave = '/home/peterjr/Pictures/'
    imageScore.symmetryScore(axis=0)

if __name__ == "__main__":
    main()

'''

