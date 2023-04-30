from django.contrib import messages
from django.contrib.messages import SUCCESS, ERROR
from django.shortcuts import render, redirect

from core.models import Worker


def index(request):
    return render(request, "index.html")


def delete_worker(request, worker_id):
    Worker.objects.filter(id=worker_id).delete()
    return redirect(workers_list)


def workers_list(request):
    workers = tuple(
        (worker_index, worker)
        for worker_index, worker in enumerate(
            reversed(Worker.objects.order_by("id")), 1
        )
    )
    return render(request, "workers_list.html", context={"workers": workers})


def worker_of_month(request):
    worker = Worker.objects.order_by("id").last()
    return render(request, "worker_of_month.html", context={"worker": worker})


def add_worker_post(request):
    name = request.POST.get("name")
    last_name = request.POST.get("last_name")
    patronymic = request.POST.get("patronymic")
    job = request.POST.get("job")
    phone_number = request.POST.get("phone_number")
    address = request.POST.get("address")
    email = request.POST.get("email")
    success = True
    try:
        Worker.objects.create(
            name=name,
            last_name=last_name,
            patronymic=patronymic,
            job=job,
            phone_number=phone_number,
            address=address,
            email=email,
        )
    except Exception as e:
        success = False
    if success:
        messages.add_message(
            request, SUCCESS, "Сотрудник успешно занесён в базу данных"
        )
    else:
        messages.add_message(request, ERROR, "Произошла ошибка")
    return render(request, "add_worker.html")


def add_worker(request):
    if request.method == "POST":
        return add_worker_post(request)
    return render(request, "add_worker.html")
