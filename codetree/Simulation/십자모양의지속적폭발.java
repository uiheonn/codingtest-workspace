import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        int[] bombCols = new int[m];
        for (int i = 0; i < m; i++)
            bombCols[i] = sc.nextInt()-1;
        
        for (int col : bombCols){
            // 터질 위치 찾기
            int row = 0;
            while (row < n) {
                if (grid[row][col] != 0)
                    break;
                row++;
            }
            if (row == n)
                continue;
            int bombSize = grid[row][col]-1; // 폭발 규모
            // 폭발 수행하기
            // 1. 하방 폭발
            for (int i=row+1;i<row+1+bombSize;i++) {
                if (i < n)
                    grid[i][col] = 0;
            }
            // 2. 좌측 폭발
            for (int i=col-bombSize;i<col;i++) {
                if (i >= 0)
                    grid[row][i] = 0;
            }
            // 3. 우측 폭발
            for (int i=col+bombSize;i>col;i--) {
                if (i < n)
                    grid[row][i] = 0;
            }
            grid[row][col] = 0;
            // 중력에 따라 재배치
            List<List<Integer>> semi = new ArrayList<>();
            for (int i=0; i<n; i++) {
                List<Integer> tmp = new ArrayList<>();
                for (int j=0; j<n; j++) {
                    if (grid[j][i] != 0)
                        tmp.add(grid[j][i]);
                }
                while (n != tmp.size())
                    tmp.add(0,0);
                semi.add(tmp);
            }
            for (int i=0; i<n; i++) {
                for (int j=0; j<n; j++) {
                    grid[i][j] = semi.get(j).get(i);
                }
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