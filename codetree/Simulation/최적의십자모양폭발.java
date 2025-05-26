import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<List<Integer>> grid = new ArrayList<>();
        for (int i = 0; i < n; i++){
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < n; j++)
                tmp.add(sc.nextInt());
            grid.add(tmp);
        }
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        int result = 0;
        // 폭발 경우의 수 완전 탐색
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                List<List<Integer>> tester = new ArrayList<>();
                for (List<Integer> row : grid) {
                    tester.add(new ArrayList<>(row));
                }
                int bombSize = tester.get(i).get(j)-1;
                // 폭발 시도
                // 1. 하방 폭발 + 상단 폭발
                for (int k=i-bombSize; k<=i+bombSize; k++) {
                    if (k >= 0 && k < n)
                        tester.get(k).set(j,0);
                }
                // 2. 좌측 폭발 + 우측 폭발
                for (int k=j-bombSize; k<=j+bombSize; k++) {
                    if (k >= 0 && k < n)
                        tester.get(i).set(k,0);
                }
                // System.out.println(i + "행 " + j + "열 " + " 폭발 작용");
                // for (List<Integer> ele : tester)
                //     System.out.println(ele);
                // 중력 작용
                List<List<Integer>> gravity = new ArrayList<>();
                for (int ii=0; ii<n; ii++) {
                    List<Integer> tmp = new ArrayList<>();
                    for (int jj=0; jj<n; jj++) {
                        if (!tester.get(jj).get(ii).equals(0))
                            tmp.add(tester.get(jj).get(ii));
                    }
                    int count = tmp.size();
                    for (int jj=0; jj<n-count; jj++) {
                        tmp.add(0,0);
                    }
                    gravity.add(tmp);
                }
                List<List<Integer>> last = new ArrayList<>();
                for (int ii=0; ii<n; ii++) {
                    List<Integer> tmp = new ArrayList<>();
                    for (int jj=0; jj<n; jj++) {
                        tmp.add(gravity.get(jj).get(ii));
                    }
                    last.add(tmp);
                }

                // System.out.println("중력 작용 이후");
                // for (List<Integer> ele : last)
                //     System.out.println(ele);

                // 쌍을 계산
                int cal = 0;
                for (int ii=0; ii<n; ii++) {
                    for (int jj=0; jj<n; jj++) {
                        if (last.get(ii).get(jj).equals(0))
                            continue;
                        for (int x=0; x<4; x++) {
                            int nx = ii + dx[x];
                            int ny = jj + dy[x];
                            if (nx >= 0 && nx < n && ny >= 0 && ny < n && last.get(ii).get(jj).equals(last.get(nx).get(ny)))
                                cal++;
                        }
                    }
                }
                int realCal = (int)(cal/2);
                if (realCal > result)
                    result = realCal;
            }
        }
        System.out.println(result);
    }
}