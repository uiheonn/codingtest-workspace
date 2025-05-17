import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt()-1;
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        // 테트리스의 가장 먼저 닿는 row를 찾는다
        int[] tetrice = new int[m]; // 테트리스의 열 번호
        for (int i=0; i<m; i++) {
            tetrice[i] = k + i;
        }
        int minRow = n-1;
        for (int col : tetrice) {
            for (int i=0; i<n; i++) {
                if (grid[i][col] != 0) {
                    int tmp = i-1;
                    if (tmp < minRow) {
                        minRow = tmp;
                    }
                }
            }
        }
        // System.out.println("쌓아야 하는 row : " + minRow);
        if (minRow != -1) {
            for (int i=0; i<m; i++) {
                grid[minRow][k+i] = 1;
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }
}