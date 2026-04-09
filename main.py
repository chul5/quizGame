from game import QuizGame

if __name__ == "__main__":
    game = QuizGame()
    try:
        game.run()
    except Exception as e:
        print(f"\n⚠️  예기치 못한 오류가 발생했습니다: {e}")
    finally:
        game.save()
        print("데이터를 저장하고 종료합니다.")