from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려 원형을 일자형으로 변환
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1  # 투입할 친구 수가 최소가 돼야 하므로 len(dist) + 1로 초기화

    for start in range(length):  # 취약 지점에서 출발
        for friends in list(permutations(dist, len(dist))):  # 친구를 나열하는 모든 경우의 수 각각에 대해서 확인
            count = 1  # 투입할 친구 수
            position = weak[start] + friends[count - 1]  # 도착 위치 = 출발 위치 + 친구의 최대 거리

            for index in range(start, start + length):  # 시작점부터 모든 취약 지점 확인
                if position < weak[index]:  # 친구가 최대 거리를 갔는데도 취약 지점이 있으면 친구 추가
                    count += 1
                    if count > len(dist):  # 더 투입이 불가하면 종료
                        break
                    position = weak[index] + friends[count - 1]  # 새 친구의 도착 위치 초기화
            answer = min(answer, count)  # 최솟값 계산

    if answer > len(dist):
        return -1
    return answer