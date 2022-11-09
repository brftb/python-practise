# -*- coding: utf-8 -*-
"""Untitled3-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LzMkHzvBbtb8twck3Ce3kieC4rkyHjUT

# 繰り返し
## for文
"""

words = ['dog', 'cat', 'mouse']
for w in words:
    print(w, ':', len(w))
print('----------')
word = 'supercalifragilisticexpialidocious'
for c in word:
    print(c)

# 組み込み関数 ord は与えられた文字の番号（コード）を整数として返します。
# 組み込み関数 chr は逆に与えられた整数をコードとする文字を返します。
print(ord('a'))
print(ord('b'))
print(ord('z'))

print(chr(97))

# 文字コードを利用して文字列を分析してみる
# 各文字の頻度を求める
word = 'supercalifragilisticexpialidocious'
height = [0] * 26
for c in word:
  height[ord(c) - ord('a')] += 1
print(height)
  
# プロットしてみよう
import matplotlib.pyplot as plt
plt.plot(height)

# なんかグラフの凡例とか変更するやつ
left = list(range(26))  # range関数については以下を参照してください。
labels = [chr(i + ord('a')) for i in range(26)]  # 内包表記については 6-1 を参照ください。
plt.bar(left,height,tick_label=labels)

"""## 繰り返しと辞書"""

# 辞書の中身を取り出す
dic1 = {'cat': 3, 'dog': 3, 'elephant': 8}
for key in dic1.keys():
    print('key:', key, ', value:', dic1[key])

# items()を使って辞書の中身を取り出す
dic1 = {'cat': 3, 'dog': 3, 'elephant': 8}
for key, value in dic1.items():
    print('key:', key, 'value:', value)

# 多重listの中身を取り出す
list1 = [[0, 10], [1, 20], [2, 30]]
for i, j in list1:
    print(i, j)

# 練習
def reverse_lookup2(dic1):
  dic2 = {}
  for key, value in dic1.items():
    dic2[value] = key
  return dic2
print(reverse_lookup2({'apple': 3, 'pen': 5, 'orange': 7}) == {3: 'apple', 5: 'pen', 7: 'orange'})

"""## range関数

### 引数を1つ与えると:
* 0 から引数までの整数列を返します。 このとき引数の値は含まれないことの注意。

### 引数を2つあるいは3つ与えると:
* 最初の引数を数列の開始 (start)、2番目を停止 (stop)、3番目を数列の刻み (step) とする整数列を返します。
* 3番目の引数は省略可能で、既定値は 1 。
* 2番目の引数の値は含まれないことの注意。

"""

for value in range(5):
    print('Hi!', value)

# listの中身を取り出す2
ln = ['e', 'd', 'a', 'c', 'f', 'b']
for value in range(len(ln)):
    print(ln[value])

s = 0
for i in range(10):
    s = s + i
print('0 から 9 までの整数列の総和：', s)
s = 0
for i in range(1,10,2):
    s = s + i
print('0 から 9 までの奇数の総和：', s)

# 練習
def sum_n(x,y):
  s = 0
  for i in range(x,y+1):
    s += i
  return s
print(sum_n(1, 3) == 6)
# 練習
def construct_list(int_size):
  relist = []
  for i in range(int_size):
    relist.append(i)
  return relist
print(construct_list(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# range 関数は整数列を返すが、リストは返さない
seq_list = list(range(5))
print(seq_list)

# for文の入れ子
## for文を多重に入れ子（ネスト）して使う
list1 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]

for i in range(4):
    for j in range(3):
        print('list1の', i + 1, '番目の要素（リスト）の', j + 1, '番目の要素 =', list1[i][j])

# C[i][j] は、i 個から j 個を選ぶ組み合わせの数
C = [[1]]
for i in range(100):
  C.append([1]+[0]*i+[1]) # [1,0,...,0.1]の要素を追加
  for j in range(i):
    C[i+1][j+1] = C[i][j] + C[i][j+1]
# C[:10]
for i in range(10):
  print(C[i])
plt.plot(C[100]) # C[100] を視覚化

# 練習
def sum_lists(list1):
  s = 0
  # if type(list1) is list:
  for i in range(len(list1)):
    for j in range(len(list1[i])):
      s += list1[i][j]
  return s
print(sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]]) == 158)
# 別解
def sum_lists2(list1):
  total = 0
  for row in list1:
    for value in row:
      total += value
  return total

# 練習
def sum_matrix(list1, list2):
  ans = [[0,0,0],[0,0,0],[0,0,0]] # init
  for i in range(3):
    for j in range(3):
      ans[i][j] = list1[i][j] + list2[i][j]
  return ans
print(sum_matrix([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]) == [[2, 6, 10], [6, 10, 14], [10, 14, 18]])

"""## for文の計算量

### 「計算量とは、 アルゴリズムをもとにしたプログラムの実行時間を見積もるための指標である。」<br>「この見積もりは計算量のオーダーと呼ばれる非常におおまかな尺度で考える。」

```python
for x in リスト:
    要素xに対する処理
```
では、「要素に対する処理」が要素の数だけ実行される。要素の数をnとしたとき、全体の処理にはnに比例する時間がかかり、このことを、オーダーnといって、O(n)と書く。

```python
for x in リスト:
    for y in 同じリスト:
        要素の組み合わせ(x,y)に対する処理
```
という二重のループでは、全体の処理には、nの二乗に比例する時間がかかり、このことをO(n`2)と書く。

## enumerate

* 要素の順序を把握したいとき
* リストから辞書に変換
"""

