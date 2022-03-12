from django.db import models



class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    location= models.CharField(max_length=100)
    tech_skills = models.JSONField(default=list)
    experience = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    db_table ='candidate'