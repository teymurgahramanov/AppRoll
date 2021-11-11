import os.path
import sys
import requests.status_codes
import yaml.loader

class colors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def printOk():
    print(colors.OK,"OK",colors.ENDC)

def printFail(message=None):
    if message is None:
        print(colors.FAIL,"FAIL",colors.ENDC)
    else:
        print(colors.FAIL,"FAIL:",message,colors.ENDC)

def healthcheck(host,port,endpoint,method,response):
    url="http://" + host + ":" + port + endpoint
    if method != "" and method == "GET":
        try: 
            request=requests.get(url,timeout=5)
            if str(request.status_code) == response:
                print(url,colors.OK,str(request.status_code),'OK',colors.ENDC)
            else:
                print(url,colors.WARNING,str(request.status_code),'WARNING',response,'EXPECTED',colors.ENDC)
        except:
            print(url,colors.FAIL,'FAIL: Connection failed',colors.ENDC)
    else:
        printFail("Method is not provided")

appName = sys.argv[1]
appEnv = sys.argv[2]
appLoc = sys.argv[3]
appManifestDir = "./approll/vars/main/"
appManifestFile = os.path.join(appManifestDir,appName + '.yml')
appManifestData = yaml.load(open(appManifestFile,'r'), Loader=yaml.FullLoader)
try:
    app_targets = appManifestData[appName]['targets'][appEnv][appLoc]
except:
    print(colors.WARNING,'Location',appEnv,appLoc,'for',appName,'is not defined',colors.ENDC)
    sys.exit(0)

for targets in app_targets:
    host=targets.split(':')[0]
    healthcheck(
    host,
    str(appManifestData[appName]['ports']['http']),
    str(appManifestData[appName]['healthcheck']['endpoint']),
    str(appManifestData[appName]['healthcheck']['method']),
    str(appManifestData[appName]['healthcheck']['response'])
    )