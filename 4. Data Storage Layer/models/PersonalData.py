def sex_converter(sex):
    to_outside = {0: "female",
                  1: "male",
                  2: "other"}
    to_class = {"female": 0,
                "male": 1,
                "other": 2}

    if type(sex) is str:
        if sex in to_class:
            return to_class[sex]
        else:
            return to_class[2]
    else:
        if sex in range(0, 2):
            return to_outside[sex]
        else:
            return to_outside[2]


class PersonalData:
    """ This class represents the data we get about the owners of the company"""

    # Constructor
    def __init__(self, fiscal_code: str, name: str, surname: str, sex: str, date_of_birth: str, ethnicity: str,
                 highest_degree: str, address: str, e_mail: str, telephone_number: str, state: str,
                 firm_registration_number: str):
        self._fiscal_code = fiscal_code
        self._name = name
        self._surname = surname
        self._sex = sex_converter(sex)
        self._date_of_birth = date_of_birth
        self._ethnicity = ethnicity
        self._highest_degree = highest_degree
        self._address = address
        self._email = e_mail
        self._telephone_number = telephone_number
        self._state = state
        self._firm_registration_number = firm_registration_number

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

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        # checks
        if name == "":
            print("Couldn't modify name, string was empty")
            return
        # capitalize name
        name = name[0].upper() + name[1:]

        self._name = name

    def get_surname(self) -> str:
        return self._surname

    def set_surname(self, surname: str):
        # checks
        if surname == "":
            print("Couldn't modify surname, string was empty")
            return
        # capitalize name
        surname = surname[0].upper() + surname[1:]

        self._surname = surname

    def get_sex(self) -> str:
        return sex_converter(self._sex)

    def set_sex(self, sex: str):
        self._sex = sex_converter(sex)

    def get_DOB(self) -> str:
        return self._date_of_birth

    def set_DOB(self, date_of_birth: str):
        # checks
        if date_of_birth == "":
            print("Date of birth was empty, could not update")
            return
            # TODO: add other checks

        self._date_of_birth = date_of_birth

    def get_ethnicity(self) -> str:
        return self._ethnicity

    def set_ethnicity(self, ethnicity: str):
        # checks
        if ethnicity == "":
            print("Couldn't modify ethnicity, string was empty")
            return

        self._ethnicity = ethnicity

    def get_highest_degree(self) -> str:
        return self._highest_degree

    def set_highest_degree(self, highest_degree: str):
        # checks
        if highest_degree == "":
            print("Couldn't modify highest_degree, string was empty")
            return

        self._highest_degree = highest_degree

    def get_address(self) -> str:
        return self._address

    def set_address(self, address: str):
        # checks
        if address == "":
            print("Couldn't modify address, string was empty")
            return

        self._address = address

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        # TODO: add checks
        if email == "":
            print("Couldn't modify e_mail, string was empty")
            return

        self._email = email

    def get_phone_number(self) -> str:
        return self._telephone_number

    def set_phone_number(self, phone_number: str):
        # TODO: add checks
        if phone_number == "":
            print("Phone number has an invalid format, so it was not modified")

        self._telephone_number = phone_number

    def get_state(self) -> str:
        return self._state

    def set_state(self, state: str):
        # checks
        if state == "":
            print("Couldn't modify state, string was empty")
            return

        self._state = state

    def get_firm_registration_number(self) -> str:
        return self._firm_registration_number

    def set_firm_registration_number(self, firm_registration_number: str):
        # checks
        if firm_registration_number == "":
            print("Couldn't modify firm_registration_number, string was empty")
            return

        self._firm_registration_number = firm_registration_number

    # TODO: add print and repr
