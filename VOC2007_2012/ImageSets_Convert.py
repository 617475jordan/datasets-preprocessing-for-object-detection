import os
import random
import time

root = "F:\\DataSets\\UA_DETRAC\\"
xmlfilepath = root + r'./VOC2007/Annotations'
saveBasePath = root + r"./"

if(os.path.exists(xmlfilepath)==False):
    os.mkdir(xmlfilepath)
if (os.path.exists(saveBasePath) == False):
    os.mkdir(saveBasePath)
trainval_percent = 0.8
train_percent = 0.85
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

print("train and val size", tv)
print("traub suze", tr)
if (os.path.exists(os.path.join(saveBasePath, 'VOC2007/ImageSets')) == False):
    os.mkdir(os.path.join(saveBasePath, 'VOC2007/ImageSets'))
ftest = open(os.path.join(saveBasePath, 'VOC2007/ImageSets/test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'VOC2007/ImageSets/train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'VOC2007/ImageSets/val.txt'), 'w')
# Start time
start = time.time()
for i in list:
    name = total_xml[i][:-4]
    value = "../Annotations/" + name + ".xml ../JPEGImages/" + name + '.jpg\n'
    if i in trainval:
        # ftrainval.write(name)
        if i in train:
            ftrain.write(value)
        else:
            fval.write(value)
    else:
        ftest.write(value)
# End time
end = time.time()
seconds = end - start
print("Time taken : {0} seconds".format(seconds))

ftrain.close()
fval.close()
ftest.close()
