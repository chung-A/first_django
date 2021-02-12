import random
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        "current_date": now
    }
    return render(request, 'first/index.html', context)


def select(request):
    context = {}
    return render(request, 'first/select.html', context)


def read(request, id):
    message = str(id) + " 번 데이터 입니다."
    return HttpResponse(message)


def result(request):
    chosen = int(request.GET['number'])

    results = []
    if 1 <= chosen <= 45:
        results.append(chosen)

    box = []
    for i in range(0, 45):
        if chosen != i + 1:
            box.append(i + 1)

    random.shuffle(box)
    while len(results) < 6:
        results.append(box.pop())

    context = {
        "numbers": results
    }
    return render(request, 'first/result.html', context)
