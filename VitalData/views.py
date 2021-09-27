from django.contrib.auth import authenticate, login
from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import *
from datetime import date
import json
from rest_framework.views import APIView
# Create your views here.

#++++++++++++++++++++++++++++ USER AUTHENTICATION ++++++++++++++++++++++++++++++++++++++


@api_view(('POST',))
@csrf_exempt
def Login_Page(request):
    data = request.body
    dict = json.loads(data)
    username = dict.get('username')
    password = dict.get('password')
    obj = authenticate(request,username=username,password=password)
    if obj  is not None:
        login(request,obj)
        listOfMember = []
        UserDataObj = user_data.objects.filter(user__username = username)[0]
        listOfMember.append({"fullName" : UserDataObj.fullName, "email":UserDataObj.email})
        users = User.objects.get(username=username)
        dict={"Message":"Success","email":UserDataObj.email, 'status' : True, "fullname":UserDataObj.fullName}
    else:
        dict={"Message":"Fail", 'status' : False}
    return JsonResponse(data = dict,safe=False)


@api_view(('POST',))
@csrf_exempt
def Register_User(request):
    data = request.body
    dict = json.loads(data)
    print(dict)
    username = dict.get('username')
    password = dict.get('password')
    fullName = dict.get('fullName')
    obj,created = User.objects.get_or_create(username=username)
    if created:
        user_data.objects.get_or_create(user = User.objects.get(username=username), fullName=fullName, email=username)
        obj.username = username
        obj.set_password(password)
        obj.save()
        dict={"message":"registered"}
    else:
        dict={"message":"not registered"}
    return JsonResponse(data = dict,safe=False)




@api_view(('POST',))
def AddBioTag(request):
    if request.method == 'POST':
        data = request.body
        dict = json.loads(data)
        username = dict.get('username', None)
        familyMemberName = dict.get('familyMemberName',None)
        familyMemberImage = dict.get('familyMemberImage', None)
        familyMemberRelationship = dict.get('familyMemberRelationship', None)
        gender = dict.get('gender', None)
        marital_status = dict.get('marital_status', None)
        dob = dict.get('dob', None)
        height = dict.get('height', None)
        weight = dict.get('weight', None)
        bmi = dict.get('bmi',None)
        ethinicity = dict.get('ethinicity')
        disability = dict.get('disability', None)
        preferred_language = dict.get('preferred_language', None)
        address = dict.get('address', None)

        biotagObj = biotag.objects.get_or_create(
            user = User.objects.get(username=username),
            familyMemberName = familyMemberName,
            familyMemberImage = familyMemberImage,
            familyMemberRelationship = familyMemberRelationship,
            gender = gender,
            marital_status = marital_status,
            dob = dob,
            height = height,
            weight = weight,
            bmi = bmi,
            ethinicity = ethinicity,
            disability = disability,
            preferred_language = preferred_language,
            address = address
        )

        return JsonResponse(data = {"message":"Success"}, safe=False)


@api_view(('POST',))
@csrf_exempt
def listBioTag(request):
    data = request.body
    dict = json.loads(data)
    username = dict.get('username')
    biotagObj = biotag.objects.filter(user__username = username)
    listOfMember = []
    for i in biotagObj:
        dict = {}
        dict['id'] = i.id
        dict['memberImage'] = i.memberImage
        if i.dob:
            dict['dob'] = i.dob
        else:
            dict['dob'] = ""

        if i.familyMemberName:
            dict['familyMemberName'] = i.familyMemberName
        else:
            dict['familyMemberName'] = ""

        # dict['familyMemberImage'] = i.familyMemberImage

        if i.familyMemberRelationship:
            dict['familyMemberRelationship'] = i.familyMemberRelationship
        else:
            dict['familyMemberRelationship'] = ""

        if i.gender:
            dict['gender'] = i.gender
        else:
            dict['gender'] = ""

        if i.marital_status:
            dict['marital_status'] = i.marital_status
        else:
            dict['marital_status'] = ""

        if i.height:
            dict['height'] = i.height
        else:
            dict['height'] = ""

        if i.weight:
            dict['weight'] = i.weight
        else:
            dict['weight'] = ""

        if i.bmi:
            dict['bmi'] = i.bmi
        else:
            dict['bmi'] = ""

        if i.ethinicity:
            dict['ethinicity'] = i.ethinicity
        else:
            dict['ethinicity'] = ""

        if i.disability:
            dict['disability'] = i.disability
        else:
            dict['disability'] = ""

        if i.preferred_language:
            dict['preferred_language'] = i.preferred_language
        else:
            dict['preferred_language'] = ""

        if i.address:
            dict['address'] = i.address
        else:
            dict['address'] = ""

        listOfMember.append(dict)
    data = {"message":"Success", "data":listOfMember}
    return JsonResponse(data = data, safe=False)


