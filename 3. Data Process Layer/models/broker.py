from dataclasses import dataclass


@dataclass
class Broker:
    fiscal_code: str
    first_name: str
    last_name: str
    sex: str
    DOB: str
    ethnicity: str
    education: str
    phone_number: str
    email: str
    agency_country: str
    agency_name: str
    from60to90: str
    from30to60: str
    morethan90: str
    debit_id: str
    insolvent: str
    insolvent_amount: str
