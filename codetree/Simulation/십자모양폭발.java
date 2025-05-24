import java.util.*;

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
        // 폭발 수행
        int size = grid[r][c];
        int bombSize = size-1;
        int startRow = c - bombSize;
        for (int i=startRow; i<startRow+2*bombSize+1; i++) {
            if (i >= 0 && i < n)
                grid[r][i] = 0;
        }
        int startCol = r - bombSize;
        for (int i=startCol; i<startCol+2*bombSize+1; i++) {
            if (i >= 0 && i < n)
                grid[i][c] = 0;
        }
        // 중력으로 인한 값 변동
        List<List<Integer>> result = new ArrayList<>();
        for (int i=0; i<n; i++) {
            List<Integer> tmp = new ArrayList<>();
            for (int j=0; j<n; j++){
                if (grid[j][i] != 0) {
                    tmp.add(grid[j][i]);
                }
            }
            int tmpSize = tmp.size();
            for (int k=0; k<n-tmpSize; k++) {
                tmp.add(0,0);
            }
            result.add(tmp);
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                System.out.print(result.get(j).get(i) + " ");
            }
            System.out.println();
        }
    }
}