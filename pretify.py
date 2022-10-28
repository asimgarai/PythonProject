import os
#format
# C:\Users\ASIM GARAI\Desktop\project
def soilder_pretify(path, file, format):
    os.chdir(path)
    list = os.listdir(path)
    new_list = [item.capitalize() for item in list]
    for i in range(len(list)):
        if os.path.isfile(list[i]) == True:
            os.rename(list[i], new_list[i])
    with open(file,'r') as f:
        line = f.readlines()
    with open("file.txt", "w") as f:
        line = [item.capitalize() if item != "this\n" and item !="that\n" and item != "the\n" else item for item in line]
        for item in line:
            f.write(item)
    i = 1
    for item in new_list:
        if os.path.isfile(item) == True:
            format1 = item.split(".")[1]
            if format1 == format:
                os.rename(item, f"{i}.{format}")
                i = i + 1

soilder_pretify("C:/Users/ASIM GARAI/Desktop/project","file.txt","bmp")
