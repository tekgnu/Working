# This is just a python wrapper for Authenticating via an Azure Service Principle
#   It is reliant on an accounts.ini - see example for more details

import configparser

parser = configparser.ConfigParser()
parser.read('./accounts.ini')
print(parser.sections())
if parser.has_section('Account') == False:
    print("AZ Auth was unable to access the accounts.ini file required for authenticating.")
    print("See the example Accounts.ini file for more information")
else:
    parser.sections()
#for sect in parser.section():