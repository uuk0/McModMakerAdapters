"""
Main interface for the index.json file. Provides function to read informations out of it
"""

import json


class IndexAdapter:
    def __init__(self, file):
        with open(file) as f:
            self.data = json.load(f)

    def get_mcmodmaker_build_ids(self) -> list:
        return self.data["forge_versions"].keys()

    def get_supported_forge_build_ids(self) -> list:
        return self.data["mcmodmaker_versions"].keys()

    def get_adapters_for_forge_build_and_mcmodmaker_build(self, forge, mcmodmaker) -> list:
        pass

