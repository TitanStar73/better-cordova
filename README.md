# better-cordova

A wrapper around the [Apache Cordova](https://github.com/apache/cordova) project

Apache Cordova is a tool used to conver HTML/CSS/JS into mobile apps.

This tool takes it one step further!

# How to use

Simply run the python script in the directory you would like to create a new project in.

This tool will guide you through basic setup, and even provides easy to use basic html and javascript framework along with indepth css classes and guidance websites!

All the info will be easy to access right in the index.html/css/js files!

# Common Issues

> Directory not empty: The directory must be empty to run the script (This is a cordova thing). Reference the python script with its absolute path and store it elsewhere. It is suggested to keep the script in a folder in PATH so that it can be easily accessed. 

> It can also be accessed using a bat file with the following command (assuming the script is main.py and is in the same folder)
```python "main.py" new %PluginType% %ProjectName% %DisplayName% %Author% %Description% %Confirm%```
