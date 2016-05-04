from .models import User, Session
from .dataServices import SessionDataService

class UserBusinessService:
    def all_users(self):
#  return {'cedula': 'nombres'} 
        return User.objects.all()

    def getUserProfile(self, facebook_profile_id):
        return User.objects.all().filter(facebook_profile_id=facebook_profile_id)
    
    def getUser(self, facebook_profile_id):
        users = User.objects.all().filter(facebook_profile_id=facebook_profile_id)        
        return users 
    
class SessionBusinessService:
    def getNextSession(self, session):
        try:
            sessionDataService = SessionDataService()
            return sessionDataService.getNextSession(session.id)
        except Session.DoesNotExist as e:
            try:
                return sessionDataService.getNextLevelSession(session.level_id)
            except Session.DoesNotExist as e:
                return 'MAX_LEVEL'