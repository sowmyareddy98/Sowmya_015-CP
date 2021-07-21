# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    #return None
    c1 = len(m1[0])
    r2 = len(m2)

    if (c1 != r2):
        return None
    else:
        result = [[sum(a*b for a,b in zip(m1_row, m2_col))
                for m2_col in zip(*m2)]
                for m1_row in m1]
        return result




