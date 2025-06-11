import java.util.*;
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        // graph = [[1], [0]]
        // graph = [[1],[0,2],[1]]
        List<List<Integer>> graphs = new ArrayList<>();
        for (int i=0; i<n; i++) {
            List<Integer> tmp = new ArrayList<>();
            graphs.add(tmp);
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (i==j)
                    continue;
                if (computers[i][j] == 1) {
                    graphs.get(i).add(j);
                }
            }
        }
        System.out.println(graphs);
        int[] visited = new int[n];
        for (int i=0; i<n; i++) {
            visited[i] = -1;
        }
        for (int i=0; i<n; i++) {
            if (visited[i] != -1)
                continue;
            List<Integer> tmp = graphs.get(i);
            Deque<Integer> deque = new LinkedList<>();
            deque.addLast(i);
            visited[i] = i;
            while (deque.size() != 0) {
                int data = deque.removeFirst();
                
                for (int ele : graphs.get(data)) {
                    if (visited[ele] == -1) {
                        deque.addLast(ele);
                        visited[ele] = i;
                    }
                }
            }
        }
        HashSet<Integer> set = new HashSet<>();
        for (int i=0; i<n; i++) {
            // System.out.println("i : " + i + " visited : " + visited[i]);
            set.add(visited[i]);
        }

        return set.size();
    }
}