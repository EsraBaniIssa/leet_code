# class Solution:
    # def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    #     # Step 1: Initialize groups with character pairs from s1 and s2
    #     groups = [set([s1[i], s2[i]]) for i in range(len(s1))]
        
    #     # Step 2: Merge groups with common characters until no further merges are possible
    #     changed = True
    #     while changed:
    #         changed = False
    #         i = 0
    #         while i < len(groups):
    #             j = i + 1
    #             while j < len(groups):
    #                 if groups[i] & groups[j]:  # If groups share any character
    #                     groups[i] |= groups[j]  # Merge groups
    #                     groups.pop(j)  # Remove the merged group
    #                     changed = True  # Mark that a merge occurred
    #                 else:
    #                     j += 1
    #             i += 1
        
    #     # Step 3: Sort each group to ensure the lexicographically smallest character is first
    #     clean_groups = [sorted(group) for group in groups]
        
    #     # Step 4: Transform baseStr by mapping each character to the smallest in its group
    #     clean_str = ""
    #     for char in baseStr:
    #         found = False
    #         for group in clean_groups:
    #             if char in group:
    #                 clean_str += group[0]  # Use lexicographically smallest character
    #                 found = True
    #                 break
    #         if not found:
    #             clean_str += char  # Keep original character if not in any group
        
    #     return clean_str

class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        # Choose the lexicographically smaller character as the root
        if root_x < root_y:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Initialize Union-Find
        uf = UnionFind()
        
        # Step 1: Build equivalence classes by uniting characters from s1 and s2
        for c1, c2 in zip(s1, s2):
            uf.union(c1, c2)
        
        # Step 2: Transform baseStr
        result = []
        for char in baseStr:
            # Find the root (lexicographically smallest) of the equivalence class
            smallest_char = uf.find(char)
            result.append(smallest_char)
        
        return ''.join(result)