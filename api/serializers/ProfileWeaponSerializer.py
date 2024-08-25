from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from api.models.Weapon import Weapon, ProfileWeapon, WeaponRating, FpsWeapon

class ProfileWeaponSerializer(WritableNestedModelSerializer):
    weapon_name = serializers.CharField(source='weapon.name', read_only=True)
    fps = serializers.SerializerMethodField(read_only=True)
    upped = serializers.SerializerMethodField()
    rating_normal = serializers.SerializerMethodField()
    rating_upper = serializers.SerializerMethodField()

    write_upped = serializers.BooleanField(write_only=True, required=False)
    write_rating_normal = serializers.DecimalField(max_digits=5, decimal_places=2, write_only=True, required=False)
    write_rating_upper = serializers.DecimalField(max_digits=5, decimal_places=2, write_only=True, required=False)

    class Meta:
        model = ProfileWeapon
        fields = '__all__'

    def get_rating_normal(self, obj):
        latest_rating = obj.profile_weapon_weapon_rating.filter(upped=False).first()
        return latest_rating.value if latest_rating else None

    def get_rating_upper(self, obj):
        latest_rating = obj.profile_weapon_weapon_rating.filter(upped=True).first()
        return latest_rating.value if latest_rating else None

    def get_fps(self, obj):
        latest_fps = obj.profile_weapon_fps_weapon.first()
        return latest_fps.value if latest_fps else None

    def get_upped(self, obj):
        upped = obj.profile_weapon_weapon_rating.filter(upped=True).first()
        return upped.upped if upped else None

    def create(self, validated_data):
        fps_value = validated_data.pop('fps', None)
        rating_normal_value = validated_data.pop('write_rating_normal', None)
        rating_upper_value = validated_data.pop('write_rating_upper', None)
        upped = validated_data.pop('write_upped', None)

        profile_weapon = super().create(validated_data)

        if rating_normal_value is None:
            rating_normal_value = 1
        if rating_upper_value is None:
            rating_upper_value = 1

        if upped is not None and upped is not False:
            WeaponRating.objects.create(profile_weapon=profile_weapon, upped=upped, value=rating_upper_value)
            WeaponRating.objects.create(profile_weapon=profile_weapon, upped=False, value=rating_normal_value)
        else:
            WeaponRating.objects.create(profile_weapon=profile_weapon, upped=False, value=rating_normal_value)

        if fps_value is not None:
            FpsWeapon.objects.create(profile_weapon=profile_weapon, value=fps_value)


        return profile_weapon

    def update(self, instance, validated_data):
        rating_normal_value = validated_data.pop('write_rating_normal', None)
        rating_upper_value = validated_data.pop('write_rating_upper', None)
        upped = validated_data.pop('write_upped', None)

        profile_weapon = super().update(instance, validated_data)

        if rating_normal_value is None:
            rating_normal_value = 1
        if rating_upper_value is None:
            rating_upper_value = 1

        if upped is not None and upped is not False:
            result = profile_weapon.profile_weapon_weapon_rating.filter(upped=True);
            if result:
                result.update(value=rating_upper_value)
            else:
                WeaponRating.objects.create(profile_weapon=profile_weapon, upped=upped, value=rating_upper_value)
            profile_weapon.profile_weapon_weapon_rating.filter(upped=False).update(value=rating_normal_value)
        else:
            weaponRatingUpper = profile_weapon.profile_weapon_weapon_rating.filter(upped=True).first()
            if weaponRatingUpper:
                weaponRatingUpper.delete()

            profile_weapon.profile_weapon_weapon_rating.filter(upped=False).update(value=rating_normal_value)

        return profile_weapon