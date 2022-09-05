class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        t = 3
		# Checking if mat equals to target
        if target == mat:
            return True
		# Checking if target is obtainned when mat is roatated 90 degrees each time (90,180,270)
		# in each roation the matrix is rotated by 90 degrees
		# for example matrix  if i -> row j -> col
		#[00 01 02]
		#[10 11 12]
		#[20 21 22]
		#When roated by 90
		#[20 10 00]
		#[21 11 01]
		#[22 12 02] in each row the  col element is kept constatnt and row element is changed
        while t > 0:
            n = len(mat)
            mat2 = []
            j = 0
            while j<n:
                temp = []
                i = n-1
                while i>=0:
                    temp.append(mat[i][j])
                    i-=1
                mat2.append(temp)
                j += 1
            if mat2 == target:
                return True
            else:
                mat = mat2
            t -= 1
        return False # if not any returning false 