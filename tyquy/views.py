from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from sys import stderr
from sys import stderr
from sys import stderr
from sys import stderr
from .processServices import UserProcessService, CommentProcessService 

# Create your views here.

def index(request):
# return HttpResponse("Tengo Hambre")
    userProcessService = UserProcessService()
    users = userProcessService.getUsers()
    jsonUsers = []
    for user in users:
        jsonUser = {"facebook_id":user.facebook_profile_id, "first_name":user.first_name, "last_name":user.last_name}
        jsonUsers.append(jsonUser)
# return JsonResponse({'cedula': 'nombres'})
# return JsonResponse(userService.all_users())
    return HttpResponse(jsonUsers)

def userData(request, facebook_profile_id):
    userProcessService = UserProcessService()
    user = userProcessService.getUser(facebook_profile_id)
    jsonUsers = []
    jsonUser = {"facebook_id":user.facebook_profile_id, "first_name":user.first_name, "last_name":user.last_name}
    jsonUsers.append(jsonUser)
    return HttpResponse(jsonUsers)
 
'''
 users = userProcessService.getUserProfile(user_profile)
 return users
 jsonUsers = []
 for user in users:
  jsonUser = {"facebook_id":user.facebook_profile_id, "first_name":user.first_name, "last_name":user.last_name}
  jsonUsers.append(jsonUser)
# return JsonResponse({'cedula': 'nombres'})
# return JsonResponse(userService.all_users())
 return HttpResponse(jsonUsers)
'''

def createUser(self, facebook_profile_id, first_name, middle_name , last_name, full_name):
    userProcessService = UserProcessService()
    result = userProcessService.createUser(facebook_profile_id, first_name, middle_name, last_name, full_name)
    return HttpResponse([{"result": result}])

def createComment(self, user_id, application, description):
    commentProcessService = CommentProcessService()
    result = commentProcessService.createComment(user_id, application, description)
    return HttpResponse([{"result": result}])

def saveUserSession(self, user_id, session_id, feedback_level, feedback):
    userProcessService = UserProcessService()
    userProcessService.saveUserSession(user_id, session_id, feedback_level, feedback)
    