@api_view(('DELETE',))
@csrf_exempt
def deleteBioTag(request, id):
    biotag.objects.get(id=id).delete()
    data = {"message" :"Success"}
    return JsonResponse(data, safe=False)


@api_view(('PUT',))
@csrf_exempt
def updateBioTag(request, id):
    data = json.loads(request.body)
    familyMemberName = data.get('familyMemberName')
    # familyMemberImage = request.FILES
    familyMemberRelationship = data.get('familyMemberRelationship')
    gender = data.get('gender')
    marital_status = data.get('marital_status')
    dob = data.get('dob')
    height = data.get('height')
    weight = data.get('weight')
    bmi = data.get('bmi')
    ethinicity = data.get('ethinicity')
    disability = data.get('disability')
    preferred_language = data.get('preferred_language')
    address = data.get('address')


    biotagObj = get_object_or_404(biotag, id=id)

    biotagObj.familyMemberName = familyMemberName
    # familyMemberImage = familyMemberImage,
    biotagObj.familyMemberRelationship = familyMemberRelationship
    biotagObj.gender = gender
    biotagObj.marital_status = marital_status
    biotagObj.dob = dob
    biotagObj.height = height
    biotagObj.weight = weight
    biotagObj.bmi = bmi
    biotagObj.ethinicity = ethinicity
    biotagObj.disability = disability
    biotagObj.preferred_language = preferred_language
    biotagObj.address = address
    biotagObj.save()
    if biotagObj:
        data = {"message" :"Success"}
    else:
        data = {"message" :"Failure"}
    return JsonResponse(data, safe=False)


#+++++++++++++++++++++++++++++++  DOCTOR ++++++++++++++++++++++++++++
@api_view(('POST',))
@csrf_exempt
def AddDoctor(request):
    if request.method == 'POST':
        data = request.body
        dict = json.loads(data)
        username = dict.get('username', None)
        docName = dict.get('docName', None)
        # docImage = request.FILES
        docPhoneNumber = dict.get('docPhoneNumber', None)
        docClinicName = dict.get('docClinicName', None)
        docSpecialization = dict.get('docSpecialization', None)

        DoctorObj = Doctor.objects.create(
            user = User.objects.get(username=username),
            docName = docName,
            # docImage = docImage,
            docPhoneNumber = docPhoneNumber,
            docClinicName = docClinicName,
            docSpecialization = docSpecialization,
        )

        if DoctorObj:
            data = {"message" : "Success"}
        else:
            data = {"message" : "Failure"}
        return JsonResponse(data, safe=False)


@api_view(('GET',))
@csrf_exempt
def listDoctor(request):
    doctorObj = Doctor.objects.filter(user__username = request.user.username)
    listOfMember = []
    for i in doctorObj:
        dict = {}
        if i.docName:
            dict['docName'] = i.docName
        else:
            dict['docName'] = ""
        # dict['familyMemberImage'] = i.familyMemberImage
        if i.docPhoneNumber:
            dict['docPhoneNumber'] = i.docPhoneNumber
        else:
            dict['docPhoneNumber'] = ""
        if i.docClinicName:
            dict['docClinicName'] = i.docClinicName
        else:
            dict['docClinicName'] = ""
        if i.docSpecialization:
            dict['docSpecialization'] = i.docSpecialization
        else:
            dict['docSpecialization'] = ""
        listOfMember.append(dict)
    if listOfMember:
        data = {"message":"Success", "data":listOfMember}
    else:
        data = {"message":"Failure"}
    return JsonResponse(data, safe=False)



@api_view(('DELETE',))
@csrf_exempt
def deleteDoctor(request, id):
    Doctor.objects.get(id=id).delete()

    return JsonResponse(data="deleted successfully",safe=False)


