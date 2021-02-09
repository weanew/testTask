import json
from xml.etree import ElementTree as ET


def generator_task1(request: str) -> str:
    request = json.loads(request)
    output = ''

    for item in request:
        if item['title'] and item['body']:
            title = ET.Element('h1')
            title.text = item['title']
            output += ET.tostring(title).decode()
            body = ET.Element('p')
            body.text = item['body']
            output += ET.tostring(body).decode()

    return output


def generator_task2(request: str) -> str:
    request = json.loads(request)
    output = ''

    for item in request:
        for key in item:
            element = ET.Element(key)
            element.text = item[key]
            output += ET.tostring(element).decode()

    return output


def generator_task3(request: str) -> str:
    request = json.loads(request)
    output = ''

    if type(request) is list:
        ul = ET.Element('ul')
        for item in request:
            li = ET.SubElement(ul, 'li')
            for key in item:
                element = ET.SubElement(li, key)
                element.text = item[key]
        output += ET.tostring(ul).decode()

    return output
