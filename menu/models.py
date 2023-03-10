from django.db import models
from django.urls import reverse

# Create your models here.
class AbstractModel(models.Model):
    is_visible = models.BooleanField(default=True, verbose_name='Visibility')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Menu(AbstractModel):
    title = models.CharField(max_length=50, verbose_name='Title')
    slug = models.SlugField(max_length=255, verbose_name='Slug')
    named_url = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        return self.title

    def get_absolute_path(self):
        if self.named_url:
            url = reverse(f'{self.named_url}')
        else:
            url = f'/{self.slug}/' 
        
        return url

class MenuItem(AbstractModel):
    menu = models.ForeignKey(Menu, related_name='items', verbose_name='menu', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='items', 
        verbose_name='parent menu items', blank=True, 
        null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Item title')
    url = models.CharField(max_length=255, verbose_name='Link', blank=True)
    named_url = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'

    def get_url(self):
        if self.named_url:
            url = reverse(f'{self.named_url}')
        elif self.url:
            url = self.url
        else:
            url = '/'

        return url

    def __str__(self):
        return self.title