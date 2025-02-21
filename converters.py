class SocialMediaConverter:
    @staticmethod
    def instagram(text):
        emojis = "✨🌟💫🎉"
        converted = ''
        
        for i, sentence in enumerate(text.split('.')):
            if sentence.strip():
                converted += f"{sentence.strip()} {emojis[i % len(emojis)]}\n\n"
        
        return (f"{converted}"
                "이 순간을 여러분과 공유하고 싶었어요 💝\n"
                "오늘도 행복한 하루 보내세요! ✨\n\n"
                ".\n.\n.\n"
                "#일상 #데일리 #소통 #좋아요 #팔로우")

    @staticmethod
    def twitter(text):
        first_sentence = text.split('.')[0].strip()
        converted = first_sentence[:277] + "..." if len(first_sentence) > 280 else first_sentence
        
        replacements = {
            "것 같아요": "것 같네요",
            "있습니다": "있음",
            "합니다": "함"
        }
        for old, new in replacements.items():
            converted = converted.replace(old, new)
        
        return (f"{converted}\n\n"
                "📢 RT & 좋아요 부탁드립니다!\n"
                "#트친소 #맞팔 #소통")

    @staticmethod
    def linkedin(text):
        replacements = {
            "안녕하세요": "귀하십니다",
            "좋아요": "긍정적으로 생각합니다",
            "알려드려요": "알려드리고자 합니다"
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return (f"안녕하세요, 프로페셔널 여러분 👋\n\n"
                f"{text}\n\n"
                "여러분의 귀중한 의견을 댓글로 공유해 주시면 감사하겠습니다.\n\n"
                "업계 전문가들과 네트워킹을 통해 함께 성장하고 싶습니다.\n\n"
                "#비즈니스 #전문가 #커리어 #네트워킹 #프로페셔널") 