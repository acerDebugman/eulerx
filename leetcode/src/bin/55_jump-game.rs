/*
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
*/

struct Solution;
impl Solution {
    //这是暴力搜索的方法
    pub fn can_jump2(nums: Vec<i32>) -> bool {
        fn _jump(s:usize, max_len:usize, nums:&[i32]) -> bool {
            if nums[s] as usize + s >= max_len {
                return true;
            } 
            for i in 1..(nums[s] as usize + 1) {
                if _jump(s+i, max_len, nums) {
                    return true;
                }
            }
            false
        }
        
        _jump(0, nums.len() - 1, &nums)
    }

    //dp方法
    pub fn can_jump3(nums: Vec<i32>) -> bool {
        let len = nums.len();
        if len == 1 {
            return true;
        }
        let mut dp = vec![vec![0;len]; len];
        for j in 0..len {
            if j as i32 <= nums[0] {
                dp[0][j] = nums[0];
            }
        }        
        for i in 1..len {
            for j in i..len {
                if i as i32 + nums[i] >= j as i32 {
                    dp[i][j] = std::cmp::max(dp[i-1][j], i as i32 + nums[i]);
                } else {
                    dp[i][j] = std::cmp::max(dp[i-1][j], 0);
                }
            }
        }
        
        println!("{:?}", dp);
        if dp[len-2][len-1] >= (len - 1) as i32 {
            return true;
        }
        false
    }

    //贪心方法:将dp 矩阵融合
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let len = nums.len();
        if len == 1 {
            return true;
        }
        let mut max_step = nums[0] as usize;
        for i in 1..len {
            if i > max_step {
                return false;
            }
            
            if i <= max_step && i + nums[i] as usize > max_step {
                max_step = i + nums[i] as usize;
            };

            if max_step >= len-1 {
                return true;
            }
        }
        
        false
    }
}


pub fn main() {
    //let nums = vec![2,3,1,1,4];
    let nums = vec![3,2,1,0,4];
    //let nums = vec![2,0,0];
    //let nums = vec![0];
    println!("{:?}", nums);
    let ans = Solution::can_jump(nums);
    println!("ans: {:?}", ans);
}

