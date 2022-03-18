# Name: file_walker
# Author: Reacubeth
# Time: 2021/5/24 10:49
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

import os


def traverse(file, file_type, absolute_path):
    files_ls = []
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        for f in files:
            cur_file_path = os.path.join(root, f)
            if file_type.lower() in cur_file_path:
                if absolute_path:
                    # print(cur_file_path)
                    files_ls.append(cur_file_path)
                else:
                    file_name = cur_file_path[cur_file_path.rfind('/') + 1:]
                    # print(file_name)
                    files_ls.append(file_name)
        # 遍历所有的文件夹
        for d in dirs:
            os.path.join(root, d)
    return files_ls


if __name__ == '__main__':
    res = traverse("DLcovid/tKG", 'csv', False)
    print(res)
