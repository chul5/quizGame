import json
import os
from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = None
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
        if not os.path.exists("state.json"):
            self.quizzes = self._get_default_quizzes()
            print("state.json을 찾을 수 없습니다. 기본데이터를 불러옵니다.")
            return
        
        try:
            with open("state.json", "r", encoding="utf-8") as f:
                data = json.load(f)

                self.quizzes = [
                    Quiz(q["question"], q["choices"], q["answer"])
                    for q in data["quizzes"]
                ]
                self.best_score = data["best_score"]
                print(f" 저장된 데이터를 불러왔습니다. Quiz {len(self.quizzes)}개, 최고점수 {self.best_score}")
        except (json.JSONDecodeError, KeyError):
            print("저장 파일이 손상되었습니다. 기본데이터를 불러옵니다.")
            self.quizzes = self._get_default_quizzes()
            self.best_score = None

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
                self.play()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_list()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("\n프로그램을 종료합니다. 👋")
                break
            else:
                print("⚠️  잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
    
    def _get_number_input(self, prompt, min_val, max_val):
        while True:
            try:
                value = input(prompt).strip()
            except (KeyboardInterrupt, EOFError):
                # print("\n\n입력을 중단합니다.")
                return None

            if value == "":
                print(f"⚠️  입력이 없습니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
                continue
            elif not value.isdigit():
                print(f"⚠️  잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
                continue

            value = int(value)

            if value < min_val or value > max_val:
                print(f"⚠️  {min_val}-{max_val} 사이의 숫자를 입력하세요.")
                continue

            return value
        
    def play(self):
        if not self.quizzes:
            print("\n⚠️  등록된 퀴즈가 없습니다.")
            return

        total = len(self.quizzes)
        score = 0

        print(f"\n START QUIZ! (TOTAL:{total})")
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"\n----------------------------------------")
            print(f"[QUIZ {i}]")
            quiz.display()

            user_answer = self._get_number_input("Write Answer: ", 1, 4)
            if user_answer is None:
                print("\n퀴즈를 중단합니다.")
                return
            
            if quiz.check(user_answer):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번이에요.")
            
        percent = int(score / total * 100)
        print(f"\n========================================")
        print(f"🏆 결과: {total}문제 중 {score}문제 정답! ({percent}점)")

        if self.best_score is None or percent > self.best_score:
            self.best_score = percent
            print(f"🎉 새로운 최고 점수입니다!")
            self.save()
        print(f"========================================")

    def add_quiz(self):
        print("\n 새로운 퀴즈를 추가합니다.")

        try:
            question = input("문제를 입력하세요: ").strip()
        except(KeyboardInterrupt, EOFError):
            print("\n\n프로그램을 종료합니다.")
            return None
        
        if question == "":
            print("⚠️ 문제를 입력해야합니다.")
            return
        
        choices = []
        for i in range(1, 5):
            try:
                choice = input(f"선택지 {i}: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\n프로그램을 종료합니다.")
                return None

            if choice == "":
                print("⚠️ 선택지를 입력해야 합니다.")
                return
            choices.append(choice)
        
        answer = self._get_number_input("정답 번호 (1-4): ", 1, 4)
        if answer is None:
            return
        
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save()

        print("✅ QUIZ가 추가되었습니다.")

    def save(self):
        data = {
            "quizzes" : [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        try:
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"⚠️ 저장 중 오류 발생: {e}")

    def show_list(self):
        if not self.quizzes:
            print("\nThere are no quizzes")
            return
        
        print("----------------------------------------")
        print(f"\n 등록된 퀴즈 목록 총 {len(self.quizzes)}개")

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"[{i}] {quiz.question}")
        print("----------------------------------------")

    def show_score(self):
        if self.best_score is None:
            print("\n아직 퀴즈를 풀지 않았습니다.")
            return
        print(f"\n🏆 최고 점수: {self.best_score}점")

