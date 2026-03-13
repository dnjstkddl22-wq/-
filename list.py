movie_rank = ["닥터스트레인지", "스플릿", "럭키"]
print(movie_rank)
movie_rank.append("베트멘")
print(movie_rank)
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)
del movie_rank[3]
print(movie_rank)

num_list = [1, 2, 3, 4, 5]
print(num_list)
num_list.reverse()
print(num_list)
print(max(num_list), min(num_list), sum(num_list)/len(num_list))


lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3 =  lang1 + lang2
print(lang3)


price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(nums[::2])
print(nums[::2])


interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])
interest = ['삼성전자', 'LG전자', 'Naver']

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']


scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(valid_score)



ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격: ", ice["메로나"])     





