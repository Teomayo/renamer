import os
from datetime import datetime
s = 1
folder = r"C:\Users\Teodor\OneDrive - University of Waterloo\UWAFT work\Pictures\Misc"
location = input("Photo Location:")
files = os.listdir(folder)
for filename in files:
    if not filename.startswith("."):
        file = os.path.join(folder, filename)
        m_time = os.path.getmtime(file)
        real_time = datetime.fromtimestamp(m_time)
        f_time = datetime.strftime(real_time, "%Y-%b-%d")
        ext = os.path.splitext(file)[-1].lower()
        new_filename = f_time + "_" + location + "_" + str(s) + ext
        new_file = os.path.join(folder, new_filename)
        os.rename(file, new_file)
        s += 1
