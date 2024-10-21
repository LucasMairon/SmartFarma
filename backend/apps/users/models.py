from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone
from .managers import CustomUserManager
from django.core.validators import MinLengthValidator
from .validators import (
    cpf_regex_validator,
    email_regex_validator,
    legal_age_validator,
    name_regex_validator,
    phone_number_regex_validator,
    valid_cpf_validator,
    city_regex_validator,
    state_regex_validator,
    neighborhood_regex_validator,
    complement_regex_validator,
    reference_point_regex_validator,
    street_regex_validator,
    zip_code_regex_validator,
    number_regex_validator
)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(
        _("name"),
        max_length=150,
        validators=[MinLengthValidator(2), name_regex_validator]
    )
    email = models.EmailField(
        _("email address"),
        validators=[email_regex_validator],
        unique=True
    )
    cpf = models.CharField(
        _("CPF"),
        max_length=11,
        validators=[
            valid_cpf_validator,
            cpf_regex_validator,
            MinLengthValidator(11)
        ],
        unique=True
    )
    date_of_birth = models.DateField(
        _("date of birth"),
        validators=[legal_age_validator]
    )
    phone_number = models.CharField(
        _("phone number"),
        max_length=11,
        validators=[phone_number_regex_validator, MinLengthValidator(11)]
    )
    street = models.CharField(
        max_length=100,
        validators=[street_regex_validator]
    )
    city = models.CharField(max_length=50, validators=[city_regex_validator])
    state = models.CharField(max_length=50, validators=[state_regex_validator])
    number = models.CharField(
        max_length=50,
        validators=[number_regex_validator]
    )
    neighborhood = models.CharField(
        max_length=50,
        validators=[neighborhood_regex_validator]
    )
    complement = models.CharField(
        max_length=50,
        validators=[complement_regex_validator]
    )
    reference_point = models.CharField(
        max_length=50,
        validators=[reference_point_regex_validator]
    )
    zip_code = models.CharField(
        max_length=50,
        validators=[zip_code_regex_validator]
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return str(self.email)
