from api_python_3decision import api
from os import listdir
from os.path import isfile, join, splitext
import os.path
import os
import csv
import gzip
import shutil
import configparser
import json
import time
from datetime import date

#objects setup
imported=[]
configVolume='/3dec_api_config'
inputStructuresVolume='/3dec_api_input'
registrationVolume='/3dec_api_recepies'




#####################################################################################################
## A BUNCH OF FUNCTIONS THAT NEED CLEANING INTO SEPARATE EXTERNAL MODULES
#####################################################################################################

def readImportHistory(fName):
    impStr=[]
    if os.path.exists(fImpName):
        with open(fImpName, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                #if line_count == 0:
                #    print(f'Column names are {", ".join(row)}')
                #print(f'\t{row["ID"]}')
                impStr.append(row)
                line_count += 1
            #print(f'Processed {line_count} lines.')
    else:
        print('no file '+ fImpName +' , creating it')
        with open(fImpName, mode='w') as impFile:
            fieldnames = ['ID', 'Import_Date', 'Status']
            impFile_writer = csv.DictWriter(impFile, fieldnames=fieldnames)
            impFile_writer.writeheader()
            #writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    
    return impStr

def appendHistory(code, state='ok'):
    with open(fImpName, "a") as myfile:
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        myfile.write(code+'cif.gz,'+d1+','+state)


def listAllAvailableFiles(folderPath):
    return [f for f in listdir(folderPath) if isfile(join(folderPath, f))]

def listAvailableFiles(folderPath, ext='pdb'):
    return [f for f in listdir(folderPath) if f.endswith(ext)]

def extractGzip(filePath):
    with gzip.open(filePath, 'rb') as f_in:
        with open(removeFileExt(filePath), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def removeFileExt(fileName):
    return splitext(fileName)[0]

def listToCSVRecord(l):
    return (';').join(l)


def convertCIFifRequired(metaDic):
    print('start convert check')
    filename=os.path.split(metaDic['STRUCTURE_FILE'])[1]
    code=os.path.splitext(filename)[0]
    if os.path.splitext(filename)[1] == '.cif':
        print('its a cif file, it must be converted')
        folder=registrationVolume+'/'+code+'/source/struc1/'
        pdb=folder+code+'.pdb'
        os.system('maxit -input '+ folder+filename + ' -output '+pdb+' -o 2')
        metaDic['STRUCTURE_FILE']='/struc1/'+code+'.pdb'
    return metaDic

def prepareZipArchive(destFolder, base):
    '''  '''
    shutil.make_archive(destFolder+'/post_structure', 'zip', base,)

def writePostConfigCsv(fPath, strDic):
    """
    """
    #TODO: write the dic to actual file
    with open(fPath+'/'+'post_structure_configuration.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_NONE)
        writer.writerow(['structureId', 'infoType', 'infoValue1', 'infoValue2', 'infoValue3', 'infoValue4', 'infoValue5'])
        writer.writerow(['struct1','TITLE',strDic["TITLE"],'','','',''])
        writer.writerow(['struct1','STRUCTURE_FILE',strDic["STRUCTURE_FILE"],'','','',''])
        writer.writerow(['struct1','METHOD', strDic["METHOD"], '', '', '', ''])
        writer.writerow(['struct1','SOURCE', strDic["SOURCE"], '' , '', '', ''])
        writer.writerow(['struct1','CREATED_BY', strDic["CREATED_BY"], '', '', '', ''])
        writer.writerow(['struct1','RESOLUTION',strDic["RESOLUTION"], '','','',''])
        for lig in strDic["LIGAND"]:
            writer.writerow(['struct1','LIGAND',lig,'','','',''])
        for annot in strDic["ANNOTATION"]:
            writer.writerow(['struct1','ANNOTATION',annot[0],annot[1],'','',''])
        for proj in strDic["PROJECT_ID"]:
            writer.writerow(['struct1','PROJECT_ID',proj,'','', ''])
        for mapping in strDic["UNIPROT_MAPPING"]:
            writer.writerow(['struct1','UNIPROT_MAPPING',mapping[0], mapping[1],mapping[2], ''])
        for f in strDic["LINKED_FILE"]:
            writer.writerow(['struct1','LINKED_FILE',f[0],f[1],f[2],''])
    return 0

def convertInternalIdToCode(iID, strCodeList):
    for s in strCodeList:
        #get structure metadata
        response = api.get_structure_metadata(s)
        obj = json.loads(response.text)
        for annot in obj["data"]["structures"][0]["annotations"]:
            if annot["type"] == "Internal ID" and annot["value"] == iID:
                return obj["data"]["structures"][0]["general"]["code"]
    return 0

def getProjectID(pName):
    response = api.get_project_ids('community')
    obj = json.loads(response.text)
    return obj["data"]["projects"][0]["general"]["id"]

def createRegistrationFolder(fPath, code):
    if not os.path.exists(fPath+'/'+code):
        os.makedirs(fPath+'/'+code)
    if not os.path.exists(fPath+'/'+code+'/source'):
        os.makedirs(fPath+'/'+code+'/source')
    if not os.path.exists(fPath+'/'+code+'/source/struc1'):
        os.makedirs(fPath+'/'+code+'/source/struc1')
    #else:
    #    raise Exception("Folder "+ fPath + '/'+ code+  " already exists, cannot create it")
    return [fPath+'/'+code, fPath+'/'+code+'/source', fPath+'/'+code+'/source/struc1']

def copyFilesToRegfolder(dest, sMeta):
    ''' copy files to folder'''
    p=sMeta["STRUCTURE_FILE"]
    shutil.copy(p, dest)
    extractGzip(dest+'/'+os.path.split(p)[1])
    sMeta["STRUCTURE_FILE"]='struc1/'+os.path.splitext(os.path.split(p)[1])[0]
    for idx,files in enumerate(sMeta["LINKED_FILE"]):
        full_file_name = files[0]
        print('full file name to copy', full_file_name)
        file_name = os.path.split(full_file_name)[1]
        print(file_name)
        if os.path.isfile(full_file_name):
            print('copying to', dest)
            shutil.copy(full_file_name, dest)
            sMeta["LINKED_FILE"][idx][0]='struc1/'+file_name
    return sMeta



def getStrMetadata(struc):
    #call alchemy/external customer module to fill info
    info = ['Structure to register for test',
            inputStructuresVolume+'/'+struc+'.cif.gz',
            'X-RAY DIFFRACTION',
            'User',
            'alexandre.gillet___discngine.com',
            1.5,
            [],
            [['Comment', 'Test script'], ['Internal ID', struc]],
            [24],
            [['A', 'A1JMF7_YERE8', '1-110'], ['A', 'LOLA_YERE8', '']],
            [[inputStructuresVolume+'/'+struc+'_phases.mtz', '', 'All']],
            []
            ]
    
    #fill dic with alchemy dic info
    dic = {
        "TITLE": info[0],
        "STRUCTURE_FILE": info[1],
        "METHOD": info[2],
        "SOURCE": info[3],
        "CREATED_BY": info[4],
        "RESOLUTION": info[5],
        "LIGAND": info[6],
        "ANNOTATION": info[7],
        "PROJECT_ID": info[8],
        "UNIPROT_MAPPING": info[9],
        "LINKED_FILE": info[10],
        "STRUCTURE_RELATION": info[11]
    } 
    return dic

def register(archivePath):
    ''' registration '''
    response = api.post_structure(archivePath)
    return 0
    

def preparePOST(structureCode):
    #create a working folder
    archivePath, csvPath, filesPath = createRegistrationFolder(registrationVolume, structureCode)
    #get the csv recipe information in a dictionnary
    #here this should be done by an external module with a given signature
    structureDic = getStrMetadata(structureCode)
    #write the recipe and files to registration folder
    structureDic=copyFilesToRegfolder(filesPath, structureDic)
    structureDic=convertCIFifRequired(structureDic)
    writePostConfigCsv(csvPath, structureDic)
    #zip the folder
    prepareZipArchive(archivePath, csvPath)
    return archivePath+'/post_structure.zip'

def waitForStructure(internalCode, knownList, pid):
    response = api.get_project(str(pid))
    strInCommunity = json.loads(response.text)
    diff = [ x for x in strInCommunity["data"]["projects"][0]["structureCodes"] if x not in knownList]
    if len(diff) == 0:
        print('going to sleep for 20s')
        time.sleep(20)
        print('make a check')
        return waitForStructure(internalCode, knownList, pid)
    else:
        print('something finished', diff[0])
        return diff[0]

def codeHasInternalID(code, internalid):
    structureResp = api.get_structure_metadata(code)
    obj = json.loads(structureResp.text)
    for annot in obj["data"]["structures"][0]["annotations"]:
        if annot["type"] == "Internal ID" and annot["value"] == internalid:
            return 'Y'
    return 'N'

########################################################################################################
########################################################################################################
#################### STARTING THE SPAGHETTI ############################################################
########################################################################################################

#read config
configFile=configVolume+'/config.properties'
config = configparser.ConfigParser()
config.read(configFile)
fImpName = config["import"]["historyfile"]

#read import history
importHistory=readImportHistory(fImpName)
print(importHistory, importHistory)


#list available pdb files
pdbGzFilesList=listAvailableFiles(inputStructuresVolume,'gz')
pdbGzFilesListNoGzExt=[removeFileExt(f) for f in pdbGzFilesList]
#pdbFilesList=listAvailableFiles(inputStructuresVolume,'pdb')

#create the list of fies to register (the one not already extracted or not already registered)
gzfilesToRegister = [x for x in pdbGzFilesList if x not in [x["ID"] for x in importHistory if x["Status"] in ['ok']] ]
filesToRegister=[removeFileExt(f) for f in gzfilesToRegister]
internalCodesToRegister=[removeFileExt(f) for f in filesToRegister]
print('List of internal codes to register', internalCodesToRegister)

#get "community" project
project_id = getProjectID('community')
response = api.get_project(str(project_id))
obj = json.loads(response.text)
structuresInCommunityProject = obj["data"]["projects"][0]["structureCodes"]


for s in internalCodesToRegister:
    # Structure endpoints:
    print(" -- Starting structure code", s)
    #double check we really have to register the structure: look for it into the community project
    code=convertInternalIdToCode(s, structuresInCommunityProject)
    if code == 0:
        print("      Structure is indeed not registered (because the internal id was not found in community project)")
        print("      LETS REGISTER IT !!")
        #prepare archive for POST /structure
        archivePath = preparePOST(s)
        #register the structure
        register(archivePath)
        #wait for the registration to finish
        newCode = waitForStructure(s, structuresInCommunityProject, project_id)
        print('newCode', newCode)
        isGoodOrNot = codeHasInternalID(newCode, s)
        if isGoodOrNot == 'Y':
             appendHistory(s, state='ok')
        else:
             appendHistory(s, state='fail')
        print('Is the structure registered the one we thing it is ? :)', isGoodOrNot)
        #TODO in v2: send a notification of success/fail somewhere with David's stuff
    else:
        print("Structure is already registered, its code is: ", code)




