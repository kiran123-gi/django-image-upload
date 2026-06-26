from django.db import models

class imageModel(models.Model):
    imageName=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.imageName} isuploaded on {self.date}"
