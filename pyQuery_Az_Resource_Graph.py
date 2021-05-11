### PYTHON AZURE RESOURCE GRAPH QUERY EXAMPLE TAKEN FROM:
## https://docs.microsoft.com/en-us/azure/governance/resource-graph/first-query-python
# Import Azure Resource Graph library
import azure.mgmt.resourcegraph as arg

# Import specific methods and models from other libraries
from azure.common.credentials import get_azure_cli_credentials
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import SubscriptionClient

# Wrap all the work in a function
def getresources( strQuery ):
    # Get your credentials from Azure CLI (development only!) and get your subscription list
    subsClient = get_client_from_cli_profile(SubscriptionClient)
    subsRaw = []
    for sub in subsClient.subscriptions.list():
        subsRaw.append(sub.as_dict())
    subsList = []
    for sub in subsRaw:
        subsList.append(sub.get('subscription_id'))

    # Create Azure Resource Graph client and set options
    argClient = get_client_from_cli_profile(arg.ResourceGraphClient)
    argQueryOptions = arg.models.QueryRequestOptions(result_format="objectArray")

    # Create query
    argQuery = arg.models.QueryRequest(subscriptions=subsList, query=strQuery, options=argQueryOptions)

    # Run query
    argResults = argClient.resources(argQuery)

    # Show Python object
    print(argResults)

getresources("Resources | project name, type | limit 5")

