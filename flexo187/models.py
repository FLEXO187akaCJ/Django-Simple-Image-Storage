from django.db import models
from django.utils import timezone


class Picture(models.Model):
    AUTHOR=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    COMMENT=models.CharField(max_length=200)
    IMAGE=models.ImageField(upload_to='')
    UPLOADED_DATE=models.DateTimeField(blank=True, null=True)

    def upload(self):
        self.UPLOADED_DATE=timezone.now()
        self.save()

    def __str__(self):
        return self.COMMENT