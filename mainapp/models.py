from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class BaseModel(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    update = models.DateTimeField(
        auto_now=True, verbose_name='Дата последнего изменения')
    deleted = models.BooleanField(default=False, verbose_name='Удален')

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()



class RecipesCategory(BaseModel):
    category_name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.category_name

class Recipe(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    cooking_steps = models.TextField(verbose_name='Шаги приготовления')
    cooking_time = models.DurationField(verbose_name='Время приготовления')
    image = models.ImageField(upload_to='/recipe', 
                      height_field=100, width_field=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipesCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'








    
