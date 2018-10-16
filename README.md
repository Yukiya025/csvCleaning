# Special Thanks
Dear [Christian](https://amzn.to/2Oro3Ka). You takes me into deep Python sea and sky.

# CSV operation
This repository idea is from [Here](https://www.freelancer.com/projects/python/Need-Python-program-some-data/?w=f)

This is practical Python learning. The repository is useful to clean data.
# How to use
1. Run `main.py`. `original.csv` is processed and non-English letters are converted to "?"
2. If open `OnlyEn.csv`, there are `user_id` and `comment` by English.
# Dev. Environment
- Python 3.7.0
- Pycharm
- Linux Mint 19 "Tara" Cinnamon

## Libraries
- pandas
- warnings (To ignore warnings. It's optional)

# Initial Folder Structure
--main.py

--main0.py

--original.csv (before process)

# Folder Structure after Process
--main.py

--main0.py

--original.csv (processed)

--OnlyEn.csv (New)
# Reference Site
[pandas itterrows](http://www.kisse-logs.com/2017/04/26/python3-iterrows/)

[Test regular expressions](https://regex101.com/)

[Pythonで配列や二次元配列をcsvファイルに書き込む](http://www.irohabook.com/python-csv-write)

[Python Tips：文字列を検索したい](https://www.lifewithpython.com/2015/04/python-search-string-pattern.html)
[[python3 pandas] 複数のセルの内容を一つにまとめたい](https://teratail.com/questions/152220#reply-228758)
# Requirement definition
- Delete non-English comment. DONE
- Delete the non-English comment row. DONE
- Delete user_id duplication.
- Integrate comments into 1 user_id if there are some comments made by same user.

# original.csv before process
user_id,comment

1,Hi

2,World

3,Hello

5,привет

4,Python

2,きょう

1,あゆむ

3,Sato

5,露西亜

4,class

3,find

5,руссия

4,コーヒー

3,солдат

2,alice

# Ooriginal.csv after process
user_id,comment

1,Hi

2,World

3,Hello

5,??????

4,Python

2,???

1,???

3,Sato

5,???

4,class

3,find

5,??????

4,????

3,??????

2,alice

# What to do NEXT?
- Delete user_id duplication.
- Integrate comments into 1 user_id if there are some comments made by same user.