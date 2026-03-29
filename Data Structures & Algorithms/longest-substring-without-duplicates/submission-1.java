class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> charSet = new HashSet<>();
        int left = 0;
        int right = 0;
        int maxRes = 0;
        while (right < s.length()) {
            char c = s.charAt(right);
            while (charSet.contains(c)) {
                char c_left = s.charAt(left);
                charSet.remove(c_left);
                left++;
            }
            maxRes = Math.max(maxRes, ((right-left)+1));
            // System.out.println("here");
            charSet.add(c);
            right++;
        }
        return maxRes;
    }
}
