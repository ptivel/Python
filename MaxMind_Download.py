import requests,urllib2,urllib,re,os,zipfile,shutil
from requests import session

login_url1 = 'https://www.maxmind.com/en/member'
login_url2 = 'https://www.maxmind.com/en/download_files'
fileDir = 'C:/GEOIP'

if not os.path.exists(fileDir):
    os.makedirs(fileDir)
else:
    shutil.rmtree(fileDir)
    os.makedirs(fileDir)

payload = {'action':'login','login':'#############','password':'#########','pkit_login':'1','pkit_done':r'https://www.maxmind.com/en/account'}

with session() as c:
    c.post(login_url1, data=payload)
    request = c.get(login_url2)
    webpage = request.text
    

myUrls = re.findall(r"https://download.maxmind.com/app/geoip_download.edition_id=174.*?.>|https://download.maxmind.com/app/geoip_download.edition_id=144.*?.>|https://download.maxmind.com/app/geoip_download.edition_id=178.*?.>|https://download.maxmind.com/app/geoip_download.edition_id=172.*?.>",webpage)
for item in myUrls:
    print item[:-2]

    try:
        #Downloading Maxmind Data
        filePath = fileDir+'/'+item[59:62]+'.zip'

        urllib.urlretrieve(item[:-2],filePath)
        

        fh = open(filePath, 'rb')
        z = zipfile.ZipFile(fh)
        for name in z.namelist():
            #extract only csv files
            if name[-3:] == 'csv':
                print name
                outpath = fileDir
                z.extract(name, outpath)
        fh.close()
        os.remove(filePath)

    except:
        item + " was not a good file"
