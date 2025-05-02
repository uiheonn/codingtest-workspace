import java.util.*;
  
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        int count = 0;
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int arrayCount = 1;
            int maxArrayCount = 1;
            for (int j = 0; j < n-1; j++) {
                if (grid[i][j] == grid[i][j+1]) {
                    arrayCount++;
                    if (arrayCount > maxArrayCount) {
                        maxArrayCount = arrayCount;
                    }
                } else {
                    arrayCount = 1;
                }
            }
            // System.out.println("수열의 행복도 : " + maxArrayCount);
            if (m <= maxArrayCount) {
                count++;
            }
        }
        for (int i = 0; i < n; i++) {
            int arrayCount = 1;
            int maxArrayCount = 1;
            for (int j = 0; j < n-1; j++) {
                if (grid[j][i] == grid[j+1][i]) {
                    arrayCount++;
                    if (arrayCount > maxArrayCount) {
                        maxArrayCount = arrayCount;
                    }
                } else {
                    arrayCount = 1;
                }
            }
            // System.out.println("수열의 행복도 : " + maxArrayCount);
            if (m <= maxArrayCount) {
                count++;
            }
        }
        System.out.println(count);
    }
}