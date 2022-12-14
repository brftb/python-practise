# -*- coding: utf-8 -*-
"""Untitled2-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l3vJbroAbQLJoQistYsvf243vFD4eSwT
"""

### リストとタプル（配列みたいなもの）
## LIST
numbers = [0, 10, 20, 30, 40, 50]
print(numbers)
print(type(numbers))
# あらゆる型が混在できる
fruits = ['apple', 'banana', 'chelly']
menu = ['ハンバーガー', 120, 'チーズバーガー', 180]
empty = [] # 空リスト
print(fruits[2])

# 代入で変更
abcd = ['a', 'b', 'c', 'd']
abcd[0] = 'apple'
print(abcd)
# 文字列同様に切り取りも可能
print(abcd[1:3])
# 応用例いろいろ
print(abcd[1::2])
abcd[1:3] = ['x','y','z']
print(abcd)

# 練習
def remove_evenindex(ln):
  return ln[1::2]
print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'] )
print(remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])

## 多重リスト（多重配列みたいなもの）
lns = [[1,2,3], [10,20,30], ['a','b','c']]
print(lns[0][1])
print(lns[2])

## リストに対する関数・演算子・メソッド
numbers = [0, 10, 20, 30, 40, 50]
print('要素数：', len(numbers))
print('最大値：', max(numbers))
print('最小値：', min(numbers))
print('合計値：', sum(numbers))
lol = ['q','w','e','r']
print('文字列の最大値：', max(lol))
print('空の合計値：', sum([]))
print('連結：', numbers + lol)
print('繰り返し：', lol*3)

# 後の更新で影響が出る
x = [[0, 1], [2, 3]]
y = x*3
print(y)
x[0][0] = 99
print(y)

numbers = [0, 10, 20, 30, 40, 50]
print('含むかい？：', 10 in numbers)
print('orを簡潔にできる：', 'z' in ['a','p','p','l','e'])
print('含まないでしょ？：', 30 not in numbers)
print('インデックス：', numbers.index(20)) # find()は使えない
all20 = [20]*3
print(all20)
print(all20.count(20))

## 並び替え
numbers = [62,73,26,2,96,14,24,17,4]
characters = ['n','e','w','t','a','q']
# 元のlistをsort
numbers.sort()
print(numbers)
characters.sort(reverse = True)
print(characters)
# 新たなlistを作成
print(sorted(characters))
print(sorted(numbers, reverse=True))

"""sortメソッドのように元のリストを変更する操作を「破壊的」又は「in-place」と呼ぶ。<br>
sorted関数のように新しいリストを作成する操作を「非破壊的」と呼ぶ。
"""

# リストに要素を追加する
# リスト.append(追加する要素)
numbers = [10, 20, 30, 40, 50]
numbers.append(100)
print(numbers)
# 主な使われ方
numbers1 = [10, -10, 20, 30, -20, 40, -30]
positives = [] # 空のリストを作成する
positives.append(numbers1[0])
positives.append(numbers1[2])
positives.append(numbers1[3])
positives.append(numbers1[5])
print(positives)

# リストにリストの要素を追加する
numbers = [10, 20, 30, 40, 50]
numbers.extend([200, 300, 400, 200]) # numbers += [200, 300, 400, 200] と同じ
numbers

# リストに要素を挿入する
# リスト.insert(インデックス, 新しい要素)
numbers = [10, 20, 30, 40, 50]
numbers.insert(1, 1000)
numbers

# リストから要素を削除する
# リスト.remove(削除したい要素)
numbers = [10, 20, 30, 40, 20]
numbers.remove(30) # 指定した要素を削除
numbers
# 指定した要素が複数個リストに含まれる場合、一番最初の要素を削除
# リストに含まれない値を指定するとエラー

# リストからインデックスで指定した要素を削除する
# リスト.pop(削除したい要素のインデックス)
numbers = [10, 20, 20, 30, 20, 40]
print(numbers.pop(3))
print(numbers)
# リスト.pop()：インデックスを指定しない場合、最後尾の要素を削除して返します。

# リスト要素を削除する
numbers = [10, 20, 30, 40, 50]
del numbers[2]
print(numbers)
# スライスを使うことも可能
numbers = [10, 20, 30, 40, 50]
del numbers[2:4]
numbers

# リストの要素を逆順にする
characters = ['e', 'd', 'a', 'c', 'f', 'b']
characters.reverse()
characters

