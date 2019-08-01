"""
Main interface for the index.json file. Provides function to read informations out of it
"""


class IndexAdapter:
    def __init__(self, file):
        pass

    def get_mcmodmaker_build_ids(self) -> list:
        pass

    def get_supported_forge_build_ids(self) -> list:
        pass

    def get_adapters_for_forge_build_and_mcmodmaker_build(self, forge, mcmodmaker) -> list:
        pass

