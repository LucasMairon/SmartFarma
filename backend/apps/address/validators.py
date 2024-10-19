from django.core.validators import RegexValidator

names_with_space_regex_validator = RegexValidator(
    regex=r'^[a-zá-ùA-ZÁ-Ù]+((?:[\s][a-zá-ùA-ZÁ-Ù]+)?)+$',
    message="O nome deve conter apenas letras"
)

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
