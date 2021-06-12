import os
  
# Path
path = "C:/TTL/Seasons-CallCentre/Seasons-CallCentre/Helpers/CountryList.json"
  
# Path of Start directory
start = "C:/TTL"
  
# Compute the relative file path
# to the given path from the 
# the given start directory.
relative_path = os.path.relpath(path, start)
  
# Print the relative file path
# to the given path from the 
# the given start directory.
print(relative_path)
  
  
  
# Path
path = "C:/TTL/Seasons-CallCentre/Seasons-CallCentre/Helpers/CountryList.json"
  
# Compute the relative file path
# to the given path from the 
# the current directory.
  
# if we do not specify the start
# parameter it will default to
# os.curdir i.e current directory 
relative_path = os.path.relpath(path)
  
# Print the relative file path
# to the given path from the 
# the given start directory.
print(relative_path)
  
  
# Path
path = "C:/TTL/Seasons-CallCentre/Seasons-CallCentre/Helpers/CountryList.json"
  
# Path of Start directory
start = "c:/TTL/Seasons-CallCentre"
  
# Compute the relative file path
# to the given path from the 
# the given start directory.
relative_path = os.path.relpath(path, start)
  
# Print the relative file path
# to the given path from the 
# the given start directory.
print(relative_path)
  
  
# Path
path = "C:/TTL/Seasons-CallCentre/Seasons-CallCentre/Helpers/CountryList.json"
  
# Path of Start directory
start = "C:"
  
# Compute the relative file path
# to the given path from the 
# the given start directory.
relative_path = os.path.relpath(path, start)
  
# Print the relative file path
# to the given path from the 
# the given start directory.
print(relative_path)