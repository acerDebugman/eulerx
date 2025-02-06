/*
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
    若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
    若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

示例 2：
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。

示例 3：
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
*/

/*
 * 1. 这个题的重点是原来的严格递增的数组，旋转有一个特性：最后的元素，不会高于第一个元素！
 * 所以可以放心用 nums[pivot] < nums[r] 元素进行比较，pivot位置的元素比 r
 * 的高，说明左边是有序的；pivot的元素比右边低，说明右边是有序的; 
 * 最低的元素肯定不再最低的一边
 * 2. 边界的问题，while l<=r 还是  while l<r , 重点还是要考虑 最后只剩下 2 个元素边界怎么变化！比如
 *    不论前面怎么二分处理，最后的场景一定是落到 [1,2] 或者 [2,1] 这样的数，而pivot = l + (r-l)/2
 *    是落到左边的，因此是l向前，还是r向后，要根据具体情况区分了！
 */
struct Solution;
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let (mut l, mut r) = (0, nums.len() as i32 - 1);
        while l < r {
            let pivot = l + (r - l) / 2;
            if nums[pivot as usize] < nums[r as usize] {
                r = pivot;
            } else {
                l = pivot + 1;
            }
        }
        return nums[l as usize] 
    }
    pub fn find_min2(nums: Vec<i32>) -> i32 {
        let (mut l, mut r) = (0, nums.len() as i32 - 1);
        let mut min = nums[0];
        while l < r {
            let mid = l + (r-l)/2;
            let mid_r = l + (r-l)/2 + 1;
            min = std::cmp::min(min, nums[mid as usize]);
            min = std::cmp::min(min, nums[mid_r as usize]);
            if nums[l as usize] < nums[mid as usize] {
                l = mid; 
            } else {
                r = mid;
            }
        }
        min
    } 
}

pub fn main() {
    let nums = vec![4,5,6,7,0,1,2];
    //let nums = vec![2,1];
    println!("{:?}", nums);
    let ans = Solution::find_min(nums);
    println!("ans: {:?}", ans);
}

