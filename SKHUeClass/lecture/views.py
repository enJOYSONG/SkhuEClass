from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Lecture
from django.core.exceptions import ObjectDoesNotExist

@login_required
def main(request):
    if request.method == "GET":
        try:
            request.user.professor
        except ObjectDoesNotExist:
            return redirect('my_lecture_list')

        return render(request, 'lectureCreate.html')

    if request.method == "POST":
        try:
            request.user.professor
        except ObjectDoesNotExist:
            return redirect('my_lecture_list')


        new_lecture = Lecture(name=request.POST['lecture_name'],
                              professor=request.user.professor)
        new_lecture.save()
        return redirect('lecture_list')

@login_required
def my_lecture_list(request):
    if request.method == "GET":
        try:
            request.user.student
        except ObjectDoesNotExist:
            lectures = Lecture.objects.filter(professor=request.user.professor).all()
            return render(request, 'lectureList.html', {'lectures': lectures})

        lectures = request.user.student.lecture_set.all()
        return render(request, 'lectureList.html', {'lectures': lectures})

    if request.method == "POST":
        try:
            request.user.student
        except ObjectDoesNotExist:
            return redirect('my_lecture_list')

        lecture_id = request.POST['h1']
        lecture = Lecture.objects.get(id=lecture_id)

        lecture.students.add(request.user.student)

        return redirect('my_lecture_list')

@login_required
def lecture_detail(request):
    if request.method == "GET":
        return render(request, 'myLecture.html')

@login_required
def lecture_list(request):
        if request.method == "GET":
            lectures = Lecture.objects.select_related('professor__base_user').all()
            return render(request, 'lectureApply.html', {'lectures': lectures})