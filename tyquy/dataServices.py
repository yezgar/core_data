'''
Created on 10/10/2015

@author: yez
'''
from models import User, UserSession, Session, Comment
from django.db.models import Max
from django.core.exceptions import MultipleObjectsReturned

class UserDataService:
    def newUser(self, facebook_profile_id, first_name, middle_name , last_name, full_name):
        user = User(facebook_profile_id = facebook_profile_id, first_name = first_name, middle_name = middle_name , last_name = last_name, full_name = full_name)
        user.save()
        return user
    
    def getUser(self, facebook_profile_id):
        try:
            user = User.objects.get(facebook_profile_id = facebook_profile_id)
            return user
        except User.DoesNotExist as e:
            return None
        except MultipleObjectsReturned as e:
            return 'MULTIPLE'

class UserSessionDataService:
    def getLastSession(self, user_id):
        userSessions = UserSession.objects.filter(user_id = user_id).aggregate(Max('id'))
        userSession = userSessions[0]
        return Session.objects.get(id = userSession.session_id)
    
    def saveUserSession(self, user_id, session_id, feedback_level, feedback):
        userSession = UserSession(user_id = user_id, session_id = session_id, feedback_level = feedback_level, feedback = feedback)
        userSession.save()


class SessionDataService:
    def getNextSession(self, session_id):
        currentSession = Session.objects.get(id = session_id)
        return Session.objects.get(level_id = currentSession.level_id, session_order = currentSession.session_order+1)
    
    def getNextLevelSession(self, level_id):
        return Session.objects.get(level_id = level_id, session_order = 1)


'''FALTA DESARROLLAR TODO ESTE METODO, OJO    
    def getCurrentSession(self, session_id):
        try:
            currentSession = Session.objects.get(id = session_id)
            return currentSession
        Exception Session.DoesNotExist
'''

class CommentDataService:
    def notViewedComment(self, user_id):
        try:
            comment = Comment.objects.get(user_id = user_id, viewed = 0)
            return True
        except Comment.DoesNotExist as e:
            return False
        except MultipleObjectsReturned as e:
            return True
        
    def createComment(self, user_id, application, description):
        comment = Comment(description = description, viewed = False, application = application, user_id = user_id)
        comment.save()
        return comment