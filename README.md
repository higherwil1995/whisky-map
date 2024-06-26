# Whisky Map App
為了熟悉、掌握 FastAPI 功能而建立的應用程式。
這是一個威士忌百科全書，旨在記錄來自世界各地的威士忌資訊、風味敘述。
未來，我們計劃新增客戶資訊管理功能，並提供一個寄酒資訊管理的介面，以改善現有的寄酒流程，有效減少因人為疏失而導致的營業損失。

# 如何開始
## 下載程式碼
1. 開啟終端機或命令提示字元。
2. 新增並切換至欲存放程式碼的資料夾。
3. 執行以下命令將程式碼複製到本地端：

```
git clone https://github.com/higherwil1995/whisky-map.git
```

## 安裝相依套件
在開始之前，請確保您已經安裝了以下相依套件：
- Docker
- Docker Compose

## 設定環境變數
在專案根目錄下，複製 `.env.example` 檔案並將其重新命名為 `.env`。然後，根據您的需求，調整 `.env` 檔案中的環境變數設定。

## 設定 GitHub Access
請按照以下步驟在 `$HOME/.docker/config.json` 檔案中設定 GitHub Access Token：

1. 至 GitHub 個人帳號申請 Access Token。
2. 開啟終端機或命令提示字元。
3. 使用文本編輯器開啟 `$HOME/.docker/config.json` 檔案。
4. 在 `auths` 部分新增以下內容，將 `<YOUR_GITHUB_USERNAME>` 和 `<YOUR_GITHUB_ACCESS_TOKEN>` 替換為您的 GitHub 使用者名稱和 Access Token：
    ```json
    "auths": {
         "ghcr.io": {
              "auth": "<YOUR_GITHUB_USERNAME>:<YOUR_GITHUB_ACCESS_TOKEN>"
         }
    }
    ```
5. 儲存並關閉檔案。

完成上述步驟後，您的 Docker 將能夠使用 GitHub Access Token 進行相關操作。

## 啟動應用程式
使用以下指令來啟動應用程式：
```
docker-compose -f docker-compose-cd.yaml up
```
這將會建立並啟動相關的容器，包括 FastAPI 伺服器和 MongoDB 資料庫以及監控程序 Watch Tower。

## API 文件瀏覽
現在，您可以在瀏覽器中輸入 `http://127.0.0.1:8000/docs` 來訪問 Whisky Map App 的交互式 API 文件囉。
