class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            newRow = []
            for j in range(len(image[0]) - 1, -1, -1):
                newRow.append(image[i][j])
            image[i] = newRow

        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        
        return image