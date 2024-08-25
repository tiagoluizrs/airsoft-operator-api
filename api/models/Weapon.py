from api.models.Profile import Profile
from api.models import models

class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='uploads/brands/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    image = models.ImageField(upload_to='uploads/weapons/', null=True, blank=True)
    fps = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, related_name='category_weapon', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='brand_weapon', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class ProfileWeapon(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_profile_weapong', on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, related_name='weapon_profile_weapong', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.profile.user.username} - {self.weapon.name}'

class WeaponRating(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    profile_weapon = models.ForeignKey(ProfileWeapon, related_name='profile_weapon_weapon_rating', on_delete=models.CASCADE)
    upped = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.profile_weapon.profile.user.username} - {self.profile_weapon.weapon.name}'

class FpsWeapon(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    profile_weapon = models.ForeignKey(ProfileWeapon, related_name='profile_weapon_fps_weapon', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.profile_weapon.profile.user.username

class Equipaments(models.Model):
    name = models.TextField()
    type = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name