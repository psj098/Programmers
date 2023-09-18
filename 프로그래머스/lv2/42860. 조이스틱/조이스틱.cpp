#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(string name) {
    int answer = 0, n = name.size();
    int move = n - 1;  // 최대로 움직일 수 있는 거리 (왼쪽으로만 이동하거나, 오른쪽으로만 이동하는 경우)

    for (int i = 0; i < n; ++i) {
        // 위아래 조작 횟수 계산
        answer += min(name[i] - 'A', 'Z' - name[i] + 1);
        
        // 좌우 조작 횟수 계산
        int next = i + 1;
        while (next < n && name[next] == 'A') {
            ++next;
        }
        move = min(move, i + n - next + min(i, n - next));
    }
    answer += move;

    return answer;
}
