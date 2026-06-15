def BOJ_10814():
    N = int(input())
    members = []

    for _ in range(N): # 회원 수 만큼 반복
        age, name = input().split()
        members.append((int(age), name)) # 나이 이름 입력받고 나이만 정수로 변환
    print() # 입력 출력 보기 편하게 한 줄 내림

    members.sort(key=lambda x: x[0]) # 나이 이름 튜플에서 인덱스 0(나이) 기준으로 정렬
                                        # 파이썬은 기본적으로 입력순서(가입 순서) 기억함
    for age, name in members: # 튜플 리스트이므로 받는 변수도 2개
        print(f"{age} {name}")

if __name__ == '__main__':
    BOJ_10814()