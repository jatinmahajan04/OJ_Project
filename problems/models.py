from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Problem(models.Model):
    prob_id = str(uuid.uuid4())
    name = models.CharField(max_length=100)
    statement = models.TextField()
    difficulty = models.CharField(max_length=50)
    
class Solution(models.Model):
    sol_id = str(uuid.uuid4())
    language = models.CharField(blank=True, max_length=50)
    code = models.TextField(blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Testcase(models.Model):
    tc_id = str(uuid.uuid4())
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()

