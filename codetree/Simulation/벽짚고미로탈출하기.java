import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int y = sc.nextInt();
        char[][] maze = new char[n][n];
        for (int i = 0; i < n; i++) {
            String line = sc.next();
            for (int j = 0; j < n; j++) {
                maze[i][j] = line.charAt(j);
            }
        }
        // 시작은 -> 방향
        // direction으로 공의 방향을 설정하고 해당 방향의 우측을 항상 체크
        int[] dx = new int[] {0,1,0,-1};
        int[] dy = new int[] {1,0,-1,0};
        int row = x-1;
        int col = y-1;
        int direction = 0;
        int count = 0;
        while (true) {
            if (count > 1000000) {
                count = -1;
                break;
            }
            if (row >= n || row < 0 || col >= n || col < 0) {
                break;
            }
            // 1. 앞이 막혀있는 경우 -> 경로 찾기
            // 2. 우측에 벽이 없는 경우 -> 아래로 이동
            // 3. else -> 일반적인 이동
            int nextX = row + dx[direction];
            int nextY = col + dy[direction];
            int rightX = row + dx[(direction+1) % 4];
            int rightY = col + dy[(direction+1) % 4];

            if (rightX < n && rightX >= 0 & rightY < n && rightY >= 0 && maze[rightX][rightY] != '#') {
                // direction 변경
                direction = (direction+1) % 4;
            }
            else if (nextX < n && nextX >= 0 && nextY < n && nextY >= 0 && maze[nextX][nextY] == '#') {
                direction = (direction + 3) % 4;
                int semiX = row + dx[direction];
                int semiY = col + dy[direction];
                if (semiX < n && semiX >= 0 && semiY < n && semiY >= 0 && maze[semiX][semiY] == '#') {
                    direction = (direction + 3) % 4;
                }
                int lastX = row + dx[direction];
                int lastY = col + dy[direction];
                if (lastX < n && lastX >= 0 && lastY < n && lastY >= 0 && maze[lastX][lastY] == '#') {
                    count = -1;
                    break;
                }
            }
            // 이동
            row += dx[direction];
            col += dy[direction];
            count++;
            // System.out.println(count + "번째 위치는 : " + row + "행 " + col + "열입니다");
        }
        System.out.println(count);
    }
}