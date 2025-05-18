import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = sc.nextInt();
        List<Integer> l = new ArrayList<>();
        List<Integer> r = new ArrayList<>();
        List<Integer> d = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            l.add(sc.nextInt());
        }
        for (int i = 0; i < n; i++) {
            r.add(sc.nextInt());
        }
        for (int i = 0; i < n; i++) {
            d.add(sc.nextInt());
        }
        for (int i=0; i < t; i++) {
            int ltmp = l.remove(l.size()-1);
            int rtmp = r.remove(r.size()-1);
            int dtmp = d.remove(d.size()-1);
            l.add(0,dtmp);
            r.add(0,ltmp);
            d.add(0,rtmp);
        }
        for (int i=0; i<l.size(); i++) {
            System.out.print(l.get(i)+" ");
        }
        System.out.println();
        for (int i=0; i<r.size(); i++) {
            System.out.print(r.get(i)+" ");
        }
        System.out.println();
        for (int i=0; i<d.size(); i++) {
            System.out.print(d.get(i)+" ");
        }
        System.out.println();
    }
}