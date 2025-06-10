a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ]
b=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ]
c =[[1,2]]
d=[[1,2,3],[4,5,6]]

#Matrix-Addition
def matrix_addition(a,b):
    results_a = []
    if not add_sub_constraint_checking(a,b):
       return AssertionError("matrix addition is allowed only when rows and cols are equal")
    else:
        results_a = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
      for j in range(len(a[0])):
          results_a[i][j] = a[i][j]+b[i][j]
    return results_a
