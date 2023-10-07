def solution(park, routes):
    # 현재 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j

    # 방향에 따른 이동 정의
    direction = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    for route in routes:
        d, n = route.split()
        dx, dy = direction[d]
        
        # 이동 가능한지 체크
        can_move = True
        temp_x, temp_y = x, y
        for _ in range(int(n)):
            if 0 <= temp_x + dx < len(park) and 0 <= temp_y + dy < len(park[0]) and park[temp_x + dx][temp_y + dy] != 'X':
                temp_x += dx
                temp_y += dy
            else:
                can_move = False
                break

        # 미리 체크한 결과에 따라 실제 이동 수행
        if can_move:
            x, y = temp_x, temp_y

    return [x, y]

