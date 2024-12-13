/*
给你一个整数 n ，返回和为 n 的完全平方数的最少数量。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9 
*/

struct Solution;
impl Solution {
    //递归子问题：f(k) = 1 + min(f(k-j^2)) , j in [1, sqrt(k)]
    pub fn num_squares(n: i32) -> i32 {
        let f = n as f32;
        let sqrt_f = f.sqrt();
        if sqrt_f == sqrt_f.trunc() || n == 1 {
            return 1;
        } 
        let mut f = vec![0;(n+1) as usize];
        f[1] = 1;
        for i in 2..=n {
            let mut min_v = i32::MAX;
            let sqrt_i = (i as f32).sqrt().trunc() as i32;
            for v in 1..=sqrt_i {
                min_v = min_v.min(f[(i-v*v) as usize]);
            }
            f[i as usize] = 1 + min_v;
        }
        println!("{:?}", f);
        f[n as usize]
    }
}

pub fn main() {
    //let nums = vec![1,2,3,4];    
    //println!("{:?}", nums);
    let n = 12;
    let ans = Solution::num_squares(n);
    println!("ans: {:?}", ans);
}

