def detail_array(data):
    
    panjang_array = len(data)
    
    print("array memiliki panjang {0} ".format(panjang_array))
    print("array memiliki isi yaitu:")

    for x in data:
        print(x)
array = ['Andita', 'Farah', 2]
detail_array(array)

