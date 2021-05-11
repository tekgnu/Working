#!/usr/bin/python3

#To run this against Azure machines
#Invoke-AzVMRunCommand -ResourceGroupName {RESOURCE_GROUP} -Name {SERVERNAME} -CommandId "RunShellScript" -ScriptPath {SCRIPT_FILE&REL_PATH}

import os
import requests
import json


azInstMetaSvcIp = '169.254.169.254'
azInstMetaSvc = '/metadata/instance?api-version=2020-09-01'
headers = {'Metadata': 'True'}

azInstMetaVal = None #Placeholder for AIM values.
vmEnvVariables = None #Placeholder for environment variables.

# Get a list of environment variables (Print or assign value)
# for val in os.environ:
#	print(f"Key: {val} Value: {os.environ.get(val)}")
## Commented out 
# vmEnvVariables = os.environ

req = requests.get('http://' + azInstMetaSvcIp + azInstMetaSvc, headers=headers)

parsed = json.loads(req.text)

print(json.dumps(parsed, indent=4, sort_keys=True))
