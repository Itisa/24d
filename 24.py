def solve_24(m,n,o,p):
	sort = [[n, p, o, m], [n, p, m, o], [n, m, p, o], [n, m, o, p], [n, o, m, p], [n, o, p, m], [o, m, p, n], [o, m, n, p], [o, n, m, p], [o, n, p, m], [o, p, n, m], [o, p, m, n], [p, n, m, o], [p, n, o, m], [p, o, n, m], [p, o, m, n], [p, m, o, n], [p, m, n, o], [m, o, n, p], [m, o, p, n], [m, p, o, n], [m, p, n, o], [m, n, p, o], [m, n, o, p]]
	fu = []
	ans = []
	for i in sort:
		n = suan(i,fu)
		if n:
			for i1 in n:
				fu.append(i1)
				an = [i[0],i1[0],i[1],i1[1],i[2],i1[2],i[3],i1[3]]				
				ans.append(an)
	return ans
def suan(a,fu):
	ans_f = []
	for i in range(2):
		if i == 0:
			ans1 = a[0]+a[1]
		elif i == 1:
			ans1 = a[0]-a[1]
		for i1 in range(2):
			if i1 == 0:
				ans2 = a[2]+a[3]
			elif i1 == 1:
				ans2 = a[2]-a[3]
			if ans1*ans2 == 24:
				anss = i,2,i1,-2
				if not anss in fu:
					ans_f.append(anss)
	for i in range(2):
		if i == 0:
			ans1 = a[1]+a[2]
		elif i == 1:
			ans1 = a[1]-a[2]
		for i1 in range(2):
			if i1 == 0:
				ans2 = a[0]*ans1
			elif i1 == 1 and ans1 != 0:
					ans2 = a[0]/ans1
			for i2 in range(4):
				if i2 == 0:
					ans3 = ans2+a[3]
				elif i2 == 1:
					ans3 = ans2-a[3]
				elif i2 == 2:
					ans3 = ans2*a[3]
				elif i2 == 3 and a[3] != 0:
					ans3 = ans2/a[3]
				if ans3 == 24:
					anss = i1+2,i,i2,-1
					if not anss in fu:
						ans_f.append(anss)
	for i in range(4):
		if i == 0:
			ans1 = a[0]+a[1]
		elif i == 1:
			ans1 = a[0]-a[1]
		elif i == 2:
			ans1 = a[0]*a[1]
		elif i == 3 and a[1] != 0:
			ans1 = a[0]/a[1]
		for i1 in range(4):
			if i1 == 0:
				ans2 = ans1+a[2]
			elif i1 == 1:
				ans2 = ans1-a[2]
			elif i1 == 2:
				ans2 = ans1*a[2]
			elif i1 == 3 and a[2] != 0:
				ans2 = ans1/a[2]
			for i2 in range(4):
				if i2 == 0:
					ans3 = ans2+a[3]
				elif i2 == 1:
					ans3 = ans2-a[3]
				elif i2 == 2:
					ans3 = ans2*a[3]
				elif i2 == 3 and a[3] != 0:
					ans3 = ans2/a[3]
				if ans3 == 24:
					anss = i,i1,i2,0
					if not anss in fu:
						ans_f.append(anss)
	return ans_f
def fy(a):
	ans = []
	y = ['+','-','*','/']
	for i in a:
		x = [i[0],y[i[1]],i[2],y[i[3]],i[4],y[i[5]],i[6],i[7]]
		if x[-1] == 0:
			if x[1] == '+' or x[1] == '-':
				if x[3] == '*' or x[3] == '/':
					x.insert(0,'(')
					x.insert(4,')')
				elif x[5] == '*' or x[5] == '/':
					x.insert(0,'(')
					x.insert(6,')')
			x.pop(-1)
		elif x[-1] == -1:
			x.pop(-1)
			x.insert(2,'(')
			x.insert(6,')')
		elif x[-1] == -2:
			x.pop(-1)
			x.insert(0,'(')
			x.insert(4,')')
			x.insert(6,'(')
			x.insert(10,')')
		ans_1 = ''
		for i1 in x:
			 ans_1 = ans_1 + '%s' % i1
		ans.append(ans_1)
	return ans
if __name__ == '__main__':
	a = solve_24(4,6,5,6)
	ans = fy(a)
	for i in ans:
		print(i)