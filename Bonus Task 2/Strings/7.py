s=str(input())
s1=s[ :s.find('h')+1]
s2=s[s.find('h'): s.rfind('h')+1]
reversed=''.join(reversed(s2))
s3=s[s.rfind('h')+1:  ]
print(s1+reversed+s3)