i = 0
some_list = [1,2,3]
for val in some_list:
  print(i, val) # 繰り返させたい処理
  i += 1
print('----------=----------=----------')
for i, val in enumerate(some_list):
  print(i, val) # 繰り返させたい処理
print('----------=----------=----------')
# リストから辞書に変換
words = ['dog', 'cat', 'mouse']
mapping = {}
for i, w in enumerate(words):
    mapping[w] = i
print(mapping)

"""## while文"""

x = 1
total = 0
while x <= 10:
  total += x
  x += 1
print('x=',x, 'total=',total)
print('----------=----------=----------')
total = 0
for x in range(11):
    total += x
print('x=',x, 'total=',total)

"""## 制御構造とreturn文
return文は1-2で説明したように関数を終了し、値を返す（返値）機能を持つ。<br>
以下の関数 simple_lsearch は与えられたリスト lst に myitem と等しいものがあれば True を、なければ False を返す。
```python
def simple_lsearch(lst, myitem):
    for item in lst:
        if item == myitem:
            return True
    return False
```

## break文
break文は、 for文もしくはwhile文の実行文グループで利用可能。<br>
break文は実行中のプログラムで最も内側の繰り返し処理を中断し、そのループを終了させる。<br>
以下のプログラムは、初項 256、公比 1/2、の等比級数の和を求めるもの。ただし、総和が 500 をこえれば打ち切られる。
```python
x = 256
total = 0
while x > 0:
    if total > 500:
        break           # 500 を超えれば while ループを抜ける
    total += x
    x = x // 2          # // は少数点以下を切り捨てる除算
print(x, total)
```

"""

# 練習
# 部分文字列 str2 が開始される str1 のインデックスを返値として返す。
def simple_match(str1, str2):
  if str2 in str1:
    return str1.index(str2)
  return -1
print(simple_match('location', 'cat') == 2)
print(simple_match('soccer', 'cat') == -1)
print(simple_match('category', 'cat') == 0)
print(simple_match('carpet', 'cat') == -1)

"""## continue文
continue文はbreak文同様、for および while ループの実行文グループで利用可能。<br> 
continue文は実行中のプログラムで最も内側の繰り返し処理を中断し、次のループの繰り返しの処理を開始する。<br>
下記のプログラムは、colors リストの 'black' は印字されないが 'white' は印字される。
```python
colors = ['red', 'green', 'blue', 'black', 'white']
for c in colors:
    if c == 'black':
        continue
    print(c)
```

## for文とwhile文における else
for文およびwhile文では else を書くこともでき、この実行文グループは、ループの最後に一度だけ実行される。ただし、break でループを終了したときは実行されない。

## pass文
Pythonでは空の実行文グループは許されていないが、可読性向上のために、なにもしないpass文を用いて、正常に実行させることがある。

"""

# 練習
# 1秒おきに print が永久に実行されるので、10回 print が実行された後にwhile文を終了するようにする。
from time import sleep
cnt = 0
while True:
  print('Yeah!',cnt)
  cnt += 1
  if cnt >= 10:
    break
  sleep(1)
print('finish!')

# 練習
# 英語の文章に含まれる3文字以上の全ての英単語を要素とするリストを返す関数
def collect_engwords(str_engsentence):
  ans = []
  str_engsentence = str_engsentence.replace(',', '') # 「,」の削除
  str_engsentence = str_engsentence.replace('.', '') # 「.」の削除
  words = str_engsentence.split(' ')
  for word in words:
    if len(word) >= 3:
      ans.append(word)
  return ans
print(collect_engwords('Unfortunately no, it requires something with a little more kick, plutonium.') == ['Unfortunately', 'requires',
'something', 'with', 'little', 'more', 'kick', 'plutonium'])

# 練習
# 2つの同じ大きさのリストの奇数インデックスの要素を入れ替えて、その結果得られる2つのリストをタプルにして返す関数
def swap_lists(ln1, ln2):
  ln3 = []
  ln4 = []
  for i in range(len(ln1)):
    if i%2 == 0:
      ln3.append(ln1[i])
      ln4.append(ln2[i])
    else:
      ln3.append(ln2[i])
      ln4.append(ln1[i])
  return (ln3, ln4)
  #   if i % 2 == 1:
  #     ln1[i], ln2[i] = ln2[i], ln1[i]
  # return ln1, ln2
