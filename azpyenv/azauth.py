# This is just a python wrapper for Authenticating via an Azure Service Principle
#   It is reliant on an accounts.ini - see example for more details

import configparser

parser = configparser.ConfigParser()

parser['Account'] = {}
parser['Account']['TenantId'] = '72f988bf-86f1-41af-91ab-2d7cd011db47'
parser['Account']['PyServicePrinciple'] ='mwppy-sp-rbac-001'
parser['Account']['PyPwd'] = 't9Yfi0Bx5_D3wqEwbYR-9sfenidcvr~N2n'

parser['Resources'] = {}
parser['Resources']['ResourceGroup'] = 'rg-deve1py001'
parser['Resources']['Location'] ='eastus'

with open('Accounts.cfg', 'w') as configfile:
    parser.write(configfile)


#parser.read_file('accounts.cfg')
#print(parser.sections())
#if parser.has_section('Account') == False:
#    print("AZ Auth was unable to access the accounts.cfg file required for authenticating.")
#    print("See the example Accounts.cfg file for more information")
#else:
#    parser.sections()
#for sect in parser.section():