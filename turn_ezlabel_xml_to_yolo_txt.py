# Adapted by LiaoSteve on 2020/10/18
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=[('2007', 'train_all')]

classes = ["trash"]


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0 
    y = (box[2] + box[3])/2.0 
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(year, image_id):
    # convert pascal-voc(.xml) labels to YOLO(.txt) labels 
    in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    out_file = open('VOCdevkit/VOC%s/labels/%s.txt'%(year, image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):        
        cls = obj.find('attribute').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()
num = 0
image_ids = list()
xml_ids = list()
for year, image_set in sets:
    if not os.path.exists('VOCdevkit/VOC%s/labels/'%(year)):        
        os.makedirs('VOCdevkit/VOC%s/labels/'%(year))
    image_ids = os.listdir('./VOCdevkit/VOC%s/JPEGImages/'%(year))  
    xml_ids = os.listdir('./VOCdevkit/VOC%s/Annotations/'%(year))
    image_ids.sort()
    xml_ids.sort()
    if not len(image_ids) ==len(xml_ids):
        raise RuntimeError(f'number of images and .xml files not equal.')
    for image_id in image_ids:        
        convert_annotation(year, os.path.splitext(image_id)[0])   
        num += 1
        
print(f'JPEGImages: {len(image_ids)} images')
print(f'turn {len(xml_ids)} .xml files to {num} .txt files')
print('DONE')
