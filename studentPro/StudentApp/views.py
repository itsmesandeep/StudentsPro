from django.shortcuts import render,redirect
from .models import StudentsData


def home_view(request):
    if request.method == "POST":
        srnum = request.POST.get('srnum')
        srnumm = request.POST.get('srnumm')
        sfname = request.POST.get('sfname')
        slname = request.POST.get('slname')
        semail = request.POST.get('semail')
        ssname = request.POST.get('ssname')
        ssection = request.POST.get('ssection')
        sclass = request.POST.get('sclass')
        tmarks = request.POST.get('tmarks')
        emarks = request.POST.get('emarks')
        hmarks = request.POST.get('hmarks')
        mmarks = request.POST.get('mmarks')
        smarks = request.POST.get('smarks')
        ssmarks = request.POST.get('ssmarks')
        data = StudentsData(
            studentsRollNumber=srnum,
            studentsRollOfMonth=srnumm,
            studentfName=sfname,
            studentlName=slname,
            studentEmail=semail,
            studentSchoolName=ssname,
            studentClassName=sclass,
            studenSectionName=ssection,
            student_telMarks=tmarks,
            student_englishMarks=emarks,
            student_hindiMarks=hmarks,
            student_mathMarks=mmarks,
            student_science=smarks,
            student_social=ssmarks,
        )
        data.save()
        students = StudentsData.objects.all()
        context = {'students': students}
        return render(request, 'displayView.html', context)

    else:
        return render(request, 'home.html')


def displayView(request):
    students = StudentsData.objects.all()
    context = {'students': students}
    return render(request, 'displayView.html', context)


def updateView(request, pk):
    student = StudentsData.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'updateView.html', context)


def insertUpdatedData(request, pk):
    student = StudentsData.objects.get(id=pk)
    student.studentsRollNumber = request.POST.get('srnum')
    student.studentsRollOfMonth = request.POST.get('srnumm')
    student.studentfName = request.POST.get('sfname')
    student.studentlName = request.POST.get('slname')
    student.studentEmail = request.POST.get('semail')
    student.studentSchoolName = request.POST.get('ssname')
    student.studenSectionName = request.POST.get('ssection')
    student.studentClassName = request.POST.get('sclass')
    student.student_telMarks = request.POST.get('tmarks')
    student.student_englishMarks = request.POST.get('emarks')
    student.student_hindiMarks = request.POST.get('hmarks')
    student.student_mathMarks = request.POST.get('mmarks')
    student.student_science = request.POST.get('smarks')
    student.student_social = request.POST.get('ssmarks')
    student.save()
    return redirect(home_view)


def deleteView(request,pk):
    student =StudentsData.objects.get(id = pk)
    student.delete()
    return redirect(displayView)