from allauth.account import signals as allauth_signals
from django.dispatch import receiver

from helpers.constants import Provider

@receiver(allauth_signals.user_signed_up)
def user_signed_up(request, user, social_login=None, **kwargs):
    if social_login:
        user.first_name, user.last_name = get_name_from_social_account(
            social_login.account)
        user.save()


def get_name_from_social_account(account):
    '''Returns first_name, last_name data of account'''
    if account.provider == Provider.FACEBOOK:
        return account.extra_data[Provider.Data.FACEBOOK_FIRST_NAME], account.extra_data[Provider.Data.FACEBOOK_LAST_NAME]

    elif account.provider == Provider.GOOGLE:
        return account.extra_data[Provider.Data.GOOGLE_FIRST_NAME], account.extra_data[Provider.Data.GOOGLE_LAST_NAME]

    elif account.provider == Provider.TWITTER:
        name = account.extra_data[Provider.Data.FULL_NAME]
        return name.split(' ', 1)
