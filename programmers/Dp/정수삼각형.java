class Solution {
    int[][] memo;
    public int solution(int[][] triangle) {
        memo = new int[triangle.length][triangle.length];
        int answer = Math.max(dp(triangle, 1, 0), dp(triangle, 1, 1)) + triangle[0][0];
        return answer;
    }
    public int dp(int[][] triangle, int depth, int index) {
        if (memo[depth][index] > 0) {
            return memo[depth][index];
        }
        if (depth == triangle.length-1){
            memo[depth][index] = triangle[depth][index];
            return triangle[depth][index];
        }
        memo[depth][index] = Math.max(dp(triangle,depth+1,index)+triangle[depth][index], dp(triangle,depth+1,index+1)+triangle[depth][index]);
        return memo[depth][index];
    }
}