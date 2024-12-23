/*
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
*/

struct Solution;
impl Solution {
    /*
     * f(x) = max{
     *          f(k) + 1 if nums[x] > nums[k], 
     *          f(k) if nums[x] <= nums[k]
     *      },    k in [0,x-1] 
     *init: f(0) = 1
     */
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut f = vec![0; nums.len()];
        for x in 0..nums.len() {
            let mut max_v = 1;
            for k in 0..x {
                if nums[x] > nums[k] {
                    max_v = max_v.max(f[k] + 1)
                } 
            }
            f[x] = max_v;
            println!("{:?}", f);
        }
        f.into_iter().max().unwrap()
    }
}

pub fn main() {
    //let nums = vec![10,9,2,5,3,7,101,18];
    let nums = vec![4,10,4,3,8,9];
    //let nums = vec![4,10,0,4,3,8,9];
    println!("{:?}", nums);
    let ans = Solution::length_of_lis(nums);
    println!("ans: {:?}", ans);
}