@api_view(('PUT',))
@csrf_exempt
def updateDoctor(request, id):
    docName = request.POST.get('docName')
    # docImage = request.FILES
    docPhoneNumber = request.POST.get('docPhoneNumber')
    docClinicName = request.POST.get('docClinicName')
    docSpecialization = request.POST.getlist('docSpecialization')
    dict = {}
    dict['docSpecialization'] = docSpecialization

    DoctorObj = get_object_or_404(Doctor, id=id)
    DoctorObj.docName = docName
    DoctorObj.docPhoneNumber = docPhoneNumber
    DoctorObj.docClinicName = docClinicName
    DoctorObj. docSpecialization = dict
    DoctorObj.save()

    return JsonResponse(data="Update successfully", safe=False)



#++++++++++++++++++++++++++++++++ FAMILY_HISTORY +++++++++++++++++++++++++++++
@api_view(('POST',))
@csrf_exempt
def AddFamilyHistory(request):
    today = date.today()
    Name = request.POST.get('Name')
    # docImage = request.FILES
    dob = request.POST.get('dob')
    relationship = request.POST.get('relationship')
    status = request.POST.get('status')     ### CHOICE FIELD
    cause_of_death = request.POST.getlist('cause_of_death')
    dict = {}
    dict['cause_of_death'] = cause_of_death
    adopted = request.POST.get('adopted')       ## CHOICE FIELD
    age = request.POST.get('age')

    FamilyHistObj = FamilyHistory.objects.create(
        # user = User.objects.get(username=request.user.username),
        name = Name,
        # docImage = docImage,
        dob = dob,
        relationship = relationship,
        status = status,
        cause_of_death = dict,
        adopted = adopted,
        age = age
    )
    return JsonResponse(data = "successfully added", safe=False)



@api_view(('GET',))
@csrf_exempt
def listFamilyHistory(request):
    familyHistoryObj = FamilyHistory.objects.filter(user__username = "abhishek")
    listOfMember = []
    for i in familyHistoryObj:
        dict = {}
        dict['name'] = i.name
        # dict['familyMemberImage'] = i.familyMemberImage
        dict['dob'] = i.dob
        dict['relationship'] = i.relationship
        dict['status'] = i.status
        dict['cause_of_death'] = i.cause_of_death
        dict['adopted'] = i.adopted
        dict['age'] = i.age
        listOfMember.append(dict)
    return JsonResponse(data = listOfMember, safe=False)


@api_view(('DELETE',))
@csrf_exempt
def deleteFamilyHistory(request, id):
    FamilyHistory.objects.get(id=id).delete()
    return JsonResponse(data="deleted successfully",safe=False)



@api_view(('PUT',))
@csrf_exempt
def updateFamilyHistory(request, id):
    today = date.today()
    Name = request.POST.get('Name')
    # docImage = request.FILES
    dob = request.POST.get('dob')
    relationship = request.POST.get('relationship')
    status = request.POST.get('status')
    cause_of_death = request.POST.getlist('cause_of_death')
    dict = {}
    dict['cause_of_death'] = cause_of_death
    adopted = request.POST.get('adopted')
    age = request.POST.get('age')

    FamilyHistObj = get_object_or_404(FamilyHistory, id=id)
    # user = User.objects.get(username=request.user.username),
    FamilyHistObj.name = Name
    FamilyHistObj.dob = dob
    FamilyHistObj.relationship = relationship
    FamilyHistObj.status = status
    FamilyHistObj.cause_of_death = dict
    FamilyHistObj.adopted = adopted
    FamilyHistObj.age = age
    FamilyHistObj.save()
    return JsonResponse(data = "successfully updated", safe=False)



#++++++++++++++++++++++++++++++++ MEDICATION +++++++++++++++++++++++++++++
@api_view(('POST',))
@csrf_exempt
def Addmedication(request):
    drug_name = request.POST.get('drug_name')
    # docImage = request.FILES
    drug_dosage = request.POST.get('drug_dosage')
    begun_date = request.POST.get('begun_date')
    frequency = request.POST.get('frequency')
    reason_taking = request.POST.get('reason_taking')
    side_effect = request.POST.get('side_effect')

    medicationObj = medication.objects.create(
        # user = User.objects.get(username=request.user.username),
        drug_name = drug_name,
        drug_dosage = drug_dosage,
        begun_date = begun_date,
        frequency = frequency,
        reason_taking = reason_taking,
        side_effect = side_effect
    )
    return JsonResponse(data = "successfully added", safe=False)



