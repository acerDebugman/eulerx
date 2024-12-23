/*
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
*/

struct Solution;
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        fn is_in_dict(s2: &str, word_dict: &Vec<String>) -> bool {
            if word_dict.iter().any(|x| x == s2) {
                return true
            } 
            false
        } 

        let mut dp = vec![false; s.len()];
        
        for i in 0..s.len() {
            for k in 0..=i {
                if k == 0 && is_in_dict(&s[k..=i], &word_dict) {
                    dp[i] = true;
                    break;
                }
                if k > 0 && dp[k-1] && is_in_dict(&s[k..=i], &word_dict) {
                    dp[i] = true;
                    break;
                }
            }
            println!("{:?}", dp);
        }
        
        return dp[s.len()-1]
    }
}

pub fn main() {
    //let s = "catsandog".to_string();
    //let word_dict = vec!["cats", "dog", "sand", "and", "cat"];
    let s = "leetcode".to_string();
    let word_dict = vec!["leet", "code"];
    //println!("{:?}", nums);
    let word_dict = word_dict.into_iter().map(|x| x.to_string()).collect::<Vec<_>>();
    let ans = Solution::word_break(s, word_dict);
    println!("ans: {:?}", ans);
}

