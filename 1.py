import os

def get_all_img_files(folder_path):
    # 存图片绝对路径
    img_list = []
    # 允许的后缀
    suffixs = (".jpg", ".jpeg", ".png", ".JPG", ".PNG")

    # 遍历文件夹所有文件
    for file in os.listdir(folder_path):
        # 拼接完整路径
        full_path = os.path.join(folder_path, file)
        # 只判断文件，不是文件夹
        if os.path.isfile(full_path):
            # 判断后缀
            if file.lower().endswith(suffixs):
                # 转绝对路径
                abs_p = os.path.abspath(full_path)
                img_list.append(abs_p)
    return img_list


# ========== 使用示例 ==========
# 填你要扫描的文件夹路径
target_folder = "background"   # 当前项目文件夹

# 获取所有图片绝对路径列表
imgs = get_all_img_files(target_folder)
print("找到的图片文件：")
print(imgs)