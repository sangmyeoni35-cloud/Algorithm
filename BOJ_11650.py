def BOJ_11650():
    coordinates = [] # 좌표
    N = int(input())

    for _ in range(N):
        x, y = map(int, input().split()) # 둘 다 정수로 좌표 입력
        coordinates.append((x, y)) # 튜플로 리스트에 추가
    print()
    coordinates.sort(key=lambda x : (x[0],  x[1])) # x[0] > x좌표 기준 정렬, 같으면 x[1] > y좌표 기준 정렬
    for x, y in coordinates:                       # 기본적으로 오름차순, 내림은 -x[0], -x[1] 같이 - 붙이면 됨
        print(f'{x} {y}')

if __name__ == '__main__':
    BOJ_11650()