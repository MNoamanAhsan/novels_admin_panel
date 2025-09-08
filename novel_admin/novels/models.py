from django.db import models

class Categoryn(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Novels(models.Model):
    category=models.ForeignKey(Categoryn,on_delete=models.CASCADE,related_name="novels")
    title=models.CharField(max_length=200)
    auther=models.CharField(max_length=100)
    summary=models.TextField()
    image=models.ImageField(upload_to="novel_images/")
    def __str__(self):
        return self.title


class Episode(models.Model):
    novel=models.ForeignKey(Novels,on_delete=models.CASCADE,related_name="episodes")
    name=models.CharField(max_length=200)
    text=models.TextField()

    def __str__(self):
        return f"{self.novel.title}-{self.name}"