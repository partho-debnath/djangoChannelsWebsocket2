from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(verbose_name='Group Name', max_length=20, blank=False, unique=True)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + '   |   ' + str(self.datetime)
    
    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'



class Chat(models.Model):
    group = models.ForeignKey(Group, models.CASCADE, verbose_name='Group Name', related_name='chat')
    text = models.CharField(verbose_name='Messages', max_length=100, blank=False)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group.name + '   |   ' + str(self.datetime)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'