from plugins.base_plugin.base_plugin import BasePlugin
from PIL import Image, ImageOps, ImageColor
import logging
import random
import os

from utils.image_utils import pad_image_blur

logger = logging.getLogger(__name__)

class test(BasePlugin):
    def generate_image(self, settings, device_config):

        # get image location
        image_location = self.get_plugin_dir("georgie.jpg")

        # Get dimensions
        dimensions = device_config.get_resolution()
        orientation = device_config.get_config("orientation")
        if orientation == "vertical":
            dimensions = dimensions[::-1]
            logger.debug(f"Vertical orientation detected, dimensions: {dimensions[0]}x{dimensions[1]}")

        try:
            # Use adaptive loader for memory-efficient processing
            image = self.image_loader.from_file(image_location, dimensions, resize=False)
            if not image:
                raise RuntimeError("Failed to load image from file")
            return image
        except Exception as e:
            logger.error(f"Failed to read image file: {str(e)}")
            raise RuntimeError("Failed to read image file.")