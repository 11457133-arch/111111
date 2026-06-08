<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML 網站 Prompt 產生器</title>
    <style>
        :root {
            --primary-color: #4a90e2;
            --bg-color: #f5f7fa;
            --card-bg: #ffffff;
            --text-color: #333333;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: var(--card-bg);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: var(--primary-color);
            margin-bottom: 30px;
        }
        .section {
            background: #f9fbfd;
            padding: 20px;
            border-left: 4px solid var(--primary-color);
            margin-bottom: 20px;
            border-radius: 0 8px 8px 0;
        }
        .section h2 {
            margin-top: 0;
            font-size: 1.2rem;
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        input[type="text"], select, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            font-size: 1rem;
        }
        textarea {
            resize: vertical;
        }
        button {
            display: block;
            width: 100%;
            padding: 12px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background-color: #357abd;
        }
        .output-section {
            margin-top: 30px;
        }
        #resultPrompt {
            background: #282c34;
            color: #abb2bf;
            padding: 20px;
            border-radius: 5px;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: 'Courier New', Courier, monospace;
        }
        .copy-btn {
            background-color: #28a745;
            margin-top: 10px;
        }
        .copy-btn:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>🌐 HTML 網站 Prompt 產生器</h1>
    
    <div class="section">
        <h2>🎨 1. 視覺與整體風格</h2>
        <div class="form-group">
            <label for="style">整體設計風格：</label>
            <select id="style">
                <option value="極簡風 (Minimalist)">極簡風</option>
                <option value="和風 (Japanese Traditional/Modern)">和風</option>
                <option value="中國風 (Chinese Traditional/Chinoiserie)">中國風</option>
                <option value="現代科技風 (Modern Tech)">現代風</option>
                <option value="兒童可愛風 (Cute/Kawaii/Kids)">兒童風</option>
                <option value="歐美商務風 (Corporate/Professional)">歐美商務風</option>
            </select>
        </div>
        <div class="form-group">
            <label for="primaryColor">主色調 (例如: #4a90e2 或 溫暖大地色)：</label>
            <input type="text" id="primaryColor" placeholder="請輸入顏色描述或 Hex 碼" value="根據風格自由搭配">
        </div>
    </div>

    <div class="section">
        <h2>⚙️ 2. HEAD 設定</h2>
        <div class="form-group">
            <label for="headContent">Head 需要包含什麼？(多選/填寫)：</label>
            <input type="text" id="headContent" value="RWD 響應式設定, FontAwesome 圖標庫, Google Fonts 字體, SEO Meta 標籤">
        </div>
    </div>

    <div class="section">
        <h2>🧭 3. NAV 導覽列與架構</h2>
        <div class="form-group">
            <label for="navContent">Nav 包含哪些項目？(用逗號分開)：</label>
            <input type="text" id="navContent" value="首頁, 關於我們, 產品服務, 圖庫展示, 聯絡我們">
        </div>
        <div class="form-group">
            <label for="siteLayers">網站層級深度 (有幾層？)：</label>
            <select id="siteLayers">
                <option value="單頁式網站 (One-page SEO)">單頁式網站 (滾動錨點)</option>
                <option value="標準 2 層結構 (主頁 + 內頁)">標準 2 層結構 (主頁 + 內頁)</option>
                <option value="複雜 3 層以上結構 (含子分類)">複雜 3 層以上結構 (含子分類)</option>
            </select>
        </div>
    </div>

    <div class="section">
        <h2>📝 4. MAIN 主要內容</h2>
        <div class="form-group">
            <label for="mainType">主要網頁類型與元件：</label>
            <select id="mainType">
                <option value="標準官方網站 (首頁 Banner + 服務特點 + 聯絡表單)">標準官方網站</option>
                <option value="部落格/文章清單 (含側邊欄)">部落格/文章清單</option>
                <option value="產品 landing page (著陸頁)">產品 Landing Page</option>
                <option value="純展示型儀表板 (Dashboard)">純展示型儀表板</option>
            </select>
        </div>
        <div class="form-group">
            <label for="galleryStyle">圖庫展示樣式 (Gallery Style)：</label>
            <select id="galleryStyle">
                <option value="無圖庫需求">無圖庫需求</option>
                <option value="瀑布流圖卡 (Masonry Cards with hover effects)">瀑布流圖卡 (Hover 放大效果)</option>
                <option value="輪播投影片 (Slider/Carousel)">輪播投影片 (自動播放與左右箭頭)</option>
                <option value="3x3 標準網格圖卡 (Grid Layout)">3x3 標準網格圖卡 (含標題與描述)</option>
                <option value="燈箱彈出式圖庫 (Lightbox Gallery)">燈箱彈出式圖庫 (點擊放大)</option>
            </select>
        </div>
        <div class="form-group">
            <label for="mainDetail">其他 Main 區塊補充說明：</label>
            <textarea id="mainDetail" rows="3" placeholder="例如：需要一個填寫名字跟 Email 的聯絡表單、圖卡點擊後要能連到外部連結..."></textarea>
        </div>
    </div>

    <div class="section">
        <h2>👣 5. FOOTER 與程式架構建議</h2>
        <div class="form-group">
            <label for="footerContent">Footer 包含內容：</label>
            <input type="text" id="footerContent" value="版權所有 © 2026, 社交平台連結 (FB/IG/GitHub), 隱私權政策">
        </div>
        <div class="form-group">
            <label for="codeStructure">CSS 與 JS 是否分開設計？(架構建議)：</label>
            <select id="codeStructure">
                <option value="完全獨立分開 (index.html, style.css, script.js 獨立檔案)">完全獨立分開 (適合中大型專案)</option>
                <option value="單一 HTML 檔案 (CSS 放 &lt;style&gt;, JS 放 &lt;script&gt; 底部)">單一 HTML 檔案 (適合快速部署/公用電腦開發)</option>
                <option value="CSS 獨立、JS 放在 HTML 底部">CSS 獨立、JS 放在 HTML 底部</option>
            </select>
        </div>
    </div>

    <button onclick="generatePrompt()">🔥 產生前端建構 Prompt</button>

    <div class="output-section">
        <h2>✨ 產生的提示詞 (Prompt)</h2>
        <div id="resultPrompt">點擊上方按鈕後，提示詞會在這裡生成...</div>
        <button class="copy-btn" onclick="copyPrompt()">📋 複製提示詞</button>
    </div>
</div>

<script>
    function generatePrompt() {
        const style = document.getElementById('style').value;
        const primaryColor = document.getElementById('primaryColor').value;
        const headContent = document.getElementById('headContent').value;
        const navContent = document.getElementById('navContent').value;
        const siteLayers = document.getElementById('siteLayers').value;
        const mainType = document.getElementById('mainType').value;
        const galleryStyle = document.getElementById('galleryStyle').value;
        const mainDetail = document.getElementById('mainDetail').value;
        const footerContent = document.getElementById('footerContent').value;
        const codeStructure = document.getElementById('codeStructure').value;

        let prompt = `你現在是一位專業的前端網頁工程師，請幫我寫出一套符合以下規格的網頁程式碼：

### 1. 整體視覺與風格
- **設計風格**：${style}
- **主色調**：${primaryColor}
- **UI/UX 要求**：畫面要現代化、乾淨精緻、元件有適當的 Padding 與邊框陰影、按鈕需有 Hover 動態效果。

### 2. HTML 頁面結構
- **<head> 區塊**：必須包含 ${headContent}。
- **<nav> 導覽列**：包含項目有 [ ${navContent} ]。必須做成響應式導覽列（手機版自動切換為漢堡選單）。
- **網站層級深度**：採用 ${siteLayers}。

### 3. <main> 主要內容區塊
- **網頁核心類型**：${mainType}。
- **圖庫/多媒體展示樣式**：採用「${galleryStyle}」，必須包含精美的圖片佔位符（可使用 unsplash 圖片網址），且視覺樣式需完全符合圖庫設定。
- **補充細節**：${mainDetail ? mainDetail : '無特定補充，請依據風格自由發揮最佳佈局。'}

### 4. <footer> 頁尾區塊
- **頁尾內容**：${footerContent}。

### 5. 檔案與程式架構要求
- **架構方式**：請使用「${codeStructure}」的方式提供。
- **技術棧**：原生 HTML5, CSS3 (可以使用 Flexbox/Grid 佈局), 以及原生 Vanilla JavaScript。
- **其他要求**：請確保程式碼具備良好的 RWD 響應式設計（支援手機、平板、桌面端），程式碼中附上關鍵註解。

請直接輸出完整且可以直接執行的程式碼，不要省略任何區塊。`;

        document.getElementById('resultPrompt').innerText = prompt;
    }

    function copyPrompt() {
        const text = document.getElementById('resultPrompt').innerText;
        navigator.clipboard.writeText(text).then(() => {
            alert('提示詞已複製到剪貼簿！可以拿去貼給 AI 囉！');
        }).catch(err => {
            alert('複製失敗，請手動全選複製。');
        });
    }
</script>

</body>
</html>