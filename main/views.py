from django.shortcuts import render ,redirect,get_object_or_404
from django.http import HttpResponse ,request
from datetime import datetime,timedelta

from .models import Todo
def all_todo(requests):
    data=Todo.objects.all()
    data={
        "todo":data
    }
    return render(requests,"index.html",context=data)

def create_todo(requests):
    data=requests.POST
    
    if requests.POST:
        title=requests.POST.get("title")
        desc=requests.POST.get("desc")
        date=requests.POST.get("data")
        time=requests.POST.get("time")
        status=requests.POST.get("status")
        
        date=datetime.strptime(date,"%Y-%m-%d")
        time=datetime.strptime(time,"%H:%M")
        date=date+timedelta(hours=time.hour,minutes=time.minute)
        
        Todo.objects.create(
            title=title,
            desc=desc,
            time=date,
            status=status
            
        )
    return redirect("/")


def delate_todo(requests,id):
    data=Todo.objects.filter(id=id)
    
    if data:
        data.delete()
        return redirect("/")
    else:
        return HttpResponse ("ID notogri")

def update_todo(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == "POST":
        todo.title = request.POST.get("title", todo.title)
        todo.desc = request.POST.get("desc", todo.desc)

        date = request.POST.get("data")
        time = request.POST.get("time")
        if date and time:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            time_obj = datetime.strptime(time, "%H:%M")
            todo.time = date_obj + timedelta(hours=time_obj.hour, minutes=time_obj.minute)

        
        todo.status = request.POST.get("status", todo.status)

        todo.save()
        return redirect("/")

    return render(request, "update.html", {"todo": todo})
