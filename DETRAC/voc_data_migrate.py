import os
import random
import shutil
import threading
from multiprocessing import cpu_count

def parser_image(total_xml, saveBasePath, pictureBasePath):
    for xml in total_xml:
        if( xml.find(".xml")<0):
            continue
        xml_temp = xml.split("__")
        folder = xml_temp[0]
        filename = xml_temp[1].split(".")[0] + ".jpg"
        # print(folder)
        # print(filename)
        temp_pictureBasePath = os.path.join(pictureBasePath, folder)
        filePath = os.path.join(temp_pictureBasePath, filename)
        # print(filePath)
        newfile = xml.split(".")[0] + ".jpg"
        newfile_path = os.path.join(saveBasePath, newfile)
        print(newfile_path)
        shutil.copyfile(filePath, newfile_path)

if __name__ == "__main__":

    #xml路径的地址
    root = "F:\\DataSets\\UA_DETRAC"
    XmlPath = root + r'\xml_test'
    #原图片的地址
    pictureBasePath = root + r"\DETRAC-train-data\Insight-MVT_Annotation_Train"
    #保存图片的地址
    saveBasePath = root + r"\picture_test"

    total_xml = os.listdir(XmlPath)
    num = len(total_xml)
    list = range(num)
    print("xml file total number", num)
    if os.path.exists(saveBasePath) == False:  #判断文件夹是否存在
        os.makedirs(saveBasePath)

    each_process_totalxml = []
    for index in range(0,cpu_count()):
        each_process_totalxml.append([])
    for index in range(0, len(total_xml)):
        each_process_totalxml[index % cpu_count()].append(total_xml[index])

    thread =[]
    for each in each_process_totalxml:
        t = threading.Thread(
            target=parser_image, args=(
                each,
                saveBasePath,
                pictureBasePath,
            ))
        thread.append(t)
    for t in thread:
        t.start()
