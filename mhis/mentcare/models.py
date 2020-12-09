from django.db import models
from datetime import datetime, date

# Create your models here.

#Employee table
class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    rank = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.surname



#disstrict htable
class Districts(models.Model):
    home_district = models.CharField(max_length=50)

    def __str__(self):
        return self.home_district



#education table
class Education(models.Model):
    Education_level = models.CharField(max_length=50)

    def __str__(self):
        return self.Education_level


#tribe table
class Tribe(models.Model):
    tribe = models.CharField(max_length=50)

    def __str__(self):
        return self.tribe


#marural satus table
class Marital(models.Model):
    marital_status = models.CharField(max_length=50)

    def __str__(self):
        return self.marital_status


#religion table
class Religion(models.Model):
    religion = models.CharField(max_length=50)

    def __str__(self):
        return self.religion



class Gender(models.Model):
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.gender

class Employement(models.Model):
    employement = models.CharField(max_length=50)

    def __str__(self):
        return self.employement


class Patient(models.Model):
    history_of_consultation = models.CharField(max_length=50)
    # hospital_in_patient_number = models.IntegerField()
    # hospital_OPD_number = models.IntegerField()
    first_name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    date_of_birth = models.DateField(auto_now_add=False, auto_now = False, blank=True)
    nationality = models.CharField(max_length=20)
    home_village = models.CharField(max_length=20)
    home_TA = models.CharField(max_length=20)
    phone_number = models.IntegerField(null = True)
    name_of_next_of_kin = models.CharField(max_length=30)
    phone_of_guardian = models.IntegerField()
    employment =  models.ForeignKey(Employement, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    marital_status = models.ForeignKey(Marital, on_delete=models.CASCADE)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)
    Education_level =  models.ForeignKey(Education, on_delete=models.CASCADE)
    home_district = models.ForeignKey(Districts, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + " " + self.surname




class Region(models.Model):
    region_reffered_from  = models.CharField(max_length=50)

    def __str__(self):
        return self.region_reffered_from 



class RefferalMode(models.Model):
    mode_of_refferal  = models.CharField(max_length=50)

    def __str__(self):
        return self.mode_of_refferal 


class MedicalPsychiatricHistorys(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referring_institution = models.CharField(max_length=50)
    last_time_treated_at = models.CharField(max_length=20)
    region_reffered_from = models.ForeignKey(Region, on_delete=models.CASCADE)
    mode_of_refferal = models.ForeignKey(RefferalMode, on_delete=models.CASCADE)
    history_of_mental_illness_in_family = models.CharField(max_length=5)
    history_of_epilepsy = models.CharField(max_length=35)
    date_of_OPD_review = models.DateField()
    type_of_OPD_exit = models.CharField(max_length=25)
    number_of_addmission = models.IntegerField()
    type_of_ward_exit = models.CharField(max_length=50)
    number_of_abscond = models.IntegerField()
    if_transferred_where = models.CharField(max_length=50)

    def __str__(self):
        return str(self.patient_name)#returning a non string type

class PsychiatricDiagnosis(models.Model):
    Psychiatric  = models.CharField(max_length=50)

    def __str__(self):
        return self.Psychiatric 

class MedicalDiagnosis(models.Model):
    medical  = models.CharField(max_length=50)

    def __str__(self):
        return self.medical

class Diagnoses(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    psychiatric =  models.ForeignKey(PsychiatricDiagnosis, on_delete=models.CASCADE)
    medical =  models.ForeignKey(MedicalDiagnosis, on_delete=models.CASCADE)





class HIVStatus(models.Model):
    HIV_sero_status  = models.CharField(max_length=50)

    def __str__(self):
        return self.HIV_sero_status 



class HAARTIndication(models.Model):
    indication_for_HAART  = models.CharField(max_length=100)

    def __str__(self):
        return self.indication_for_HAART

class HAARTDuration(models.Model):
    how_long_on_HAART  = models.CharField(max_length=50)

    def __str__(self):
        return self.how_long_on_HAART

class HAARTRegime(models.Model):
    if_on_HAART_what_is_regime  = models.CharField(max_length=50)

    def __str__(self):
        return self.if_on_HAART_what_is_regime


class Prescriptions(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription_name = models.TextField(max_length=2000)
    
    def __str__(self):
        return str(self.patient_name)


class HIVTest(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    HIV_sero_status = models.ForeignKey(HIVStatus, on_delete=models.CASCADE)
    if_reactive_when_was_tested = models.CharField(max_length=25)
    if_reactive_is_on_HAART = models.CharField(max_length=5)
    indication_for_HAART = models.ForeignKey(HAARTIndication, on_delete=models.CASCADE)
    how_long_on_HAART = models.ForeignKey(HAARTDuration, on_delete=models.CASCADE)
    if_on_HAART_when_initiated = models.CharField(max_length=30)
    if_on_HAART_what_is_regime = models.ForeignKey(HAARTRegime, on_delete=models.CASCADE)

    def __str__(self):
        return self.HIV_sero_status

class Exit(models.Model):
    doctor_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    final_prescription = models.TextField(max_length=2000)
    date_of_exit = models.DateField()

    def __str__(self):
        return self.final_prescription


class DoctorNote(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor_notes = models.TextField(max_length=1000)


class NurseNote(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Nurse_notes = models.TextField(max_length=1000)



    def __str__(self):
        return self.prescription



class Appointment(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    checked_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    updated_at = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField()
    comments = models.TextField(max_length=500)
    services = models.TextField(max_length=500)

    def __str__(self):
        return str(self.patient_name)



class Report(models.Model):
    ward_name = models.CharField(max_length=3000)
    General_Report = models.TextField(max_length=10000)

    def __str__(self):
        return self.ward_name


#Patients wards tables
class Male_Acute_Ward(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_name)#returning a non string type

class Female_Acute_Ward(models.Model):
    patient_name= models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_name)#returning a non string type
    

class Male_Rehabilitation_Ward(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_name)#returning a non string type
    

class Female_Rehabilitation_Ward(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient_name)#returning a non string type
    

class Paying_Ward(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.patient_name)#returning a non string type