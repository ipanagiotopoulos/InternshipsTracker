from .enums import DEPARTMENT_CHOICES_GR,DEPARTMENT_CHOICES




def username_to_register_number(username):
  delimited_username = username.split('@')
  register_no = delimited_username[0][2:]
  return register_no


def translate_uni_departments(department_alias):
    for choice in  DEPARTMENT_CHOICES_GR:
        if  choice[1] ==  department_alias :
            for choice2 in DEPARTMENT_CHOICES:
              if choice2[0]==choice[0]:
                 return choice2[0]