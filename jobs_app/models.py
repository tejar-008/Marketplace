from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    first_name = models.CharField(max_length=150, blank=True, default="", null=True)
    last_name = models.CharField(max_length=150, blank=True, default="", null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    date_joined = models.DateTimeField(("date joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    @property
    def full_name(self):
        return self.get_full_name()

    def get_full_name(self):
        full_name = None
        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name
        elif self.username:
            full_name = self.username
        else:
            full_name = self.email
        return full_name

    def __str__(self):
        """Unicode representation of User."""
        return self.email

    class Meta:
        """Meta definition for User."""

        ordering = ["-is_active"]
        verbose_name = "User"
        verbose_name_plural = "Users"


class Job(models.Model):
    # jobid = models.CharField(max_length=50, unique=True,)
    title = models.TextField(null=True, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Skill(models.Model):
    technology = models.TextField(null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    courseDuration = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.technology)


class CandidatesProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    technology = models.ManyToManyField(Skill, related_name='skillset',)
    title = models.ManyToManyField(Job, related_name='job')
    experience = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='resume', default='0')
    description = models.TextField(null=True, blank=True)
    specializedIn = models.TextField(null=True, blank=True)

    # Create your models here.
