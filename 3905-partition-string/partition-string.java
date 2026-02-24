import java.util.*;

public class Solution {

    public List<String> partitionString(String s) {
        Set<String> seen = new HashSet<>();
        List<String> segments = new ArrayList<>();

        int i = 0;
        int n = s.length();

        while (i < n) {
            StringBuilder sb = new StringBuilder();
            int j = i;

            while (j < n) {
                sb.append(s.charAt(j));
                String current = sb.toString();
                if (!seen.contains(current)) {
                    segments.add(current);
                    seen.add(current);
                    break;
                }
                j++;
            }

            i = j + 1;
        }

        return segments;
    }
}