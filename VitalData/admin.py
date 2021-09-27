from django.contrib import admin
# from .models import user_data
# admin.site.register(user_data)
from .models import *

admin.site.register(user_data)
admin.site.register(biotag)
admin.site.register(Doctor)
admin.site.register(FamilyHistory)
admin.site.register(education)
admin.site.register(sexual)
admin.site.register(caffine)
admin.site.register(Tobacco)
admin.site.register(Alchol)
admin.site.register(Other)
