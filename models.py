from django.db import models

# Create your models here.
class Table1(models.Model):
    s_no=models.IntegerField()
    name=models.CharField(max_length=100)
    email=models.EmailField()

    # def __str__(self):
    #     return self.name  # makes it readable in admin list
    def __str__(self):
     return f"{self.s_no} - {self.name} - {self.email}"