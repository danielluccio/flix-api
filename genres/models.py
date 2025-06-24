from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='nome', blank=False, null=False)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Genêros'
        db_table = 'generos'

    def __str__(self):
        return self.name