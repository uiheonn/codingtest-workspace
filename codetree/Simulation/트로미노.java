import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        int max = 0;
        // ArrayList<ArrayList<ArrayList<Integer>>> L_tromino = new ArrayList<>();
        List<List<List<Integer>>> L_tromino = new ArrayList<>(
            Arrays.asList(
                Arrays.asList(
                    Arrays.asList(0, 0),
                    Arrays.asList(1, 0),
                    Arrays.asList(1, 1)
                ),
                Arrays.asList(
                    Arrays.asList(0, 0),
                    Arrays.asList(0, 1),
                    Arrays.asList(1, 1)
                ),
                Arrays.asList(
                    Arrays.asList(0, 1),
                    Arrays.asList(1, 0),
                    Arrays.asList(1, 1)
                ),
                Arrays.asList(
                    Arrays.asList(0, 0),
                    Arrays.asList(0, 1),
                    Arrays.asList(1, 0)
                )
            )
        );
        for (List<List<Integer>> ele : L_tromino) {
            // System.out.println("트로미노 : " + ele);
            for (int i=0; i < n-1; i++){
                for (int j=0; j < m-1; j++){
                    int sum = 0;
                    for (List<Integer> location : ele) {
                        int x = i + location.get(0);
                        int y = j + location.get(1);
                        sum += grid[x][y];
                    }
                    if (sum > max) {
                        max = sum;
                    }
                    // System.out.println("ㄱ자 트로미노의 합 : " + sum);
                }
            }
        }
        List<List<List<Integer>>> l_tromino = new ArrayList<>(
            Arrays.asList(
                Arrays.asList(
                    Arrays.asList(0, 0),
                    Arrays.asList(1, 0),
                    Arrays.asList(2, 0)
                )
            )
        );
        for (List<List<Integer>> ele : l_tromino) {
            for (int i=0; i < n-2; i++){
                for (int j=0; j < m; j++){
                    int sum = 0;
                    for (List<Integer> location : ele) {
                        int x = i + location.get(0);
                        int y = j + location.get(1);
                        sum += grid[x][y];
                    }
                    if (sum > max) {
                        max = sum;
                    }
                    // System.out.println("l자 트로미노의 합 : " + sum);
                }
            }
        }
        List<List<List<Integer>>> b_tromino = new ArrayList<>(
            Arrays.asList(
                Arrays.asList(
                    Arrays.asList(0, 0),
                    Arrays.asList(0, 1),
                    Arrays.asList(0, 2)
                )
            )
        );
        for (List<List<Integer>> ele : b_tromino) {
            for (int i=0; i < n; i++){
                for (int j=0; j < m-2; j++){
                    int sum = 0;
                    for (List<Integer> location : ele) {
                        int x = i + location.get(0);
                        int y = j + location.get(1);
                        sum += grid[x][y];
                    }
                    if (sum > max) {
                        max = sum;
                    }
                    // System.out.println("ㅡ자 트로미노의 합 : " + sum);
                }
            }
        }
        System.out.println(max);
    }
}