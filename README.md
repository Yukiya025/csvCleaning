# CSV operation
This repository idea is from [Here](https://www.freelancer.com/projects/python/Need-Python-program-some-data/?w=f)
Clean data
# reference site
[pandas itterrows](http://www.kisse-logs.com/2017/04/26/python3-iterrows/)

# Requirement definition
- Delete non-English comment. OK
- Delete the non-English comment row
- Delete user_id duplication.
- Integrate comments into 1 user_id if there are some comments made by same user.

# Original File before process
user_id,comment

1,Hi

2,World

3,Hello

5,こんにちは

4,Python

2,きょう

1,あゆむ

3,Sato

5,Flower

4,class

3,find

# Original File after process
user_id,comment

1,Hi

2,World

3,Hello

5,NoneNoneNoneNoneNone

4,Python

2,NoneNoneNone

1,NoneNoneNone

3,Sato

5,Flower

4,class

3,find

# What to do NEXT?
Delete "None" rows.