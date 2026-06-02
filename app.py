import streamlit as st

# ==========================================
# 1. 執行長專屬網頁設定 (CEO Vibe Settings)
# ==========================================
st.set_page_config(
    page_title="Peter Tsai | 執行長個人特頁",
    page_icon="👔",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 注入尊榮感暗色調與極光藍（Aurora Blue）漸層 CSS
st.markdown("""
    <style>
    /* 全域尊榮深色調背景 */
    .stApp {
        background: radial-gradient(circle at 50% 15%, #0d131a 0%, #05080c 100%);
        color: #f1f5f9;
    }
    
    /* 執行長專屬頂級宣傳標語 */
    .ceo-slogan-box {
        text-align: center;
        padding: 25px;
        margin: 30px 0;
        background: linear-gradient(135deg, rgba(13, 148, 136, 0.15) 0%, rgba(14, 116, 144, 0.15) 100%);
        border: 1px solid rgba(45, 212, 191, 0.2);
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .ceo-slogan-text {
        font-size: 1.5rem !important;
        font-weight: 700;
        letter-spacing: 3px;
        background: linear-gradient(45deg, #2dd4bf, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* 聯絡資訊卡片樣式 */
    .contact-card {
        background: rgba(30, 41, 59, 0.5);
        padding: 15px 20px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 15px;
        transition: transform 0.3s ease;
    }
    
    /* FB 專屬高質感按鈕 */
    .fb-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(45deg, #1877f2, #2575fc);
        color: white !important;
        padding: 12px 28px;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: bold;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(24, 119, 242, 0.4);
        transition: all 0.3s ease;
        margin-top: 10px;
    }
    .fb-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(24, 119, 242, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 領袖主視覺區塊 (Hero Section)
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)
st.title("👨‍💼 Peter Tsai")
st.subheader("執行長 (CEO) | 南台資訊有限公司")

# 宣傳標語 (Slogan)
st.markdown("""
    <div class="ceo-slogan-box">
        <span class="ceo-slogan-text">「 領航數位轉型，構築資訊未來 」</span>
    </div>
""", unsafe_allow_html=True)

st.write(
    "憑藉深厚的資訊科技背景與卓越的戰略眼光，率領團隊走在科技尖端。 "
    "我們不只提供技術，更為企業提供翻轉商業模式的數位解方。"
)

st.markdown("---")

# ==========================================
# 3. 執行長理念與公司願景 (Vision)
# ==========================================
st.header("✨ 經營理念 & 企業願景")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🎯 執行長的話")
    st.write(
        "在瞬息萬變的數位時代，企業的韌性來自於對技術的掌握度。 "
        "我深信『技術因解決痛點而偉大』，南台資訊始終秉持誠信與創新，"
        "做企業最值得信賴的數位決策夥伴。"
    )

with col2:
    st.markdown("### 🏢 關於南台資訊")
    st.info(
        "**南台資訊有限公司** 是南台灣領先的網路資訊服務商。 "
        "我們專注於將最前沿的網頁架構、雲端原生技術與頂級資安防禦，"
        "無縫整合至客戶的商業場景中，全面釋放數據潛能。"
    )

st.markdown("---")

# ==========================================
# 4. 網路資訊公司常見服務項目 (Services)
# ==========================================
st.header("🛠️ 南台資訊 ‧ 頂級核心服務")
st.caption("為企業量身打造的全方位數位兵器庫：")

# 使用 2x2 網格佈局呈現專業服務項目
sc1, sc2 = st.columns(2)

with sc1:
    with st.container(border=True):
        st.markdown("#### 🌐 高階客製化網頁與系統開發")
        st.write("精準對接商業邏輯，打造高併發、極致流暢的 RWD 響應式企業官網與大型核心電商平台。")

    with st.container(border=True):
        st.markdown("#### 🔒 零信任架構資安防護")
        st.write("全面導入企業資安健檢、深度弱點掃描與端點防禦，為商業機密構築滴水不漏的數位防線。")

with sc2:
    with st.container(border=True):
        st.markdown("#### ☁️ 雲端整合與微服務部署")
        st.write("跨足 AWS / Azure 雲端多活架構設計，協助企業將傳統地端系統無痛移轉至高彈性的雲端生態。")

    with st.container(border=True):
        st.markdown("#### 📊 大數據架構與商業智慧 (BI)")
        st.write("建構高效數據中台，透過清洗與深度視覺化分析，協助高層管理團隊從數據中萃取破局關鍵。")

st.markdown("---")

# ==========================================
# 5. 聯絡資訊與社群連結 (Contact & Social)
# ==========================================
st.header("📞 執行長親自對接管道")
st.write("若您有重大商務合作、企業轉型顧問需求，歡迎透過以下方式直接與我聯絡：")

cc1, cc2 = st.columns(2)

with cc1:
    st.markdown("""
        <div class="contact-card">
            <span style="color:#2dd4bf; font-weight:bold;">📧 官方電子郵件</span><br>
            <a href="mailto:chtsai@stust.edu.tw" style="color:#f1f5f9; text-decoration:none;">chtsai@stust.edu.tw</a>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="contact-card">
            <span style="color:#2dd4bf; font-weight:bold;">☎️ 聯絡專線</span><br>
            <a href="tel:06-253-3131" style="color:#f1f5f9; text-decoration:none;">06-253-3131</a>
        </div>
    """, unsafe_allow_html=True)

with cc2:
    st.markdown("### 🌐 社群互動")
    st.write("關注我的 Facebook 帳號，一同交流最新資訊科技趨勢與企業管理心法：")
    # 高質感 FB 聯絡按鈕
    st.markdown("""
        <a href="https://www.facebook.com/keepbusytsai" target="_blank" class="fb-btn">
             追蹤執行長 Facebook
        </a>
    """, unsafe_allow_html=True)

# ==========================================
# 6. 頁尾 (Footer)
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Peter Tsai. All Rights Reserved. Powered by Streamlit & 南台資訊有限公司")