# Import the necessary libraries
import cv2 
import numpy as np
import os

class Input:

    def __init__(self):
        return

    def take_file(self, filename, image_direction = "Right"):
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in [".csv"]:
            array = self.read_dataset_csv(filename)
            return array
        elif file_ext in [".jpg", ".png"]:
            array = self.read_dataset_img(filename, image_direction)
            return array
        else:
            raise ValueError("Error, file type not matching")
        

    # input for csv files that will convert to numpy files for processing
    def read_dataset_csv(self, filename):
        data = np.loadtxt(filename, delimiter= ",")
        # return the transposed data
        return data.T

    # load the image and convert into numpy array of avg
    # of r g b values
    def read_dataset_img(self, imgName, direction="Right"):
        # used to convert images to a numpy array

        image = cv2.imread(imgName)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # get image dimensions (height, width, channels)
        height, width, _ = image.shape

        # list to store average R, G, and B values for each column
        avg_r_values = []
        avg_g_values = []
        avg_b_values = []

        avg_rgb_values = []

        if direction == "Right":
            for col in range(width):
                column_pixels = image[:, col, :]
                avg_r_values.append(np.mean(column_pixels[:, 0]))
                avg_g_values.append(np.mean(column_pixels[:, 1]))
                avg_b_values.append(np.mean(column_pixels[:, 2]))

        elif direction == "Left":
            for col in range(width - 1, -1, -1):
                column_pixels = image[:, col, :]
                avg_r_values.append(np.mean(column_pixels[:, 0]))
                avg_g_values.append(np.mean(column_pixels[:, 1]))
                avg_b_values.append(np.mean(column_pixels[:, 2]))

        elif direction == "Up":
            for row in range(height - 1, -1, -1):
                row_pixels = image[row, :, :]
                avg_r_values.append(np.mean(row_pixels[:, 0]))
                avg_g_values.append(np.mean(row_pixels[:, 1]))
                avg_b_values.append(np.mean(row_pixels[:, 2]))

        elif direction == "Down":
            for row in range(height):
                row_pixels = image[row, :, :]
                avg_r_values.append(np.mean(row_pixels[:, 0]))
                avg_g_values.append(np.mean(row_pixels[:, 1]))
                avg_b_values.append(np.mean(row_pixels[:, 2]))


        # convert lists to NumPy arrays for computation
        avg_r_values = np.array(avg_r_values)
        avg_g_values = np.array(avg_g_values)
        avg_b_values = np.array(avg_b_values)

        avg_rgb_values = np.stack((avg_r_values, avg_g_values, avg_b_values), axis=0)

        return avg_rgb_values