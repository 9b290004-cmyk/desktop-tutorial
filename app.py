import streamlit as st

# ==========================================
# 1. 網頁基本設定 (The Vibe Settings)
# ==========================================
st.set_page_config(
    page_title="Jia Wen Xie | 專業個人簡歷",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 注入自訂 CSS，打造暗色高質感微光（Glow）與卡片效果
st.markdown("""
    <style>
    /* 全局背景與字體優化 */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #121826 0%, #0b0f17 100%);
        color: #ECF0F1;
    }
    
    /* 宣傳標語容器 */
    .slogan-box {
        text-align: center;
        padding: 20px;
        margin: 25px 0;
        background: linear-gradient(90deg, rgba(0, 123, 245, 0.1), rgba(0, 242, 254, 0.1));
        border-left: 5px solid #007bf5;
        border-radius: 4px;
    }
    .slogan-text {
        font-size: 1.4rem !important;
        font-weight: 600;
        letter-spacing: 2px;
        background: linear-gradient(45deg, #00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* 聯絡資訊特製樣式 */
    .contact-badge {
        background-color: #1a2333;
        padding: 12px 20px;
        border-radius: 8px;
        border: 1px solid #2c3a52;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 頂部主視覺 (Hero Section)
# ==========================================
st.title("💼 Jia Wen Xie")
st.subheader("資管系工讀生 @ 南臺資訊有限公司")

# 宣傳標語 (Slogan)
st.markdown("""
    <div class="slogan-box">
        <span class="slogan-text">「 數據驅動未來，技術創造價值 」</span>
    </div>
""", unsafe_allow_html=True)

st.write("致力於將資訊管理理論轉化為企業實戰力，專注於系統維護、效率優化與技術支援。")

st.markdown("---")

# ==========================================
# 3. 關於我 & 公司簡介 (About Me)
# ==========================================
st.header("✨ 關於我 & 在職單位")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🎯 職涯定位")
    st.write(
        "目前於 **南臺資訊有限公司** 擔任 **資管系工讀生**。 "
        "在工作中協助核心系統日常維運、資訊設備故障排除以及客戶技術問題回饋，"
        "擅長在緊湊的企業節奏中保持細心，是團隊中最堅實的後勤技術尖兵。"
    )

with col2:
    st.markdown("### 🏢 公司概況")
    st.info(
        "**南臺資訊有限公司** 為具備前瞻性的網路資訊服務商，"
        "旨在協助傳統企業跨越數位鴻溝，透過客製化軟體與雲端技術，"
        "為客戶打造高效、安全、且具備擴充性的數位生態系。"
    )

st.markdown("---")

# ==========================================
# 4. 網路資訊公司常見服務項目 (Services)
# ==========================================
st.header("🛠️ 網路資訊公司 ‧ 核心服務項目")
st.caption("南臺資訊全面驅動企業數位轉型的四把利刃：")

# 使用 2x2 網格佈局呈現專業服務
sc1, sc2 = st.columns(2)

with sc1:
    with st.container(border=True):
        st.markdown("#### 🌐 客製化軟體與網頁開發")
        st.write("根據企業需求量身打造高安全性官網、電商系統及 RWD 響應式網頁，流暢應對高併發流量。")

    with st.container(border=True):
        st.markdown("#### 🔒 資安防護與網絡資訊安全")
        st.write("提供全方位的系統弱點掃描、伺服器防火牆部署與資安健檢，建立滴水不漏的數位資產防線。")

with sc2:
    with st.container(border=True):
        st.markdown("#### ☁️ 雲端架構部署與整合")
        st.write("協助企業導入 AWS / Azure 雲端環境，提供地端轉雲端的系統移轉與微服務架構優化服務。")

    with st.container(border=True):
        st.markdown("#### 📊 大數據分析與智慧決策")
        st.write("清洗海量業務數據，透過視覺化報表與商業智慧（BI）工具，協助企業精準發掘潛在商機。")

st.markdown("---")

# ==========================================
# 5. 聯絡資訊區塊 (Contact)
# ==========================================
st.header("📞 聯絡資訊")
st.write("歡迎隨時與我聯繫，洽談技術合作或業務諮詢：")

cc1, cc2 = st.columns(2)

with cc1:
    st.markdown(f"""
        <div class="contact-badge">
            <span style="color:#00f2fe; font-weight:bold;">📧 電子郵件</span><br>
            <a href="mailto:9B290004@stust.edu.tw" style="color:#ECF0F1; text-decoration:none;">9B290004@stust.edu.tw</a>
        </div>
    """, unsafe_allow_html=True)

with cc2:
    st.markdown(f"""
        <div class="contact-badge">
            <span style="color:#00f2fe; font-weight:bold;">☎️ 聯絡電話</span><br>
            <a href="tel:06-253-3131,4301" style="color:#ECF0F1; text-decoration:none;">06-253-3131 #4301</a>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 6. 頁尾 (Footer)
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Jia Wen Xie. Powered by Streamlit & 南臺資訊有限公司")