import os
import shutil

# os.makedirs(r'C:\Users\ER.Caspian-Server\Desktop\Test')

src = r'C:\Users\ER.Caspian-Server\Desktop\create_folder'
dest = r'C:\Users\ER.Caspian-Server\Desktop\Test'
shutil.copytree(src, dest)
