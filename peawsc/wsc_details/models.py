from django.db import models

# Create your models here.
class WSCDetail(models.Model):
    wsc_name = models.CharField(max_length=250, null=False, blank=False)
    wsc_year = models.CharField(max_length=4,null=False, blank=False)
    wsc_location = models.CharField(max_length=200)
    wsc_detail = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    wsc_active = models.BooleanField(default=False)
    


