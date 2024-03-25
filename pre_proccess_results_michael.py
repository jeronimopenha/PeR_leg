import re

from src.python.util.util import Util

base = Util.get_project_root()
data_files = Util.get_files_list_by_extension(base + "/reports/results_michael/", ".dot")


pattern = r' \[label\s*=\s*[^;]*;\s*op\s*=\s*[^;]*;\s*\]'
patter2 = r'port=\d; '
new_data_files = []
for dot_file, dot_name in data_files:
    new_data_files.append(dot_file)
    with open(dot_file) as f:
        rows = f.readlines()
    for i in range(len(rows)):
        rows[i] = re.sub(pattern, ';', rows[i])
        rows[i] = re.sub(patter2,'',rows[i])
        rows[i] = rows[i].replace(";]","];")
    
    with open(dot_file,'w') as f:
        f.writelines(rows)
