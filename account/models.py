from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class register(models.Model):
    first_name = models.CharField(("firstname"), max_length=100)
    last_name  = models.CharField(("lastname"), max_length=100)
    user_email = models.EmailField(("E-mail"), max_length=254,default="")
    wish_rrp = models.IntegerField(("How much will you pay:"))
    user_msg = models.TextField(("What do you think:"))
    post_date = models.DateTimeField(("Post time"), auto_now=False, auto_now_add= True)

    #tell the Django to sort results in the post_date in descending order
    class Meta:
        ordering = ['-post_date'] 
    
    def __str__(self):
        return self.first_name

    def was_add_recently(self):
        return self.post_date >= timezone.now() - datetime.timedelta(days=1)
    
  
