## Example Script to Kick off a Batch App from a 
## Predefined Shared Drive - Z:

$Batch_App_Src = "Z:\batchapp.zip"
$Batch_App_Dest = "C:\"
$Batch_Working_Set = "Z:\file3.txt"

Expand-Archive -LiteralPath $Batch_App_Src -DestinationPath $Batch_App_Dest -Force

Set-Location $Batch_App_Dest

####### REPLACE FILES 3 with Network location i.e. z:\files3.txt
.\BatchApp.exe $Batch_Working_Set
