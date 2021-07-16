###### tag:`git`
# Git簡易教學 
git是分散式版本控制軟體，軟體共同開發者可以複製一份完整程式碼，並記錄歷史更改資訊，允許多人共同開發一個專案，版本控制系統以repository（＝資料庫、目錄、project）為單位。<br>
**優點：可以備份、可進行版本控管、支持多人開發**<br>
而這次讀書會使用的github是程式碼儲存雲端(**repository**)，也有其他程式可以達到此目的，例如backlog，當然要在自己的伺服器上部署repository也是可以的。<br>
在這裡會針對這次讀書會會比較常用到的幾個git指令進行說明，包括**clone**、**branch**、**checkout**、**pull**、**add**、**commit**以及**push**

**簡單來說在第一次從github把專案clone下來，之後branch自己的分支，在編輯完成後add file並commit最後將自己的分支push上去，而如果main有變動則就pull下來**

## Clone
當第一次要從repository複製git專案下來的時候會需要使用clone指令，指令如下
```
git clone https://github.com/justin71213/2021_Lab_Study.git
```
指令中網址部分是專案所在的路徑，有兩種不同方式的路徑:SSH及HTTPS，其中SSH會需要密碼或金鑰，在這次讀書會中建議使用HTTPS，專案會被複製到你現在的路徑底下，當然你要先複製在移動也是可以的。

## Add
Add是用來將你的檔案加入git的指令，指令如下
```
git add Your/File/Directory
```
add的檔案類型可以是任何檔案或路經，但是如套件等可以由使用者自行安裝的檔案請避免加入，只提供套件的清單即可，如果你要加入工作目錄底下的所有檔案就可以使用
```
git add .
```
另外覺得為了避免不必要的檔案只能一件一件add這件事很煩的話你可以使用.gitignore來建立一個忽略清單，.gitignore是一個文字檔，你可以編輯或新增它，然後在裡面寫上你不想被add的檔案或路徑例如
```
#.gitignore的內容
file
directory/
# 忽略所有附檔名是 .txt 的檔案
*.txt
```
編輯完成後就會生效，但會建議將.gitignore也add進去並commit這樣下次pull下來後就不用再編輯一次，要注意的是.gitignore只適用在新增它之後的檔案，如果比它早建立的檔案是不行的，需要再使用其他指令才能讓它適用

## Commit
在你add檔案之後需要commit來記錄下你檔案的狀態，指令如下
```
git commit
```
在下完指令之後會進入一個文字編輯畫面它會讓你輸入這次commit要留下的訊息，編輯完成後儲存並離開就會記下這次commit，如果沒有內容就離開就會取消這次commit，記下這次commit後會產生一組commit id供你在其他功能指定這個commit，可以利用git log來看每個commit的訊息及commit id

## Pull
只要曾經clone過之後git就會記下repository的位置，之後只要repository上的檔案有變動就可以利用pull將新的檔案從repository載下來，指令如下
```
git pull
```
如果本地端跟repository都有變動，git會試圖幫你將兩者變動都合併，但如果有衝突會要求你解決，關於解決方式請先自行上網google

## Push
Push與pull相反，是把本地端的commit上傳至repository，指令如下
```
git push
```

## Branch
在多人開發的過程中會對同一份程式碼進行編輯，如此一來會造成混亂，因此會利用branch產生分支，可以先理解為複製一份相同的code後在自己的線上進行開發，指令如下
```
git branch NewBranchName
```
如此一來就會產生一個名為NewBranchName的新分支，接著可以利用待會提到的checkout來切換到該分支進行add、commit等其他git的操作，如果你不知道目前的分支一共有哪些的話你可以直接下branch指令而不使用名字
```
git branch
```
這樣就會列出目前所有分支並以*標出你在的分支
```
C:\Users> git branch
* main

```
在多人開發時大家會在各自的分支開發負責的功能，最後再利用merge、cherrypick等方式將它們合併完成開發。<br>
在實務上有可能會出現編輯到同一個檔案導致衝突，但在這次的讀書會彼此檔案分開的狀況下應該不會發生就先不介紹解決方式。

## Checkout
checkout可以讓你將工作目錄底下的檔案回到你選擇的commit的狀態，指令如下
```
git checkout CommitID/BranchName
```
checkout如果接的是BranchName會選擇該branch最新的commit位置，如果是接CommitID就會選擇到指定commit，另外checkout可以額外使用-b參數:
```
git checkout NewBranchName
```
這樣的話就會新增branch並切換到該分支

