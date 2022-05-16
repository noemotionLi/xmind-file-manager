# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:01:42 2022

@author: 10291
"""
import re
import os
import xmind


# 主程序模块
def gen_my_xmind_file(target_path):
    # 获取当前目录
    original_path = os.getcwd()
    # 切换到目标目录
    os.chdir(target_path)
    # 加载一个xmind文件，如果没有则自动创建
    workbook = xmind.load("my.xmind")
    # 加载空白页
    sheet1 = workbook.getPrimarySheet()
    # 页面设计
    design_sheet1(sheet1, target_path)
    # now we save as test.xmind
    os.chdir(original_path)
    xmind.save(workbook, path= os.path.basename(target_path) + '.xmind')


def design_sheet1(sheet1, target_path):
    center_title = os.path.basename(target_path)
    # 第一页标题
    sheet1.setTitle(center_title)  

    # 创建中心主题
    root_topic = sheet1.getRootTopic()
    root_topic.setTitle(center_title)
    # 下一步（扫描目标目录，创建思维导图）
    scanfile(root_topic, target_path)

def scanfile(father_node, filepath):
    filelist = os.listdir(filepath)
    for filename in filelist:
        next_file_path = os.path.join(filepath, filename)
        if os.path.isdir(next_file_path):
            father_topic = add_father_topic(filename, father_node)
            scanfile(father_topic, next_file_path)
        else:
            add_sub_topic(next_file_path, father_node)

def add_sub_topic(file_path , root_topic ):
    # 修改节点名称和路径
    file_name = change_node_name(file_path)
    sub_topic = root_topic.addSubTopic()
    sub_topic.setTitle(file_name)
    
    # 创建链接
    file_link = file_path.replace(os.getcwd()+'\\','')
    sub_topic.setFileHyperlink(file_link) 

def add_father_topic(directory, upper_topic):
    father_name = change_node_name(directory)
    # 如果不是叶子节点（文件夹）则作为中间节点处理
    father_topic = upper_topic.addSubTopic()
    father_topic.setTitle(father_name)
    return father_topic
    
def change_node_name(string, is_open = False):
    string = os.path.basename(string)
    if is_open:
        # 匹配文件后缀
        pattern = re.compile('(.*?)\.[a-zA-Z]*$')
        # 返回去除后缀的
        try:
            return pattern.findall(string)[0]
        except:
            return string
    else :
        return string

if __name__ == '__main__':
    gen_my_xmind_file(r'C:\Users\10291\Desktop\疫情防控')



