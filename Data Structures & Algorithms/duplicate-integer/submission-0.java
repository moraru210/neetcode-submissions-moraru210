class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> setCheck = new HashSet();
        for (int i : nums)
        {
            if (setCheck.contains(i))
            {
                return true;
            }
            setCheck.add(i);
        }
        return false;
    }
}
