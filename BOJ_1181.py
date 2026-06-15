def BOJ_1181():
    N = int(input())
    string = []

    for _ in range(N):
        s = input()
        string.append(s)
    print()
    
    string = list(set(string)) # set() > 집합은 중복 자동으로 제거해줌
    string.sort(key=lambda x: (len(x), x)) # 문자열(string의 값 x)의 길이를 기준, 같으면 x(사전순)
     # 기본적으로 사전순이라 안적어도( sort() )되지만 앞에 길이를 기준으로 잡았기 때문에 한 번 더 써줘야함
    for s in string:
        print(f'{s}')

if __name__ == '__main__':
    BOJ_1181()