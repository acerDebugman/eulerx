/*
给你一个 只包含正整数 的 非空 数组 nums 。
请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
*/

struct Solution;
impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let sum = nums.iter().sum::<i32>();
        if sum % 2 == 1 {
            return false; 
        }
        let target = sum / 2;
        let max_v = *nums.iter().max().unwrap();
        if max_v > target {
            return false;
        }
        let mut dp = (0..=target as usize).map(|_| {
            vec![false; nums.len()]
        }).collect::<Vec<_>>();
        for j in 0..nums.len() {
            dp[0][j] = true;
        }
        for t in 1..=target as usize {
            if t as i32 == nums[0] {
                dp[t][0] = true;
            } else {
                dp[t][0] = false;
            }
        }
        //dp[nums[0] as usize][0] = true;
        for t in 1..=target as usize {
            for j in 1..nums.len() {
                if nums[j] > t as i32 {
                    dp[t][j] = dp[t][j-1];
                    continue 
                }
                dp[t][j] = dp[t-nums[j] as usize][j-1] | dp[t][j-1];
            }
        }
        /*
        for t in 0..=target as usize {
            println!("{:?}", dp[t]);
        }
        */
        dp[target as usize][nums.len()-1]
    }
}

pub fn main() {
    //let nums = vec![1,5,11,5];
    //let nums = vec![1,2,3,5];
    let nums = vec![1,5,10,6];
    println!("{:?}", nums);
    let ans = Solution::can_partition(nums);
    println!("ans: {:?}", ans);
}

