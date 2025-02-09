# 기본 라이브러리라 파이썬 설치시 자동으로 설치됩니다!
# random 모듈은 랜덤한 숫자를 생성할 때 사용합니다.
import random
from itertools import count

# 게임에 사용될 단어 목록
words = ["apple", "banana", "orange", "grape", "lemon"]

# 행맨 그림
hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---"""
]
game_over = """
     ------
     |    |
     |    
     |    
     |    \O/
     |     /
    ---  / |
    GAME OVER
"""
print(game_over)

class HangmanGame:
    def __init__(self):
        # 단어를 고르기 위해 랜덤으로 숫자를 할당한다.
        self.random_number = random.randrange(0, len(words))
        # 할당된 숫자를 가지고 words에서 값을 가져온다.
        self.word_pick = words[self.random_number]
        # 선택된 단어 길이에 맞게 '_' 를 출력한다.
        self.emp_string = '_' * len(self.word_pick)

    def display(self, display_num, string_line):
        # return print(hangman_pics[display_num])
        # for hangman in hangman_pics:
        #     yield print(hangman)
        print(hangman_pics[display_num])
        print(string_line)


    def play(self):
        word_pick = self.word_pick
        # 테스트를 위한 선택된 단어를 보여줍니다.
        print(word_pick)
        # str 인덱스로 값을 바꿀수 없기때문에 인덱스로 문자를 바꾸기 위한 리스트로 선언
        emp_string = list(self.emp_string)
        self.display(0, self.emp_string)
        # 단어에 해당 문자가 없을때 카운트가 1개씩 올라간다.
        count_num = 0

        while True:
            input_string = input("알파벳 입력 (종료: exit)\n>  ")

            try:
                # 단어가 들어 있다면
                if input_string in word_pick:
                    # 해당 단어가 중복이 있다면
                    if word_pick.count(input_string) > 1:
                        for i, char in enumerate(word_pick):
                            if input_string == char:
                                emp_string[i] = input_string
                        self.display(count_num, ''.join(emp_string))



                    else:
                        # 중복 문자가 없을 경우
                        index = word_pick.index(input_string)
                        emp_string[index] = input_string
                        self.display(count_num, ''.join(emp_string))
                else:
                    # 문자가 하나도 안들어 있을때
                    count_num += 1
                    self.display(count_num, ''.join(emp_string))

            except IndexError:
                print(game_over)
                print("게임을 종료 합니다.")
                break
            finally:
                if not '_' in emp_string:
                    print("게임 승리!!")
                    break


            if 'exit' in input_string:
                break



if __name__ == "__main__":
    game = HangmanGame()
    game.play()


# line_string = list("_____")
#
# line_string[0] = 'a'
# print(''.join(line_string))

# print(hangman_pics[6])
# # words = ["apple", "banana", "orange", "grape", "lemon"]
# print(words[random.randrange(0, len(words))])

# words 리스트에 추가된 단어들을 사용해주세요
#   words = ["apple", "banana", "orange", "grape", "lemon"]
# 단어의 길이에 맞게 밑줄을 출력해주세요
# (예)banana의 경우 _ _ _ _ _ _
# 사용자부터 1글자씩 입력을 받되,
#   단어에 입력값이 포함되면 "단어를 맞추셨군요. 더 힘내봐요"라고 출력해주세요"
#   단어에 입력값이 포함되어 있지 않다면 "틀렸습니다. 남은 시도 횟수 "란 메시지와 함꼐 남은 횟수를 출력해주세요
# 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시(맞히면 글자는 밑줄 출력)

# 예) a 입력 시 : a _ _ _ _
