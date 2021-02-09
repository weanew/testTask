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

