import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        List<List<Integer>> grid = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < n; j++)
                tmp.add(sc.nextInt());
            grid.add(tmp);
        }
        for (int count = 0; count<k; count++) {
            // 폭탄 터트리기 + 중력 적용
            grid = bomb(grid, n, m);

            // System.out.println("폭발 + 중력 작용 후");
            // for (List<Integer> ele : grid)
            //     System.out.println(ele);

            // 회전 시키기 + 중력 적용
            List<List<Integer>> rotation = new ArrayList<>();
            for (int i=0; i<n; i++){
                List<Integer> tmp = new ArrayList<>();
                for (int j=n-1; j>=0; j--){
                    tmp.add(grid.get(j).get(i));
                }
                rotation.add(tmp);
            }
            grid = gravity(rotation,n);
            // System.out.println("회전 후 ");
            // for (List<Integer> ele : grid)
            //     System.out.println(ele);
        }
        grid = bomb(grid, n, m);
        int result = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (!grid.get(i).get(j).equals(0)) {
                    result++;
                }
            }
        }
        // System.out.println("최종 결과");
        // for (List<Integer> ele : grid)
        //     System.out.println(ele);
        System.out.println(result);
    }

    public static List<List<Integer>> bomb(List<List<Integer>> grid, int n, int m) {
        for (int i=0; i<n; i++) {
            int bombCount = 1;
            boolean backRequired = false;
            for (int j=0; j<n-1; j++) {
                if (!grid.get(j).get(i).equals(0) && grid.get(j).get(i).equals(grid.get(j+1).get(i))){
                    bombCount++;
                } else {
                    if (m <= bombCount) { // 폭발
                        int index = j - bombCount + 1;
                        for (int ii = index; ii < index+bombCount; ii++) {
                            grid.get(ii).set(i, 0);
                        }
                        backRequired = true;
                    }
                    bombCount = 1;
                }
            }
            if (m <= bombCount) {
                int index = n - bombCount;
                for (int ii = index; ii < index+bombCount; ii++) {
                    grid.get(ii).set(i, 0);
                }
            }

            // 중력 적용
            List<Integer> tmp = new ArrayList<>();
            for (int j=0; j<n; j++) {
                if (!grid.get(j).get(i).equals(0)) {
                    tmp.add(grid.get(j).get(i));
                }
            }
            int start = n - tmp.size();
            for (int j=0; j<start; j++) {
                grid.get(j).set(i,0);
            }
            int bombIndex = 0;
            for (int j=start; j<n; j++) {
                grid.get(j).set(i, tmp.get(bombIndex));
                bombIndex++;
            }
            if (backRequired == true && m!=1)
                i--;
        }
        return grid;
    }
    public static List<List<Integer>> gravity(List<List<Integer>> grid, int n) {
        for (int i=0; i<n; i++) {
            List<Integer> tmp = new ArrayList<>();
            for (int j=0; j<n; j++) {
                if (!grid.get(j).get(i).equals(0)) {
                    tmp.add(grid.get(j).get(i));
                }
            }
            int start = n - tmp.size();
            for (int j=0; j<start; j++) {
                grid.get(j).set(i,0);
            }
            int bombIndex = 0;
            for (int j=start; j<n; j++) {
                grid.get(j).set(i, tmp.get(bombIndex));
                bombIndex++;
            }
        }
        return grid;
    }
}