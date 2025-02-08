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
    ---""",
]


class HangmanGame:
    def __init__(self):
        self.random_number = random.randrange(0, len(words))
        self.word_pick = words[self.random_number]
        self.emp_string = '_' * len(self.word_pick)

    def display(self, display_num, string_line):
        # return print(hangman_pics[display_num])
        # for hangman in hangman_pics:
        #     yield print(hangman)
        print(hangman_pics[display_num])
        print(string_line)


    def play(self):
        # self.display(0)
        # hangman_count = self.display()
        # print(next(hangman_count))
        # print(self.emp_string)
        word_pick = self.word_pick
        print(word_pick)
        emp_string = list(self.emp_string)
        self.display(0, self.emp_string)
        count_num = 0

        while True:
            input_string = input("알파벳 입력 (종료: exit)\n>  ")

            try:
                # 단어가 들어 있다면
                if input_string in word_pick:
                    # 해당 단어가 중복이 있다면
                    if input_string.count() > 1:
                        for char in input_string:
                            pass


                    else:
                        index = word_pick.index(input_string)
                        emp_string[index] = input_string
                        self.display(count_num, ''.join(emp_string))
                else:
                    count_num += 1
                    self.display(count_num, ''.join(emp_string))

            except StopIteration:
                print("게임 오버!!")
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
