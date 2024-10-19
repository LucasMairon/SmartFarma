from django.core.validators import RegexValidator

names_with_space_regex_validator = RegexValidator(
    regex=r'^[a-zá-ùA-ZÁ-Ù]+((?:[\s][a-zá-ùA-ZÁ-Ù]+)?)+$',
    message="O nome deve conter apenas letras"
)

names_with_space_and_numbers_regex_validator = RegexValidator(
    regex=r'^[a-zá-ùA-ZÁ-Ù0-9]+((?:[\s][a-zá-ùA-ZÁ-Ù0-9]+)?)+$',
    message="O nome deve conter apenas letras e números"
)

qrcode_regex_validator = RegexValidator(
    regex=r'^([0-9]{13})$',
    message="O codigo de barras(EAN) deve conter 13 números"
)

sku_regex_validator = RegexValidator(
    regex=r'^([0-9-A-Z]{13})$',
    message="O codigo SKU deve conter 13 caracteres(números, Letras maiusculas e traço(-))"
)


name_regex_validator = names_with_space_regex_validator
brand_regex_validator = names_with_space_and_numbers_regex_validator
maker_regex_validator = names_with_space_and_numbers_regex_validator
ean_regex_validator = qrcode_regex_validator
sku_regex_validator= sku_regex_validator

