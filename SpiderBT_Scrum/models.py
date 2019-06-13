from django.db import models
from django.contrib.auth.models import User

from SpiderBT_Cases.models import (
    Product, ProductVersion
)

from SpiderBT_Users.models import UserGroup

status = (
    ('rejected', 'Rejected'),
    ('pending', 'Pending'),
    ('development', 'Development'),
    ('testing', 'Testing'),
    ('done', 'Done'),
)

class Task(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	target_release = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, blank=True)

	title = models.CharField(max_length=120)
	description = models.TextField()

	assigned_user = models.ManyToManyField(User, related_name='assigned_user', blank=True)
	assigned_group = models.ManyToManyField(UserGroup, related_name='assigned_group', blank=True)

	status = models.CharField(choices=status, max_length=50, default='pending')

