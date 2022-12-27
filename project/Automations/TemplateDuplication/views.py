from django.shortcuts import render
from .TemplateDuplication  import OutputTemplate,GettingTemplateJsonFromCatalog,PushingTemplateJsonUsingApi
import  pandas as pd
import json
import copy
import datetime
import requests


# Gettingtoken = "eyJ0eXAiOiJqd3QifQ==.eyJsZWdhbEVudGl0eUlEIjoxNCwicGVybWlzc2lvbiI6IlJXIiwiaWF0IjoiMjAyMjEyMjZUMDk1MjQ0WiIsImV4cCI6IjIwMjIxMjI3VDA5NTI0NFoiLCJpc3MiOiJzdGFnaW5nLXBsYXRmb3JtLmVudGVycHJpc2UuYnkubWUifQ==.37366b566761424a667866616562536e5a42354a565547684632584b71594354774c64635a3170337769633d"
# PushingToken = "eyJ0eXAiOiJqd3QifQ==.eyJsZWdhbEVudGl0eUlEIjoyMywicGVybWlzc2lvbiI6IlJXIiwiaWF0IjoiMjAyMjEyMjZUMDcxMjMzWiIsImV4cCI6IjIwMjIxMjI3VDA3MTIzM1oiLCJpc3MiOiJzdGFnaW5nLXBsYXRmb3JtLmVudGVycHJpc2UuYnkubWUifQ==.6f47576f4a7559504351312b614350554e5568463552776f6a7530587732414344396350624d31436933733d"

# TemplateReference = '30_S2IBIFHO'
# NewReference = 'mnmnmn'




# Create your views here.


# df = pd.read_excel('C:\\Users\\PJN13\\projects\\arahanth\\travello\InputList(Casino).xlsx')
# FromList1 = df['Casino'].tolist()
# ToList2 = df['Nobilia'].tolist()


brandID = ''
FromList1 = ''
ToList2 = ''
Gettingtoken = ""
PushingToken = ''


def home(request):

    return render(request,"TemplateInformation.html")


def TemplateDuplication(request):
    global Gettingtoken,brandID,FromList1,ToList2,PushingToken

    Gettingtoken = request.POST['Token']


    FromList1 = request.POST['ParentIDs']
    ToList2 = request.POST['ChildIDs']

    FromList1= FromList1.split(',')
    ToList2 = ToList2.split(',') 

   
    brandID = request.POST['brandID']

    PushingToken = request.POST['PushingToken']


    return render(request,"TemplateInformation1.html")



def TemplateDuplication1(request):

    global Gettingtoken,brandID,FromList1,ToList2,PushingToken


    TemplateReference = request.POST['Reference']

    NewReference = request.POST['NewReference']
    
    Template_json = GettingTemplateJsonFromCatalog(TemplateReference,Gettingtoken)

    if Template_json == {'error': {'httpCode': '404', 'id': 'BM_3407', 'message': 'Template not found'}}:

        res = 'There is no such template for the reference {}'.format(TemplateReference)

        return render(request,"TemplateInformation1.html",{'res':res})

    else:

        print(Template_json)

        TemplateToBePushed =OutputTemplate(Template_json,NewReference,brandID,FromList1,ToList2)

        res = TemplateToBePushed 

    res = TemplateToBePushed

    res = PushingTemplateJsonUsingApi(TemplateToBePushed,PushingToken,NewReference)


    return render(request,"TemplateInformation1.html",{'res':res})


 

