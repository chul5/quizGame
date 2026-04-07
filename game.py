from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load()
    
    def _get_default_quizzes(self):
        return [
            Quiz(
                question="세계에서 가장 넓은 나라는?",
                choices=["미국", "중국", "러시아", "캐나다"],
                answer=3
            ),
            Quiz(
                question="나일강이 흐르는 대륙은?",
                choices=["아시아", "아프리카", "남아메리카", "유럽"],
                answer=2
            ),
            Quiz(
                question="세계에서 가장 높은 산은?",
                choices=["K2", "에베레스트", "킬리만자로", "몽블랑"],
                answer=2
            ),
            Quiz(
                question="일본의 수도는?",
                choices=["오사카", "교토", "도쿄", "나고야"],
                answer=3
            ),
            Quiz(
                question="세계에서 인구가 가장 많은 나라는? (2024년 기준)",
                choices=["중국", "인도", "미국", "인도네시아"],
                answer=2
            ),
        ]
    
    def load(self):
        self.quizzes = self._get_default_quizzes()

    def show_menu(self):
        print("\n========================================")
        print("        🌍 세계 상식 퀴즈 게임 🌍")
        print("========================================")
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 종료")
        print("========================================")

    def run(self):
        while True:
            self.show_menu()

            try:
                choice = input("choice: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\nProgram EXIT")
                break

            if choice == "":
                print("⚠️  입력이 없습니다. 1-5 사이의 숫자를 입력하세요.")
                continue
            elif not choice.isdigit():
                print("⚠️  잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue
            
            choice = int(choice)

            if choice == 1:
                pass    # Step 7에서 구현
            elif choice == 2:
                pass    # Step 8에서 구현
            elif choice == 3:
                pass    # Step 9에서 구현
            elif choice == 4:
                pass    # Step 10에서 구현
            elif choice == 5:
                print("\n프로그램을 종료합니다. 👋")
                break
            else:
                print("⚠️  잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
    