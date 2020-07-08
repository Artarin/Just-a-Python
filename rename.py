def rename(nam):
    new_nam=''
    for i in range (len(nam)):
        new_nam+= (chr(ord(nam[i])+1))
    print (new_nam)


print ('введите свое имя:')
nam = input()
rename(nam)