@api_view(('GET',))
@csrf_exempt
def listMedication(request):
    medicationObj = medication.objects.filter(user__username = "abhishek")
    listOfMember = []
    for i in medicationObj:
        dict = {}
        dict['drug_name'] = i.drug_name
        # dict['familyMemberImage'] = i.familyMemberImage
        dict['drug_dosage'] = i.drug_dosage
        dict['begun_date'] = i.begun_date
        dict['frequency'] = i.frequency
        dict['reason_taking'] = i.reason_taking
        dict['side_effect'] = i.side_effect
        listOfMember.append(dict)
    return JsonResponse(data = listOfMember, safe=False)


@api_view(('DELETE',))
@csrf_exempt
def deleteMedication(request, id):
    medication.objects.get(id=id).delete()
    return JsonResponse(data="deleted successfully",safe=False)



@api_view(('PUT',))
@csrf_exempt
def updateMedication(request, id):
    drug_name = request.POST.get('drug_name')
    # docImage = request.FILES
    drug_dosage = request.POST.get('drug_dosage')
    begun_date = request.POST.get('begun_date')
    frequency = request.POST.get('frequency')
    reason_taking = request.POST.get('reason_taking')
    side_effect = request.POST.get('side_effect')

    medicationObj = get_object_or_404(medication, id=id)
    # user = User.objects.get(username=request.user.username),
    medicationObj.drug_name = drug_name
    medicationObj.drug_dosage = drug_dosage
    medicationObj.begun_date = begun_date
    medicationObj.frequency = frequency
    medicationObj.reason_taking = reason_taking
    medicationObj.side_effect = side_effect
    medicationObj.save()
    return JsonResponse(data = "successfully updated", safe=False)






#++++++++++++++++++++++++++++++ EDUCATION ++++++++++++++++++++++++++++++++
@api_view(('POST',))
@csrf_exempt
def AddEducation(request):
    year_of_education = request.POST.get('year_of_education')
    # docImage = request.FILES
    employee_status = request.POST.get('employee_status')
    occupation = request.POST.getlist('occupation')
    dict = {}
    dict['occupation'] = occupation

    EducationObj = education.objects.create(
        # user = User.objects.get(username=request.user.username),
        year_of_education = year_of_education,
        employee_status = employee_status,
        occupation = dict
    )
    return JsonResponse(data = "successfully added", safe=False)



@api_view(('GET',))
@csrf_exempt
def listEducation(request):
    educationObj = education.objects.filter(user__username = "abhishek")
    listOfMember = []
    for i in educationObj:
        dict = {}
        dict['year_of_education'] = i.year_of_education
        dict['employee_status'] = i.employee_status
        dict['occupation'] = i.occupation
        listOfMember.append(dict)
    return JsonResponse(data = listOfMember, safe=False)


@api_view(('DELETE',))
@csrf_exempt
def deleteEducation(request, id):
    education.objects.get(id=id).delete()
    return JsonResponse(data="deleted successfully",safe=False)



@api_view(('PUT',))
@csrf_exempt
def updateEducation(request, id):
    year_of_education = request.POST.get('year_of_education')
    # docImage = request.FILES
    employee_status = request.POST.get('employee_status')
    occupation = request.POST.getlist('occupation')
    dict = {}
    dict['occupation'] = occupation

    educationObj = get_object_or_404(education, id=id)
    # user = User.objects.get(username=request.user.username),
    educationObj.year_of_education = year_of_education
    educationObj.employee_status = employee_status
    educationObj.occupation = dict
    educationObj.save()
    return JsonResponse(data = "successfully updated", safe=False)



#++++++++++++++++++++++++++++++ SEXUAL ++++++++++++++++++++++++++++++++
@api_view(('POST',))
@csrf_exempt
def AddSexual(request):
    abusement = request.POST.get('abusement')
    abusement_status = request.POST.getlist('abusement_status')
    dict = {}
    dict['abusement_status'] = abusement_status
    sexual_status = request.POST.getlist('sexual_status')
    dict1 = {}
    dict1['sexual_status'] = sexual_status

    EducationObj = sexual.objects.create(
        # user = User.objects.get(username=request.user.username),
        abusement = abusement,
        abusement_status = dict,
        sexual_status = dict1
    )
    return JsonResponse(data = "successfully added", safe=False)



