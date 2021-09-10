def rotate_90_inplace(img):
    if len(img) != len(img[0]):
        print('matrix must be n x n')
        return -1
    # 90 degree rotation = first reverse, then transpose matrix 
    img.reverse() 
    for i in range(len(img)):
        for j in range(i): # <-- Note : range(i) not range(len(img))
            img[i][j], img[j][i] = img[j][i], img[i][j]
    # No return since it is inplace    

def show(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=' ')
        print()

if __name__ == "__main__":
    img = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    show(img)
    # 1 2 3 
    # 4 5 6 
    # 7 8 9 
    rotate_90_inplace(img)
    print('--------')
    show(img)
    # 7 4 1 
    # 8 5 2 
    # 9 6 3
