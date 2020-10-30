
UserInfo = input('введите известные данные пользователя без пробелов: ')
UserInversed = UserInfo.swapcase()
UserInfo+=UserInversed
UserInfo= ''.join(sorted(''.join(set(UserInfo))))
print (UserInfo)

FullAlphabet = '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()'
                
print (set(FullAlphabet))
Difference = ''.join(set (FullAlphabet) - set(UserInfo))
print (Difference)
Alphabet = UserInfo + ''.join(sorted(Difference))
print (Alphabet)