@api_view(('GET',))
@csrf_exempt
def listSexual(request):
    sexualObj = sexual.objects.filter(user__username = "abhishek")
    listOfMember = []
    for i in sexualObj:
        dict = {}
        dict['abusement'] = i.abusement
        dict['abusement_status'] = i.abusement_status
        dict['sexual_status'] = i.sexual_status
        listOfMember.append(dict)
    return JsonResponse(data = listOfMember, safe=False)


@api_view(('DELETE',))
@csrf_exempt
def deleteSexual(request, id):
    sexual.objects.get(id=id).delete()
    return JsonResponse(data="deleted successfully",safe=False)



@api_view(('PUT',))
@csrf_exempt
def updateSexual(request, id):
    abusement = request.POST.get('abusement')
    abusement_status = request.POST.getlist('abusement_status')
    dict = {}
    dict['abusement_status'] = abusement_status
    sexual_status = request.POST.getlist('sexual_status')
    dict1 = {}
    dict1['sexual_status'] = sexual_status

    sexualObj = get_object_or_404(sexual, id=id)
    # user = User.objects.get(username=request.user.username),
    sexualObj.abusement = abusement
    sexualObj.abusement_status = dict
    sexualObj.sexual_status = dict1
    sexualObj.save()
    return JsonResponse(data = "successfully updated", safe=False)



#++++++++++++++++++++++++++++++++ CAFFINE +++++++++++++++++++++++++++++
@api_view(('POST',))
@csrf_exempt
def Addcaffine(request):
    name = request.POST.get('name')
    current_status = request.POST.get('current_status')
    previous_status = request.POST.get('previous_status')
    frequency = request.POST.get('frequency')
    year_started = request.POST.get('year_started')
    year_stopped = request.POST.get('year_stopped')

    caffineObj = caffine.objects.create(
        # user = User.objects.get(username=request.user.username),
        name = name,
        current_status = current_status,
        previous_status = previous_status,
        frequency = frequency,
        year_started = year_started,
        year_stopped = year_stopped
    )
    return JsonResponse(data = "successfully added", safe=False)



@api_view(('GET',))
@csrf_exempt
def listCaffine(request):
    caffineObj = caffine.objects.filter(user__username = "abhishek")
    listOfMember = []
    for i in caffineObj:
        dict = {}
        dict['name'] = i.name
        dict['current_status'] = i.current_status
        dict['previous_status'] = i.previous_status
        dict['frequency'] = i.frequency
        dict['year_started'] = i.year_started
        dict['year_stopped'] = i.year_stopped
        listOfMember.append(dict)
    return JsonResponse(data = listOfMember, safe=False)


@api_view(('DELETE',))
@csrf_exempt
def deleteCaffine(request, id):
    caffine.objects.get(id=id).delete()
    return JsonResponse(data="deleted successfully",safe=False)



@api_view(('PUT',))
@csrf_exempt
def updateCaffine(request, id):
    name = request.POST.get('name')
    # docImage = request.FILES
    current_status = request.POST.get('current_status')
    previous_status = request.POST.get('previous_status')
    frequency = request.POST.get('frequency')
    year_started = request.POST.get('year_started')
    year_stopped = request.POST.get('year_stopped')

    caffineObj = get_object_or_404(caffine, id=id)
    # user = User.objects.get(username=request.user.username),
    caffineObj.name = name
    caffineObj.current_status = current_status
    caffineObj.previous_status = previous_status
    caffineObj.frequency = frequency
    caffineObj.year_started = year_started
    caffineObj.year_stopped = year_stopped
    caffineObj.save()
    return JsonResponse(data = "successfully updated", safe=False)


#++++++++++++++++++++++++++++++++ Tobacco +++++++++++++++++++++++++++++
@api_view(('POST',))
@csrf_exempt
def AddTobacco(request):
    name = request.POST.get('name')
    current_status = request.POST.get('current_status')
    previous_status = request.POST.get('previous_status')
    frequency = request.POST.get('frequency')
    year_started = request.POST.get('year_started')
    year_stopped = request.POST.get('year_stopped')

    TobaccoObj = Tobacco.objects.create(
        # user = User.objects.get(username=request.user.username),
        name = name,
        current_status = current_status,
        previous_status = previous_status,
        frequency = frequency,
        year_started = year_started,
        year_stopped = year_stopped
    )
    return JsonResponse(data = "successfully added", safe=False)



