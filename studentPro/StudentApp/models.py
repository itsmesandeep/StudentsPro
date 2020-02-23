from django.db import models


# Create your models here.
class StudentsData(models.Model):
    studentsRollNumber = models.IntegerField(unique=True )
    studentsRollOfMonth = models.IntegerField()
    studentfName = models.CharField(max_length=100)
    studentlName = models.CharField(max_length=100)
    studentEmail = models.EmailField(max_length=100)
    studentSchoolName = models.CharField(max_length=100)
    studentClassName = models.CharField(max_length=100)
    studenSectionName = models.CharField(max_length=100)
    student_telMarks = models.IntegerField()
    student_hindiMarks = models.IntegerField()
    student_englishMarks = models.IntegerField()
    student_mathMarks = models.IntegerField()
    student_science = models.IntegerField()
    student_social = models.IntegerField()
