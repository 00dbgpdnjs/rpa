import os

# < Get path >

# print(os.getcwd()) # Curr Working Dir

# os.chdir("rpa") # Change the dir
# print(os.getcwd())

# os.chdir("..") # To parents dir
# print(os.getcwd())

# os.chdir("../..") # To grandparents dir
# print(os.getcwd())

# os.chdir("c:/") # To absolute path.
# print(os.getcwd())

# Create a file path (not a folder).
# file_path = os.path.join(os.getcwd(), "my_file.txt") # Create an absolute path.
# print(file_path)

# Get folder path from file path
# print(os.path.dirname(r"C:\Users\USER\Desktop\SW\project\PythonWorkspace\my_file.txt"))

#----------------------------------------------------------------------------------------
# < Get file info >

import datetime

# 1. Created Date
# file_path = "rpa/1_excel/3_cell.py"
# ctime = os.path.getctime(file_path)  # c: create
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime)) # more intuitive than the code just above
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 2. Modified Date
# mtime = os.path.getmtime(file_path) # m : modified
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 3. The last access date
# atime = os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 4. size
# size = os.path.getsize(file_path) # 바이트 단위
# print(size) 

#-------------------------------------------------------------------------
# < Get the all files&folders -> Find a file or a folder with the result >

# 1. Get the file&folder list
# print(os.listdir())
# print(os.listdir("rpa")) # Based on the folder.

# 1-1. Advanced) All the sub-folders
# result = os.walk("rpa") 
# result = os.walk(".") # The top dir is the standard.
# print(result) # >> "generator" (which returns a tuple having[with] three values. The values are root[a dir], dirs in root and files in root))

# for root, dirs, files in result:
#     print(root, dirs, files)

# 2. To check if there's a specific file in the folder?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))
# print(result) # If you wanna get a whole path, os.walk(os.getcwd()) instead of os.walk(".")

# 2-1. Advanced) Find with a specific pattern
# ex) *.xlsx, *.txt, 자동화*.png
# import fnmatch # FileName match
# pattern = "*.py" # file*.py *.png ..
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files: # To find files in "files" list
#         if fnmatch.fnmatch(name, pattern): # If the "name" matches the "pattern"
#             result.append(os.path.join(root, name))
# print(result)

#----------------------------------------------------
# 1. Is the path given  a file/ a folder?
# print(os.path.isdir("rpa")) # Is is a folder? >> True
# print(os.path.isfile("run_btn.png")) # Is it a file? >> True

# 2. 주어진 경로가 존재하는지
# if os.path.exists("rpa"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

#-------------------------------------------------
# < file&folder CUD >

# 1. 파일 만들기 (Based on cwd)
# Easier than  with open("파일명", encoding=) as f:...
# open("new_file.txt", "a").close() # 2nd arg: writing mode (a: append)

# 2. 파일명 변경
# os.rename("new_file.txt", "new_file_rename.txt")

# 3. 파일 삭제
# os.remove("new_file_rename.txt")


# 4. 폴더 만들기
# os.mkdir("new_folder")
# os.mkdir("C:\\Users\\USER\\Desktop\\SW\\project\\PythonWorkspace\\new_folder") # Based on the absolute path

# os.makedirs("new_folders/a/b/c")

# 5. 폴더명 변경
# os.rename("new_folder", "new_folder_rename")

# 6. 폴더 지우기 (Only folders with nothing inside.)
# os.rmdir("new_folder_rename")

# 폴더 안이 비어 있지 않아도 삭제 가능
import shutil # shell utilities
# shutil.rmtree("new_folders")

#-----------------------------------------
# < Copy $ Move >

# 1. 다른 폴더에 파일 복사
# shutil.copy("run_btn.png", "test_folder") # (what-file path, where-folder or file path)
# 다른 이름으로 복사
# shutil.copy("run_btn.png", "test_folder/copied_run_btn.png")
# shutil.copyfile("run_btn.png", "test_folder/copied_run_btn_2.png") # 2nd: file name  not only folder name

# Difference
# shutil.copy("run_btn.png", "test_folder/copy.png") # Date : today 
# shutil.copy2("run_btn.png", "test_folder/copy2.png") # Date : The date when the first arg was created. / 2nd: file or folder path
# copy, copyfile : 메타정보 복사x
# copy2 : 메타정보 복사 o

# 2. 폴더 복사
# shutil.copytree("test_folder", "test_folder2")

# 3. 폴더 이동
# shutil.move("test_folder", "test_folder_rename") # If there isn't test_folder_rename, change to it 