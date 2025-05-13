import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = sc.nextInt();
        List<Integer> top = new ArrayList<>();
        List<Integer> bottom = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int tmp = sc.nextInt();
            top.add(tmp);
        }
        for (int i = 0; i < n; i++) {
            int tmp = sc.nextInt();
            bottom.add(tmp);
        }
        for (int i=0; i<t; i++) {
            int topSlice = top.remove(top.size()-1);
            int bottomSlice = bottom.remove(bottom.size()-1);
            top.add(0,bottomSlice);
            bottom.add(0,topSlice);
        }
        for (Integer ele : top) {
            System.out.print(ele+" ");
        }
        System.out.println();
        for (Integer ele : bottom) {
            System.out.print(ele+" ");
        }
    }
}