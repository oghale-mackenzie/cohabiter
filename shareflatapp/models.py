from django.db import models
from django import forms
from django.conf import settings

class Profile(models.Model):

	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	phone_number = models.CharField(verbose_name='Phone no',max_length=15)
	gender = models.CharField(verbose_name='Gender', max_length=1)
	date_of_birth = models.DateField(verbose_name='Date of Birth',blank=False, null=False,default='1900-01-01')
	photo = models.ImageField(verbose_name='Passport Photo',upload_to='users/%Y/%m/%d/',blank=True)
	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

class AccommodationType(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	description = models.TextField(blank=True)
	image_path = models.CharField(max_length=500)
	active = models.BooleanField(default=True)

	class Meta:
	    ordering=('name',)
	    verbose_name='accommodationtype'
	    verbose_name_plural='accommodationtypes'
	def __str__(self):
		return self.name

class Country(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    code = models.CharField(max_length=3,unique=True)
    
    class Meta:
	    ordering=('name',)
	    verbose_name='country'
	    verbose_name_plural='countries'

    def __str__(self):
    	return self.name

class State(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    country = models.ForeignKey(Country,related_name='states',on_delete=models.CASCADE)

    class Meta:
	    ordering=('name',)
	    verbose_name='state'
	    verbose_name_plural='states'

    def __str__(self):
	    return self.name

class Town(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    zipcode = models.CharField(max_length=10,unique=True)
    state = models.ForeignKey(State,related_name='towns',on_delete=models.CASCADE)

    class Meta:
	    ordering=('name',)
	    verbose_name='town'
	    verbose_name_plural='towns'

    def __str__(self):
    	return self.name

class Area(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    zipcode = models.CharField(max_length=10,unique=True)
    town = models.ForeignKey(Town,related_name='areas',on_delete=models.CASCADE)

    class Meta:
	    ordering=('name',)
	    verbose_name='area'
	    verbose_name_plural='areas'

    def __str__(self):
	    return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    image_path = models.CharField(max_length=500)
    active = models.BooleanField(default=True)

    class Meta:
	    ordering=('name',)
	    verbose_name='roomtype'
	    verbose_name_plural='roomtypes'

    def __str__(self):
    	return self.name

class AdvertCategory(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=20, decimal_places=2)
    duration = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
	    ordering=('title',)
	    verbose_name='advertcategory'
	    verbose_name_plural='advertcategories'

    def __str__(self):
	    return self.title

class Advert(models.Model):
	occupation_types = ((1, "Dont mind"),(2, "Professional"),(3, "Student"),(4, "Clergy"),(5, "Retired"),)
	advert_types = ((1, "On Advert"),(2, "Advert Ended"),(3, "Archived"),)
	day_types = ((1, "Week days"),(2, "Weekends"),(3, "Both"),)
	landlord_types = ((1, "Dont mind"),(2, "Yes"),(3, "No"),)
	title = models.CharField(max_length=500, db_index=True)
	description = models.TextField(blank=True)
	rate = models.DecimalField(max_digits=30, decimal_places=2)
	duration = models.IntegerField()
	accommodationtype = models.ForeignKey(AccommodationType,related_name='adverts',on_delete=models.CASCADE)
	advertcategory = models.ForeignKey(AdvertCategory,related_name='adverts',on_delete=models.CASCADE)
	roomtype = models.ForeignKey(RoomType,related_name='adverts',on_delete=models.CASCADE)
	servicecharges = models.DecimalField(max_digits=30, decimal_places=2)
	service_charge_description = models.TextField(blank=True)
	rent = models.BooleanField(default=False)
	sale = models.BooleanField(default=False)
	geoLocation = models.CharField(max_length=500)
	address = models.CharField(max_length=255)
	bills_included = models.BooleanField(default=False)
	females = models.BooleanField(default=False)
	males = models.BooleanField(default=False)
	couples = models.BooleanField(default=False)
	furnished = models.BooleanField(default=False)
	smoking_allowed = models.BooleanField(default=False)
	pets_allowed = models.BooleanField(default=False)
	min_stay = models.IntegerField()
	max_stay = models.IntegerField()
	move_in_anytime = models.BooleanField(default=False)
	bathrooms = models.IntegerField()
	bedrooms = models.IntegerField()
	garages = models.IntegerField()
	agency = models.DecimalField(max_digits=30, decimal_places=2)
	legal = models.DecimalField(max_digits=30, decimal_places=2)
	caution = models.DecimalField(max_digits=30, decimal_places=2)
	movein_date = models.CharField(max_length=20)
	occupation_option = models.IntegerField(choices=occupation_types, default=1)
	min_age = models.IntegerField()
	max_age = models.IntegerField()
	landlord_option = models.IntegerField(choices=landlord_types, default=1)
	day_option = models.IntegerField(choices=day_types, default=3)
	advert_status = models.IntegerField(choices=advert_types, default=1)
	area = models.ForeignKey(Area,related_name='adverts',on_delete=models.CASCADE)
	photo1 = models.CharField(max_length=500,blank=True)
	photo2 = models.CharField(max_length=500,blank=True)
	photo3 = models.CharField(max_length=500,blank=True)
	photo4 = models.CharField(max_length=500,blank=True)
	photo5 = models.CharField(max_length=500,blank=True)
	photo6 = models.CharField(max_length=500,blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	user_id = models.CharField(max_length=500)
	active = models.BooleanField(default=True)
	class Meta:
	    ordering=('title',)
	    verbose_name='advert'
	    verbose_name_plural='adverts'
	def __str__(self):
		return self.title

class AdvertReview(models.Model):
	name = models.CharField(max_length=255)
	user_id = models.CharField(max_length=255, db_index=True)
	comments = models.TextField()
	rating = models.IntegerField()
	advert = models.ForeignKey(Advert,related_name='advertreviews',on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	class Meta:
	    ordering=('-date_created',)
	    verbose_name='advertreview'
	    verbose_name_plural='advertreviews'
	def __str__(self):
		return self.name