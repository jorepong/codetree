#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> pii;

const int INF = 1e9;
int n;
int grid[100][100];
int dp[101][101]; // dp[i][j] : (i, j)까지 갔을 때의 최소 합
int dx[] = {1, 0};
int dy[] = {0, -1};
queue<pii> q;

bool isin(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < n;
}

void bfs() {
    q.push({0, n - 1});
    dp[0][n - 1] = grid[0][n - 1];

    while (!q.empty()) {
        pii cur = q.front();
        int x = cur.first;
        int y = cur.second;
        q.pop();

        for (int i = 0; i < 2; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (isin(nx, ny)) {
                //cout << "Debug: " << x << " " << y << " " << nx << " " << ny << "\n";
                q.push({nx, ny});
                dp[nx][ny] = min(dp[nx][ny], dp[x][y] + grid[nx][ny]);
            }
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dp[i][j] = INF;
        }
    }

    bfs();
    cout << dp[n - 1][0] << "\n";

    return 0;
}
