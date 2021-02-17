import os


# 需要搜索的文件,后期可以改成input输入
folder = input("folder_name： ")
# 获取当前所在路径
current_path = os.getcwd()
i = 0
while True:
    # 获取当前路径下所有的文件
    current_files = os.listdir(current_path)
    # 判断folder是否在当前文件中
    for current_file in current_files:
        if current_path == os.sep:
            new_path = current_path
        else:
            new_path = os.path.join(current_path, current_file)
        try:
            if os.path.isdir(new_path):
                if folder in os.listdir(new_path):
                    print(os.path.join(new_path, folder))
                    exit()
        except Exception as e:
            continue
    else:
        i += 1
        current_path = os.path.dirname(current_path)
        if i == 5:
            print("超过预设次数了,文件应该不存在,兄弟,别试了")
            exit()
        continue
