import re
from datetime import date
from django.core.validators import ValidationError
from dateutil.relativedelta import relativedelta
from django.core.validators import RegexValidator


name_regex_validator = RegexValidator(
    regex=r'^[a-zá-ùA-ZÁ-Ù]+((?:[\s][a-zá-ùA-ZÁ-Ù]+)?)+$',
    message="O nome deve conter apenas letras"
)


phone_number_regex_validator = RegexValidator(
    regex=r'^[0-9]{11}$',
    message="Número de telefone deve conter apenas e estar no formato: 'DDD9XXXXXXXX'"
)


cpf_regex_validator = RegexValidator(
    regex=r'^[0-9]{11}$',
    message="O CPF de conter 11 números"
)


email_regex_validator = RegexValidator(
    regex=r"^[a-zA-Z0-9._]+@[a-z]+\.com$",
    message="Número de telefone deve estar no formato: 'DDD9XXXXXXXX'"
)


def legal_age_validator(value):
    "Válida se o usuario é maior de idade"
    idade = relativedelta(date.today(), value)
    if idade.years >= 18:
        return value
    raise ValidationError('É necessário ser maior de idade')


def valid_cpf_validator(value):
    """ válida o CPF do usuário com o cálculo do mesmo """

    cpf = str(value)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        raise ValidationError('Digite um cpf valido')

    new_cpf = cpf[:-2]
    reverse = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(new_cpf[index]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            digit = 11 - (total % 11)

            if digit > 9:
                digit = 0
            total = 0
            new_cpf += str(digit)

    sequence = new_cpf == str(new_cpf[0]) * len(cpf)

    if cpf == new_cpf and not sequence:
        return cpf

    raise ValidationError("Digite um cpf valido")


names_with_space_and_numbers_regex_validator = RegexValidator(
    regex=r'^[a-zá-ùA-ZÁ-Ù0-9]+((?:[\s][a-zá-ùA-ZÁ-Ù0-9]+)?)+$',
    message="O nome deve conter apenas letras e números"
)

number_regex_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9-]+((?:[a-zA-Z0-9-]+)?)+$',
    message="O nome deve conter apenas letras números e o serparador '-'"
)

zip_code_regex_validator = RegexValidator(
    regex=r'^[0-9]{8}$',
    message="O CEP deve conter 8 números"
)


city_regex_validator = names_with_space_and_numbers_regex_validator
state_regex_validator = names_with_space_and_numbers_regex_validator
neighborhood_regex_validator = names_with_space_and_numbers_regex_validator
complement_regex_validator = names_with_space_and_numbers_regex_validator
reference_point_regex_validator = names_with_space_and_numbers_regex_validator
street_regex_validator = names_with_space_and_numbers_regex_validator
