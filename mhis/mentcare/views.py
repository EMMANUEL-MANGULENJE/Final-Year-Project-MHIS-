from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .decorators import *
from .forms import *
from .models import * 



# Create your views here.
#home route function
@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def main(request):
    return render(request, 'main.html')


#nurse data entry form function
@login_required
@allowed_user(allowed_roles = ['NURSES'])
def NurseNotes(request):
    form = NurseNotesForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Notes successfully added')
        return redirect('nurseDetails')
    context = {
        "form": form,
    }
    return render(request, 'NurseNotes.html',{'form':form})

 
#function to get all nurses notes
@login_required
def NurseDetail(request):
    nurses = NurseNote.objects.all()
    context = {'nurses': nurses}
    return render(request, 'NurseDetail.html', context)

#delete nurses notes
@allowed_user(allowed_roles = ['NURSES'])
@login_required
def DeleteNnotes(request, pid):
    note = NurseNote.objects.get(id=pid)
    note.delete()
    return redirect('nurseDetails')

#notes updating function
@allowed_user(allowed_roles = ['NURSES'])
@login_required
def NnotesUpdate(request, pk):
    note = NurseNote.objects.get(id=pk) 
    form = NurseNotesForm(instance = note)
    if request.method == 'POST':
        form = NurseNotesForm(request.POST, instance = note)
        if form.is_valid():
            form.save()
            messages.success(request, f'Notes successfully updated')
            return redirect('nurseDetails')
    context = {
        "form": form,
    }
    return render(request, 'NurseNotes.html',context)





#doctor data entry form function
@login_required
@allowed_user(allowed_roles = ['DOCTORS'])
def DoctorNotes(request):
    form = DoctorNotesForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Notes successfully added')
        return redirect('doctorDetails')
    context = {
        "form": form
    }
    return render(request, 'DoctorNotes.html', context)

@login_required
def DoctorDetail(request):
    doctors = DoctorNote.objects.all()
    context = {'doctors': doctors}
    return render(request, 'DoctorDetail.html', context)


@login_required
@allowed_user(allowed_roles = ['DOCTORS'])
def DeleteDnotes(request, pid):
    notes = DoctorNote.objects.get(id=pid)
    notes.delete()
    return redirect('doctorDetails')


#patient updating function
@login_required
@allowed_user(allowed_roles = ['DOCTORS'])
def DNotesUpdate(request, pk):
    notes = DoctorNote.objects.get(id=pk) 
    form = DoctorNotesForm(instance = notes)
    if request.method == 'POST':
        form = DoctorNotesForm(request.POST, instance = notes)
        if form.is_valid():
            form.save()
            messages.success(request, f'Notes successfully updated')
            return redirect('doctorDetails')
    context = {
        "form": form,
    }
    return render(request, 'DoctorNotes.html',context)





#add patient into the system function
@login_required
@allowed_user(allowed_roles = ['RECORDS'])
def PatientAdd(request):
    form = PatientAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Patient successfully added')
        return redirect('patientDetail')
    context = {
        "form": form,
    }
    return render(request, 'PatientAdd.html',{'form':form})


