import os

image_files = []
path = os.getcwd()
os.chdir("./VOCdevkit/VOC2007/JPEGImages")
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".jpeg") \
        or filename.endswith(".JPEG") or filename.endswith(".png") or filename.endswith(".PNG"): 
        image_files.append(path + "/VOCdevkit/VOC2007/JPEGImages/" + filename)
os.chdir("../../../")
with open("2007_train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")

