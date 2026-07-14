// Last updated: 7/14/2026, 2:00:13 PM
import java.util.Arrays;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}
 