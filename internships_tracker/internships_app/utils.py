from .enums import DEPARTMENT_CHOICES_GR


def username_to_register_number(username):
  delimited_username = username.split('@')
  register_no = delimited_username[0][2:]
  return register_no


def translate_uni_departments(department_alias):
    for choice in  DEPARTMENT_CHOICES_GR:
        if( choice ==  department_alias ):
            return choice