from django.contrib import admin
from shareflatapp.models import Profile, AccommodationType, RoomType, AdvertCategory, Advert, AdvertReview, Country, State, Town, Area 
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Town)
admin.site.register(Area)
admin.site.register(AccommodationType)
admin.site.register(RoomType)
admin.site.register(AdvertCategory)
admin.site.register(Advert)
admin.site.register(AdvertReview)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user','phone_number','gender','date_of_birth','photo']


