def logstr(s,t):
	m = len(s) 
	n = len(t)
	cnt = [[0]*(n+1) for x in range(m+1)]
	lg = 0
	lcs_set = set()
	for i in range(m):
		for j in range(n):
			if s[i] == t[j]:
				c=cnt[i][j]+1
				cnt[i+1][j+1]=c
				if c > lg:
					lcs_set= set()
					lg=c
					lcs_set.add(s[i-c+1:i+1])
				elif c == lg:
					lcs_set.add(s[i-c+1:i+1])
	return lcs_set		

x = logstr('abcbc','abcdba')
for l in x:
	print l
