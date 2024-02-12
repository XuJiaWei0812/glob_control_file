# glob_control_file

glob_control_file 中包含三個 Python 程序，用於處理圖片檔案：批次重新命名、格式轉換以及圖片壓縮。

## 功能介紹

- `rename.py`: 批次重新命名指定資料夾內的所有圖片檔案。
- `convert_format.py`: 將指定資料夾內的圖片檔案從一種格式轉換成另一種格式。
- `compression.py`: 壓縮指定資料夾內的 JPG 圖片檔案，減少檔案大小。

## 安裝需求

這些程序需要安裝 Pillow 函式庫。

```bash
pip install Pillow
```

## 使用方法

### 批次重新命名 rename.py

將想要重新命名的圖片放入"img"資料夾，然後運行：

```bash
python rename.py
```

### 圖片格式轉換 convert_format.py

將想要格式轉換的圖片放入"img"資料夾，然後運行：

```bash
python convert_format.py
```

### 圖片壓縮

將想要壓縮名的圖片放入"img"資料夾，然後運行：

```bash
python compression.py
```
