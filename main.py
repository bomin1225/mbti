import streamlit as st

# 🛠️ 페이지 설정 (맨 위에 있어야 함!)
st.set_page_config(page_title="MBTI 직업 추천기 💼", page_icon="🌟", layout="centered")

# 🎨 CSS 스타일 추가
st.markdown("""
    <style>
    .title {
        font-size:40px;
        text-align:center;
        color:#FF6F61;
        font-weight:bold;
        margin-top:20px;
        margin-bottom:20px;
    }
    .job-box {
        background-color:#FFF3E0;
        padding:15px;
        border-radius:10px;
        margin-bottom:10px;
        box-shadow: 2px 2px 10px rgba(255, 111, 97, 0.2);
        font-size:18px;
    }
    </style>
""", unsafe_allow_html=True)

# 🎯 제목
st.markdown('<div class="title">✨ MBTI로 찾는 꿈의 직업 ✨</div>', unsafe_allow_html=True)

# 💡 MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
mbti = st.selectbox("👉 당신의 MBTI를 선택하세요:", mbti_list)

# 📌 MBTI별 직업 추천 데이터
job_recommendations = {
    "INTJ": ["👨‍💻 개발자", "📊 데이터 분석가", "📚 연구원"],
    "INTP": ["🧪 과학자", "💻 시스템 설계자", "📈 전략 컨설턴트"],
    "ENTJ": ["💼 CEO", "📣 프로젝트 매니저", "🏦 경영 컨설턴트"],
    "ENTP": ["🧠 전략가", "📢 마케팅 전문가", "💡 창업가"],
    "INFJ": ["🎨 예술가", "📖 작가", "🧘‍♀️ 상담가"],
    "INFP": ["🎨 디자이너", "✍️ 작가", "🎭 예술가"],
    "ENFJ": ["👩‍🏫 교사", "🤝 상담가", "🎤 커뮤니케이터"],
    "ENFP": ["🎬 콘텐츠 크리에이터", "📢 홍보 전문가", "🎨 기획자"],
    "ISTJ": ["📋 행정직", "💼 회계사", "📦 물류 관리자"],
    "ISFJ": ["🧑‍⚕️ 간호사", "🏫 유치원 교사", "🏥 의료 보조"],
    "ESTJ": ["📊 매니저", "🏢 경영 관리자", "⚖️ 공무원"],
    "ESFJ": ["👩‍🏫 교사", "🤝 상담가", "👩‍⚕️ 간호사"],
    "ISTP": ["🔧 엔지니어", "🚘 자동차 정비사", "🔬 기술자"],
    "ISFP": ["🎨 일러스트레이터", "📸 사진작가", "🎶 뮤지션"],
    "ESTP": ["💼 영업 담당자", "🎤 방송인", "🚀 창업가"],
    "ESFP": ["🎤 엔터테이너", "🎬 배우", "🛍️ 스타일리스트"]
}

# 🔍 결과 출력
if mbti:
    st.subheader(f"💡 {mbti} 유형에게 어울리는 직업은?")
    jobs = job_recommendations.get(mbti, ["🤔 아직 정보가 없어요."])
    for job in jobs:
        st.markdown(f'<div class="job-box">{job}</div>', unsafe_allow_html=True)

