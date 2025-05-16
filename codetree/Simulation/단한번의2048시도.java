import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] grid = new int[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        char dir = sc.next().charAt(0);
        // 방향에 맞게 리스트 재구현
        // 동시에 터진다는 생각으로 2048시도
        List<List<Integer>> result = change(grid, dir);
        if (dir == 'L') {
            for (int i=0; i<4; i++) {
                for (int j=0; j<4; j++) {
                    if (result.get(i).size() > j)
                        System.out.print(result.get(i).get(j) + " ");
                    else
                        System.out.print(0 + " ");
                }
                System.out.println();
            }
        } else if (dir == 'R') {
            for (int i=0; i<4; i++) {
                for (int j=3;j>=0;j--) {
                    if (result.get(i).size()-1 < j)
                        System.out.print(0 + " ");
                    else
                        System.out.print(result.get(i).get(j) + " ");
                }
                System.out.println();
            }
        } else if (dir == 'D') {
            for (int i=3; i>=0; i--) {
                for (int j=0; j<4; j++) {
                    if (result.get(j).size()-1 < i)
                        System.out.print(0 + " ");
                    else
                        System.out.print(result.get(j).get(i) + " ");
                }
                System.out.println();
            }
        } else {
            for (int i=0; i<4; i++) {
                for (int j=0; j<4; j++){
                    if (result.get(j).size()-1 < i)
                        System.out.print(0 + " ");
                    else
                        System.out.print(result.get(j).get(i) + " ");
                }
                System.out.println();
            }
        }

    }
    public static List<List<Integer>> change(int[][] grid, char dir) {
        List<List<Integer>> lst = new ArrayList<>();
        
        if (dir == 'L') {
            for (int i=0; i<4; i++) {
                List<Integer> semi = new ArrayList<>();
                for (int j=0; j<4; j++) {
                    if (grid[i][j] != 0) {
                        semi.add(grid[i][j]);
                    }
                }
                lst.add(semi);
            }
        } else if (dir == 'R') {
            for (int i=0; i<4; i++) {
                List<Integer> semi = new ArrayList<>();
                for (int j=3; j>=0; j--) {
                    if (grid[i][j] != 0) {
                        semi.add(grid[i][j]);
                    }
                }
                lst.add(semi);
            }
        } else if (dir == 'U') {
            for (int i=0; i<4; i++) {
                List<Integer> semi = new ArrayList<>();
                for (int j=0; j<4; j++) {
                    if (grid[j][i] != 0) {
                        semi.add(grid[j][i]);
                    }
                }
                lst.add(semi);
            }
        } else {
            for (int i=0; i<4; i++) {
                List<Integer> semi = new ArrayList<>();
                for (int j=3; j>=0; j--) {
                    if (grid[j][i] != 0) {
                        semi.add(grid[j][i]);
                    }
                }
                lst.add(semi);
            } 
        }
        // System.out.println("폭발 전 : " + lst);
        // 동시에 폭발되어야 함
        for (int i=0; i<lst.size(); i++) {
            List<Integer> semi = new ArrayList<>();
            for (int j=0; j<lst.get(i).size(); j++) {
                if (j == lst.get(i).size()-1) {
                    semi.add(lst.get(i).get(j));
                } else if (lst.get(i).get(j).equals(lst.get(i).get(j+1))) {
                    semi.add(lst.get(i).get(j) + lst.get(i).get(j+1));
                    j++;
                } else {
                    semi.add(lst.get(i).get(j));
                }
            }
            lst.set(i, semi);
        }
        // System.out.println("폭발 후 : " + lst);
        return lst;
    }
}