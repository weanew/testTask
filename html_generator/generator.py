import json
import re
from xml.etree import ElementTree as ET


def check_html(tag: str) -> dict:
    tag_attributes = {}
    classes = []
    ids = []
    attrs = re.split('([#.])', tag)
    tag_attributes['tag'] = attrs[0]
    if len(attrs) > 1:
        for i in range(2, len(attrs), 2):
            if attrs[i - 1] == '.':
                classes.append(attrs[i])
            elif attrs[i - 1] == '#':
                ids.append(attrs[i])
        tag_attributes['classes'] = classes
        tag_attributes['ids'] = ids

    return tag_attributes


def create_tag(key: str) -> "ET.Element":
    tag_attributes = check_html(key)
    tag = ET.Element(tag_attributes['tag'])
    if len(tag_attributes) > 1:
        if len(tag_attributes['classes']) > 0:
            tag.set('class', ' '.join(tag_attributes['classes']))
        if len(tag_attributes['ids']) > 0:
            tag.set('id', ' '.join(tag_attributes['ids']))
    return tag


def main_generator(request: str) -> str:

    def json_iter(item):
        if isinstance(item, list):
            root = ET.Element('ul')
            for element in item:
                li = ET.SubElement(root, 'li')
                sub_element = json_iter(element)
                if isinstance(sub_element, list):
                    for elem in sub_element:
                        li.append(elem)
                else:
                    li.append(sub_element)
            return root
        else:
            tags = []
            for k, v in item.items():
                if isinstance(v, dict) or isinstance(v, list):
                    tag = create_tag(k)
                    sub_elem = json_iter(v)
                    if isinstance(sub_elem, list):
                        for elem in sub_elem:
                            tag.append(elem)
                    else:
                        tag.append(sub_elem)
                    tags.append(tag)
                    continue
                else:
                    tag = create_tag(k)
                    tag.text = v
                    tags.append(tag)

            return tags

    request = json.loads(request)
    elements = json_iter(request)
    if isinstance(elements, list):
        output = ''
        for item in elements:
            output += ET.tostring(item).decode()
        return output
    return ET.tostring(elements).decode()
