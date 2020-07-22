import xml.etree.ElementTree as ET
import requests
from django.core import serializers
import random
import string
from qalog import models


def sendTrigger(url,systemtype,qaconnid):
    #models.QALog.objects.all().delete()
    #models.Todo.objects.all().delete()
    print("Calling...")
    print(url)

    r = requests.get(url)
                
    string_xml = r.content
    root = ET.fromstring(string_xml)
 
    
    for child in root.iter('Row'):
        for Path in child.iter('Path'):
            for Object in child.iter('Object'):
                for CreatedBy in child.iter('CreatedBy'):
                    for TracerStatus in child.iter('TracerStatus'):
                        for WriteFileStatus in child.iter('WriteFileStatus'):
                            for CreatedDate in child.iter('CreatedDate'):
                        
                                print(Path.text+"-----"+Object.text)
                                testxml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Content><TracerStatus>"+TracerStatus.text+"</TracerStatus><WriteFileStatus>"+WriteFileStatus.text+"</WriteFileStatus></Content>"
                                print("testxml : " + testxml)
                                models.QALog(SystemType=systemtype,QAConnID=qaconnid,
                                QACreatedDate=CreatedDate.text,JIRALogFlag='NA',QALog=testxml,
                                QALoggedDate=CreatedDate.text,ObjectName=Object.text,
                                ObjectPath=Path.text,DevelopedBy=CreatedBy.text).save()