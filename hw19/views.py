from django.shortcuts import render

from django.http import HttpResponse


def index1(request):
    line1 = request.POST.get("first")
    line2 = request.POST.get("second")
    line3 = request.POST.get("third")
    lines = [line1, line2, line3]
    longest_line = line1
    for line in lines:
        if len(line) > len(longest_line):
            longest_line = line
    return HttpResponse(f"The longest field: {longest_line}")