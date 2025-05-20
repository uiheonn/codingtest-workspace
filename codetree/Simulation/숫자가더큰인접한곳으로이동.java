import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] grid = new int[n+1][n+1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        int[] dx = new int[] {-1,1,0,0};
        int[] dy = new int[] {0,0,-1,1};
        boolean[][] visited = new boolean[n+1][n+1];
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                visited[i][j] = false;
            }
        }
        while(true) {
            // visited 업데이트
            visited[r][c] = true;
            System.out.print(grid[r][c] + " ");
            // 근접한 데이터 중 큰 거 찾기
            boolean[] location = new boolean[] {false,false,false,false}; // 상,하,좌,우
            for (int i=0; i<4; i++) {
                int nx = r + dx[i];
                int ny = c + dy[i];
                if (nx >= 1 && nx <= n && ny >= 1 && ny <= n && grid[r][c] < grid[nx][ny]) {
                    location[i] = true;
                }
            }
            // 우선순위에 맞춰 이동하기
            int index = find(location);
            if (index == 4) {
                break;
            } else {
                r = r + dx[index];
                c = c + dy[index];
            }
        }
    }
    public static int find(boolean[] location) {
        int count = 0;
        for (int i=0; i<4; i++) {
            if (location[i] == true)
                break;
            count++;
        }
        return count;
    }
}