import numpy as np
from PIL import Image

class ImageScoring:
    def __init__(self,filePath):
        self.filePath = filePath
        self.imageList = self.importImage(filePath)
    
    #Method for reading images from a file path
    def importImages(self,filePath):
        imageList = []
        #Check if folder or individual file here
        img = Image.open(filePath)
        imageList.append(img)
        return imageList

    #Method for writing images to a file path
    def exportImages(self,filePath,fileType,quality):
        for index,image in enumerate(self.imageList):

            imgName = "Image_Export"+str(index)+"."
            image.save(filePath+imgName+fileType.lower(),fileType,quality)
        
    #Method for resizing images
    def resize(self,sizeX=500,sizeY=500,quality=80,antialias=True):
        for index,image in enumerate(self.imageList):

            if antialias:
                imResize = image.resize((sizeX,sizeY), Image.ANTIALIAS)
            else:
                imResize = image.resize((sizeX,sizeY))

            self.imageList[index] = imResize

    #Method for symmetry scoring on images
    def symmetryScore(self):
        symmetryScoreList = []

        for image in self.imageList:
            currSymScore = 0
            symmetryScoreList.append(currSymScore)

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
    pathImport = '/home/peterjr/Pictures/TestImages'
    imageScore = ImageScoring(pathImport)
    pathSave = '/home/peterjr/Pictures/'

    imageScore.export(imageScore.imageList,pathSave)
    #print(imageScore.imageList)
    imageScore.symmetryScore(imageScore.imageList,allImages=False)


if __name__ == "__main__":
    main()
'''


