from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from.forms import *
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
def NurseDetail(request):
    nurses = NurseNote.objects.all()
    context = {'nurses': nurses}
    return render(request, 'NurseDetail.html', context)

#delete nurses notes
@login_required
def DeleteNnotes(request, pid):
    note = NurseNote.objects.get(id=pid)
    note.delete()
    return redirect('nurseDetails')

#notes updating function
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

def DoctorDetail(request):
    doctors = DoctorNote.objects.all()
    context = {'doctors': doctors}
    return render(request, 'DoctorDetail.html', context)


@login_required
def DeleteDnotes(request, pid):
    notes = DoctorNote.objects.get(id=pid)
    notes.delete()
    return redirect('doctorDetails')


#patient updating function
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
def patientDetail(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patientDetail.html', context)


#delete patient function
@login_required
def DeletePatient(request, pid):
    patients = Patient.objects.get(id=pid)
    patients.delete()
    return redirect('patientDetail')


#patient updating function
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

def DischargeDetail(request):
    discharge = Exit.objects.all()
    context = {'discharge': discharge,
               }
    return render(request, 'DischargeDetail.html', context)


@login_required
def DeleteDischarge(request, pid):
    discharge = Exit.objects.get(id=pid)
    discharge.delete()
    return redirect('dischargeDetails')


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


def DiagnosisDetail(request):
    diagnosis = Diagnoses.objects.all()
    context = {'diagnosis':  diagnosis}
    return render(request, 'DiagnosisDetail.html', context)


@login_required
def DeleteDiagnosis(request, pid):
    diagnosis = Diagnoses.objects.get(id=pid)
    diagnosis.delete()
    return redirect('diagnosisDetails')

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


def HistoryDetail(request):
    history = MedicalPsychiatricHistorys.objects.all()
    context = {'history': history}
    return render(request, 'MedicalPsychiatricHistoryDetail.html', context)



#prescription form function
@login_required
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
def prescriptionDetails(request):
    pre = Prescriptions.objects.all()
    context = {'pre': pre}
    return render(request, 'PrescriptionDetails.html', context)


@login_required
def DeletePrescription(request, pid):
    prescription = Prescriptions.objects.get(id=pid)
    prescription.delete()
    return redirect('prescriptionDetails')

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
def login(request):
    loginform = UserReg()
    return render(request, 'login.html',{'form':loginform})


#logout route function
@login_required
def logout(request):
    return render(request, 'logout.html')


@login_required
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

def Rdetail(request):
    generalreport = Report.objects.all()
    context = {'generalreport': generalreport}
    return render(request, 'ReportsDetail.html', context)


 
"""wards functions, ward = male acute ward, MRward = Male Rehabilitation ward
FAward = Female Acute award, FRward = Female rrehabilitation ward
Pward = Paying ward"""
def ward(request):
    patientward = Male_Acute_Ward.objects.all()
    context = {'patientward': patientward}
    return render(request, 'Wards.html', context)

def MRward(request):
    maleward = Male_Rehabilitation_Ward.objects.all()
    context = {'maleward': maleward}
    return render(request, 'MRward.html', context)

def FRward(request):
    femaleward = Female_Rehabilitation_Ward.objects.all()
    context = {'femaleward': femaleward}
    return render(request, 'FRward.html', context)

def FAward(request):
    femaleAward = Female_Acute_Ward.objects.all()
    context = {'femaleAward': femaleAward}
    return render(request, 'FAward.html', context)

def Pward(request):
    payward = Paying_Ward.objects.all()
    context = {'payward': payward}
    return render(request, 'Pward.html', context)