# リストのコピー
numbers = [10, 20, 30, 40, 50]
numbers2 = numbers.copy()
del numbers[1:3]
numbers.reverse()
print(numbers)
print(numbers2)
# 代入を用いた場合、元のリストは影響を受ける
numbers = [10, 20, 30, 40, 50]
numbers2 = numbers
del numbers[1:3]
numbers.reverse()
print(numbers)
print(numbers2)

## リストと文字列の相互変換
# explode at php
print(list('abc123'))
print('banana'.split('n'))
print('A   B\nC  '.split()) # 無引数で呼び出すと、連続した空白文字を区切りと見做す
# implode at php
print(''.join(['a', 'b', 'c', '1', '2', '3']))
print('n'.join(['ba', 'a', 'a']))

# 練習
def change_domain(email, domain):
  return email.split('@')[0] + '@' + domain
  # return '@'.join([email.split('@')[0], domain])
print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')

"""### タプル(tuple)
リストと同じようにデータの並びだが、一度設定した要素は変更不可能。
<br>
変数と定数みたいなモノですな。

"""

x = 3
y = 5
point = (x,y)
print(point)
print(type(point))

# 要素がひとつのみの場合
t = (9,)
print(t)
print(type(t))
tt = (9) # tt=int(9) と同等
print(tt)
print(type(tt))

# 要素が空の場合
empty = ()
print(empty)
print(type(empty))

# 要素の取得
numbers3 = (1,3,5,7,11,13,17,19)
print(numbers3[1]) # インデックス指定の値の取得
print(len(numbers3)) # 要素数
print(numbers3[1:3]) # スライス

numbers3 = (1,3,5,7,11,13,17,19)
list3 = list(numbers3) # リストに変換
print(list3)
tuple3 = tuple(list3) # タプルに変換
print(tuple3)

# 練習
def reverse_totuple(ln):
  ln.reverse() # リストの要素を逆順にする
  return tuple(ln)
print(reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))

## 多重代入
# タプルやリストの全ての要素を一度の操作で代入する
numbers = [0, 10, 20, 30, 40]
[a, b, c, d, e] = numbers
print(b)
# 文字列も一括代入できる
a, b, c, d, e = 'hello'
print(b)
# 様々な書き方がある
(x,y,z) = (1, 2, 3)
x,y,z = (1, 2, 3)
(x,y,z) = 1, 2, 3
x,y,z = 1, 2, 3
# 変数の値の入れ替えに多用される
x = 'apple'
y = 'pen'
x, y = y, x
print(x, y) #w = x; x = y; y = w と同じ結果

"""## リストやタプルの比較演算
比較演算子を用いて2つのリストやタプルを比較することもできる
<hr>
大小の比較は、いわゆる辞書式による比較<br>
リストやタプルの最初の要素から順に比較して大小を決める
"""

# いわゆる拡張for文
ls = [0,1,2]
for value in ls:
# for value in [0,1,2]: 直接リストを記述してもよい
  print('For loop:', value)

print('~~~~~=-----=-----=~~~~~')
# リストに対するfor文の典型例
numbers = [0,1,2,3,4,5]
squares1 = []
for x in numbers:
  squares1.append(x**2)
print(squares1)

# 練習
def sum_list(ln):
  sum = 0
  for val in ln:
    sum += val
  return sum
print(sum_list([10, 20, 30]) == 60)
print(sum_list([-1, 2, -3, 4, -5]) == -3)

# 文字列も拡張for文が使用可能
str1 = 'Apple and pen'
for c in str1:
    print(c.upper()) # 大文字表示

# 練習
def atgc_countlist(str_atgc):
  list = []
  for x in 'ATGC':
    cnt = str_atgc.count(x)
    list.append([cnt,x])
  return list
print(sorted(atgc_countlist('AAGCCCCATGGTAA')) == sorted([[5, 'A'], [2, 'T'], [3, 'G'], [4, 'C']]))

## 拡張for文を使用した短縮表記
# 二乗を格納する典型例
numbers = [0,1,2,3,4,5]
squares2 = [x**2 for x in numbers]
print(squares2)

# その他（オブジェクトの等価性と同一性）
a = []
b = []
print('a == b：', a==b)
print('a is b：', a is b)
c = [a,b]
print('c：', c)
print('~~~~~=-----=-----=~~~~~')
a.append(1)
print('c：', c)
print('~~~~~=-----=-----=~~~~~')
print('a != b：', a != b)
print('a is not b：', a is not b)

