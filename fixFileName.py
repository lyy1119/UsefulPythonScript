import os
import re

dir_path = r"."   # 改成你的目录

pattern = re.compile(r'^(\d+)\.jpg$', re.IGNORECASE)

for filename in os.listdir(dir_path):
    match = pattern.match(filename)
    if not match:
        continue

    num_str = match.group(1)
    new_name = f"{int(num_str):03d}.jpg"

    if new_name == filename:
        continue  # 已经是三位，跳过

    old_path = os.path.join(dir_path, filename)
    new_path = os.path.join(dir_path, new_name)

    print(f"{filename} -> {new_name}")
    os.rename(old_path, new_path)

