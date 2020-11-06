class DisjSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[yset] < self.rank[xset]:
            self.parent[yset] = xset
        else:
            self.parent[xset] = yset
            self.rank[yset] += 1


dj = DisjSet(5)
print("Previous")
print(dj.rank)
print(dj.parent)
dj.union(0, 2)
dj.union(4, 2)
dj.union(4, 3)
dj.union(1, 3)

print("\nLater")
print(dj.rank)
print(dj.parent)

if dj.find(4) == dj.find(0):
    print("yes")
else:
    print("no")

if dj.find(1) == dj.find(4):
    print("yes")
else:
    print("no")
