import os 

for root, directories, files in os.walk("flags-mini"):
    for file in files:
        # print(file)
        os.system(f"python wave_flag.py {root}/{file}")
        # print(root)