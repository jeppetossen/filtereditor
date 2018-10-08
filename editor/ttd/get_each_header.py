from django.test import TestCase
from pprint import pprint
import json


class GetEachHeaderTest(TestCase):

    def test_get_first_head(self):
        filter = "editor/ttd/headers.json"

        with open(filter, "r") as f:
            data = json.load(f)
            for i, head in enumerate(data):
                for e, sub in enumerate(data[head]):
                    for k, tier in enumerate(data[head][sub]):
                        pass
            f.close()
