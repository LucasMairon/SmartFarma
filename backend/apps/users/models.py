from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone
from .managers import CustomUserManager
from django.core.validators import MinLengthValidator
from .validators import (
    legal_age_validator,
    valid_cpf_validator,
    phone_number_regex_validator
)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    ACCESS_LEVEL_CLIENTE = 'C'
    ACCESS_LEVEL_GERENTE = 'G'
    ACCESS_LEVEL_FUNCIONARIO = 'F'

    ACCESS_LEVEL_CHOICES = [
        (ACCESS_LEVEL_CLIENTE, 'Cliente'),
        (ACCESS_LEVEL_GERENTE, 'Gerente'),
        (ACCESS_LEVEL_FUNCIONARIO, 'Funcionário'),
    ]

    name = models.CharField(_("name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    cpf = models.CharField(
        _("CPF"),
        max_length=11,
        validators=[valid_cpf_validator, MinLengthValidator(11)],
        unique=True,
        blank=True
    )
    date_of_birth = models.DateField(
        _("date of birth"),
        validators=[legal_age_validator],
        blank=True
    )
    phone_number = models.CharField(
        _("phone number"),
        max_length=11,
        validators=[phone_number_regex_validator],
        blank=True
    )
    access_level = models.CharField(
        _("acess_level"),
        max_length=1,
        choices=ACCESS_LEVEL_CHOICES,
        blank=True
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
