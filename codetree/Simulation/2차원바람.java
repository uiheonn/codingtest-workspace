import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int q = sc.nextInt();
        List<List<Integer>> building = new ArrayList<>();
        for (int i = 0; i < n; i++){
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < m; j++){
                tmp.add(sc.nextInt());
            }
            building.add(tmp);
        }
        int[][] queries = new int[q][4];
        for (int i = 0; i < q; i++)
            for (int j = 0; j < 4; j++)
                queries[i][j] = sc.nextInt()-1;
        // 직사각형 shift 연산 수행
        for (int k = 0; k < q; k++) {
            int startX = queries[k][0];
            int startY = queries[k][1];
            int endX = queries[k][2];
            int endY = queries[k][3];
            int x = startX;
            int y = startY;
            int tmp = building.get(startX).get(y);
            // 우측 이동
            while (y < endY) {
                int res = building.get(startX).get(y+1); // 다음 값을 임시 저장소에 저장하기
                building.get(startX).set(y+1,tmp); // 다음 노드에 현재값 삽입하기
                tmp = res;
                y++;
            }
            // 아래로 이동
            while (x < endX) {
                int res = building.get(x+1).get(endY);
                building.get(x+1).set(endY,tmp);
                tmp = res;
                x++;
            }
            // 왼쪽으로 이동
            while (y > startY) {
                int res = building.get(endX).get(y-1);
                building.get(endX).set(y-1,tmp);
                tmp = res;
                y--;
            }
            // 위로 이동
            while (x > startX) {
                int res = building.get(x-1).get(startY);
                building.get(x-1).set(startY,tmp);
                tmp = res;
                x--;
            }

            // 직사각형의 평균값 계산
            int[] dx = new int[] {0,1,0,-1,0};
            int[] dy = new int[] {1,0,-1,0,0};
            List<List<Integer>> building_copy = new ArrayList<>();
            for (List<Integer> ele : building) {
                building_copy.add(new ArrayList<>(ele));
            }
            for (int i=startX; i<=endX; i++) {
                for (int j=startY; j<=endY; j++) {
                    int sum = 0;
                    int count = 0;
                    for (int ii=0; ii<5; ii++) {
                        int nx = i + dx[ii];
                        int ny = j + dy[ii];
                        if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                            sum+=building.get(nx).get(ny);
                            count++;
                        }
                    }
                    building_copy.get(i).set(j, (int)sum/count);
                }
            }
            building = building_copy;
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                System.out.print(building.get(i).get(j) + " ");
            }
            System.out.println();
        }

    }
}