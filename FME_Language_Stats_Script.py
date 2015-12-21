#This script is does and returns several things. It finds if something is multi lingual or a sinlge language, as well if it is a possibe emoticon that isnt in emoticon excel file.
#In addtion it performs a varaeity of statistics on the content of the data. If the Languages are "AAAAAAABBBBCDEEEEEEAAAAA" the script formats it as 7A 4B 1C 1D 6E 5A. This helps
#determine if it is multi lingual and gives another usefull statistic of the data. 
import fmeobjects, re
def LanguageGroup(feature):

    #Def function that will checks if all things in the list are the same language
    def all_same(items):
        return all(x == items[0] for x in items)
    #Represents the LanguageAll field that contains the language of each character code
    languageString = feature.getAttribute("LanguageAll")
    contentString = feature.getAttribute("Content")
    contentList = list(contentString)
    #Creating a list from the LanguageAll field string using a space as the delimiter
    languageList = languageString.split(" ")

    #Setting up counters and empty variables to be used shortly
    groupCounter = 1
    loopCounter = 0
    pattern = ""
    patternList =[]
    patternList2 =[]


    for group in languageList:

        try:
            #Checking if the next item in the list is the same item as the current item, if so then
            #the count of that language type is increased.
            if languageList[loopCounter+1] == group:
                groupCounter += 1
                loopCounter += 1
            #If the next item in the Language list is not the same as the current item then a new language
            #group with a reset counter is started
            else:
                groupcount = str(groupCounter) + "(" + group + ")"
                pattern = pattern + " " + groupcount
                patternList.append(groupCounter)
                patternList2.append(group)
                groupCounter = 1
                loopCounter += 1
                
        #This except occurs when the try statement above runs into the end of the list and can't check
        #what's after the last item in the list. 
        except:
            groupcount = str(groupCounter) + "(" + group + ")"
            pattern = pattern + " " + groupcount
            #patfin represents the language and the group count eg. [5(Arabic), 3(Basic_Latin), 8(Arabic)]
            patfin = pattern[5:-3]
            patternList.append(groupCounter)
            patternList2.append(group)
            
    #patlistgc represents just the number in patfin eg. [5,3,8] This will be what allows us to find
    #single vs multiple languages in the content and later possible emoticons
    patlistgc = patternList[1:-1] 
    #patlistg represents just the language in patfin eg. [Arabic,Basic_Latin, Arabic]
    patlistg = patternList2[1:-1]
    #Changing palistgc to string to aid in the search of emoticons [5,3,8] will now appear as 5_3_8
    #we are doing this to find the pattern 1_1_1 which will identify a possible emoticon

    indexpos = 0
    possemotechar=''
    ltype = ''
    possemote = ''

   
    for group in patlistgc:
        try:
            #Variable containing conditions for if statement to find possible emoticons. Ignoring Ignore Characters. Farsi, and Latin supplements and extended
            #because they cause to many false positives to get through.
            condition1 = patlistgc[indexpos] == 1 and patlistgc[indexpos+1] == 1 and patlistgc[indexpos+2] == 1
            condition2 = patlistg[indexpos] != "Ignore_Character" and patlistg[indexpos+1] != "Ignore_Character"and patlistg[indexpos+2] != "Ignore_Character"
            condition3 = patlistg[indexpos] != "Latin-1_Supplement" and patlistg[indexpos+1] != "Latin-1_Supplement"and patlistg[indexpos+2] != "Latin-1_Supplement"
            condition4 = patlistg[indexpos] != "Latin_Extended-A" and patlistg[indexpos+1] != "Latin_Extended-A"and patlistg[indexpos+2] != "Latin_Extended-A"
            condition5 = patlistg[indexpos] != "Latin_Extended-B" and patlistg[indexpos+1] != "Latin_Extended-B"and patlistg[indexpos+2] != "Latin_Extended-B"
            condition6 = patlistg[indexpos] != "Farsi" and patlistg[indexpos+1] != "Farsi"and patlistg[indexpos+2] != "Farsi"
            if condition1 and condition2 and condition3 and condition4 and condition5 and condition6:
                
                contentpos = 0
                for x in patlistgc[0:indexpos]:
                    contentpos = contentpos + x
                indexpos+=1
                possemotechar = possemotechar + contentList[contentpos] + contentList[contentpos+1] + contentList[contentpos+2] + '    '
                possemote = "Possible Emoticon"
                
            else:
                indexpos += 1
        except:
            break

    #We don't want special characters like a space, period, octothorp, etc to count towards something being
    #multiple languages or a possilbe emoticon. The below code causes these characters to be ignored in this 
    #type of consideration. We are sssuming emoticons that use these symbols are caught in the
    #input emoticon file in the FME model.
    indexpos = 0

    for group in patlistg:
        if group == "Ignore_Character":
            
            patlistg.remove(group)
            del(patlistgc[indexpos])
            indexpos += 1
            
        else:
            indexpos += 1

    contentpos = 0        
    for item in languageList:

        try:
            if item == "Ignore_Character":
                del(contentList[contentpos])
                
            else:
                contentpos+=1
        except:
            break
            

    #Checking to see if content is single or multi language using def function all_same() created at the start
    for group in patlistg:

        if all_same(patlistg) == True:
            ltype = "Single Language"
        else:
            ltype = "Multi Language"
        


    feature.setAttribute("LanguageGrouping", patfin)
    feature.setAttribute("LanguageType", ltype)
    feature.setAttribute("PossibleEmoteChar", possemotechar)  
    feature.setAttribute("EmoticonDetection", possemote)
