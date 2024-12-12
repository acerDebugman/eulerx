/*
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
*/

struct Solution;
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let (mut a, mut b) = (1, 1);
        for _ in 1..n {
            (a, b) = (b, a+b);
        }
        return b;
    }
}

pub fn main() {
    //let nums = vec![1,2,3,4];    
    //println!("{:?}", nums);
    let n = 4;
    let ans = Solution::climb_stairs(n);
    println!("ans: {:?}", ans);
}

