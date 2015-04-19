from allauth.account import signals as allauth_signals
from django.dispatch import receiver

PROVIDER_FACEBOOK = 'facebook'
PROVIDER_GOOGLE = 'google'
PROVIDER_TWITTER = 'twitter'
FACEBOOK_FIRST_NAME_DATA = 'first_name'
FACEBOOK_LAST_NAME_DATA = 'last_name'
GOOGLE_FIRST_NAME_DATA = 'given_name'
GOOGLE_LAST_NAME_DATA = 'family_name'
FULL_NAME_DATA = 'name'


@receiver(allauth_signals.user_signed_up)
def user_signed_up(request, user, social_login=None, **kwargs):
    if social_login:
        user.first_name, user.last_name = get_name_from_social_account(
            social_login.account)
        user.save()


def get_name_from_social_account(account):
    '''Returns first_name, last_name data of account'''
    if account.provider == PROVIDER_FACEBOOK:
        return account.extra_data[FACEBOOK_FIRST_NAME_DATA], account.extra_data[FACEBOOK_LAST_NAME_DATA]

    elif account.provider == PROVIDER_GOOGLE:
        return account.extra_data[GOOGLE_FIRST_NAME_DATA], account.extra_data[GOOGLE_LAST_NAME_DATA]

    elif account.provider == PROVIDER_TWITTER:
        name = account.extra_data[FULL_NAME_DATA]
        return name.split()[0], name.split()[1]
