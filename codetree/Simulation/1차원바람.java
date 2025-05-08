import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int q = sc.nextInt();
        // int[][] a = new int[n][m];
        List<List<Integer>> a = new ArrayList<>();
        for (int i = 0; i < n; i++){
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < m; j++){
                tmp.add(sc.nextInt());
            }
            a.add(tmp);
        }
        for (int i = 0; i < q; i++) {
            int r = sc.nextInt()-1;
            char d = sc.next().charAt(0);
            // 바람에 맞춰 이동 수행하기
            if (d == 'L') {
                int tmp = a.get(r).remove(a.get(r).size()-1);
                a.get(r).add(0,tmp);
            } else {
                int tmp = a.get(r).remove(0);
                a.get(r).add(tmp);
            }
            // 윗층에 영향을 미치는지 확인하기
            int up = r;
            char upd = d;
            while (up > 0) {
                // 일치하는 공간이 있는지 확인
                boolean exist = false;
                for (int j=0; j<m; j++) {
                    if (a.get(up).get(j) == a.get(up-1).get(j)) {
                        exist = true;
                        break;
                    }
                }
                // 존재하는 공간이 있으면 이동 연산 수행 이후 up--
                if (exist == true) {
                    int tmp = up-1;
                    if (upd == 'L') {
                        upd = 'R';
                    } else {
                        upd = 'L';
                    }
                    if (upd == 'L') {
                        int change = a.get(tmp).remove(a.get(tmp).size()-1);
                        a.get(tmp).add(0,change);
                    } else {
                        int change = a.get(tmp).remove(0);
                        a.get(tmp).add(change);
                    }
                    up--;
                } else {
                    break;
                }
            }
            int down = r;
            char downd = d;
            while (down < n-1) {
                // 일치하는 공간이 있는지 확인
                boolean exist = false;
                for (int j=0; j<m; j++) {
                    if (a.get(down).get(j) == a.get(down+1).get(j)) {
                        exist = true;
                        break;
                    }
                }
                // 존재하는 공간이 있으면 이동 연산 수행 이후 down++
                if (exist == true) {
                    int tmp = down+1;
                    if (downd == 'L') {
                        downd = 'R';
                    } else {
                        downd = 'L';
                    }
                    if (downd == 'L') {
                        int change = a.get(tmp).remove(a.get(tmp).size()-1);
                        a.get(tmp).add(0,change);
                    } else {
                        int change = a.get(tmp).remove(0);
                        a.get(tmp).add(change);
                    }
                    down++;
                } else {
                    break;
                }
            }
        }
        for (int i=0; i < n; i++) {
            for (int j=0; j < m; j++) {
                System.out.print(a.get(i).get(j)+" ");
            }
            System.out.println();
        }
        // System.out.println(a);
    }
}