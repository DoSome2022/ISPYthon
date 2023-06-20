[來源](https://www.w3cschool.cn/python3/)   

Python3 安裝
===  
Python 官網：https://www.python.org/

## Python 安裝  
- Python 已經被移植在許多平台上（經過改動使它能夠工作在不同平台上）。  
- 您需要下載適用於您使用平台的二進制代碼，然後安裝Python。  
- 如果您平台的二進制代碼是不可用的，你需要使用C 編譯器手動編譯源代碼。  
- 編譯的源代碼，功能上有更多的選擇性， 為Python 安裝提供了更多的靈活性。 

以下為不同平台上安裝Python 的方法：  

## Unix & Linux 平台安裝Python:
- 以下為在Unix & Linux 平台上安裝Python 的簡單步驟：  

- 打開WEB 瀏覽器訪問 https://www.python.org/downloads/source/  
- 選擇適用於Unix/Linux 的源碼壓縮包。  
- 下載及解壓壓縮包 Python-3.x.x.tgz，3.x.x 為你下載的對應版本號。  
- 如果你需要自定義一些選項修改 Modules/Setup  

--- 

以 Python3.8.5 版本為例:  
<img src="https://atts.w3cschool.cn/attachments/image/20200918/1600394980732776.png">

```
# tar -zxvf Python-3.8.5.tgz
# cd Python-3.8.5
# ./configure
# make && make install

```
檢查Python3 是否正常可用：
```
# python3 -V
Python 3.8.5
```

---

## Windows 平台安裝Python:  
以下為在Windows 平台上安裝Python 的簡單步驟：  

打開WEB 瀏覽器訪問https://www.python.org/downloads/windows/  

<img src="https://atts.w3cschool.cn/attachments/image/20200919/1600505215261096.png">  

- 在下載列表中選擇Windows 平台安裝包，包格式為：python-3.8.5-amd64.exe文件， -3.8.5 為你要安裝的版本號，-amd64為你係統的版本。  

- 下載後，雙擊下載包，進入Python 安裝嚮導，安裝非常簡單，你只需要使用默認的設置一直點擊"下一步"直到安裝完成即可。

---  
## MAC 平台安裝Python:  
MAC 系統一般都自帶有Python2.7 版本的環境，你也可以在鏈接 https://www.python.org/downloads/mac-osx/ 上下載最新版安裝。
<img src="https://atts.w3cschool.cn/attachments/image/20200918/1600398717560696.png">  
環境變量配置  
- 程序和可執行文件可以在許多目錄，而這些路徑很可能不在操作系統提供可執行文件的搜索路徑中。  
- path (路徑)存儲在環境變量中，這是由操作系統維護的一個命名的字符串。這些變量包含可用的命令行解釋器和其他程序的信息。  
- Unix 或Windows 中路徑變量為PATH（UNIX 區分大小寫，Windows 不區分大小寫）。  
- 在Mac OS 中，安裝程序過程中改變了python 的安裝路徑。如果你需要在其他目錄引用Python，你必須在path 中添加Python 目錄。  

## 在Unix/Linux 設置環境變量  
- 在csh shell 輸入:  
```
setenv PATH "$PATH:/本機/local/bin/python"
```  
按下 Enter。  
-  在bash shell (Linux) 輸入:
```
export PATH="$PATH:/本機/local/bin/python" 
```
按下 Enter。 
- 在sh 或者ksh shell 輸入:  
```
PATH="$PATH:/本機/local/bin/python"
```
按下 Enter。   
注意:/本機/local/bin/python是Python 的安裝目錄。  

---  
## 在Windows 設置環境變量
 注意！在python安裝的時候勾選自動添加python到path路徑可可以免去配置環境這個過程，本教程介紹的是當在命令提示符中輸入python顯示指令不存在的情況下需要進行的操作。

在環境變量中添加Python 目錄：

在命令提示符中(cmd) : 輸入
```
path=%path%;C:\Python 
```
按下"Enter"。  

注意: C:\Python 是Python 的安裝目錄。  
也可以通過以下方式設置：

1. 右鍵點擊"計算機"，然後點擊"屬性"  
2. 然後點擊"高級系統設置"  
3. 選擇"系統變量"窗口下面的"Path",雙擊即可！  
4. 然後在"​ Path​"行，添加python 安裝路徑即可(我的D:\Python32)，所以在後面，添加該路徑即可。ps：記住，路徑直接用分號"​ ;​"隔開！  
5. 最後設置成功以後，在cmd 命令行，輸入命令"​ python​"，就可以有相關顯示。  
---
## 運行Python

交互式解釋器：  
- 你可以通過命令行窗口進入Python，並在交互式解釋器中開始編寫Python 代碼。
- 你可以在Unix、DOS 或任何其他提供了命令行或者shell 的系統進行Python 編碼工作。
```
$ python # Unix/Linux
```
or
```
C:>python # Windows/DOS
```  
<img src="https://atts.w3cschool.cn/attachments/image/20211012/1634006505683208.jpeg">  

## 如何退出？  

在交互型解釋器中輸入​exit()​按回車即可退出。