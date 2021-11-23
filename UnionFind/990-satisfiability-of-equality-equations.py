class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[find(x)] = find(y)
            
        for e in equations:
            if e[1] == '=':
                union(e[0], e[-1])
        for e in equations:
            if e[1] == '!':
                if find(e[0]) == find(e[-1]):
                    return False
        return True