/*
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
*/

struct Solution;
impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let (mut s, mut e) = (-1, -1);
        let (mut l, mut r) = (0, nums.len() as i32 - 1);
        while l <= r {
            let mid = l + (r-l)/2;
            if nums[mid as usize] == target {
                s = mid;
                e = mid;
                while s >= 0 && nums[s as usize] == target {
                    s -= 1;
                }
                while e < nums.len() as i32 && nums[e as usize] == target {
                    e += 1;
                }
                return vec![s+1, e-1];
            }
            if target > nums[mid as usize] {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return vec![s, e];
    }
}

pub fn main() {
    //let nums = vec![5,7,7,8,8,10];
    //let target = 6;
    let nums = vec![1];
    let target = 1;
    println!("{:?}, {}", nums, target);
    let ans = Solution::search_range(nums, target);
    println!("ans: {:?}", ans);
}

