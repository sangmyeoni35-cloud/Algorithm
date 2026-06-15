def merge_sort(arr): 
    if len(arr) == 1: # 재귀로 불렀을 때 원소가 하나만 남았다면 반환
        return arr
    mid = len(arr) // 2 # 길이가 짝수든 홀수든 대충 반으로 나눔
    left_arr = arr[:mid] # 그 반을 기준으로 왼쪽 오른쪽 저장
    right_arr = arr[mid:]
    left = merge_sort(left_arr) # 나눈 배열로 다시 재귀
    right = merge_sort(right_arr) # 계속 재귀하다 위 if에 걸린 하나짜리 원소가 저장됨
    return merge(left, right) # 그 2개 원소를 투포인터로 병합
                              # 그 후 다시 처음으로 돌아오면서 left, right는 정렬된 데이터 2, 4, 8 개로 커짐
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right): # 투포인터 방식으로 받은 두 배열 병합
        if left[i] < right[j]:              # 투포인터는 정렬된거만 병합 가능
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:]) # 남았으면 나머지 통째로 넣음
    result.extend(right[j:]) # 재귀하면서 정렬된 데이터가 들어오기 때문에 남은거 통째로 넣어도 됨
    return result

if __name__ == '__main__':
    arr = [12, 43, 42, 132, 5,1, 45, 6,1,3,4,67,2]
    print(merge_sort(arr))