from django.contrib import admin
from django.apps import apps
from .models import *
from django import forms

# Register your models here.
admin.site.register(TraineePosition)
admin.site.register(Assignment)
admin.site.register(CarrierConsent)
admin.site.register(CarrierAssesement)

class CarrierAssignmentPeriodForm(forms.ModelForm):
    class Meta:
        model = CarrierAssignmentPeriod
        fields='__all__'

    def clean(self):
        from_date = self.cleaned_data.get('from_date')
        to_date = self.cleaned_data.get('to_date')
        if from_date > to_date:
            raise forms.ValidationError("Dates are incorrect")
        return self.cleaned_data

class CarrierAssignmentPeriodAdmin(admin.ModelAdmin):
        form = CarrierAssignmentPeriodForm


admin.site.register(CarrierAssignmentPeriod, CarrierAssignmentPeriodAdmin)

class ApplicationPeriodForm(forms.ModelForm):
    class Meta:
        model = ApplicationPeriod
        fields='__all__'

    def clean(self):
        from_date = self.cleaned_data.get('from_date')
        to_date = self.cleaned_data.get('to_date')
        if from_date > to_date:
            raise forms.ValidationError("Dates are incorrect")

        cas = CarrierAssignmentPeriod.objects.filter(
            department=self.cleaned_data.get('department')
        ).first()
        if cas:
            if cas.to_date > from_date:
                raise forms.ValidationError("Carrier Assignment Period hasnt expired")
        else:
            raise forms.ValidationError("Carrier Assignment Period doesnt exist")
        return self.cleaned_data

class ApplicationPeriodAdmin(admin.ModelAdmin):
        form = ApplicationPeriodForm


admin.site.register(ApplicationPeriod, ApplicationPeriodAdmin)

class AssignmentPeriodForm(forms.ModelForm):
    class Meta:
        model = AssignmentPeriod
        fields='__all__'

    def clean(self):
        from_date = self.cleaned_data.get('from_date')
        to_date = self.cleaned_data.get('to_date')
        if from_date > to_date:
            raise forms.ValidationError("Dates are incorrect")

        cas = ApplicationPeriod.objects.filter(
            department=self.cleaned_data.get('department')
        ).first()
        if cas:
            if cas.to_date > from_date:
                raise forms.ValidationError("Application Period hasnt expired")
        else:
            raise forms.ValidationError("Application Period doesnt exist")
        return self.cleaned_data

class AssignmentPeriodAdmin(admin.ModelAdmin):
        form = AssignmentPeriodForm


admin.site.register(AssignmentPeriod, AssignmentPeriodAdmin)

class  InternshipReportPeriodForm(forms.ModelForm):
    class Meta:
        model = InternshipReportPeriod
        fields='__all__'

    def clean(self):
        from_date = self.cleaned_data.get('from_date')
        to_date = self.cleaned_data.get('to_date')
        if from_date > to_date:
            raise forms.ValidationError("Dates are incorrect")

        cas = AssignmentPeriod.objects.filter(
            department=self.cleaned_data.get('department')
        ).first()
        if cas:
            if cas.to_date > from_date:
                raise forms.ValidationError("Assignment Period hasnt expired")
        else:
            raise forms.ValidationError("Assignment Period doesnt exist")
        return self.cleaned_data

class InternshipReportPeriodAdmin(admin.ModelAdmin):
        form = InternshipReportPeriodForm


admin.site.register(InternshipReportPeriod, InternshipReportPeriodAdmin)