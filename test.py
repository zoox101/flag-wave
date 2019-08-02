import os 

for root, directories, files in os.walk("flags-ultra"):
    for file in files:
        # print(file)
        os.system(f"python wave_flag.py {root}/{file}")
        # print(root)