
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License. The full text
# of the license is available at
# https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.

#------------------------------------------------------------------------------#
# Imports
#------------------------------------------------------------------------------#

# Standard imports
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence
import colorsys
import cv2
import imageio


#------------------------------------------------------------------------------#
# Main Method
#------------------------------------------------------------------------------#

# #Runs the main method
# if __name__ == '__main__':
#     print(sys.argv[1])
#     fname, name = sys.argv[1], sys.argv[1].split(os.sep)[-1].split('.')[0]
#     print('Looking for file: ' + str(fname))
#     flag = load_flag(fname)
#     frames = wave_flag(flag)
#     print('Saving output as: ' + name + '.gif')
#     imageio.mimsave(name + '.gif', frames, duration=1/16)

#------------------------------------------------------------------------------#
#
#------------------------------------------------------------------------------#
class FlagWaver():
    def __init__(self, gradient, white, shadow):
        self.gradient = gradient
        self.white = white
        self.shadow = shadow
        #------------------------------------------------------------------------------#
        # Loading Data
        #------------------------------------------------------------------------------#

        print('Loading source files (this may take a few seconds)')

        # Getting the frames from the gradient
        # gradient_fname = os.path.join(f'{os.path.dirname(os.path.realpath(__file__))}/source', 'color_flag_mask.gif')
        # filename should be "color_flag_mask.gif"
        gradient_fname = self.gradient
        gradient = Image.open(gradient_fname)
        self.gradient_frames = np.array([np.array(frame.copy().convert('RGB').getdata(), dtype=np.uint8)
                                         .reshape(frame.size[1], frame.size[0], 3) for frame in ImageSequence.Iterator(gradient)])

        # Getting the frames from the pure white flag
        # white_fname = os.path.join(f'{os.path.dirname(os.path.realpath(__file__))}/source', 'white_flag.gif')
        # filenane should be "white_flag.gif"
        white_fname = self.white
        white = Image.open(white_fname)
        self.white_frames = np.array([np.array(frame.copy().convert('RGB').getdata(), dtype=np.uint8)
                                      .reshape(frame.size[1], frame.size[0], 3) for frame in ImageSequence.Iterator(white)])

        # Getting the frames from the shadow flag
        # shadow_fname = os.path.join(f'{os.path.dirname(os.path.realpath(__file__))}/source', 'white_flag_shadow.gif')
        # filename should be "white_flag_shadow.gif"
        shadow_fname = self.shadow
        shadow = Image.open(shadow_fname)
        self.shadow_frames = np.array([np.array(frame.copy().convert('RGB').getdata(), dtype=np.uint8)
                                       .reshape(frame.size[1], frame.size[0], 3) for frame in ImageSequence.Iterator(shadow)])

        print('Finished loading source files')

    #------------------------------------------------------------------------------#
    # Wave Flag
    #------------------------------------------------------------------------------#

    # Returns the set of images in a waving flag
    def wave_flag(self, flag):

        # Converting the flag to a new color
        color_frames = []
        for i in range(len(self.gradient_frames)):

            # Pulling out the appropriate images
            mask = self.gradient_frames[i].copy()
            white = self.white_frames[i].copy()
            color = self.white_frames[i].copy()
            shadow = self.shadow_frames[i].copy()

            # Finding the parts of the image that are the flag
            part_of_flag = mask[:, :, 0] != 0

            # Getting the safe part of the blur
            wblur = white.copy()
            wblur[~part_of_flag], wblur[part_of_flag] = 0, 255
            wblur = cv2.blur(wblur, (10, 10))
            wblur[wblur != 255] = 0
            wblur = wblur.astype(bool)

            # Creating blurred image
            blur = cv2.blur(mask, (10, 10))
            mask[wblur] = blur[wblur]

            # Converting pixels where the gradient is non-zero
            hits = mask[part_of_flag]  # blur[part_of_flag]
            x = ((hits[:, 1] / 256) * flag.shape[1]).astype(int)  # 1
            y = ((hits[:, 2] / 256) * flag.shape[0]).astype(int)  # 0

            # Adding color
            color[part_of_flag] = [flag[val] for val in zip(y, x)]

            # Applying shadow
            shadow_mask = ((white - shadow)[:, :, 0] > 40)
            hits = color.reshape(-1, 3)[shadow_mask.ravel()]

            # Applying shadow
            OFFSET = 20
            for i, hit in enumerate(hits):
                hls = colorsys.rgb_to_hls(*hit.astype(int))
                hls = (hls[0], max(hls[1]-OFFSET, 0), hls[2])
                hits[i] = colorsys.hls_to_rgb(*hls)

            # Applying shadow
            color.reshape(-1, 3)[shadow_mask.ravel()] = hits

            # Saving the converted frame
            color_frames.append(color)

        # Returning the color frames
        return color_frames

    # Loads the flag as a numpy array from a file
    def load_flag(self, fname):
        flag = Image.open(fname)
        flag = np.array(flag.convert('RGB').getdata(), dtype=np.uint8)\
            .reshape(flag.size[1], flag.size[0], 3)
        return flag

    #------------------------------------------------------------------------------#
    # Display Flag
    #------------------------------------------------------------------------------#

    def create_gif(self, file_path):
        fname, name = file_path, file_path.split(os.sep)[-1].split('.')[0]
        print('Looking for file: ' + str(fname))
        flag = self.load_flag(fname)
        frames = self.wave_flag(flag)
        print('Saving output as: ' + name + '.gif')
        imageio.mimsave(name + '.gif', frames, duration=1/16)

    #------------------------------------------------------------------------------#
    # Display Flag
    #------------------------------------------------------------------------------#

    def imshow(self, image):
        plt.imshow(image)
        plt.show()

# flag_waver = FlagWaver()