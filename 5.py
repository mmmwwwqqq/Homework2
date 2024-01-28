import string
def password_level(s):
    if len(s)<8:
        print('Недопустимый пароль')
        return
    low_list=list(string.ascii_lowercase)
    up_list=list(string.ascii_uppercase)
    sp_list='@#$%&*().,-_+'
    num_list='0123456789'
    low=False
    up=False
    sp=False
    num=False
    for i in range (len(s)):
        if s[i] in low_list:
           low=True
        if s[i] in up_list:
            up=True
        if s[i] in sp_list:
            sp=True
        if s[i] in num_list:
            num=True
    if num==True and sp==True and up==True and low==True:
        print('Надежный пароль')
        return
    if (num==True and sp==False and up==False and low==False) or (num==False and sp==False and up==False and low==True) or (num==False and sp==False and up==True and low==False):
        print("Ненадежный пароль")
        return
    else:
        print('Слабый пароль')
        return


password_level('GJJjejc$%665')
