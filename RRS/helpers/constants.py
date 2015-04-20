class Status:
    HTTP_302_FOUND = 302
    HTTP_200_OK = 200
    
class Provider:
    FACEBOOK = 'facebook'
    GOOGLE = 'google'
    TWITTER = 'twitter'
    LIST = (FACEBOOK, GOOGLE, TWITTER)
    
    class Data:
        '''Stored in allauth's model SocialAccount.extra_data in json format'''
        FACEBOOK_FIRST_NAME = 'first_name'
        FACEBOOK_LAST_NAME = 'last_name'
        GOOGLE_FIRST_NAME = 'given_name'
        GOOGLE_LAST_NAME = 'family_name'
        FULL_NAME = 'name'
