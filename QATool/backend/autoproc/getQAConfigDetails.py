from qaconfig import models
from django.core import serializers
from autoproc import talkToMIIQASystem
from autoproc import talkToABAPQASystem
#from qalog import models

def getQACofig():
    #models.QALog.objects.all().delete()
    #models.Todo.objects.all().delete()
    print("getting Data...")

    if(True):
        queryset = models.Qaconfig.objects.filter(systemtype="MII") #qaconfig model
        ip=""
        port=""
        user=""
        pswd=""
        qaconnid=""
        object_list = serializers.serialize("python", queryset)
        
        url = ""

        for object in object_list:
            for field_name, field_value in object['fields'].items():
                #print(field_name, field_value)
                if(field_name == "ipaddress"):
                    ip = field_value
                if(field_name == "port"):
                    port = field_value
                if(field_name == "adminuser"):
                    user = field_value
                if(field_name == "adminpass"):
                    pswd = field_value
                if(field_name == "qaconnid"):
                    qaconnid = field_value  
                          
            #print("URL : " + ip + ":" + port + "/"+user + "?" + pswd)
            #url = "http://"+ip+":"+port+"/XMII/Illuminator?service=scheduler&mode=List&content-type=text/xml&IllumLoginName="+user+"&IllumLoginPassword="+pswd
            url = "http://"+ip+":"+port+"/XMII/Runner?Transaction=CodeReview/Transaction/BLS_ReviewTransaction_TL&I_Objects=CodeReview/Transaction/BLS_ReviewTransaction_Old&OutputParameter=O_CROutputXML&content-type=text/xml&IllumLoginName="+user+"&IllumLoginPassword="+pswd
            print("MII URL : " + url)
            talkToMIIQASystem.sendTrigger(url,"MII",qaconnid)

        queryset = models.Qaconfig.objects.filter(systemtype="ABAP") #qaconfig model
        ip=""
        port=""
        user=""
        pswd=""
        qaconnid=""
        client=""
        sysid=""
        object_list = serializers.serialize("python", queryset)
        
        url = ""

        for object in object_list:
            for field_name, field_value in object['fields'].items():
                #print(field_name, field_value)
                if(field_name == "ipaddress"):
                    ip = field_value
                if(field_name == "port"):
                    port = field_value
                if(field_name == "adminuser"):
                    user = field_value
                if(field_name == "adminpass"):
                    pswd = field_value
                if(field_name == "qaconnid"):
                    qaconnid = field_value 
                if(field_name == "client"):
                    client = field_value 
                if(field_name == "sysid"):
                    sysid = field_value  
                          
            #talkToABAPQASystem.sendTrigger(url,"ABAP",qaconnid)

        queryset = models.Qaconfig.objects.filter(systemtype="UI5") #qaconfig model
        ip=""
        port=""
        user=""
        pswd=""
        qaconnid=""
        githuburl=""
        object_list = serializers.serialize("python", queryset)
        
        url = ""

        for object in object_list:
            for field_name, field_value in object['fields'].items():
                #print(field_name, field_value)
                if(field_name == "ipaddress"):
                    ip = field_value
                if(field_name == "port"):
                    port = field_value
                if(field_name == "adminuser"):
                    user = field_value
                if(field_name == "adminpass"):
                    pswd = field_value
                if(field_name == "qaconnid"):
                    qaconnid = field_value 
                if(field_name == "githuburl"):
                    githuburl = field_value 
               
                          
            #talkToUI5QASystem.sendTrigger(url,"UI5",qaconnid)
        


