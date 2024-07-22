class Solution(object):
    def sortPeople(self, names, heights):
        hashmap = {heights[i]: names[i] for i in range(len(names))}
        names = []
        while hashmap:
            maxi = max(hashmap.keys())
            names.append(hashmap[maxi])
            del hashmap[maxi]
        return names