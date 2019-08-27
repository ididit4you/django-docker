from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.utils.translation import ugettext_lazy as _

from django.utils.translation import gettext_lazy as _

from django.utils import timezone

from .managers import ProjectUserManager

class ProjectUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    objects = ProjectUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')