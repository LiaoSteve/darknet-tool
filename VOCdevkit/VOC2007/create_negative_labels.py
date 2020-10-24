# Create by LiaoSteve on 2020/10/19
import os

num = 0
name_list = list()

image_names = os.listdir('./JPEGImages')
os.makedirs('./labels', exist_ok=True)

for image_name in image_names:        
    if image_name.endswith('.jpg') or image_name.endswith('.png') or image_name.endswith('.PNG') or image_name.endswith('.JPG'):
        name_list.append(image_name[:-4])
    elif image_name.endswith('.jpeg') or image_name.endswith('.JPEG'):            
        name_list.append(image_name[:-5])
    else:            
        raise RuntimeError(f'- [x] Not the correct image format: {image_name}, delete this image and xml please.')    

for image_name in name_list:
    file = open('./labels/' + image_name + '.txt', 'w')    
    file.close()

image_names = os.listdir('./JPEGImages')
label_list = os.listdir('./labels')
print(f'- [x] JPEGImages dir: {len(image_names)} images')
print(f'- [x] labels dir: {len(label_list)} txt file')