print(swap_lists([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']) == ([1, 'b', 3, 'd', 5], ['a', 2, 'c', 4, 'e']))

# 練習
# 文字列の中に含まれる大文字の数を返す関数
def count_capitalletters(str1):
  cnt = 0
  for char in str1:
    if char == char.upper() and char != char.lower():
      cnt += 1
      # print(char)
  return cnt
print(count_capitalletters('Que Será, Será') == 3)

# 練習
# 長さが 3 の倍数である文字列を長さ 3 の文字列に区切り、それらを順に格納したリストを返す関数
def identify_codons(str_augc):
  ans = []
  for i in range(0,len(str_augc),3):
    word = str_augc[i:i+3]
    ans.append(word)
  # print(ans)
  return ans
print(identify_codons('CCCCCGGCACCT') == ['CCC', 'CCG', 'GCA', 'CCT'])

# 練習
# 正の整数の下桁から3桁毎にコンマ (,) を入れた文字列を返す関数
def add_commas(int1):
  str1 = str(int1)
  ans = ''
  cnt = 0
  # 文字列を逆順にして一文字ずつ検査
  for val in reversed(str1):
    # 先頭に連結
    ans = val + ans
    cnt += 1
    if cnt%3 == 0 and cnt != len(str1):
      ans = ',' + ans
  # print(ans)
  return ans
print(add_commas(14980) == '14,980')
print(add_commas(3980) == '3,980')
print(add_commas(298) == '298')
print(add_commas(1000000) == '1,000,000')

# 練習
#  k 個の要素を持つリストの要素が文字列でなければ文字列に変換し、
# リストの1番目から k-2 番目の各要素の後ろには ', ' を、 k-1 番目の要素の後ろには' and ' を加え、
# 1番目から k 番目までの要素を繋げた文字列を返す関数
def sum_strings(list1):
  ans = ''
  cnt = 0
  # リストの要素が文字列でなければ文字列に変換
  list2 = []
  for val in list1:
    if type(val) == str:
      list2.append(val)
    else:
      list2.append(str(val))
  # 
  for val in list2:
    ans += val
    cnt += 1
    if cnt < len(list2)-1:
      ans += ', '
    elif cnt == len(list2):
      ans += ''
    else:
      ans += ' and '
  # print(ans)
  return ans
print(sum_strings(['a', 'b', 'c', 'd']) == 'a, b, c and d')
print(sum_strings(['a']) == 'a')
print(sum_strings([1, 2, 3]) == '1, 2 and 3')

# 練習
# 辞書 dic1 と長さ 10 以下の文字列 str1 が引数として与えられたとき、
# dic1 に str1 の長さ n がキーとして登録されていない場合、dic1 に キー n、n に対応する値 str1 を登録
# dic1 に str1 の長さ n がキーとして登録されている場合、i の値を n+1, n+2, …と1つずつ増やしていき、dic1 にキーとして登録されていない値 i を探す
# i を 10 まで増やしても登録されていない値が見つからない場合は、i を 1 に戻した上で i を増やす作業を続行
# 登録可能な i が見つかった場合、登録する
# 登録可能な i が見つからなかった場合、変更しない
def handle_collision2(dic1, str1):
  ans = 'ans'
  # 未登録の場合
  if len(str1) not in dic1:
    dic1[len(str1)] = str1
  else:
    # 登録済の場合→[1,10]をlen(str1)+1始まりで一周して探索
    for i in range(0,9):
      index = (i+len(str1))%10 + 1
      # print(index)
      if index not in dic1:
        dic1[index] = str1
        break
  # for key, value in dic1.items():
  #   print(key, value)
  # print('--------')
  return ans
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd'}
handle_collision2(dic1_orig, 'Big Four')
print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four'})
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House'}
handle_collision2(dic1_orig, 'Edgware')
print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware'})
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'}
handle_collision2(dic1_orig, 'ABC')
print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'})

# より効率の良い方法 & 判断方法の別解
# 先に登録済かを判断せずに[1,10]をlen(str)始まりで一周しながら判断すればいいだけ
def handle_collision22(dic1, str1):
  for i in range(-1,9):
    index = (i+len(str1))%10 + 1
    # if index not in dic1:
    if dic1.get(index) is None: # == None でもよい
      dic1[index] = str1
      break
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd'}
handle_collision22(dic1_orig, 'Big Four')
print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four'})
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House'}
handle_collision22(dic1_orig, 'Edgware')
print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware'})
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'}
handle_collision22(dic1_orig, 'ABC')
print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'})

# 練習
# 整数を最初の要素、文字列をその次の要素とするリストを要素とするリスト list1 が与えられたとき、次のような辞書 dic1 を返す関数
# 各子リスト list2 に対して、dic1 のキーは list2 の最初の要素である整数とし、そのキーに対応する値は次の要素である文字列とする。
# 2つ以上の子リストの最初の要素が同じ整数である場合、list1 においてより小さいインデックスを持つ子リストの文字列を、その整数のキーに対応する値とする。
def handle_collision3(list1):
  dicAns = {}
  for list2 in list1:
    print(list2)
    # 未登録の際のみ登録
    if list2[0] not in dicAns:
      dicAns[list2[0]] = list2[1]
  print(dicAns)
  return dicAns
print(handle_collision3([[3, 'Richard III'], [1, 'Othello'], [2, 'Tempest'], [3, 'King John'], [4, 'Midsummer'], [1, 'Lear']]) == {1: 'Othello', 2: 'Tempest', 3: 'Richard III', 4: 'Midsummer'})

