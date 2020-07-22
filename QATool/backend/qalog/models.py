from django.db import models

# Create your models here.
class QALog(models.Model):
      
    class Meta:
        unique_together = (('QAConnID', 'ObjectPath','QACreatedDate'),)

    SystemType = models.CharField(max_length=120, null=True, blank=True)
    QAConnID = models.CharField(max_length=120, null=True, blank=True)
    QACreatedDate = models.CharField(max_length=120, null=True, blank=True)
    JIRALogFlag = models.CharField(max_length=120, null=True, blank=True)
    QALog = models.CharField(max_length=100000, null=True, blank=True)
    QALoggedDate = models.CharField(max_length=120, null=True, blank=True)
    ObjectName = models.CharField(max_length=120, null=True, blank=True)
    ObjectPath = models.CharField(max_length=200, null=True, blank=True)
    DevelopedBy = models.CharField(max_length=120, null=True, blank=True)
