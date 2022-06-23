class CriminalRecords:
    # TODO: add string descriptor

    def __init__(self, fiscal_code: str, bankruptcy: bool, fraudis: bool, investigation: bool,
                 accused: bool, condemned: bool, civ_pass: bool):
        self._civ_pass = civ_pass
        self._condemned = condemned
        self._accused = accused
        self._investigation = investigation
        self._fraudis = fraudis
        self._bankruptcy = bankruptcy
        self._fiscal_code = fiscal_code

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
        
    def get_bankruptcy(self) -> bool:
        return self._bankruptcy

    # TODO: check for fraudis
    def set_bankruptcy(self, bankruptcy: bool):
        """if bankruptcy is set to true, then condemned will be set to true too"""
        # checks
        if bankruptcy:
            self._condemned = True

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

    def get_fraudis(self) -> bool:
        return self._fraudis

    def set_fraudis(self, fraudis: bool):
        # checks

        self._fraudis = fraudis

