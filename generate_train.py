import os

image_files = []
os.chdir("./VOCdevkit/VOC2007/JPEGImages")
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/VOCdevkit/VOC2007/JPEGImages/" + filename)
os.chdir("../../../")
with open("2007_train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")