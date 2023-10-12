from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100, help_text="Short 100 words title")
    image_url = models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Image_not_available.png/640px-Image_not_available.png')
    description = models.CharField(max_length=225, help_text="Short 225 words description")
    post_type = models.CharField(max_length=50, help_text="HTML5 | CSS3")
    created_by = models.CharField(max_length=225, help_text="creator's name")
    code_url = models.URLField(default='404.com')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'posts'


    def __str__(self):
        return self.title
