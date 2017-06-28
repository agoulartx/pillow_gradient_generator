import unittest
from gradient_image_generator.generate import (
    generate_image, fill_image)
from PIL import Image, ImageDraw


class GradientGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.img = generate_image(350, 150)
        self.draw = fill_image(self.img, 350, 150)

    def test_generator_returns_Image(self):
        self.assertIsInstance(self.img, Image.Image)



