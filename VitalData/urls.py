from django import urls
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('api/login/',Login_Page),
    path('api/register/',Register_User),
    path('api/AddBioTag', AddBioTag),
    path('api/listBioTag', listBioTag),
    path('api/deleteBioTag/<int:id>', deleteBioTag),
    path('api/updateBioTag/<int:id>', updateBioTag),
    path('api/AddDoc', AddDoctor),
    path('api/listDoc', listDoctor),
    path('api/deleteDoc/<int:id>', deleteDoctor),
    path('api/updateDoc/<int:id>', updateDoctor),
    path('api/AddFamilyHistory', AddFamilyHistory),
    path('api/listFamilyHistory', listFamilyHistory),
    path('api/deleteFamilyHistory/<int:id>', deleteFamilyHistory),
    path('api/updateFamilyHistory/<int:id>', updateFamilyHistory),
    path('api/AddEducation', AddEducation),
    path('api/listEducation', listEducation),
    path('api/deleteEducation/<int:id>', deleteEducation),
    path('api/updateEducation/<int:id>', updateEducation),
    path('api/Addmedication', Addmedication),
    path('api/listMedication', listMedication),
    path('api/deleteMedication/<int:id>', deleteMedication),
    path('api/updateMedication/<int:id>', updateMedication),
    path('api/AddSexual', AddSexual),
    path('api/listSexual', listSexual),
    path('api/deleteSexual/<int:id>', deleteSexual),
    path('api/updateSexual/<int:id>', updateSexual),
    path('api/Addcaffine', Addcaffine),
    path('api/listCaffine', listCaffine),
    path('api/deleteCaffine/<int:id>', deleteCaffine),
    path('api/updateCaffine/<int:id>', updateCaffine),
    path('api/AddTobacco', AddTobacco),
    path('api/listTobacco', listTobacco),
    path('api/deleteTobacco/<int:id>', deleteTobacco),
    path('api/updateTobacco/<int:id>', updateTobacco),
    path('api/AddAlchol', AddAlchol),
    path('api/listAlchol', listAlchol),
    path('api/deleteAlchol/<int:id>', deleteAlchol),
    path('api/updateAlchol/<int:id>', updateAlchol),
    path('api/AddOther', AddOther),
    path('api/listOther', listOther),
    path('api/deleteOther/<int:id>', deleteOther),
    path('api/updateOther/<int:id>', updateOther),
    path('api/list_vital', list_vital),
    path('api/update_vital/<int:id>', update_vital),
    path('api/surgery_list', surgery_list),
    path('api/surgery_update/<int:id>', surgery_update),
    path('api/social_history_update/<int:id>', alcohol_update),
    path('api/social_history_list', alcohol_list),

]