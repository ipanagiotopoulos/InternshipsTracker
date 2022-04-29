import ldap
from internships_tracker import settings
from django.contrib.auth import get_user_model

import logging
UserModel = get_user_model()
logger = logging.getLogger('internships_tracker')


def decodeAttribute(entry, attribute):
    if attribute in entry:
        return entry[attribute][0].decode('utf8')
    else:
        return None


def convertToDict(entry):
    return {
        'givenName': decodeAttribute(entry, settings.GIVEN_NAME_LDAP_ATTRIBUTE),
        'sn': decodeAttribute(entry, settings.SURNAME_LDAP_ATTRIBUTE),
        'mail': decodeAttribute(entry, settings.EXTERNAL_MAIL_LDAP_ATTRIBUTE),
        'title': decodeAttribute(entry, settings.TITLE_LDAP_ATTRIBUTE),
        'department': decodeAttribute(entry, settings.DEPARTMENT_LDAP_ATTRIBUTE),
    }


class ldapConnection:

    handler = None

    def connect(self):
        print("connect")
        """
        Connect to LDAP
        """
        logger.debug('User %s exists' % username)
        print('User %s exists' % username)
        self.handler = ldap.initialize(settings.AUTH_LDAP_SERVER_URI)
        if settings.AUTH_LDAP_START_TLS:
            self.handler.start_tls_s()

        some = self.handler.simple_bind(
            settings.AUTH_LDAP_BIND_DN, settings.AUTH_LDAP_BIND_PASSWORD)
        print("details about the connection with ssaml2", some)

    def verify(self, uid, externalMail):
        print("verify")
        """
        Verify that user externalMail is correct
        """
        query = '(&(' + settings.EXTERNAL_MAIL_LDAP_ATTRIBUTE + \
            '=' + externalMail + ')(uid=' + uid + '))'
        print("query is here", query)
        result = self.handler.search_s(
            settings.AUTH_LDAP_BASE_DN, ldap.SCOPE_SUBTREE, query)
        print("here is the result", result)
        if len(result) == 1:
            return True
        else:
            return False

    def getUserMail(self, uid):
        print("getUserMail")
        """
        get user externalMail
        """
        print("get external mail", self.request)
        query = '(uid=%s)' % uid
        result = self.handler.search_s(
            settings.AUTH_LDAP_BASE_DN, ldap.SCOPE_SUBTREE, query)
        if len(result) == 1:
            ldapEntry = result[0][1]
            if settings.EXTERNAL_MAIL_LDAP_ATTRIBUTE in ldapEntry:
                return ldapEntry[settings.EXTERNAL_MAIL_LDAP_ATTRIBUTE][0].decode('utf8')
            else:
                return None
        else:
            return None

    def getUserInfo(self, uid):
        print("getUserInfo")
        """
        get user information: username, givenName, sn and externalMail
        """
        query = '(uid=%s)' % uid
        print("the user is ", uid)
        result = self.handler.search_s(
            settings.AUTH_LDAP_BASE_DN, ldap.SCOPE_SUBTREE, query)
        print("result of ldap search", result)
        if len(result) == 1:
            some = convertToDict
            print("here are some details about the user", some.__dict__)
            return convertToDict(result[0][1])
        else:
            return None

    def close(self):
        self.handler.unbind_s()
