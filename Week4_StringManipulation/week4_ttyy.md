### [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

* '.' Matches any single character.​​​​
* '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
![](https://i.imgur.com/RTEhCC1.png)

**解題邏輯：**
遞迴從前往後檢視 ( rec(index_s, index_p) )
* 起始為rec(0, 0)，input string = **s**, pattern = **p**
* 若 p結束，則返回 s是否結束
* 若 p的下一個值為 * ，則判斷這次的 * 是0次或多次
     * 如果此次位置的 s、p元素不同或 p不為 '.'及 s沒有元素，代表 * 對應0次，則 p的index跳到 * 的下一個
     * 反之，代表 * 可能對應多次 (也有可能0次)，則要判斷 s的下一個是否跟此次 p的元素相同，以及p的index跳到 * 的下一個
* 若此次s與p的元素相同，或 p為 .以及s有元素則往下判斷
* 其他(不相符)則返回 false
 ``` c++
 class Solution {
private:
    string s, p;
public:
    bool isMatch(string ss, string pp) {
        s = ss, p = pp;
        return rec( 0, 0);
    }
    bool rec(int ind_s, int ind_p) {
        if (!p[ind_p]) return !s[ind_s];
        if (p[ind_p+1] == '*') {
            
            if (s[ind_s] == p[ind_p] || (p[ind_p] =='.' && s[ind_s])){
                return rec(ind_s, ind_p+2)||rec(ind_s+1, ind_p);
            }
            else {
                return rec(ind_s, ind_p+2);
            }
        }
//return rec(ind_s, ind_p+2) || ((s[ind_s] == p[ind_p] || (p[ind_p] =='.' && s[ind_s])) && rec(ind_s+1, ind_p));
        //if (p[ind_p] == '.') {
            //if (s[ind_s]) return rec(ind_s+1, ind_p+1);
            //else return 0;
       // }
        if (s[ind_s] == p[ind_p] || (p[ind_p] =='.' && s[ind_s])) {
            return rec(ind_s+1, ind_p+1);
            } 
        else return 0;
    }
};
```
![](https://i.imgur.com/40DgvfN.png)