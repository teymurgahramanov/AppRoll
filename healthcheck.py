import os.path
import sys
import requests.status_codes
import yaml.loader

class colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def healthcheck(host,port,endpoint,method,response):
    url="http://" + host + ":" + port + endpoint
    if method != "" and method == "GET":
        try: 
            request=requests.get(url,timeout=5)
            if str(request.status_code) == response:
                print(url + colors.OKGREEN + ' OK ' + str(request.status_code) + colors.ENDC)
            else:
                print(url + colors.WARNING + ' WARNING ' + str(request.status_code) + ' EXPECTED ' + response + colors.ENDC)
        except:
            print(url + colors.FAIL + ' FAIL ' + colors.ENDC)
    else:
        print(colors.WARNING + 'Method not provided' + colors.ENDC)

app_name = sys.argv[1]
app_env = sys.argv[2]
app_loc = sys.argv[3]
app_manifest_dir = "./approll/vars/main/"
app_manifest_file = os.path.join(app_manifest_dir,app_name + '.yml')
app_manifest_data = yaml.load(open(app_manifest_file,'r'), Loader=yaml.FullLoader)
try:
    app_targets = app_manifest_data[app_name]['targets'][app_env][app_loc]
except:
    print(colors.WARNING,'Location',app_env,app_loc,'for',app_name,'is not defined',colors.ENDC)
    sys.exit(0)

for targets in app_targets:
    host=targets.split(':')[0]
    healthcheck(
    host,
    str(app_manifest_data[app_name]['ports']['http']),
    str(app_manifest_data[app_name]['healthcheck']['endpoint']),
    str(app_manifest_data[app_name]['healthcheck']['method']),
    str(app_manifest_data[app_name]['healthcheck']['response'])
    )