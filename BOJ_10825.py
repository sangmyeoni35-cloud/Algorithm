def BOJ_10825():
    N = int(input())
    students = []

    for _ in range(N):
        student, korean, english, math = input().split()
        students.append((student, int(korean), int(english), int(math))) # 이름은 문자열, 나머진 정수
    print()

    students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0] )) # 인덱스 1번(국어) 내림, 영어 오름, 수학 내림, 이름 사전

    for student in students:
        print(f'{student[0]}') # 이름만 출력

if __name__ == '__main__':
    BOJ_10825()