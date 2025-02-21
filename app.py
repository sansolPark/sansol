import streamlit as st

def convert_to_instagram(text):
    # 인스타그램 스타일로 변환
    converted = text + "\n\n"
    converted += "."*3 + "\n"  # ... 추가
    converted += "#content #instagram #social"  # 해시태그 추가
    return converted

def convert_to_twitter(text):
    # 트위터 스타일로 변환
    if len(text) > 280:
        text = text[:277] + "..."
    return text

def convert_to_linkedin(text):
    # 링크드인 스타일로 변환
    converted = "💼 " + text + "\n\n"  # 비즈니스 이모지 추가
    converted += "What are your thoughts on this?\n"
    converted += "#professional #business #networking"
    return converted

def main():
    st.title("소셜 미디어 텍스트 변환기 ✨")
    
    # 입력 텍스트 영역
    user_text = st.text_area("변환할 텍스트를 입력하세요:", height=150)
    
    if user_text:
        # 세 개의 컬럼으로 출력 구성
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("📸 Instagram")
            st.text_area("Instagram 스타일:", 
                        value=convert_to_instagram(user_text),
                        height=200,
                        disabled=True)
            
        with col2:
            st.subheader("🐦 Twitter")
            st.text_area("Twitter 스타일:",
                        value=convert_to_twitter(user_text),
                        height=200,
                        disabled=True)
            
        with col3:
            st.subheader("💼 LinkedIn")
            st.text_area("LinkedIn 스타일:",
                        value=convert_to_linkedin(user_text),
                        height=200,
                        disabled=True)

if __name__ == "__main__":
    main() 