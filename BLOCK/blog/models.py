from django.db import models

# Create your models here


class Post(models.Model):
    """
    model of posts
    """
    author = models.CharField(max_length=25,
                              default='User')
    image = models.ImageField(upload_to='static/posts')
    title = models.CharField(max_length=50,
                             null=True,
                             blank=True)
    desc = models.TextField(max_length=150)

    def __str__(self):
        return f"{self.author}"

    class Meta:
        """
        translation posts on the czech language
        """
        verbose_name = 'Pošta'
        verbose_name_plural = 'Pošty'
