from django.db import models



class Feedback(models.Model):
    sender = models.CharField(max_length=100)


    def __unicode__(self):
        return "{sender}\n{msg}".format(sender=self.sender)

"""class Emails(models.Model):
    email_addresses = models.EmailField()
    date_subscribed = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "Email:{email_addresses}".format(email_addresses=self.email_addresses)"""        """
        name= models.CharField(max_length=100)
    index_title1= models.CharField(max_length=100)
    index_headings1= models.CharField(max_length=100)
    index_description1 = models.TextField()
    index_title2 = models.CharField(max_length=100)
    index_headings2= models.CharField(max_length=100)
    index_description2 = models.TextField()
    index_title3 = models.CharField(max_length=100)
    index_link3 = models.TextField()
    index_text= models.TextField()
    index_title4 = models.CharField(max_length=100)
    index_link4 = models.TextField()"""
# Create your models here.
