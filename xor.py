# Fixed xor 

arr1  = '1c0111001f010100061a024b53535009181c'
arr2 = '686974207468652062756c6c277320657965'
str1 =  int(arr1,16)
str2 =  int(arr2,16)
print "Fixed xor : %x\n" % (str1^str2)



