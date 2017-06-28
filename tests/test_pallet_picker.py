from unittest import TestCase
from random import randrange
from gradient_image_generator.pallet_picker import pallets, pallet_picker


class GradientColorPickerTest(TestCase):
    def setUp(self):
        self.color_one, self.color_two = pallet_picker(randrange(1, 11))

    def test_has_color_pallet(self):
        self.assertTrue(pallets)

    def test_pallet_picker_return_two_colors(self):
        self.assertTrue(self.color_one)
        self.assertTrue(self.color_two)

    def test_initial_color_and_final_color_are_different(self):
        self.assertNotEqual(self.color_one, self.color_two)


