import re
import urllib.request #importing only the request module from urllib
                      #this could be import like this; from urllib import request

#asking the page from the user.
url=input("Give the url of the page you want: ")
#program request to open the url.
site_open=urllib.request.urlopen(url)
#program reads the url source code and make it a string to work with it.
site=str(site_open.read())

#this two vars are looking in the length of the var site to find br and p tags.
#if they found they are adding 1 to themselfs
#re.findall() can be found in the re module
br_tag=len(re.findall("<br>",site))
p_tag=len(re.findall("<p>",site))

#check if br_tag got a value bigger than 0.
#if true then print that they are br tags and the amount of them.
#if br_tag=0 (else condition) prints that no br tags has been found.
if br_tag>0:
    print("br tags in this url: ",br_tag)
else:
    print("No br tags has been found in this url.")

#check if p_tag got a value bigger than 0.
#if true then print that they are p tags and the amount of them.
#if p_tag=0 (else condition) prints that no p tags has been found.
if p_tag>0:
    print("p tags in this url: ",p_tag)
else:
    print("No p tags has been found in this url.")
