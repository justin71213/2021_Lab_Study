# [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
## 題目敘述
輸入一個字串s以及正則表達式p，檢查字串s是否有符合的條件，其中:<br>
'\*'代表前一個字符可以重複任意次(包括0次)<br>
'.'可以代表任意字符<br>
例如
```
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab"
```

## 解題邏輯
'.'號不是太大的問題，問題在於'\*'號，出現'\*'號時會有幾種狀況:<br>
1. 該字符不存在<br>
2. 該字符重複多次<br>
3. 該字符重複多次，但為'.'號(.\*)或與後方字符(ex:a\*a)相同<br>
採用Dynamic Programing建立表格，以上面範例為例建立(s.length+1)\*(p.length+1)表格

|-|0|c|\*|a|\*|a|b|\*
|-|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|0|T|
|a|
|a|
|b|

從S的第一個字元開始逐個判斷是否符合P的正則表達，[0][0]預設為True因為若兩邊皆為空字串也符合條件，接著判斷S為空字串但P只有c的情況那同樣不符合正則表達因此在[0][c]的部分填入false:

|-|0|c|
|-|:-:|:-:|
|0|T|F|

遇到\*號時先確認是否為狀況1，代表C不存在，因此狀況會相當於判斷皆為空字串的狀況:

|-|0|c|\*|
|-|:-:|:-:|:-:|
|0|T|F|

變成

|-|0|
|-|:-:|
|0|T|

因此該格的答案會與前[\*-2]的答案相同為True<br>
依序填完S為空字串的情況及S內有第1個a時狀況，當遇到第一個a雖然相同但還要注意上一次的結果是否符合

|-|0|c|\*|a|\*|
|-|:-:|:-:|:-:|:-:|:-:|
|0|T|F|**T**|F|T|
|a|F|F|F|**T && [0][\*]**||

再來遇到a\*時

|-|0|c|\*|a|\*|
|-|:-:|:-:|:-:|:-:|:-:|
|0|T|F|T|F|T|
|a|F|F|F|T||

此時先判斷是否為狀況1先看[\*-2]的答案為false確定a的個數不為0，為狀況3<br>
將a視作a\*的一部份，此時的判斷會相當於

|-|0|c|\*|a|\*|
|-|:-:|:-:|:-:|:-:|:-:|
|0|T|F|T|F|T|

因此填入true，依序填完後回傳最後一個元素作為答案，代表檢查完所有S及P。
## 複雜度分析
時間複雜度:O(mn)->s長\*p長<br>
空間複雜度:O(mn)

## 程式碼
```c
bool isMatch(char * s, char * p){
    int plen = strlen(p);
    int slen = strlen(s);
    int i;//i的座標
    int j;//p的座標
    bool match[slen+1][plen+1];
    //矩陣初始化
    for(i=0;i<slen+1;i++){
        for(j=0;j<plen+1;j++){
            match[i][j] = false;
        }
    }
    
    //兩邊皆為空字串
    match[0][0] = true; 
    
    //針對皆有'*'的情況
    for(j=1;j<plen+1;j++){
        if(p[j-1]=='*'){
            match[0][j] = match[0][j-2];
        }
    }
    
    //逐漸擴增表並查詢
    for(i=1;i<slen+1;i++){
        for(j=1;j<plen+1;j++){
            if(p[j-1] == '.' || s[i-1] == p[j-1] ){
                //與上次的解過一起看，省略'&&'
                match[i][j] = match[i-1][j-1]; 
                }
            else if(p[j-1] == '*'){
                //*為零個的情況
                match[i][j] = match[i][j-2]; 
                //若與上次的字相同，視作*的一部份，併入並回到上次的判斷
                if(p[j-2] == '.' || p[j-2] == s[i-1]){
                    match[i][j] = match[i][j] || match[i-1][j];
                }
            }
            else{
                //完全不符
                match[i][j] = false;
            }
        }
    }
    return match[slen][plen];
}
```

## 運行結果
```
Runtime: 0 ms, faster than 100.00% of C online submissions for Regular Expression Matching.
Memory Usage: 5.5 MB, less than 81.00% of C online submissions for Regular Expression Matching.
```

## 資料來源
[Regular Expression Dynamic Programming](https://www.youtube.com/watch?v=l3hda49XcDE)
