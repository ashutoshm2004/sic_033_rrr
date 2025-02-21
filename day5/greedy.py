# Python3 program to find minimum number of denominations

def findMin(cost):
	deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
	n = len(deno)
	ans = []
	i = n - 1
	while(i >= 0):
		while (cost >= deno[i]):
			cost -= deno[i]
			ans.append(deno[i])
		i -= 1
	for i in range(len(ans)):
		print(ans[i], end = " ")

n = 897
print("Following is minimal number",
    "of change for", n, ": ", end = "")
findMin(n)