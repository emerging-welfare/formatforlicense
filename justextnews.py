import justext
import requests
import re
import glob
import os
import sys

from collections import Counter

response = requests.get("https://timesofindia.indiatimes.com/city/ahmedabad/Amarsinh-who-Congress-what/articleshow/1746346645.cms")

source_dir = sys.argv[1]
save_dir = sys.argv[2]

os.chdir(source_dir)

# Generating links for Folia Docs
file_link = {}
for file in glob.glob("*.xml"):
    link = file.replace("__", "://")
    link = link.replace("_", "/")
    link = link.replace(".folia.xml", ".cms")
    print(link)
    file_link[file] = link
    


# Get texts from links and writing to files
for file in file_link.keys():
    response = requests.get(file_link[file])
    with open(save_dir+file, "w+") as f:
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        for paragraph in paragraphs:
          if not paragraph.is_boilerplate:
            print (paragraph.text)
            f.write(paragraph.text+"\n")
        f.close()
