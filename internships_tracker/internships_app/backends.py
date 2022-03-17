from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from internships_tracker import settings

import logging
UserModel = get_user_model()
logger = logging.getLogger('internhsips_app')


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('User %s attempting to login' % username)
        logger.info('User %s attempting to login' % username)

        if username.endswith(settings.AUTH_LDAP_INTERNAL_DOMAIN):
            logger.debug(
                'User %s is an internal user, deffering to LDAP auth' % username)
            print(
                'User %s is an internal user, deffering to LDAP auth' % username)
            return

        try:
            user = UserModel.objects.get(username=username)
            logger.debug('User %s exists' % username)
            print('User %s exists' % username)

        except UserModel.DoesNotExist:
            print('User %s does not exist' % username)
            logger.debug('User %s does not exist' % username)
            return

        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(
                Q(email__iexact=username)).order_by('id').first()
            print(
                'There are multiple users with the username %s' % username)
            logger.debug(
                'There are multiple users with the username %s' % username)
        if user.check_password(password) and self.user_can_authenticate(user):
            logger.info('User %s was successfully authenticated' % username)
            return user
        else:
            logger.info(
                'User %s was NOT successfully authenticated' % username)