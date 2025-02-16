from sys import argv
import sys
from S import run

dic = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
    "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
    "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26,
    "a": 27, "b": 28, "c": 29, "d": 30, "e": 31, "f": 32, "g": 33, "h": 34, "i": 35,
    "j": 36, "k": 37, "l": 38, "m": 39, "n": 40, "o": 41, "p": 42, "q": 43, "r": 44,
    "s": 45, "t": 46, "u": 47, "v": 48, "w": 49, "x": 50, "y": 51, "z": 52,
    "1": 53, "2": 54, "3": 55, "4": 56, "5": 57, "6": 58, "7": 59, "8": 60, "9": 61, "0": 0,
    "!": -1, "@": -2, "#": -3, "$": -4, "%": -5, "^": -6, "&": -7, "*": -8, "(": -9, ")": -10,
    "-": -11, "_": -12, "+": -13, "=": -14, "`": -15, "~": -16, "[": -17, "]": -18, "{": -19,
    "}": -20, "\\": -21, ";": -22, ":": -23, "'": -24, '"': -25, "<": -26, ">": -27, "/": -28, "?": -29, " ": -100
}

# 딕셔너리 반전
reversed_dic = {str(v): k for k, v in dic.items()}  # 값은 문자열로 변환

def bytecode(src):
    result = []
    for char in src:  # 문자를 하나씩 확인
        if char in dic:  # 딕셔너리에 존재하는지 확인
            result.append(str(dic[char]))  # 정수값을 문자열로 변환하여 추가
            result.append(' ')  # 각 문자 사이에 공백 추가
    return ''.join(result).strip()  # 마지막 공백 제거

def code(src):
    result = []
    src = src.split()  # 공백을 기준으로 분할
    for i in src:
        if i in reversed_dic:  # 반전된 딕셔너리에 존재하는지 확인
            result.append(reversed_dic[i])  # 해당하는 문자 추가
    return "".join(result)

filename = argv[1]

try:
    with open(f"{filename}.sasm", "r") as f:
        text = f.read()
except FileNotFoundError:
    print(f"Dust: File Not Found at {filename}")
    import os
    os.system("pause")
    sys.exit()  # 프로그램 종료

cd = code(text)  # 코드 변환
if cd:  # cd가 비어있지 않을 경우
    if len(cd.split("\n")) > 1:  # 여러 줄인 경우
        for ln in cd.split("\n"):
            run("<stdin>", ln.strip())  # 각 줄을 실행
    else:
        run("<stdin>", cd.strip())  # 단일 줄을 실행
else:
    print("변환된 코드가 없습니다.")  # 변환 결과가 없을 경우
