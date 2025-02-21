import streamlit as st
from converters import SocialMediaConverter

# 페이지 설정을 추가
st.set_page_config(
    page_title="소셜 미디어 텍스트 변환기",
    page_icon="✨",
    layout="wide"
)

def create_social_media_section(col, platform, icon, text, convert_func):
    """소셜 미디어 섹션 UI 생성"""
    with col:
        st.subheader(f"{icon} {platform}")
        converted_text = convert_func(text)
        st.text_area(
            f"{platform} 스타일:",
            value=converted_text,
            height=200,
            disabled=True
        )
        if st.button(f"{platform} 텍스트 복사", key=f"copy_{platform.lower()}"):
            st.write("✅ 클립보드에 복사되었습니다!")
            st.code(converted_text)

def handle_enter():
    """Enter 키 입력 처리"""
    if '\n' in st.session_state.temp_input:
        st.session_state.user_input = st.session_state.temp_input.strip()

def main():
    try:
        st.title("소셜 미디어 텍스트 변환기 ✨")
        
        # 상태 초기화
        for state in ['temp_input', 'user_input']:
            if state not in st.session_state:
                st.session_state[state] = ''
        
        # 텍스트 입력
        user_text = st.text_area(
            "변환할 텍스트를 입력하세요:",
            height=150,
            key='temp_input',
            on_change=handle_enter
        )
        
        display_text = st.session_state.user_input or user_text
        
        if display_text:
            # 플랫폼 설정
            platforms = [
                ("Instagram", "📸", SocialMediaConverter.instagram),
                ("Twitter", "🐦", SocialMediaConverter.twitter),
                ("LinkedIn", "💼", SocialMediaConverter.linkedin)
            ]
            
            # 컬럼 생성
            cols = st.columns(len(platforms))
            
            # 각 플랫폼 섹션 생성
            for col, (platform, icon, convert_func) in zip(cols, platforms):
                create_social_media_section(col, platform, icon, display_text, convert_func)
                
    except Exception as e:
        st.error(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main() 