import os
path_folder = r'D:/Connected_women/Etxtract_annotated_images/labels'
for file in os.listdir(path_folder):
    new=[]
    path = path_folder+'/'+file
    t = open(path,"r+")
    new_str = ""
    for line in t:
        new_line = (line[0].replace(line[0],'1')+line[1:])
        new_str += new_line
    writing_file = open(path,"w")
    writing_file.write(new_str)
    writing_file.close()
    

    
    
    



