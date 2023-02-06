s=str(input())
s1=s[ :s.find('h')+1]
s2=s[s.find('h')+1: s.rfind('h')]
rep=s2.replace('h','H')
s3=s[s.rfind('h'):  ]
print(s1+rep+s3)

