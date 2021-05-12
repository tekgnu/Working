# This is just a python wrapper for Authenticating via an Azure Service Principle
#   It is reliant on an accounts.ini - see example for more details
import Utils.AccountConfig as azcfg
import configparser
import os

# This changes the directory to the python virtual env. from the Repo's directory 
os.chdir('./azpyenv')
print(os.getcwd())

authCfg = azcfg.AzAccount()
auth = authCfg.getAccount('Accounts.cfg')
print(auth)

print("End")

    