#function to get all patient details from the database
@login_required
def patientDetail(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patientDetail.html', context)


#delete patient function
@login_required
@allowed_user(allowed_roles = ['Records'])
def DeletePatient(request, pid):
    patients = Patient.objects.get(id=pid)
    patients.delete()
    return redirect('patientDetail')


#patient updating function
@login_required
@allowed_user(allowed_roles = ['Records'])
def PatientUpdate(request, pk):
    patient = Patient.objects.get(id=pk) 
    form = PatientAddForm(instance = patient)
    if request.method == 'POST':
        form = PatientAddForm(request.POST, instance = patient)
        if form.is_valid():
            form.save()
            messages.success(request, f'Patient successfully updated')
            return redirect('patientDetail')
    context = {
        "form": form,
    }
    return render(request, 'PatientAdd.html',context)



#patient discharge functions
@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def Discharge(request):
    form = DischargeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Patient successfully updated')
        return redirect('dischargeDetails')
    context = {
        "form": form
    }
    return render(request, 'Discharge.html',{'form':form})

@login_required
def DischargeDetail(request):
    discharge = Exit.objects.all()
    context = {'discharge': discharge,
               }
    return render(request, 'DischargeDetail.html', context)


@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def DeleteDischarge(request, pid):
    discharge = Exit.objects.get(id=pid)
    discharge.delete()
    return redirect('dischargeDetails')


@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def DischargeUpdate(request, pk):
    discharge = Exit.objects.get(id=pk)
    form = DischargeForm(instance=discharge)
    if request.method == 'POST':
        form = DischargeForm(request.POST, instance=discharge)
        if form.is_valid():
            form.save()
            messages.success(request, f'Patient successfully discharged')
            return redirect('dischargeDetails')
    context = {
        "form": form,
    }
    return render(request, 'Discharge.html', context)





 
#appointment functions
@login_required
def MakeAppointment(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Appointment successfully added')
        return redirect('appointmentDetails')
    context = {
        "form": form,
    }
    return render(request, 'MakeAppointment.html',{'form':form})

@login_required
def AppointmentDetail(request):
    appointments = Appointment.objects.all()
    context = {'appointments':  appointments}
    return render(request, 'AppointmentDetail.html', context)

@login_required
def DeleteAppointment(request, pid):
    appointments = Appointment.objects.get(id=pid)
    appointments.delete()
    messages.success(request, f'Appointment successfully deleted')
    return redirect('appointmentDetails')

@login_required
def AppointmentUpdate(request, pk):
    appointments = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointments)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointments)
        if form.is_valid():
            form.save()
            messages.success(request, f'Appointment successfully updated')
            return redirect('appointmentDetails')
    context = {
        "form": form,
    }
    return render(request, 'MakeAppointment.html', context)


#HIV patient status form
@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def HIVSeroStatus(request):
    form = HIVStatusForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f' Successfully added')
        return redirect('patientDetail')
    context = {
        "form": form,
    }
    return render(request, 'HIV.html',{'form':form})




#diagnosis entry form
@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def Diagnosis(request):
    form = DiagnosisForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f' Successfully added')
        return redirect('diagnosisDetails')
    context = {
        "form": form,
    }
    return render(request, 'Diagnosis.html', {'form': form})


@login_required
def DiagnosisDetail(request):
    diagnosis = Diagnoses.objects.all()
    context = {'diagnosis':  diagnosis}
    return render(request, 'DiagnosisDetail.html', context)


@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def DeleteDiagnosis(request, pid):
    diagnosis = Diagnoses.objects.get(id=pid)
    diagnosis.delete()
    return redirect('diagnosisDetails')

@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def DiagnosisUpdate(request, pk):
    diagnosis = Diagnoses.objects.get(id=pk)
    form = DiagnosisForm(instance=diagnosis)
    if request.method == 'POST':
        form = DiagnosisForm(request.POST, instance=diagnosis)
        if form.is_valid():
            form.save()
            messages.success(request, f'Patient successfully edited')
            return redirect('diagnosisDetails')
    context = {
        "form": form,
    }
    return render(request, 'Diagnosis.html', context)





#medical/ psychiatric history form function
@login_required
def MedicalPsychiatricHistory(request):
    form = MedicalPsychiatricHistoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f' Successfully added')
        return redirect('patientDetail')
    context = {
        "form": form,
    }
    return render(request, 'MedicalPsychiatricHistory.html',{'form':form})

@login_required
def HistoryDetail(request):
    history = MedicalPsychiatricHistorys.objects.all()
    context = {'history': history}
    return render(request, 'MedicalPsychiatricHistoryDetail.html', context)



#prescription form function
@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def Prescription(request):
    form = PrescriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f' Successfully added')
        return redirect('prescriptionDetails')
    context = {
        "form": form
    }
    return render(request, 'Prescription.html', context)


