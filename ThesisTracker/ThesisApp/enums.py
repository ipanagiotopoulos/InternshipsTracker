# from enum import Enum


# class UniversityDepartments(Enum):
#     IT = "Informatics and Telematics"
#     GS = "Geogrpaphy"
#     HS = "Economics & Sustainable Development"
#     DS = "Nutrition and  Dietetics"

#     @classmethod
#     def choices(cls):
#         return tuple((i.name, i.value) for i in cls)


IT = "IT"
GS = "G"
HS = "ESD"
DS = "ND"
DEPARTMENT_CHOICES = [
    (IT, "Informatics and Telematics"),
    (GS, "Geogrpaphy"),
    (HS, "Economics & Sustainable Development"),
    (DS, "Nutrition and  Dietetics"),
]
