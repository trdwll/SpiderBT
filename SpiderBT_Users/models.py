from django.db import models



class UserGroup(models.Model):
    title = models.CharField(max_length=120, help_text='The title of the user group.')
    is_staff = models.BooleanField(verbose_name='Is Staff', default=False, help_text='Is the user group a staff group?')

    def __str__(self):
        return self.title