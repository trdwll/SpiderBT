import re

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from SpiderBT_Users.models import UserGroup

visibility = (
	('public', 'Public'), # any user can view this product
	('private', 'Private'), # only staff can view this product
)

severity = (	
	('urgent', 'Urgent'), # needs to be fixed asap
	('critical', 'Critical'), # needs to be fixed in a timely manner
	('major', 'Major'), # fixed in next hotfix
	('minor', 'Minor'), # fixed in next patch
	('low', 'Low'), # fixed in next patch
	('verylow', 'Very Low'), # Won't do/probably won't do
)

status = (
	('open', 'Open'),
	('inprogress', 'In Progress'),
	('onhold', 'On Hold'),
	('fixed', 'Fixed'),
	('closed', 'Closed'),
)

reproducibility = (
	('always', 'Always'),
	('sometimes', 'Sometimes'),
	('random', 'Random'),
	('havenottried', 'Have Not Tried'),
	('unable', 'Unable to Reproduce'),
	('na', 'N/A'),
)

class Product(models.Model):
	title = models.CharField(max_length=120, help_text='The title of the product.')
	description = models.TextField()
	abbreviation = models.CharField(max_length=10, help_text='A simple identifier to reference cases.', blank=True)

	visibility = models.CharField(blank=False, max_length=120, choices=visibility, default='public')
	date = models.DateTimeField(auto_now_add=True, blank=False, help_text='The creation date of the product.')

	usergroups = models.ManyToManyField(UserGroup, related_name='usergroups', help_text='What usergroups are able to access this product?', blank=True)
	
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.abbreviation == '':
			self.abbreviation = re.sub(r'[^A-Z]', '', self.title)

		super(Product, self).save(*args, **kwargs)


	def get_cases_url(self):
		return reverse('view_cases', kwargs={'slug': self.slug})
		

class ProductVersion(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	title = models.CharField(max_length=120, help_text='The title of the product version.')

	def __str__(self):
		return self.title


# A group that the case is targetting (for example the Case is an AI related issue so post in AI category)
class Category(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	title = models.CharField(max_length=120, help_text='The title of the category.')

	def __str__(self):
		return self.title


# The initial post of an issue
class Case(models.Model):
	identifier = models.CharField(max_length=120, verbose_name='ID of this Case', blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	date_created = models.DateTimeField(auto_now_add=True, blank=False, help_text='The creation date of the case.')
	date_updated = models.DateTimeField(null=True, blank=True, help_text='The date that the case was updated.')
	date_solved = models.DateTimeField(null=True, blank=True, help_text='The date that the case was solved.')

	title = models.CharField(max_length=120, blank=False, help_text='Why are you submitting a report today?')
	body = models.TextField(blank=True, help_text='Explain why are you submitting a report today?')
	
	assigned_to_user = models.ManyToManyField(User, related_name='assigned_to_user', blank=True)
	assigned_to_group = models.ManyToManyField(UserGroup, related_name='assigned_to_group', blank=True)

	category =  models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
	visibility = models.CharField(blank=False, max_length=120, choices=visibility, default='public')
	severity = models.CharField(blank=False, max_length=120, choices=severity, default='minor')
	status = models.CharField(blank=False, max_length=120, choices=status, default='open')
	reproducibility = models.CharField(blank=False, max_length=120, choices=reproducibility, default='havenottried')

	affect_version = models.ManyToManyField(ProductVersion, related_name='affect_version', blank=True, help_text='What version(s) of the product does this affect (your current version)?', verbose_name='Affected Version(s)')

	patch_version = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, related_name='patch_version', null=True, blank=True, help_text='What version of the product will this fix be pushed out?', verbose_name='Patched Version')
	patch_commit = models.CharField(max_length=120, blank=True, help_text='What is the commit ID that this Case was fixed on?', verbose_name='Patched Commit')

	# TODO: Add FileField, but restrict to .txt, .log, and images (.png, .jpg/.jpeg, and .gif)
	# TODO: Add field for OS details (such as what OS, what OS version, etc)

	def __str__(self):
		return '[' + self.identifier + '] ' + self.status + ' - ' + self.title

	def save(self, *args, **kwargs):
		
		if self.identifier == '':
			count = Case.objects.filter(product=self.product).count() + 1
			self.identifier = self.product.abbreviation + '-' + str(count)

		# If the patch version, patch commit and the status is not fixed then save it as fixed
		if self.patch_version and self.patch_commit and not self.status == 'fixed':
			self.status = 'fixed'
			self.date_solved = timezone.now()

		# Always update the updated time since we're saving the case
		self.date_updated = timezone.now()

		super(Case, self).save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('view_case_page', kwargs={'case_id': self.identifier})

	def get_vote_url(self):
		return reverse('vote_case', kwargs={'case_id': self.identifier})



# Reply to a Case
class CaseNote(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	case = models.ForeignKey(Case, on_delete=models.CASCADE)
	body = models.TextField(blank=False, help_text='Explain why are you submitting a report today?')
	date_created = models.DateTimeField(auto_now_add=True, blank=False, help_text='The creation date of the case note.')
	
	# TODO: Add FileField, but restrict to .txt, .log, and images (.png, .jpg/.jpeg, and .gif)


class CaseVote(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	case = models.ForeignKey(Case, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, blank=False)
