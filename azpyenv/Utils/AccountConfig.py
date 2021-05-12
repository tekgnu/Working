# This class is to create the account configuration.  
#   By creating it as a separate class it allows it to be run separately, as well as 
#   Used to create a custom configuration.  
#   NOTE: Use .gitignore to hide account credentials
import configparser

class AzAccount:

    # Init with only the keys that the configuration needs to align to
    def __init__(self):
        self.accountDef = { 'tenantid': "" , 'pysp': "" , 'pypwd': ""}

    # Creates the Account configuration file with the defined key, value pairs
    def createAccount(self, file="Accounts.cfg", section="Account", configDict={}):
        writer = configparser.ConfigParser()
        writer[section] = {}
        for key in configDict:
            writer[section][key] = configDict[key]
        with open(file, 'w') as configfile:
            writer.write(configfile)
    
    # Outputs the Account file to validate
    def getAccount(self, file="Accounts.cfg", section="Account"):
        reader = configparser.ConfigParser()
        reader.read(file)

        if reader.has_section('Account') == False or reader[section]['tenantid'] == "":
            print("The Account Configuration is either missing or was not created correctly.")
        else:    
            self.accountDef['tenantid'] = reader[section]['tenantid']
            self.accountDef['pysp'] = reader[section]['pysp']
            self.accountDef['pypwd'] = reader[section]['pypwd']
        return self.accountDef

if __name__ == '__main__':
    file =  input("Name of the config file [def. Accounts.cfg]: ")
    if file == "":
        file = "Accounts.cfg"
    tenid = input("Enter the Azure TenantID:                    ")
    pysp =  input("Enter the Python Service Principal Name:     ")
    pypwd = input("Input the Python Service Principal Pwd:      ")
    if tenid == "" or pysp == "" or pypwd == "":
        print("Error data was not provided for the Account config file.")
    else:
        myazacct = AzAccount()
        myazacct.createAccount(
            file=file, section="Account", configDict={ 'tenantid': tenid , 'pysp': pysp , 'pypwd': pypwd})
        validate = myazacct.getAccount(file=file, section="Account")
        print("Validating the data input:")
        print(validate)



