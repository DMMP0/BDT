class CriminalRecords:
    # TODO: add string descriptor

    def __init__(self):
        self._civ_pass = False
        self._condemned = False
        self._accused = False
        self._investigation = False
        self._bankruptcy = 0
        self._fiscal_code = ""

    # getters and setters
    def get_fiscal_code(self) -> str:
        return self._fiscal_code

    def set_fiscal_code(self, fiscal_code: str):
        # checks
        if fiscal_code == "":
            print("Couldn't modify fiscal code, string was empty")
            return
        # fiscal code is not generated correctly, so the checks will not be implemented

        self._fiscal_code = fiscal_code
        
    def get_bankruptcy(self) -> int:
        return self._bankruptcy

    def set_bankruptcy(self, bankruptcy: int):
        """0 = no bankruptcy \n
        1 = bankruptcy \n
        2 = no bankruptcy"""
        # checks
        if bankruptcy < 0 or bankruptcy > 2:
            print("Bankrupcy was not set due to a value grater than 2 or inferior to 0")
            return

        self._bankruptcy = bankruptcy

    def get_civ_pass(self) -> bool:
        return self._civ_pass

    def set_civ_pass(self, civ_pass: bool):
        # checks

        self._civ_pass = civ_pass

    def get_condemned(self) -> bool:
        return self._condemned

    def set_condemned(self, condemned: bool):
        # checks

        self._condemned = condemned

    def get_accused(self) -> bool:
        return self._accused

    def set_accused(self, accused: bool):
        # checks

        self._accused = accused

    def get_investigation(self) -> bool:
        return self._investigation

    def set_investigation(self, investigation: bool):
        # checks

        self._investigation = investigation


