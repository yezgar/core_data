from django.db import models

# Create your models here.

# TYQUY Project > http://muysca.cubun.org/tyquy

class Level(models.Model):
#    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=512)
    level_order = models.IntegerField()

    def __unicode__(self):              # __unicode__ 
     return str(self.id) + '-' + self.name

    class Meta:
#        managed = False
        db_table = 'TQ_Level'

class Session(models.Model):
#    id = models.IntegerField(primary_key=True)  # AutoField?
    level = models.ForeignKey(Level)
    name = models.CharField(max_length=100)
    instructions = models.CharField(max_length=1024)
    session_order = models.IntegerField()

    def __unicode__(self):              # __unicode__ 
     return str(self.id) + '-' + self.name

    class Meta:
#        managed = False
        db_table = 'TQ_Session'

class Text(models.Model):
#    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    file_name = models.CharField(max_length=50)

    def __unicode__(self):              # __unicode__ 
     return str(self.id) + '-' + self.name

    class Meta:
        managed = False
        db_table = 'TQ_Text'

class SessionText(models.Model):
    session = models.ForeignKey(Session)
    text = models.ForeignKey('Text')
    sesion_text_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'TQ_SessionText'

class User(models.Model):
#    id = models.IntegerField(primary_key=True)  # AutoField?
    facebook_profile_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=300)
        
    class Meta:
        managed = False
        db_table = 'User'

class Comment(models.Model):
#    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey('User')
    description = models.CharField(max_length=1024)
    application = models.CharField(max_length=100)
    viewed = models.BooleanField(default=1)

    class Meta:
        managed = False
        db_table = 'Comment'

class UserSession(models.Model):
#    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey('User')
    session = models.ForeignKey(Session)
    feedback = models.CharField(max_length=255)
    feedback_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'TQ_UserSession'
