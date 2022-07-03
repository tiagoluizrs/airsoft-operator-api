from api.models import *

class Patent(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False, blank=False) 
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='uploads/teams/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/profiles/', null=True, blank=True)
    team = models.ForeignKey(Team, related_name='team_user', on_delete=models.CASCADE)  
    patent = models.ForeignKey(Patent, related_name='patent_user', on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass