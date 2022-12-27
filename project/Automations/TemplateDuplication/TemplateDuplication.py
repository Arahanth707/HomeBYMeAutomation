import  pandas as pd
import json
import copy
import datetime



def GettingTemplateJsonFromCatalog(TemplateReference,Gettingtoken):
    import requests
    

    TemplateReference = TemplateReference


    def generateDateISO8601():
        timestamp = (datetime.datetime.utcnow().replace(microsecond=0).isoformat()).replace("-", "", 2)
        timestamp = timestamp.replace(":", "", 2)
        timestamp = timestamp + "Z"
        return timestamp

    Headers_prod_sandBox = {
            # "apikey": "MbumSypepdlb3pY3OKFR",
            # "signature": "45365748394d4d77456d59526d436b4849787164315a34704c4f6b32536d726f6749696a345877446c54413d",
            "timestamp": generateDateISO8601(),
            "token": Gettingtoken
        }





    Template_json = requests.get(url="https://staging-platform.enterprise.by.me/api/3/templates/{}".format(TemplateReference),
                                json={"languageID": "1"}, headers=Headers_prod_sandBox)

    Template_json = Template_json.json()
    # print(Template_json)

    return Template_json


def OutputTemplate(Template_json,NewReference,brandID,FromList1,ToList2):

    FromJson = Template_json




    # print(len(FromList1))
    # print(len(ToList2))

    
    uuid =FromJson['uuid']


    Sample_template = {
        "reference": "",
        "technicalComment": "null",

        "brandID": brandID,

        "commercialInfos": [
            {
                "languageID": 1,
                "name": "EXPO11FFL",
                "description": "NOBILIA-EXPO11FFL",
                "shortDescription": "NOBILIA-EXPO11FFL",
                "sheetUrl": "null"
            }
        ],
        "url": "https://byme-enterprise-prod-stgg.s3.eu-west-1.amazonaws.com/data/templates/{}/template.BMTPROJ".format(uuid),
        "freeTag": [
            ],
        "mapProductsIDs": {
    }
    }

    products = FromJson['productIDs']

    mapProductsIds = {}

    mapProductsIds =mapProductsIds.fromkeys(products)


    for pinoIds,nobiliaIds in mapProductsIds.items():
        if pinoIds in FromList1:
            replacementIDindex = FromList1.index(pinoIds)
            mapProductsIds[pinoIds]= ToList2[replacementIDindex]

    Sample_template['mapProductsIDs'] = mapProductsIds


    Sample_template['reference']= NewReference

    Sample_template['commercialInfos'][0]['name']=  FromJson['name']
    Sample_template['commercialInfos'][0]['description']=  FromJson['description']
    Sample_template['commercialInfos'][0]['shortDescription']=  FromJson['shortDescription']


    Sample_template['technicalComment']=None
    Sample_template['commercialInfos'][0]['sheetUrl']= None
    Sample_template['freeTag']=FromJson['freeTags']

    # print(Sample_template)


    DuplicatedTemplate = copy.deepcopy(Sample_template)

    return DuplicatedTemplate


def PushingTemplateJsonUsingApi(TemplateToBePushed,PushingToken,NewReference):
    import requests
    
    def generateDateISO8601():
        timestamp = (datetime.datetime.utcnow().replace(microsecond=0).isoformat()).replace("-", "", 2)
        timestamp = timestamp.replace(":", "", 2)
        timestamp = timestamp + "Z"
        return timestamp

    # OrginalJsonName = 'NOBILIA-27_M1LBIFHO - Copy.json'

    # filepath = 'D:\\temp\\automationTask\\TemplateDuplication(Pino to Nobilia)\\DuplicatedTemplates(Casino to Nobilia)\\'

    # duplicatedJson = open(filepath+OrginalJsonName)

    # TemplateToBePushed = json.load(TemplateToBePushed)

    Headers_prod_sandBox = {
            # "apikey": "MbumSypepdlb3pY3OKFR",
            # "signature": "45365748394d4d77456d59526d436b4849787164315a34704c4f6b32536d726f6749696a345877446c54413d",
            "timestamp": generateDateISO8601(),
            "token": PushingToken
        }

    posted =requests.post(url="https://staging-platform.enterprise.by.me/api/3/templates/",
                                json=TemplateToBePushed, headers=Headers_prod_sandBox)
                                
    print(NewReference,posted.text)

    return NewReference,posted.text


