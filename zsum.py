def exp(n,k):
	rez = 1
	while k>0:
		if k&1 == 1:
			rez = (rez*n) % 10000007
		n = (n*n) % 10000007
		k = k>>1
	return (rez%10000007)
n,k = map(int,input().split())
while n!=0 and k!=0:
	nmo = exp((n-1),k) + exp((n-1),(n-1))
	nmo = (2*nmo) % 10000007
	nmz = exp(n,k) + exp(n,n)
	print((nmz+nmo)%10000007)
	n,k = map(int,input().split())
