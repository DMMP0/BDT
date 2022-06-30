def clean_string(stringa: str) -> str:
    s = stringa.lower().replace(" ", "_")
    return s


def get_meaning(stringa: str, synonyms_dictionary) -> str:
    for el in synonyms_dictionary:
        if stringa in el:
            return el[stringa]


def decode_t_f(boolean_string: str) -> str:
    if clean_string(boolean_string) == 'true':
        return '1'
    else:
        return '0'

def clean_money(value_string: str) -> str:
    return value_string.replace(",", '').replace('$', '')


statement_synonyms = (
    {
        "fiscal_code": "fiscal_code",
        "codice_fiscale": "fiscal_code",
        "id": "fiscal_code",
        "id_number": "fiscal_code"},
    {"first_name": "first_name",
     "name": "first_name",
     "nome": "first_name"},
    {"last_name": "last_name",
     "cognome": "last_name",
     "surname": "last_name"},
    {"sex": "sex",
     "biological_sex": "sex", },

    {"dob": "DOB",
     "date_of_birth": "DOB",
     "data_di_nascita": "DOB"},

    {"ethnicity": "ethnicity",
     "etnia": "ethnicity", },

    {"education": "education",
     "highest_education": "education", },

    {"phone_number": "phone_number",
     "numero_telefonico": "phone_number",
     "telefono": "phone_number"},

    {"email": "email",
     "mail": "email",
     "indirizzo_di_posta_elettronica": "email"},

{"personal_email": "pmail",
     "pmail": "pmail",
     "pemail": "pmail"},

    {"purpose": "purpose",
     "ruolo": "purpose",
     "scopo": "purpose"},

    {"registration_number": "registration_number",
     "registeration_number": "registration_number",
     "company_registration_number": "registration_number"},

    {"company_name": "company_name",
     "company": "company_name",
     "azienda": "company_name"},

    {"established_date": "established_date",
     "establied_date": "established_date",
     "fondazione": "established_date"},

    {"country": "country",
     "paese": "country", },

{"amount_of_credit": "amount_of_credit",
     "requested_credit": "amount_of_credit", },

{"duration_in_months": "duration_in_months", },


    {"employees": "employees",
     "number_of_employees": "employees",
     "employes": "employees",
     "number_of_employes": "employees",},
)

bank_synonyms = (
    {
        "fiscal_code": "fiscal_code",
        "codice_fiscale": "fiscal_code",
        "id": "fiscal_code",
        "id_number": "fiscal_code"},
    {
        "bank_name": "bank_name",
        "bank": 'bank_name'
    },
    {
        "bank_country": "bank_country",
        "country": 'bank_country'
    },
    {
        "amount_in_6_months": "amount_in_6_months",
        "ammount_in_6_months": 'amount_in_6_months'
    },
    {
        "amount_in_12_months": "amount_in_12_months",
        "ammount_in_12_months": 'amount_in_12_months'
    },
    {
        "amount_in_18_months": "amount_in_18_months",
        "ammount_in_18_months": 'amount_in_18_months'
    },
    {
        "amount_of_house_mortage": "amount_of_house_mortgage",
        "ammount_of_house_mortage": 'amount_of_house_mortgage'
    },
    {
        "amount_duee_mortage": "amount_due_mortgage",
    },
    {
        "house_property": "house_property",
    },
    {
        "total_house_amount": "total_house_amount",
    },
    {
        "credit_card_number": "credit_card_number",

    },
    {
        "credit_card_limit_total": "credit_card_limit_total",

    },
    {
        "actual_debit_credit_cards": "actual_debit_credit_cards",

    },
    {
        "monthly_income": "monthly_income",

    },
    {
        "savings": "savings",

    },
    {
        "other_savings": "other_savings",

    },
)


questura_synonyms = (
    {
        "fiscal_code": "fiscal_code",
        "codice_fiscale": "fiscal_code",
        "id": "fiscal_code",
        "id_number": "fiscal_code"},
    {
        "questura_country": "questura_country",
        "counrty": 'questura_country'
    },

    {'bankruptcy': 'bankruptcy'},
    # {'inscred':'inscred'},
    {'fraudis': 'fraudis'},
    {'condamned': 'condamned'},
    {'investegation': 'investegation'},
    {'accused': 'accused'},
    {'civ_pass': 'civ_pass'},
)

#{"agency_country": "Czech Republic",
# "agency_name": "CTC", "from30to60": 0, "from60to90": 0, "morethan90": 3
# "insolvent_ammount": "$13,884,270,465.00"}

broker_synonyms = (
    {
        "fiscal_code": "fiscal_code",
        "codice_fiscale": "fiscal_code",
        "id": "fiscal_code",
        "id_number": "fiscal_code"},
    {'agency_country': 'agency_country',
     'country':'agency_country'},
    {'agency_name':'agency_name'},
{'from30to60':'from30to60'},
{'from60to90':'from60to90'},
{'morethan90':'morethan90'},
{'insolvent_ammount':'insolvent_amount',
 'insolvent_amount':'insolvent_amount'},
)
