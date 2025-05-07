import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        List<List<Integer>> lst = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++) {
                int square = 0;
                // i행 j열부터 직사각형을 만든다
                for (int ii=i; ii<n; ii++){
                    for (int jj=j; jj<m; jj++){
                        int sum = calculate(i,j,ii,jj,grid);
                        // System.out.println(i + "행 " + j + "열부터 " + ii + "행 " + jj + "열까지의 합 : " + sum);
                        // int[] semi = new int[] {sum,i,j,ii,jj};
                        List<Integer> semi = new ArrayList<>(Arrays.asList(sum,i,j,ii,jj));
                        lst.add(semi);
                    }
                }
            }
        }
        // System.out.println(lst);
        int result = -1000000000;
        for (int i=0; i < lst.size(); i++) {
            List<Integer> tmp = lst.get(i);
            for (int j=i+1; j < lst.size(); j++) {
                List<Integer> res = lst.get(j);
                // tmp와 res이 겹치는 부분이 있는지 확인
                if (tmp.get(3) >= res.get(1) && tmp.get(4) >= res.get(2)) {
                    continue;
                } else {
                    if (tmp.get(0) + res.get(0) > result) {
                        result = tmp.get(0) + res.get(0);
                    }
                }
            }
        }
        System.out.println(result);
    }
    public static int calculate(int startX, int startY, int endX, int endY, int[][] grid){
        int sum = 0;
        for (int i=startX; i<endX+1; i++){
            for (int j=startY; j<endY+1; j++){
                sum+=grid[i][j];
            }
        }
        return sum;
    }
}