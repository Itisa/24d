

def solve_24(m,n,o,p):
	fu = []
	ans = []
	a = [m,n,o,p]
	for i in range(4):
		a.append(a[0])
		a.pop(0)
		for i1 in range(3):
			a.insert(1,a[2])
			a.pop(3)
			n = suan(a)
			if n:
				if not n in fu:
					fu.append(n)
					an = [a[0],n[0],a[1],n[1],a[2],n[2],a[3]]
					if n[-1] == -1:
						an.append('b')
					elif n[-1] == -2:
						an.append('c')
					else:
						an.append('a')					
					ans.append(an)

			a.append(a[2])
			a.pop(2)
			n = suan(a)
			if n:
				if not n in fu:
					fu.append(n)
					an = [a[0],n[0],a[1],n[1],a[2],n[2],a[3]]
					if n[-1] == -1:
						an.append('b')
					elif n[-1] == -2:
						an.append('c')
					else:
						an.append('a')					
					ans.append(an)
	return ans
	# print(ans)


def suan(a):
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
					return i,i1,i2,0

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
					return i1+2,i,i2,-1

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
				return i,2,i1,-2



def fy(a):
	ans = []
	y = ['+','-','*','/']
	for i in a:
		# x = ['%s' % i[0]+y[i[1]]+'%s' % i[2]+y[i[3]]+'%s' % i[4]+y[i[5]]+'%s' % i[6]+'%s' % i[7]]
		x = [i[0],y[i[1]],i[2],y[i[3]],i[4],y[i[5]],i[6],i[7]]
		if x[-1] == 'a':
			if x[1] == '+' or x[1] == '-':
				if x[3] == '*' or x[3] == '/':
					x.insert(0,'(')
					x.insert(4,')')
				elif x[5] == '*' or x[5] == '/':
					x.insert(0,'(')
					x.insert(6,')')
			x.pop(-1)

		elif x[-1] == 'b':
			x.pop(-1)
			x.insert(2,'(')
			x.insert(6,')')

		elif x[-1] == 'c':
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
	a = solve_24(3,8,7,8)
	ans = fy(a)
	for i in ans:
		print(i)
		# for i1 in i:
		# 	print(i1)
		# print('')