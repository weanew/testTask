import json
import re
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


def generator_task4(request: str) -> str:

    def json_iter(item):
        if isinstance(item, list):
            tag = ET.Element('ul')
            for element in item:
                li = ET.SubElement(tag, 'li')
                sub_element = json_iter(element)
                if isinstance(sub_element, list):
                    for elem in sub_element:
                        ET.SubElement(li, elem)
                else:
                    ET.SubElement(li, sub_element)
            return tag
        else:
            tags = []
            for k, v in item.items():
                if isinstance(v, dict) or isinstance(v, list):
                    print(k + ":")
                    tag = ET.Element(k)
                    sub_elem = json_iter(v)
                    ET.SubElement(tag, sub_elem)
                    tags.append(tag)
                    continue
                else:
                    print(k + ":" + str(v))
                    element = ET.Element(k)
                    element.text = v
                    tags.append(element)

            return tags

    request = json.loads(request)
    elements = json_iter(request)
    return ET.tostring(elements)


def generator_task5(request: str) -> str:
    request = json.loads(request)
    output = ''

    for key, value in request.items():
        attrs = re.split('([#.])', key)
        element = ET.Element(attrs[0])
        classes = []
        ids = []

        for i in range(2, len(attrs), 2):
            if attrs[i - 1] == '.':
                classes.append(attrs[i])
            elif attrs[i - 1] == '#':
                ids.append(attrs[i])

        if classes:
            element.set('class', ' '.join(classes))
        if ids:
            element.set('id', ' '.join(ids))

        element.text = value
        output += ET.tostring(element).decode()

    return output

