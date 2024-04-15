from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, nickname, password=None, **extra_fields):
        if not username:
            raise ValueError('유저네임을 입력하세요.')
        if not nickname:
            raise ValueError('닉네임을 입력하세요.')
        user = self.model(username=username, nickname=nickname, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, nickname, password=None, **extra_fields):
        user = self.create_user(
            username = username,
            nickname = nickname,
            password = password,
            **extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    content = models.CharField(max_length=200, default="자기소개가 아직 없습니다.")
    image = models.ImageField(upload_to="images/", blank=True, default='images/default_user_image.png')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']
    objects = CustomUserManager()

    def delete(self):
        if self.image != 'images/default_user_image.png':
            default_storage.delete(self.image.path)
        super(User, self).delete(using=None, keep_parents=False)