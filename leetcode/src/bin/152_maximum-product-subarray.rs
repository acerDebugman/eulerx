/*
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），
并返回该子数组所对应的乘积。测试用例的答案是一个 32-位 整数。

示例 1:
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
*/

struct Solution;
impl Solution {
    // 遇到前面是正负号的，需要保存两种状态!
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut fmax = vec![0; nums.len()];
        let mut fmin = vec![0; nums.len()];
        for i in 0..nums.len() {
            if i == 0 {
                fmax[0] = nums[0];
                fmin[0] = nums[0]; 
                continue ;
            } 
            fmax[i] = std::cmp::max(fmax[i-1] * nums[i], std::cmp::max(nums[i], fmin[i-1]*nums[i]));
            fmin[i] = std::cmp::min(fmax[i-1] * nums[i], std::cmp::min(nums[i], fmin[i-1]*nums[i]));
        }
        *fmax.iter().max().unwrap()
    }
}

pub fn main() {
    let nums = vec![2,3,-2,4];
    //let nums = vec![-2,3,-4];
    println!("{:?}", nums);
    let ans = Solution::max_product(nums);
    println!("ans: {:?}", ans);
}

