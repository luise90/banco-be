import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from .models import Customer, Account
# Create your views here.
def home(request):
    return HttpResponse("Bienvenida a su banco.")

def newCustomer(request):
    #print(request.method)
    if request.method == "POST":
        try:
            data =json.loads(request.body)
            customer = Customer(
            id = data["id"],
            firstName = data["firstName"],
            lastName = data["lastName"],
            email = data["email"],
            password = data["password"]
            )
            #print(member)
            customer.save()
            return HttpResponse("Nuevo cliente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'],"Método invalido")


def getAllCustomer(request):
    #print(request.method)
    if request.method == "GET":
        customers = Customer.objects.all()
        allCustData =[] 
        for x in customers:
            data = {"id": x.id, "firstName":x.firstName, "lastName": x.lastName, "email":x.email}
            allCustData.append(data)
        dataJson = json.dumps(allCustData)
        
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'],"Método invalido")

def getOneCustomer(request, id):
    #print(request.method)
    if request.method == "GET":
        customers = Customer.objects.filter(id = id).first()
        data = {"id": customers.id, "firstName":customers.firstName, "lastName": customers.lastName, "email":customers.email}
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'],"Método invalido")
        