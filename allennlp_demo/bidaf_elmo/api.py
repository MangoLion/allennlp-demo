import sys
import os
# This adds ../ to the PYTHONPATH, so that allennlp_demo imports work.
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))))

import allennlp_plugins.allennlp_models
from allennlp_demo.common import config, http

class BidafElmoModelEndpoint(http.ModelEndpoint):
    def __init__(self):
        c = config.Model.from_file(os.path.join(os.path.dirname(__file__), "model.json"))
        super().__init__(c)

if __name__ == "__main__":
    endpoint = BidafElmoModelEndpoint()
    endpoint.run()
