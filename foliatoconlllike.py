import re
from pynlpl.formats import folia
import glob
import os
import sys

def getwordtext(entity):
    annot = ""
    for word in entity.wrefs():
        annot = annot + word.text()
        if word.space:
            annot = annot + " "
    return re.sub(r" $", r"", annot)

source_dir = sys.argv[1]
save_dir = sys.argv[2]

os.chdir(source_dir)


for doc_name in glob.glob("*.xml"):
    print("Doc name : " + doc_name)
    path = save_dir
    doc = folia.Document(file=doc_name)
    path = path + doc_name
    with open(path, "w+") as f:
        for i,sentence in enumerate(doc.sentences()):
            for layer in sentence.select(folia.EntitiesLayer):
                for entity in layer.select(folia.Entity):
    
                    
                    annot = getwordtext(entity)
                    #annot = " ".join([word.text() for word in entity.wrefs()])
                    try:
                        prev_length = 0
                        jkl = re.search(r"w\.(\d+)$", entity.wrefs()[0].id)
                        prev = doc[re.sub(r"(.*w\.)\d+$", r"\g<1>" + str(int(jkl.group(1)) - 1), entity.wrefs()[0].id)]
                        
                        
                        
                        to_be_added = prev.text() + " "
                            
                        annot = to_be_added + annot
                        prev_length = len(to_be_added)
                    except:
                        #print("First Exception First Exception First Exception First Exception")
    
                        #print("No prev " + re.search(r"w\.(\d+)$", entity.wrefs()[0].id).group(1))
                        gfg = 0
    
                    try:
                        after_length = 0
                        after = re.search(r"w\.(\d+)$", entity.wrefs()[-1].id)
                        after = doc[re.sub(r"(w\.)\d+$", r"\g<1>" + str(int(after.group(1)) + 1), entity.wrefs()[0].id)]
                        

                        after_to_be_added = " " + after.text()
                        
                        annot = annot + after_to_be_added
                        after_length = len(after_to_be_added)
                        f.write(annot + "\t" + entity.cls +"\t" + str(prev_length) + ":" + str(len(annot)-after_length) + "\n")
                        
                    except:
                        #print("Last Exception Last Exception Last Exception Last Exception")
                        #print("No after " + entity.wrefs()[0].id)
                        gfg = 0
    #                [prev_length-1:len(annot)-after_length]
                    
