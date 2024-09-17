class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        places=0
        if len(flowerbed) > 1:
            for i in range(0, len(flowerbed)):
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        places += 1
                elif i == len(flowerbed) -1:
                    if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        places += 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] != 1:
                    flowerbed[i] = 1
                    places += 1
        else:
            if flowerbed[0] == 0:
                places = 1
            else:
                places = 0


        if n <= places:
            return True
        else:
            return False