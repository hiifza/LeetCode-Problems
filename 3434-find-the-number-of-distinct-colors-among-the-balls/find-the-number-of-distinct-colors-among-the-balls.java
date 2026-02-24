import java.util.*;

class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        Map<Integer, Integer> ballColorMap = new HashMap<>();
        Map<Integer, Integer> colorCountMap = new HashMap<>();
        int n = queries.length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            int ball = queries[i][0];
            int color = queries[i][1];

            if (ballColorMap.containsKey(ball)) {
                int prevColor = ballColorMap.get(ball);
                if (prevColor != color) {
                    colorCountMap.put(prevColor, colorCountMap.get(prevColor) - 1);
                    if (colorCountMap.get(prevColor) == 0) {
                        colorCountMap.remove(prevColor);
                    }
                }
            }

            if (!ballColorMap.containsKey(ball) || ballColorMap.get(ball) != color) {
                ballColorMap.put(ball, color);
                colorCountMap.put(color, colorCountMap.getOrDefault(color, 0) + 1);
            }

            result[i] = colorCountMap.size();
        }

        return result;
    }
}