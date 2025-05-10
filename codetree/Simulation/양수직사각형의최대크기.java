import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();
        int result = -1;
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++) {
                for (int ii=i; ii<n; ii++) {
                    for (int jj=j; jj<m; jj++) {
                        boolean allPlus = true;
                        for (int iii=i; iii<=ii; iii++){
                            for (int jjj=j; jjj<=jj; jjj++){
                                if (grid[iii][jjj] <= 0) {
                                    allPlus = false;
                                    break;
                                }
                            }
                        }
                        if (allPlus == true) {
                            int tmp = (jj-j+1) * (ii-i+1);
                            if (tmp > result) {
                                result = tmp;
                            }
                        }
                    }
                }
            }
        }
        System.out.println(result);
    }
}