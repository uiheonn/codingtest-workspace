import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        int r = sc.nextInt()-1;
        int c = sc.nextInt()-1;
        int m1 = sc.nextInt();
        int m2 = sc.nextInt();
        int m3 = sc.nextInt();
        int m4 = sc.nextInt();
        int dir = sc.nextInt();
        int origin = grid[r][c];
        // 우측 이동
        // System.out.println("현재 위치는 " + r + "행 " + c + "열 입니다");
        // print(grid);
        if (dir == 0) {
            for (int i=0;i<m1;i++) {
                int tmp = grid[r-1][c+1];
                grid[r-1][c+1] = origin;
                origin = tmp;
                r--;
                c++;
            }
            // System.out.println("우측 이동 후 위치는 " + r + "행 " + c + "열 입니다");
            // print(grid);
            // 위로 이동
            for (int i=0; i<m2; i++) {
                int tmp = grid[r-1][c-1];
                grid[r-1][c-1] = origin;
                origin = tmp;
                r--;
                c--;
            }
            // System.out.println("위로 이동 후 위치는 " + r + "행 " + c + "열 입니다");
            // print(grid);
            // 좌측 이동
            for (int i=0; i<m3; i++) {
                int tmp = grid[r+1][c-1];
                grid[r+1][c-1] = origin;
                origin = tmp;
                r++;
                c--;
            }
            // System.out.println("좌측 이동 후 위치는 " + r + "행 " + c + "열 입니다");
            // print(grid);
            // 아래로 이동
            for (int i=0; i<m4; i++) {
                int tmp = grid[r+1][c+1];
                grid[r+1][c+1] = origin;
                origin = tmp;
                r++;
                c++;
            }
            // System.out.println("아래 이동 후 위치는 " + r + "행 " + c + "열 입니다");
            // print(grid);
        } else {
            // 좌측 이동
            for (int i=0; i<m4; i++) {
                int tmp = grid[r-1][c-1];
                grid[r-1][c-1] = origin;
                origin = tmp;
                r--;
                c--;
            }
            // 위로 이동
            for (int i=0; i<m3; i++) {
                int tmp = grid[r-1][c+1];
                grid[r-1][c+1] = origin;
                origin = tmp;
                r--;
                c++;
            }
            // 우측 이동
            for (int i=0; i<m2; i++) {
                int tmp = grid[r+1][c+1];
                grid[r+1][c+1] = origin;
                origin = tmp;
                r++;
                c++;
            }
            // 아래로 이동
            for (int i=0; i<m1; i++) {
                int tmp = grid[r+1][c-1];
                grid[r+1][c-1] = origin;
                origin = tmp;
                r++;
                c--;
            }
        }
        print(grid);
    }
    public static void print(int[][] grid) {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }
}