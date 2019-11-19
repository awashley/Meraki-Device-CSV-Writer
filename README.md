# Meraki-Device-CSV-Writer
Code snippet to read the results of 'get devices' in the Meraki API and produce a CSV file

# Arguments

Argument 1 is the name of the JSON file

Argument 2 is the name of the CSV that you want to create

# Files

Files will and should be in the directory that you are in when the python command is evoked

# Example

python3 CSV-Device-writer.py My_Meraki_Devices.json My_Devices.CSV

# Limitations

Some columns will be off depending if the Meraki environment has a mix of devices including MX devices
I have not used this code for anything except MX, MS and MR devices. Other device columns may have issues as well
