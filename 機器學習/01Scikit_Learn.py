from sklearn.datasets import load_boston

boston = load_boston()
print(boston.keys())
print(boston['filename'])