import os
import glob
import shutil
from PIL import Image

# 原始圖片所在的資料夾
source_folder = './img/'

# 目標資料夾，存放複製並轉換格式或壓縮後的圖片
target_folder = './compression/'

# 確保目標資料夾存在，如果不存在則創建
os.makedirs(target_folder, exist_ok=True)

# 使用 glob 取得所有 jpg 檔案的原始名稱
jpg_files = glob.glob(source_folder + '*.[jJ][pP][gG]')

# 複製並壓縮 jpg 圖片
for i in jpg_files:
    # 複製檔案到目標資料夾
    target_path = shutil.copy(i, target_folder)
    
    # 壓縮圖片
    im = Image.open(target_path)
    im.save(target_path, 'JPEG', quality=50, subsampling=0)
