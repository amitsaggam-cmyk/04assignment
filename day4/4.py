# 1
arr6 = np.random.randint(1, 50, (5, 5))
print("Mean:", np.mean(arr6))
print("Median:", np.median(arr6))
print("Std Dev:", np.std(arr6))
print("Variance:", np.var(arr6))


# 2
arr7 = np.arange(1, 10).reshape(3, 3)
normalized = (arr7 - np.mean(arr7)) / np.std(arr7)
print("Normalized Array:\n", normalized)