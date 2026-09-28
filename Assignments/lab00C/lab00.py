# -*- coding: utf-8 -*-
"""Lab 00 — Introduction: Simple Image Processing.

Welcome to your first lab!  The goal is to get comfortable with the lab
workflow: implement a class in this file, run an evaluation script to see your
results.

Task
----
Implement the two methods inside the SimpleImageProcessing class:

  add_blur(image, **kwargs)
      Apply Gaussian blur to image.  Use the 'ksize' keyword argument
      (default 15) to control the kernel size (must be a positive odd integer).

  add_sharpen(image, **kwargs)
      Sharpen image using an unsharp-mask approach (subtract a blurred version
      from the original, scaled by a 'strength' keyword argument (default 1.5)).

Both methods should return the processed image as a uint8 numpy array with the
same shape as the input.
"""
import cv2
import numpy as np
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from helpers.dataloader import get_data_path, load_image  # noqa: F401




class SimpleImageProcessing:
    """Class implementing spatial-domain Gaussian blur and unsharp mask sharpening."""

    def __init__(self):
        pass

    def add_blur(self, image, **kwargs):
        """Apply Gaussian blur to the input image.

        Args:
            image (ndarray): H x W x 3 or H x W uint8 array.
            **kwargs:
                ksize (int): Gaussian kernel size (default 15).

        Returns:
            ndarray: Blurred uint8 array of same shape.
        """
        ksize = kwargs.get('ksize', 15)
        # ksize in GaussianBlur must be a tuple of positive odd integers (ksize, ksize)
        blurred = cv2.GaussianBlur(image, (ksize, ksize), 0)
        return blurred

    def add_sharpen(self, image, **kwargs):
        """Sharpen image using unsharp masking.

        Args:
            image (ndarray): H x W x 3 or H x W uint8 array.
            **kwargs:
                ksize (int): Gaussian kernel size for internal blur (default 15).
                strength (float): Strength of sharpening effect (default 1.5).

        Returns:
            ndarray: Sharpened uint8 array of same shape.
        """
        ksize = kwargs.get('ksize', 15)
        strength = kwargs.get('strength', 1.5)

        # 1. Create blurred baseline
        blurred = cv2.GaussianBlur(image, (ksize, ksize), 0)

        # 2. Weighted sum: (1 + strength) * original - strength * blurred
        sharpened = cv2.addWeighted(
            image, 1.0 + strength, blurred, -strength, 0
        )

        # 3. Clip to [0, 255] range and cast back to uint8
        sharpened_clipped = np.clip(sharpened, 0, 255).astype(np.uint8)
        return sharpened_clipped