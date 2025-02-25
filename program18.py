username = input("enter username:")
password = input("enter password:")
min_letter = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
max_letter = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
number = '0,1,2,3,4,5,6,7,8,9'
char = '@#$'
min_length=6
max_length=12
if len(password)>=min_length and len(password)<=max_length:
    if password[:] in max_letter:
        if password[:] in min_letter:
            if password[:] in char:
               print()
            else:
                print('At least  character from [@#$] is reuired')
        else:
            print('At least  letter between [a-z]')
    else:
        print('At least 1 letter between [A-Z]')
else:
    print('At least lenth between 6 to 12')

print(username)
print(password)

'''
accepted =[]
passwords = raw_input("Enter comma-separated passwords: ").split(',')

for password in passwords:

	lower = 0
	upper = 0
	digits = 0
	special = 0

	for char in password:

		if char.islower():
			lower += 1
		elif char.isupper():
			upper += 1
		elif char.isdigit():
			digits += 1
		elif special_str.find(char) != -1:
			special += 1

	if lower >= 1 and upper >= 1 and digits >= 1 and special >= 1 and len(password) in range(6,13):
		accepted.append(password)

print ",".join(accepted)'''