# Python program to print
# duplicates from a list
# of integers
def Repeat(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated

# Driver Code

	
# This code is contributed
# by Sandeep_anand



d1=[]
d2=[]
j1=""
j2=""

import json
path="data/extract/profile_link/"
with open(path+"candidates_link.json","r") as f:
    j1=json.loads(f.read())
# with open(path+"linkdin_profiles.json","r") as f:
#     j2=json.loads(f.read())
fin_urls=[]
with open('log/finishedurl.txt', 'r') as f:
    fin_urls = f.readlines()
f_url=[]
for u in fin_urls:
        u=u.split("#")[1].replace("\n","")
        f_url.append(u)
print(len(Repeat(f_url)))
j1=j1["profile_link"]
# j2=f_url
# count=0
# for i in j1:
#     for j in j2:
#         if i["link"]==j:
#             count+=1
# print(count)
filtered_profiles=[]
for i in j1:
	if i in filtered_profiles:
		pass
	else:
		filtered_profiles.append(i)
print(len(filtered_profiles))