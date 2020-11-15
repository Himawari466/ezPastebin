ezPastebin  
==========  
Licensed under [MIT License](https://mit-license.org/).
  
  
### About  
This tools if for my personal usage only, you are free to use this tools whitout any warranty.  
  
  
### Developer API key
In order to use this tools you will need a [pastebin developer key](http://pastebin.com/doc_api).  
  
  
### python module
* requests
* urllib
  
  
### Usage
```shell
$ ./ezPastebin.py -k <api_key> -f <input_file>
```
##### Example
```shell
$ ./ezPastebin.py -k YOURAPIKEY -f myfile.txt
$ ./ezPastebin.py -k YOURAPIKEY -f /path/to/myfile.txt
```
##### Piping
```shell
$ ./ezPastebin.py -k YOURAPIKEY -f myfile.txt --raw | less
```
##### With alias
```shell
$ alias ezp="/path/to/ezPastebin.py -k YOURAPIKEY -f"
$ ezp myfile.txt
```
