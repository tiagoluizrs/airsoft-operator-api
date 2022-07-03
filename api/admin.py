from django.contrib import admin

from api.models.Profile import Profile
from .models import *

class WeaponRatingAdmin(admin.ModelAdmin):
    search_fields = ('profile_weapon__weapon__name', 'profile_weapon__profile__user__username', 'profile_weapon__weapon__brand__name')
    list_filter = ('profile_weapon__weapon',)

admin.site.register(Profile)
admin.site.register(Patent)
admin.site.register(Team)
admin.site.register(Weapon)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProfileWeapon)
admin.site.register(WeaponRating, WeaponRatingAdmin)
admin.site.register(FpsWeapon)