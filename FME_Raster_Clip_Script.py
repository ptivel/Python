#UNCLASSIFIED#
#Author: Phil Tivel
#Created: 11/19/2014
#Python Version 2.75
#This script is meant to be used in FME. It it goes into the http://libremap.org/ website, finds and downloads all
#desired DRG topo maps for a state. Once the files are downloaded the script creates and returns long string of
#the tiff file paths that can be utilized in the tif Source Parameters of an FME workspace.
#This script should be set in the Private Parameters of an FME workspace.

#importing program functionality
import urllib2,urllib,re,os
sName = str(FME_MacroValues['State'])
stateName = sName.lower()
tifDir = str(FME_MacroValues['Orig_DRG'])
#Accesing the http://libremap.org website
response = urllib2.urlopen('http://libremap.org/data/state/'+stateName+'/drg/')
html = response.read()

#Declaring Variables

fpathsString = ""
#tifPath = "C:\\GCT\\Donna\\Rhode_Island_DSG\\"
uniqueUrls = []
uniqueTifPath = []

#variable replaces everything with tfw in the website with tiff
urlFix = html.replace("tfw","tif")

#variable replaces everything with fgd in the website with tiff
urlFix2 = urlFix.replace("fgd","tif")

#Utilizing Regular Expressions. Variable stores a list of URLs in the website that start with http:// and end with .tif. Thus creating a
#list of URLs for the each downloadable tif on the page. 
myUrls = re.findall(r"http://.*?.tif",urlFix2)

#for loop to crate a unique URLs list since some of the URLs became duplicates when I replaced tfw and fgd with tif
#to aid in the regular expression search abouve
for item in myUrls:
    if item not in uniqueUrls:
        uniqueUrls.append(item)
   
#for loop to try and download each tif found on the website. It tries to download it and if it fails then it
#removes it from the list and moves to the next tif.
for item in uniqueUrls:
    tifName = os.path.basename(item)

    try:
        #Downloading tif data
        urllib.urlretrieve(item,tifDir+'/'+tifName)

        #building separate file path list to be used once files are downloaded to the users computer
        uniqueTifPath.append(tifDir +'/'+ tifName)
    except:
        item + " was not a good tiff"
        #removing failed downloads from the url list
        uniqueUrls.remove(item)

#building string of tif file paths to be returned and used in the FME Source Paramters
for item in uniqueTifPath:
    fpathsString = fpathsString + '"' + item + '"' + " "

#Creating final tif path string that will be utilized in FME. This removes the final comma from the string
tifString = '"'+fpathsString[0:-1] + '"'

print "total files done: " + str(len(uniqueUrls))

#This return only works when this script is incorporated into FME.
#It ruturns a the string of tiff file paths in the form of "tiff1,tiff2,tiff3,etc"
#which then gets used in the tif source parameters of the FME model
return tifString
