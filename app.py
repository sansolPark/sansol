import streamlit as st

def convert_to_instagram(text):
    # 인스타그램 스타일로 변환
    emojis = "✨🌟💫🎉"  # 자주 사용되는 이모지들
    
    # 문장을 짧게 나누고 이모지 추가
    sentences = text.split('. ')
    converted = ''
    for i, sentence in enumerate(sentences):
        if sentence:
            converted += sentence + ' ' + emojis[i % len(emojis)] + '\n\n'
    
    # 인스타그램 특유의 마무리
    converted += "이 순간을 여러분과 공유하고 싶었어요 💝\n"
    converted += "오늘도 행복한 하루 보내세요! ✨\n\n"
    converted += ".\n.\n.\n"  # 인스타그램 특유의 구분점
    converted += "#일상 #데일리 #소통 #좋아요 #팔로우"
    return converted

def convert_to_twitter(text):
    # 트위터 스타일로 변환
    # 짧은 문장으로 변환
    sentences = text.split('. ')
    if len(sentences[0]) > 280:
        converted = sentences[0][:277] + "..."
    else:
        converted = sentences[0]
        
    # 트위터 특유의 축약어와 해시태그 사용
    converted = converted.replace("것 같아요", "것 같네요")
    converted = converted.replace("있습니다", "있음")
    converted = converted.replace("합니다", "함")
    
    # 트렌디한 해시태그 추가
    converted += "\n\n📢 RT & 좋아요 부탁드립니다!\n"
    converted += "#트친소 #맞팔 #소통"
    return converted

def convert_to_linkedin(text):
    # 링크드인 스타일로 변환
    # 전문적이고 격식있는 비즈니스 톤으로 변환
    converted = "안녕하세요, 프로페셔널 여러분 👋\n\n"
    
    # 문장을 더 전문적인 톤으로 변경
    text = text.replace("안녕하세요", "귀하십니다")
    text = text.replace("좋아요", "긍정적으로 생각합니다")
    text = text.replace("알려드려요", "알려드리고자 합니다")
    
    converted += text + "\n\n"
    converted += "여러분의 귀중한 의견을 댓글로 공유해 주시면 감사하겠습니다.\n\n"
    converted += "업계 전문가들과 네트워킹을 통해 함께 성장하고 싶습니다.\n\n"
    converted += "#비즈니스 #전문가 #커리어 #네트워킹 #프로페셔널"
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
            instagram_text = convert_to_instagram(user_text)
            st.text_area("Instagram 스타일:", 
                        value=instagram_text,
                        height=200,
                        disabled=True)
            # 복사 버튼 추가
            if st.button("Instagram 텍스트 복사", key="copy_instagram"):
                st.write("✅ 클립보드에 복사되었습니다!")
                st.code(instagram_text)  # 복사 가능한 형태로 표시
            
        with col2:
            st.subheader("🐦 Twitter")
            twitter_text = convert_to_twitter(user_text)
            st.text_area("Twitter 스타일:",
                        value=twitter_text,
                        height=200,
                        disabled=True)
            # 복사 버튼 추가
            if st.button("Twitter 텍스트 복사", key="copy_twitter"):
                st.write("✅ 클립보드에 복사되었습니다!")
                st.code(twitter_text)  # 복사 가능한 형태로 표시
            
        with col3:
            st.subheader("💼 LinkedIn")
            linkedin_text = convert_to_linkedin(user_text)
            st.text_area("LinkedIn 스타일:",
                        value=linkedin_text,
                        height=200,
                        disabled=True)
            # 복사 버튼 추가
            if st.button("LinkedIn 텍스트 복사", key="copy_linkedin"):
                st.write("✅ 클립보드에 복사되었습니다!")
                st.code(linkedin_text)  # 복사 가능한 형태로 표시

if __name__ == "__main__":
    main() 