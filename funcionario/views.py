from django.shortcuts import render, redirect  
from funcionario.forms import FuncionarioForm  
from funcionario.models import Funcionario  

def emp(request):  
    if request.method == "POST":  
        form = FuncionarioForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/funcionarios')  
            except:  
                pass  
    else:  
        form = FuncionarioForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    funcionarios = Funcionario.objects.all()  
    return render(request,"funcionarios.html",{'funcionarios':funcionarios})  

def edit(request, id):  
    funcionario = Funcionario.objects.get(id=id)  
    return render(request,'edit.html', {'funcionario':funcionario})

def update(request, id):  
    funcionario = Funcionario.objects.get(id=id)  
    form = FuncionarioForm(request.POST, instance = funcionario)  
    if form.is_valid():  
        form.save()  
        return redirect("/funcionarios")  
    return render(request, 'edit.html', {'funcionario': funcionario})  


def destroy(request, id):  
    funcionario = Funcionario.objects.get(id=id)  
    funcionario.delete()  
    return redirect("/funcionarios") 

