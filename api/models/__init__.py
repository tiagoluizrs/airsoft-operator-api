from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .Profile import Profile, Patent, Team
from .Weapon import Weapon, Brand, Category, ProfileWeapon, WeaponRating, FpsWeapon, Equipaments