#function to get all prescriptions in the database
@login_required
def prescriptionDetails(request):
    pre = Prescriptions.objects.all()
    context = {'pre': pre}
    return render(request, 'PrescriptionDetails.html', context)


@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def DeletePrescription(request, pid):
    prescription = Prescriptions.objects.get(id=pid)
    prescription.delete()
    return redirect('prescriptionDetails')

@login_required
@allowed_user(allowed_roles = ['Doctors, Nurses'])
def PrescriptionUpdate(request, pk):
    prescription = Prescriptions.objects.get(id=pk)
    form = PrescriptionForm(instance=prescription)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            messages.success(request, f'Prescription successfully edited')
            return redirect('prescriptionDetails')
    context = {
        "form": form,
    }
    return render(request, 'Prescription.html', context)

#user registration form
@login_required
def register(request):
    form = UserRegForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}!,You can login to acces oyur account')
        return redirect('login.html')
    form = UserRegForm()
    return render(request, 'register.html',{'form':form})




#user login form
@login_required
def login(request):
    loginform = UserReg()
    return render(request, 'login.html',{'form':loginform})


#logout route function
@login_required
def logout(request):
    return render(request, 'logout.html')


def reset_password(request):
    return render(request, )

def confirm(request):
    return render(request, )



"""report functions. adding report, displaying report, 
    updating report and deleting report"""
@login_required
@allowed_user(allowed_roles = ['Night Super'])
def Reports(request):
    form = ReportsForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Reports successfully added')
        return redirect('Rdetail')
    context = {
        "form": form
    }
    return render(request, 'Reports.html', context)

@login_required
def Rdetail(request):
    generalreport = Report.objects.all()
    context = {'generalreport': generalreport}
    return render(request, 'ReportsDetail.html', context)


@login_required
@allowed_user(allowed_roles = ['Night Super'])
def DeleteReports(request, pid):
    reports = Report.objects.get(id=pid)
    reports.delete()
    return redirect('Rdetail')

@login_required
@allowed_user(allowed_roles = ['DOCTORS'])
def ReportsUpdate(request, pk):
    reports = Report.objects.get(id=pk)
    form = ReportsForm(instance=reports)
    if request.method == 'POST':
        form = ReportsForm(request.POST, instance=reports)
        if form.is_valid():
            form.save()
            messages.success(request, f'Report successfully updated')
            return redirect('Rdetail')
    context = {
        "form": form,
    }
    return render(request, 'Reports.html', context)



 
"""wards functions, ward = male acute ward, MRward = Male Rehabilitation ward
FAward = Female Acute award, FRward = Female rrehabilitation ward
Pward = Paying ward"""
@login_required
def ward(request):
    patientward = Male_Acute_Ward.objects.all()
    count =  Male_Acute_Ward.objects.count()#funcrion to count all patients in the ward
    context = {'patientward': patientward}
    return render(request, 'Wards.html', {"patientward":patientward, "count": count})

@login_required
def MRward(request):
    maleward = Male_Rehabilitation_Ward.objects.all()
    count =  Male_Rehabilitation_Ward.objects.count()#funcrion to count all patients in the ward
    context = {'maleward': maleward}
    return render(request, 'MRward.html', {"maleward":maleward, "count": count})

@login_required
def FRward(request):
    femaleward = Female_Rehabilitation_Ward.objects.all()
    count =  Female_Rehabilitation_Ward.objects.count()#funcrion to count all patients in the ward
    context = {'femaleward': femaleward}
    return render(request, 'FRward.html', {"femaleward":femaleward, "count": count})

@login_required
def FAward(request):
    femaleAward = Female_Acute_Ward.objects.all()
    count =  Female_Acute_Ward.objects.count()#funcrion to count all patients in the ward
    context = {'femaleAward': femaleAward}
    return render(request, 'FAward.html', {"femaleAward":femaleAward, "count": count})

@login_required
def Pward(request):
    payward = Paying_Ward.objects.all()
    count =  Paying_Ward.objects.count()#funcrion to count all patients in the ward
    context = {'payward': payward}
    return render(request, 'Pward.html', {"payward":payward, "count": count})