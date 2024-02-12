import os
import glob
from PIL import Image

# 原始圖片所在的資料夾
source_folder = './原始圖片/'

# 目標資料夾，存放複製並轉換格式或壓縮後的圖片
target_folder = './圖片轉檔'

# 確保目標資料夾存在，如果不存在則創建
os.makedirs(target_folder, exist_ok=True)

# 使用 glob 取得所有 jpg 檔案的原始名稱
jpg_files = glob.glob(source_folder + '*.[jJ][pP][gG]')

# 複製並轉換格式
for i in jpg_files:
    # 轉換格式
    im = Image.open(i)
    name = os.path.basename(i).lower().replace('jpg', 'png')
    im.save(os.path.join(target_folder, name), 'PNG')