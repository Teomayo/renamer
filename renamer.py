import os
from datetime import datetime
folder = r"C:\Users\Teodor\OneDrive - University of Waterloo\UWAFT work\Pictures\Misc"
location = input("Photo Location:")
files = os.listdir(folder)
for filename in files:
    if not filename.startswith("."):
        file = os.path.join(folder, filename)
        m_time = os.path.getmtime(file)
        real_time = datetime.fromtimestamp(m_time)
        f_time = datetime.strftime(real_time, "%Y-%m-%d %H_%M_%S")
        new_filename = f_time + "_" + location + ".png"
        new_file = os.path.join(folder, new_filename)
        os.rename(file, new_file)