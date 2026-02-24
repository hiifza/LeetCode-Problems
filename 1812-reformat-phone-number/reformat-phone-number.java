class Solution {
    public String reformatNumber(String number) {
        String digits = number.replaceAll("[^0-9]", "");
        StringBuilder result = new StringBuilder();
        int i = 0, n = digits.length();

        while (n - i > 4) {
            result.append(digits, i, i + 3).append("-");
            i += 3;
        }

        if (n - i == 4) {
            result.append(digits, i, i + 2).append("-").append(digits, i + 2, i + 4);
        } else {
            result.append(digits.substring(i));
        }

        return result.toString();
    }
}