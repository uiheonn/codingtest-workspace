import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> blocks = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            blocks.add(sc.nextInt());
        }
        int s1 = sc.nextInt()-1;
        int e1 = sc.nextInt()-1;
        int s2 = sc.nextInt()-1;
        int e2 = sc.nextInt()-1;
        int index = s1;
        for (int i=s1; i<=e1; i++) {
            blocks.remove(index);
        }
        index = s2;
        for (int i=s2; i<=e2; i++) {
            blocks.remove(index);
        }
        System.out.println(blocks.size());
        for (int i=0; i<blocks.size(); i++) {
            System.out.println(blocks.get(i));
        }
    }
}