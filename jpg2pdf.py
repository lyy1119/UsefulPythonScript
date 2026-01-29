from PIL import Image
import glob
import os

# 获取当前目录下所有 jpg（按文件名排序）
jpg_files = sorted(glob.glob("*.jpg"))

if not jpg_files:
    raise RuntimeError("当前目录下没有 jpg 文件")

images = []
for f in jpg_files:
    img = Image.open(f).convert("RGB")
    images.append(img)

# 第一张作为封面，其余作为追加页
images[0].save(
    "output.pdf",
    save_all=True,
    append_images=images[1:]
)

print(f"已生成 output.pdf，共 {len(images)} 页")

