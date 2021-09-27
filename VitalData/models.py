from django.db import models
from django.contrib.auth import get_user_model
import jsonfield
# Create your models here.
User=get_user_model()

class user_data(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserData')
    email = models.EmailField()
    fullName = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='uploads/',max_length=254, null=True, blank=True)

    def __str__(self):
        return self.fullName


status_choice = (
    (0, 'Deceased'),
    (1, 'Alive')
)

choice = (
    (0, 'No'),
    (1, 'Yes')
)


class biotag(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    familyMemberName = models.CharField(max_length=50, blank=True,null=True)
    familyMemberImage = models.ImageField(upload_to='uploads/',max_length=254, null=True, blank=True)
    memberImage = models.URLField(default="https://i.picsum.photos/id/1005/5760/3840.jpg?hmac=2acSJCOwz9q_dKtDZdSB-OIK1HUcwBeXco_RMMTUgfY")
    familyMemberRelationship = models.CharField(max_length=50, blank=True,null=True)
    gender = models.CharField(max_length=50, blank=True,null=True)
    marital_status = models.CharField(max_length=50, blank=True,null=True)
    dob = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
    height = models.CharField(max_length=50, blank=True,null=True)
    weight = models.CharField(max_length=50, blank=True,null=True)
    bmi = models.CharField(max_length=50, blank=True,null=True)
    ethinicity = models.CharField(max_length=50, blank=True,null=True)
    disability = jsonfield.JSONField(blank=True,null=True)
    preferred_language = models.CharField(max_length=50, blank=True,null=True)
    address = models.CharField(max_length=150, blank=True,null=True)
    hip_circum = models.CharField(max_length=50, null=True, blank=True)
    waist_cicrum = models.CharField(max_length=50, null=True, blank=True)
    whr_ratio = models.CharField(max_length=50, null=True, blank=True)
    alcohol = jsonfield.JSONField(null=True, blank=True)
    coffee = jsonfield.JSONField(null=True, blank=True)
    sexual_orientation = jsonfield.JSONField(null=True, blank=True)
    tobacco = jsonfield.JSONField(null=True, blank=True)
    other = jsonfield.JSONField(null=True, blank=True)
    surgery = jsonfield.JSONField(null=True, blank=True)


    # def __str__(self):
    #     return self.familyMemberName

class Doctor(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    docName = models.CharField(max_length=50, null=True, blank=True)
    docPhoneNumber = models.CharField(max_length=50, null=True, blank=True)
    docClinicName = models.TextField()
    docSpecialization = jsonfield.JSONField(null=True, blank=True)
    docImage = models.ImageField(upload_to='uploads/media/',max_length=254, null=True, blank=True)
    memberImage = models.URLField(default="https://i.picsum.photos/id/27/3264/1836.jpg?hmac=p3BVIgKKQpHhfGRRCbsi2MCAzw8mWBCayBsKxxtWO8g")


class FamilyHistory(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
    relationship = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    cause_of_death = jsonfield.JSONField(null=True, blank=True)
    adopted = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=50, null=True, blank=True)


class medication(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    drug_name = models.CharField(max_length=100, null=True, blank=True)
    drug_dosage = models.CharField(max_length=50, null=True, blank=True)
    begun_date = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    reason_taking = models.CharField(max_length=50, null=True, blank=True)
    side_effect = models.CharField(max_length=50, null=True, blank=True)
    
    # def __str__(self):
    #     return self.user.username

class education(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    year_of_education = models.CharField(max_length=50, null=True, blank=True)
    employee_status = models.CharField(max_length=50, null=True, blank=True)
    occupation = jsonfield.JSONField(null=True, blank = True)

class sexual(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    abusement = models.CharField(max_length=50, null=True, blank=True)
    abusement_status = jsonfield.JSONField(null = True, blank = True)
    sexual_status = jsonfield.JSONField(null=True, blank = True)

class caffine(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    current_status = models.CharField(max_length=50, null=True, blank=True)
    previous_status = models.CharField(max_length=50, null=True, blank=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    year_started = models.CharField(max_length=50, null=True, blank=True)
    year_stopped = models.CharField(max_length=50, null=True, blank=True)


class Tobacco(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    current_status = models.CharField(max_length=50, null=True, blank=True)
    previous_status = models.CharField(max_length=50, null=True, blank=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    year_started = models.CharField(max_length=50, null=True, blank=True)
    year_stopped = models.CharField(max_length=50, null=True, blank=True)


class Alchol(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    current_status = models.CharField(max_length=50, null=True, blank=True)
    previous_status = models.CharField(max_length=50, null=True, blank=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    year_started = models.CharField(max_length=50, null=True, blank=True)
    year_stopped = models.CharField(max_length=50, null=True, blank=True)

class Other(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True,null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    current_status = models.CharField(max_length=50, null=True, blank=True)
    previous_status = models.CharField(max_length=50, null=True, blank=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)
    year_started = models.CharField(max_length=50, null=True, blank=True)
    year_stopped = models.CharField(max_length=50, null=True, blank=True)







