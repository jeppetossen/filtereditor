from django.test import TestCase
from pprint import pprint


# Create your tests here.
class ItemTypesTest(TestCase):

    def test_read_item_classes(self):
        with open("editor/items/ItemClasses.txt", "r") as f:
            for line in f:
                pprint(line)

    def test_read_item_base_types(self):
        with open("editor/items/ItemBaseTypes.txt", "r") as f:
            for line in f:
                pprint(line)
