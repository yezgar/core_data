'''
Created on 10/10/2015

@author: yez
'''

from tyquy.businessServices import UserBusinessService
from tyquy.dataServices import CommentDataService
from dataServices import UserDataService, UserSessionDataService
from django.template.defaultfilters import default

class UserProcessService:
    def getUser(self, facebook_profile_id):
        userBusinessService = UserBusinessService()
        users = userBusinessService.getUserProfile(facebook_profile_id)
        if len(users) > 0: return users[0]
        else: return default
        users.g
        if users is None: return "No Encontrado"
        else: return "Encontrado"
    
    def createUser(self, facebook_profile_id, first_name, middle_name, last_name, full_name):        
        userDataService = UserDataService()
        user  = userDataService.getUser(facebook_profile_id)
        if user is None:
            user = userDataService.newUser(facebook_profile_id, first_name, middle_name, last_name, full_name)
            return 'OK'
        else: return 'ERROR'
        
    def saveUserSession(self, user_id, session_id, feedback_level, feedback):
        userSessionDataService = UserSessionDataService()
        userSessionDataService.saveUserSession(user_id, session_id, feedback_level, feedback)
        
    def getUsers(self):
        userBusinessService = UserBusinessService()
        return userBusinessService.all_users()


class CommentProcessService:
    def createComment(self, user_id, application, description):
        commentDataService = CommentDataService()
        if commentDataService.notViewedComment(user_id)==False:
            commentDataService.createComment(user_id, application, description)
            return 'OK'
        else: return 'ERROR'