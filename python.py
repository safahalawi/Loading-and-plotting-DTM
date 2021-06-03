# Import libraries
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from statistics import median

class ImageProcessing:

    def __init__(self):
        # Initializing variables
        self.img = ''
        self.max = 0
        self.min = 0
        self.avrg = 0.0
        self.median = 0.0
        self.list = []

    def setList(self, list):
        self.list = list

    def setMax (self):
        # This function finds maximum height
        self.max = max(self.list)
  
    def setMin (self):
        # This function finds minimum height
        self.min = min(self.list)
  
    def setAvrg (self):
        # This function finds average height
        self.avrg = sum(self.list) / len(self.list)
  
    def setMedian (self):
        # This function finds median 
        self.median = median(self.list)
  
    def plotMap (self, img_path):
        # This function plots terrain map
        img = mpimg.imread(img_path)
        imgplot = plt.imshow(img)
        plt.show()
  
    def __str__(self):
        # This function returns results in txt
        result = ""
        result += "Max: " + str(self.max) +'\n'
        result += "Min: " + str(self.min) +'\n'
        result += "Avrg: " + str(self.avrg) +'\n'
        result += "Median: " + str(self.median) +'\n'
        return result 


# Main code

# Loading data from tif 
img = Image.open(r"6501_50m_33.tif");
pixel_values = list(img.getdata())

# Creating object for ImageProcessing class
img_process = ImageProcessing()

# Finding max and minimum heights, average, and median
img_process.setList(pixel_values)
img_process.setMax()
img_process.setMin()
img_process.setAvrg()
img_process.setMedian()

# Printing the results
print(str(img_process))

# Plotting terrain map
img_process.plotMap(r"6501_50m_33.tif")