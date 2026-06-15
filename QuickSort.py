def quick_sort(arr):
    if len(arr) == 1: # 하나면 그대로 반환
        return arr
    pivot = arr[0] # 맨 왼쪽거를 피벗으로 정함
    the_rest = arr[1:] # 나머지 저장
    left = [x for x in the_rest if x <= pivot] # 나머지 중에서 피벗보다 작은, 큰거 저장
    right = [x for x in the_rest if x > pivot] # 재귀하다보면 조금씩 정렬됨
    return quick_sort(left) + [pivot] + quick_sort(right) # 피벗을 가운데 넣기 때문, 피벗도 배열로 다시 감싸줌, 빈배열은 추가 안됨