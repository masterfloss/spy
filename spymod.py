# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 01:52:28 2022

@author: Carlos Costa
"""

import cv2
import urllib.request
import numpy as np

class Spy:
    
    """
    Spy
    ...

    Methods
    -------
    convUnicode(self,message):
        convert charts into Unicode code.
    
    readimage(self,image_location):
        read image and return the string with the information of image.
      
    gcd(self,x, y):
        returns pattern.
    
    hide(self,image_location, msg):
        hide image into an image.
    
    show(self,img_loc):
        returns a message hidden in an image.
    """    
    
    def convUnicode(self,message):
        """convert charts into Unicode code.
        Parameters
        ----------
        message : str
            text to be converted 
        """
  
        for c in message:
            yield ord(c)
    
    def readimage(self,image_location):
        """read image and return the string with the information of image.
        Parameters
        ----------
        image_location : str
            location and name of image
        """
        
        url_response = urllib.request.urlopen(image_location)
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)
        
        #img = cv2.imread(image_location)
        return img
    
    def gcd(self,x, y):
        """returns pattern.
        Parameters
        ----------
        x : int
            image width
        y : int
            image height
        """
        while(y):
            x, y = y, x % y
        return x
    
    def hide(self,image_location, msg):
        """hide image into an image.
        Parameters
        ----------
        image_location : str
            location and name of image
        message : str
            text to be converted 
        """           
        img = self.readimage(image_location)
        msg_gen = self.convUnicode(msg)
        pattern = self.gcd(len(img), len(img[0]))
        for i in range(len(img)):
            for j in range(len(img[0])):
              if (i+1 * j+1) % pattern == 0:
                try:
                  img[i-1][j-1][0] = next(msg_gen)
                except StopIteration:
                  img[i-1][j-1][0] = 0
                  return img
    
    def show(self,img_loc):
        """returns a message hidden in an image.
        Parameters
        ----------
        image_location : str
            location and name of image
        """         
        img = self.readimage(img_loc)
        pattern = self.gcd(len(img), len(img[0]))
        message = ''
        for i in range(len(img)):
          for j in range(len(img[0])):
            if (i-1 * j-1) % pattern == 0:
              if img[i-1][j-1][0] != 0:
                message = message + chr(img[i-1][j-1][0])
              else:
                return message
         