@api_view(('GET',))
@csrf_exempt
def listTobacco(request):
    caffineObj = Tobacco.objects.filter(user__username = "abhishek")
    listOfMember = []
    for i in caffineObj:
        dict = {}
        dict['name'] = i.name
        dict['current_status'] = i.current_status
        dict['previous_status'] = i.previous_status
        dict['frequency'] = i.frequency
        dict['year_started'] = i.year_started
        dict['year_stopped'] = i.year_stopped
        listOfMember.append(dict)
    return JsonResponse(data = listOfMember, safe=False)


@api_view(('DELETE',))
@csrf_exempt
def deleteTobacco(request, id):
    Tobacco.objects.get(id=id).delete()
    return JsonResponse(data="deleted successfully",safe=False)



@api_view(('PUT',))
@csrf_exempt
def updateTobacco(request, id):
    name = request.POST.get('name')
    # docImage = request.FILES
    current_status = request.POST.get('current_status')
    previous_status = request.POST.get('previous_status')
    frequency = request.POST.get('frequency')
    year_started = request.POST.get('year_started')
    year_stopped = request.POST.get('year_stopped')

    caffineObj = get_object_or_404(Tobacco, id=id)
    # user = User.objects.get(username=request.user.username),
    caffineObj.name = name
    caffineObj.current_status = current_status
    caffineObj.previous_status = previous_status
    caffineObj.frequency = frequency
    caffineObj.year_started = year_started
    caffineObj.year_stopped = year_stopped
    caffineObj.save()
    return JsonResponse(data = "successfully updated", safe=False)



#++++++++++++++++++++++++++++++++ Other +++++++++++++++++++++++++++++
@api_view(('POST',))
@csrf_exempt
def AddOther(request):
    name = request.POST.get('name')
    current_status = request.POST.get('current_status')
    previous_status = request.POST.get('previous_status')
    frequency = request.POST.get('frequency')
    year_started = request.POST.get('year_started')
    year_stopped = request.POST.get('year_stopped')

    TobaccoObj = Other.objects.create(
        # user = User.objects.get(username=request.user.username),
        name = name,
        current_status = current_status,
        previous_status = previous_status,
        frequency = frequency,
        year_started = year_started,
        year_stopped = year_stopped
    )
    return JsonResponse(data = "successfully added", safe=False)



@api_view(('GET',))
@csrf_exempt
def listOther(request):
    caffineObj = Other.objects.filter(user__username = "abhishek")
    listOfMember = []
    for i in caffineObj:
        dict = {}
        dict['name'] = i.name
        dict['current_status'] = i.current_status
        dict['previous_status'] = i.previous_status
        dict['frequency'] = i.frequency
        dict['year_started'] = i.year_started
        dict['year_stopped'] = i.year_stopped
        listOfMember.append(dict)
    return JsonResponse(data = listOfMember, safe=False)


@api_view(('DELETE',))
@csrf_exempt
def deleteOther(request, id):
    Other.objects.get(id=id).delete()
    return JsonResponse(data="deleted successfully",safe=False)



@api_view(('PUT',))
@csrf_exempt
def updateOther(request, id):
    name = request.POST.get('name')
    # docImage = request.FILES
    current_status = request.POST.get('current_status')
    previous_status = request.POST.get('previous_status')
    frequency = request.POST.get('frequency')
    year_started = request.POST.get('year_started')
    year_stopped = request.POST.get('year_stopped')

    caffineObj = get_object_or_404(Other, id=id)
    # user = User.objects.get(username=request.user.username),
    caffineObj.name = name
    caffineObj.current_status = current_status
    caffineObj.previous_status = previous_status
    caffineObj.frequency = frequency
    caffineObj.year_started = year_started
    caffineObj.year_stopped = year_stopped
    caffineObj.save()
    return JsonResponse(data = "successfully updated", safe=False)



