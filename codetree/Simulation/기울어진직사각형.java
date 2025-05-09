import java.util.*;
public class Main {
    static int max = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        // Please write your code here.
        for (int i=2; i<n; i++){
            for (int j=1; j < n-1; j++){
                dp(i-1,j+1,0,grid[i][j],i,j,n,grid);
            }
        }
        System.out.println(max);
    }
    public static void dp(int x, int y, int direction, int sum, int originX, int originY, int n, int[][] grid) {
        if (x == originX && y == originY) {
            if (sum > max) {
                max = sum;
            }
            // System.out.println("최종 결과 : " + sum);
        }
        if (x < n && x >= 0 && y < n && y >=0) {
            if (direction == 0) { // 같은 방향으로 가기 or 방향 틀기
                dp(x-1,y+1,0,sum+grid[x][y],originX,originY,n,grid);
                dp(x-1,y-1,1,sum+grid[x][y],originX,originY,n,grid);
            } else if (direction == 1) {
                dp(x-1,y-1,1,sum+grid[x][y],originX,originY,n,grid);
                dp(x+1,y-1,2,sum+grid[x][y],originX,originY,n,grid);
            } else if (direction == 2) {
                dp(x+1,y-1,2,sum+grid[x][y],originX,originY,n,grid);
                dp(x+1,y+1,3,sum+grid[x][y],originX,originY,n,grid);
            } else {
                dp(x+1,y+1,3,sum+grid[x][y],originX,originY,n,grid);
            }
        }
    }
}