from django.db import models
from user.models import User

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)

    # class Meta:
    #     verbose_name = " job"
    #     verbose_name_plural = "jobs"
    #     ordering = ["-id"]
       

    def __str__(self):
        return self.title
    
class Apply(models.Model):
    applier=models.ForeignKey(User, on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    applied_at=models.DateTimeField(auto_now_add=True)
    cv=models.FileField(upload_to="apply")

    class Meta:
        verbose_name = " apply"
        verbose_name_plural = "applys"
        ordering = ["-id"]

    def __str__(self):
        return self.job.title
   