#++++++++++++++++++++++++++++++++ ALCHOL +++++++++++++++++++++++++++++
@api_view(('POST',))
@csrf_exempt
def AddAlchol(request):
    name = request.POST.get('name')
    current_status = request.POST.get('current_status')
    previous_status = request.POST.get('previous_status')
    frequency = request.POST.get('frequency')
    year_started = request.POST.get('year_started')
    year_stopped = request.POST.get('year_stopped')

    TobaccoObj = Alchol.objects.create(
        # user = User.objects.get(username=request.user.username),
        name = name,
        current_status = current_status,
        previous_status = previous_status,
        frequency = frequency,
        year_started = year_started,
        year_stopped = year_stopped
    )
    return JsonResponse(data = "successfully added", safe=False)



@api_view(('GET',))
@csrf_exempt
def listAlchol(request):
    caffineObj = Alchol.objects.filter(user__username = "abhishek")
    listOfMember = []
    for i in caffineObj:
        dict = {}
        dict['name'] = i.name
        dict['current_status'] = i.current_status
        dict['previous_status'] = i.previous_status
        dict['frequency'] = i.frequency
        dict['year_started'] = i.year_started
        dict['year_stopped'] = i.year_stopped
        listOfMember.append(dict)
    return JsonResponse(data = listOfMember, safe=False)


@api_view(('DELETE',))
@csrf_exempt
def deleteAlchol(request, id):
    Alchol.objects.get(id=id).delete()
    return JsonResponse(data="deleted successfully",safe=False)



@api_view(('PUT',))
@csrf_exempt
def updateAlchol(request, id):
    name = request.POST.get('name')
    # docImage = request.FILES
    current_status = request.POST.get('current_status')
    previous_status = request.POST.get('previous_status')
    frequency = request.POST.get('frequency')
    year_started = request.POST.get('year_started')
    year_stopped = request.POST.get('year_stopped')

    caffineObj = get_object_or_404(Alchol, id=id)
    # user = User.objects.get(username=request.user.username),
    caffineObj.name = name
    caffineObj.current_status = current_status
    caffineObj.previous_status = previous_status
    caffineObj.frequency = frequency
    caffineObj.year_started = year_started
    caffineObj.year_stopped = year_stopped
    caffineObj.save()
    return JsonResponse(data = "successfully updated", safe=False)


# @api_view(('POST',))
# @csrf_exempt
# def add_vital(request):
#     if request.method == 'POST':
#         data = request.body
#         dict = json.loads(data)
#         username = dict.get('username')
#         height = dict.get('height', None)
#         weight = dict.get('weight', None)
#         bmi = dict.get('bmi', None)
#         hip_circum = dict.get('hip_circum', None)
#         waist_cicrum = dict.get('waist_cicrum', None)
#         whr_ratio = dict.get('whr_ratio', None)

#         biotag.objects.create(
#             user = User.objects.get(username=username),
#             height = height,
#             weight = weight,
#             bmi = bmi,
#             hip_circum = hip_circum,
#             waist_cicrum = waist_cicrum,
#             whr_ratio = whr_ratio
#         )
#         return JsonResponse(data = {"message":"Success"}, safe=False)


@api_view(('POST',))
@csrf_exempt
def list_vital(request):
    data = request.body
    dict = json.loads(data)
    username = dict.get('username')
    biotagObj = biotag.objects.filter(user__username = username)
    listOfMember = []
    for i in biotagObj:
        dict = {}
        dict['id'] = i.id
        if i.familyMemberName:
            dict['familyMemberName'] = i.familyMemberName
        else:
            dict['familyMemberName'] = ""
        
        if i.familyMemberRelationship:
            dict['familyMemberRelationship'] = i.familyMemberRelationship
        else:
            dict['familyMemberRelationship'] = ""

        if i.height:
            dict['height'] = i.height
        else:
            dict['height'] = ""
        
        if i.weight:
            dict['weight'] = i.weight
        else:
            dict['weight'] = ""
        
        if i.bmi:
            dict['bmi'] = i.bmi
        else:
            dict['bmi'] = ""
        
        if i.hip_circum:
            dict['hip_circum'] = i.hip_circum
        else:
            dict['hip_circum'] = ""
        
        if i.waist_cicrum:
            dict['waist_circum'] = i.waist_cicrum
        else:
            dict['waist_circum'] = ""

        if i.whr_ratio:
            dict['whr_ratio'] = i.whr_ratio
        else:
            dict['whr_ratio'] = ""

        listOfMember.append(dict)

    data = {"message":"Success", "data":listOfMember}
    return JsonResponse(data, safe=False)



