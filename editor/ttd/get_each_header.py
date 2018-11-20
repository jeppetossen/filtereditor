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

    def test_get_block_id(self):
        filter = "editor/ttd/headers.json"
        tier_ids = dict()

        with open(filter, "r") as f:
            data = json.load(f)
            for head in data:
                for subhead in data[head]:
                    for i, tier in enumerate(data[head][subhead]):
                        for tier_id in data[head][subhead][tier]:
                            tier_ids[tier] = tier_id
            f.close()
        return tier_ids

