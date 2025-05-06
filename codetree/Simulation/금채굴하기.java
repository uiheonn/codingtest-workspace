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
        int result = 0;
        for (int k = 0; k < 2*n; k++) {
            HashSet<List<Integer>> marummo = makeMarum(k); // 길이가 k+1인 마름모를 제작
            // System.out.println(k + "번째 마름모는 " + marummo);
            int cost = k*k + (k+1)*(k+1);
            int max = 0;
            for (int i=0; i < n; i++) {
                for (int j=0; j < n; j++) {
                    int sum = 0;
                    for (List<Integer> marum : marummo) {
                        int nx = marum.get(0) + i;
                        int ny = marum.get(1) + j;
                        if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                            sum+=grid[nx][ny];
                        }
                    }
                    if (sum > max) {
                        max = sum;
                    }
                }
            }
            if (max * m >= cost && result < max) {
                result = max;
            }
            // System.out.println("채굴하여 얻는 이득 : " + max * m + " 비용은 : " + cost);
            // System.out.println(k + "번째에서 손해가 없으며 채굴할 수 있는 금의 최대는 : " + result);
        }
        System.out.println(result);
    }
    public static HashSet<List<Integer>> makeMarum(int length){
        HashSet<List<Integer>> hashSet = new HashSet<>();
        hashSet.add(Arrays.asList(0,0));
        // System.out.println("현재 set : " + hashSet);
        int[] dx = new int[]{0,1,0,-1};
        int[] dy = new int[]{1,0,-1,0};
        for (int i=0; i < length; i++) {
            HashSet<List<Integer>> copy = new HashSet<>();
            for (List<Integer> original : hashSet){
                copy.add((original));
            }
            for (List<Integer> cp : copy) {
                for (int k=0; k < 4; k++){
                    int nx = cp.get(0) + dx[k];
                    int ny = cp.get(1) + dy[k];
                    hashSet.add(Arrays.asList(nx, ny));
                }
            }
            // System.out.println(i + "차 set : " + hashSet);
        }
        return hashSet;
    }
}