@api_view(('POST',))
@csrf_exempt      
def update_vital(request, id):
    data = json.loads(request.body)
    height = data.get('height')
    weight = data.get('weight')
    bmi = data.get('bmi')
    hip_circum = data.get('hip_circum')
    waist_circum = data.get('waist_circum')
    whr_ratio = data.get('whr_ratio')
    biotagObj = get_object_or_404(biotag, id=id)
    biotagObj.height = height
    biotagObj.weight = weight
    biotagObj.bmi = bmi
    biotagObj.hip_circum = hip_circum
    biotagObj.waist_cicrum = waist_circum
    biotagObj.whr_ratio = whr_ratio
    biotagObj.save()
    return JsonResponse({"message":"Success"}, safe=False)




@api_view(['POST'])
@csrf_exempt
def surgery_list(request):
    data = request.body
    dict = json.loads(data)
    username = dict.get('username')
    biotagObj = biotag.objects.filter(user__username = username)
    listOfMember = []
    for i in biotagObj:
        dict = {}
        dict['id'] = i.id
        if i.familyMemberName:
            dict['familyMemberName'] = i.familyMemberName
        else:
            dict['familyMemberName'] = ""
        
        if i.familyMemberRelationship:
            dict['familyMemberRelationship'] = i.familyMemberRelationship
        else:
            dict['familyMemberRelationship'] = ""

        if i.surgery:
            dict['surgery'] = i.surgery
        else:
            dict['surgery'] = []
        listOfMember.append(dict)
    return JsonResponse({"message":"Success", 'data' : listOfMember}, safe=False)


@api_view(['POST'])
@csrf_exempt
def surgery_update(request, id):
    data = request.body
    dict = json.loads(data)
    surgery = dict.get('surgery')
    surgery_obj = get_object_or_404(biotag, id=id)
    surgery_obj.surgery = surgery
    surgery_obj.save()
    return JsonResponse({"message" : "Updated Successfully"}, safe=False)







@api_view(['POST'])
@csrf_exempt
def alcohol_update(request, id):
    data = json.loads(request.body)
    alcohol = data.get('alcohol', None)
    coffee = data.get('coffee', None)
    sexual_orientation = data.get('sexual_orientation', None)
    tobacco = data.get('tobacco', None)
    other = data.get('other', None)
    biotagObj = get_object_or_404(biotag, id=id)
    biotagObj.alcohol = alcohol
    biotagObj.coffee = coffee
    biotagObj.sexual_orientation = sexual_orientation
    biotagObj.tobacco = tobacco
    biotagObj.other = other
    biotagObj.save()
    return JsonResponse({"message":"Success"}, safe=False)


@api_view(['POST'])
@csrf_exempt
def alcohol_list(request):  
    data = request.body
    dict = json.loads(data)
    username = dict.get('username')
    biotagObj = biotag.objects.filter(user__username = username)
    listOfMember = []
    for i in biotagObj:
        dict = {}

        dict['id'] = i.id


        if i.familyMemberName:
            dict['familyMemberName'] = i.familyMemberName
        else:
            dict['familyMemberName'] = ""

        # dict['familyMemberImage'] = i.familyMemberImage

        if i.familyMemberRelationship:
            dict['familyMemberRelationship'] = i.familyMemberRelationship
        else:
            dict['familyMemberRelationship'] = ""

        if i.alcohol:
            dict['alcohol'] = i.alcohol
        else:
            dict['alcohol'] = []

        if i.coffee:
            dict['coffee'] = i.coffee
        else:
            dict['coffee'] = []
        

        if i.sexual_orientation:
            dict['sexual_orientation'] = i.sexual_orientation
        else:
            dict['sexual_orientation'] = []

        if i.tobacco:
            dict['tobacco'] = i.tobacco
        else:
            dict['tobacco'] = []
        
        if i.other:
            dict['other'] = i.other
        else:
            dict['other'] = []
        listOfMember.append(dict)

    data = {"message":"Success", "data":listOfMember}
    return JsonResponse(data, safe=False)


