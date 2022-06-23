@dataclasses
class PersonalData:
    """ This class represents the data we get about the owners of the company"""

    # Constructor
    def __init__(self, fiscal_code: str, name: str, surname: str, sex: str, date_of_birth: str, ethnicity: str,
                 highest_degree: str, address: str, e_mail: str, telephone_number: str, state: str,
                 firm_registration_number: str):
        self._fiscal_code = fiscal_code
        self._name = name
        self._surname = surname
        self._sex_conversion = {"female":0,
                     "male":1,
                     "not declared":2,
                     "other":2}
        self.
        self._date_of_birth = date_of_birth
        self._ethnicity = ethnicity
        self._highest_degree = highest_degree
        self._address = address
        self._email = e_mail
        self._telephone_number = telephone_number
        self._state = state
        self._firm_registration_number = firm_registration_number

    # getters and setters
    def get_fiscal_code(self):
        return self._fiscal_code

    def set_fiscal_code(self, fiscal_code):
        # checks
        if fiscal_code == "":
            print("Couldn't modify fiscal code, string was empty")
            return
        # fiscal code is not generated correctly, so the checks will not be implemented

        self._fiscal_code = fiscal_code

    def get_name(self):
        return self._name

    def set_name(self, name):
        # checks
        if name == "":
            print("Couldn't modify name, string was empty")
            return
        # capitalize name
        name = name[0].upper() + name[1:]

        self._name = name

    def get_surname(self):
        return self._surname

    def set_surname(self, surname):
        # checks
        if surname == "":
            print("Couldn't modify surname, string was empty")
            return
        # capitalize name
        surname = surname[0].upper() + surname[1:]

        self._surname = surname

    def ge



