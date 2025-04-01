from django.shortcuts import render, redirect
from SGGS.models import Attendance, Student, Subject, Branch
from SGGS.forms import AttendanceForm, StudentForm, SubjectForm

# View to add a new subject dynamically
def add_subject(request):
    branches = Branch.objects.all()  # Fetch all branches for the dropdown
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')  # Redirect to subject list after saving
    else:
        form = SubjectForm()
    
    return render(request, 'SGGS/add_subject.html', {'form': form, 'branches': branches})

# View for showing all subjects
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'SGGS/subject_list.html', {'subjects': subjects})

# Other Views...
def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'SGGS/attendance_list.html', {'attendances': attendances})

def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'SGGS/add_attendance.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'SGGS/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'SGGS/add_student.html', {'form': form})

def index(request):
    return render(request, 'SGGS/index.html')
