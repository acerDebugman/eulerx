/*
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0
*/

struct Solution;
impl Solution {
    //1. dfs 暴力树搜索
    //2. dp 使用 coin_change 做事情: f(x) 是最小数量, x 是 amount 币值；
    // 状态转移公式： f(x) = 1 + min f(x - c_i) , c_i \in {1,2,5} 表示币值
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let len = amount as usize + 1;
        let mut dp = vec![0; len];
        for i in 1..len {
            dp[i] = i as i32;
        }
        for i in 1..len {
            let mut min_cnt = i32::MAX;
            for v in coins.iter() {
                if i as i32 - *v >= 0 {
                    let idx = i - *v as usize;
                    if dp[idx] == -1 {
                        continue ;
                    }
                    min_cnt = min_cnt.min(dp[idx]);
                }
            }
            if min_cnt == i32::MAX {
                dp[i] = -1;
            } else {
                dp[i] = 1 + min_cnt;
            }
        }
        //println!("{:?}", dp);
        return dp[len-1];
    }

}

pub fn main() {
    let coins = vec![1,2,5];
    let amount = 11;
    //let coins = vec![7,8];
    //let amount = 11; 
    println!("{:?}", coins);
    let ans = Solution::coin_change(coins, amount);
    println!("ans: {:?}", ans);
}


