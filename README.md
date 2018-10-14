# CSV operation
This repository idea is from [Here](https://www.freelancer.com/projects/python/Need-Python-program-some-data/?w=f)
Clean data
# reference site
[pandas itterrows](http://www.kisse-logs.com/2017/04/26/python3-iterrows/)

[Test regular expressions](https://regex101.com/)

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

# Original File after process
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
Delete "None" rows.