class Solution(object):
    def sortPeople(self, names, heights):
        people = list(zip(heights, names))
        people.sort(reverse=True)
        sorted_names = [i[1] for i in people]
        return sorted_names