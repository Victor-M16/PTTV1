from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubjectForm
import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
times = ['9:00', '10:00', '11:00', '12:00', '1:00', '2:00', '3:00', '4:00', '5:00']
courses = ['Mathematics', 'English', 'History', 'Physics', 'Biology', 'Chemistry']

def generate_timetable(subjects):
    timetable = {}
    for day in days:
        for time in times:
            course = random.choice(subjects)
            timetable.setdefault(day, {})[time] = course
    return timetable

def print_timetable(timetable):
    table = "<table style='border-collapse: collapse;'><thead><tr><th style='border: 1px solid black;'></th>"
    for day in days:
        table += "<th style='border: 1px solid black;'>{}</th>".format(day)
    table += "</tr></thead><tbody>"
    for time in times:
        table += "<tr><td style='border: 1px solid black;'>{}</td>".format(time)
        for day in days:
            table += "<td style='border: 1px solid black;'>{}</td>".format(timetable[day][time])
        table += "</tr>"
    table += "</tbody></table>"
    return table


def get_subjects(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subjects = [form.cleaned_data[field] for field in form.cleaned_data]
            timetable = generate_timetable(subjects)
            table = print_timetable(timetable)
            return HttpResponse(table)
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form})
