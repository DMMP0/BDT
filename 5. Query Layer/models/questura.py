from dataclasses import dataclass

@dataclass
class Questura:
    """Class for storing the arriving messages from cloud storage"""


    bankruptcy: int

    def __init__(self,bank_data):
            self.bankruptcy = bank_data[0]
