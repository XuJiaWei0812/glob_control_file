import glob
import os
import shutil

source_folder = './原始圖片/'  # 原始檔案所在資料夾
target_folder = './重新命名/'  # 目標資料夾，存放複製並重新命名的檔案

# 確保目標資料夾存在，如果不存在則創建
os.makedirs(target_folder, exist_ok=True)

# 使用 glob 取得所有檔案的原始名稱
images = glob.glob(source_folder + '*')

# 初始化名稱計數器
n = 1

# 使用 os 重新命名檔案
for i in images:
    # 構建新檔案名稱與路徑
    new_file_name = f'img-{n:03d}.jpg'
    new_file_path = os.path.join(target_folder, new_file_name)
    
    # 複製並重新命名檔案
    shutil.copy(i, new_file_path)
    
    n += 1
