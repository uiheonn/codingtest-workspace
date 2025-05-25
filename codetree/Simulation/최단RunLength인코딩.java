import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String sh = A;
        int min = 21;
        for (int i=0; i<A.length(); i++) {
            sh = shift(sh);
            // System.out.println(sh);
            int m = incoding(sh);
            if (m < min) {
                min = m;
            }
        }
        System.out.println(min);
    }
    public static String shift(String st) {
        StringBuilder stb = new StringBuilder(st);
        StringBuilder tmp = stb.deleteCharAt(stb.length()-1);
        tmp.insert(0, st.charAt(st.length()-1));
        // System.out.println("연산 전 : " + st + " 연산 후 : " + stb);
        return tmp.toString();
    }
    public static int incoding(String st) {
        char tmp = st.charAt(0);
        int count = 1;
        char check;
        StringBuilder stb = new StringBuilder();
        for (int i=1; i<st.length(); i++) {
            check = st.charAt(i);
            if (tmp == check) {
                count++;
                continue;
            } else {
                String code = tmp + Integer.toString(count);
                stb.append(code);
                tmp = check;
                count = 1;
            }
        }
        String last = tmp + Integer.toString(count);
        stb.append(last);
        // System.out.println("문자열이 " + st + "일 때 변환값은 : " + stb);
        return stb.length();
    }
}