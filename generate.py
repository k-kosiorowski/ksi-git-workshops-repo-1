with open("artifact.txt", "w") as f:
	for i in range(10_000):
		print(i, file=f)
