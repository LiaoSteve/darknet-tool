'''
# Author: LiaoSteve
# Date: 2020-10-06
# Copy images from all sub-dirs.
'''
import os 
import cv2
import uuid 

out_dir = 'out_negative/'
os.makedirs(out_dir, exist_ok=True)
show = False
images = list()
#mypath =  os.getcwd() 
mypath ='./non-garbage-queried-images/'
for root, dirs, files in os.walk(mypath):    
    #print("root: ", root)
    #print("dirs", dirs)
    #print("files: ", files)    
    for file in files:        
        file_format = file.split('.')[-1]
        if file_format == 'jpg' or file_format == 'jpeg' or file_format == 'JPG' or file_format == 'JPEG':
                
            file = os.path.join(root,file)
            images.append(file)                      
        else: 
            pass           
            #print(file)    

print(f'wait for save {len(images)} images ...')
for image in images:
    try:
        img = cv2.imread(image)
        name = out_dir + 'GINI_'+ str(uuid.uuid4()) + '.' + image.split('.')[-1]
        if img is None:
            continue       
        if show:
            cv2.imshow('esc: exit, s: save and next, ->: next', img)
            key = cv2.waitKey(0) & 0xFF
            print('key: ',key)
            print(f'file: {image}')
            if key ==  27:
                cv2.destroyAllWindows()
                break
            if key == 115:
                print('save image')    
                cv2.imwrite(name, img)    
                continue
            if key == 0:
                continue
        else:
            cv2.imwrite(name, img)
    except Exception as e:
        print(f'-[x] {image} : ')
        print(e)
print('Done')

