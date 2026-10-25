from django.db import models

# Create your models here.
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = models.CharField(max_length=200, help_text="e.g. Python, Django, SAP MM")
    
    def __str__(self):
        return self.title

class Candidate(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume_text = models.TextField(help_text="Paste resume here")
    ai_score = models.IntegerField(default=0, help_text="AI will give score")
    ai_feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"