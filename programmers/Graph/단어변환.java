import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        // 0. BFS로 최단 횟수 구하는 문제
        // 1. words 내에 단어가 하나만 다른 경우를 찾는다
        // 2. 순서대로 데큐에 넣는다
        // 3. visited이 필요한가? yes
        Deque<String> deque = new LinkedList<>();
        Deque<Integer> countDeque = new LinkedList<>();
        HashMap<String,Boolean> visited = new HashMap<String,Boolean>();
        for (String tmp : words) {
            visited.put(tmp,false);
        }
        
        deque.add(begin);
        countDeque.add(0);
        while (deque.size() != 0) {
            String word = deque.removeFirst();
            int count = countDeque.removeFirst();
            visited.replace(word, true);
            // System.out.println("word : " + word + " count : " + count);
            if (word.equals(target)) {
                answer = count;
                break;
            }
            List<String> nextWords = findOnlyOneDifferentWord(words, word);
            for (String w : nextWords) {
                if (visited.get(w) == false) {
                    deque.add(w);
                    countDeque.add(count+1);
                }
            }
        }
        return answer;
    }
    public List<String> findOnlyOneDifferentWord(String[] words, String word) {
        List<String> list = new ArrayList<>();
        int len = word.length();
        for (String tmp : words) {
            int check = 0;
            for (int i=0; i<len; i++) { // 하나만 다른지 체크
                if (word.charAt(i) != tmp.charAt(i)) {
                    check++;
                }
            }
            if (check == 1) {
                list.add(tmp);
            }
        }
        return list;
    }
}