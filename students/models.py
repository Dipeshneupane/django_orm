from django.db import models

# Create your models here.
class Teacher(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class BaseItem(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.CharField(max_length = 100)
    updated_by = models.CharField(max_length = 100)

    class Meta:
        abstract = True
        ordering = ['title']

class ItemA(BaseItem):
    contact = models.CharField(max_length = 100)
    class Meta(BaseItem.Meta):
        ordering = ['created_by']

class ItemB(BaseItem):
    file = models.FileField(upload_to='files')
    class Meta(BaseItem.Meta):
        ordering: ['updated_by']

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

class ISBN(Book):
    books_ptr = models.OneToOneField(
        Book,on_delete=models.CASCADE,
        parent_link=True,
        primary_key= True
        )
    ISBN = models.TextField()