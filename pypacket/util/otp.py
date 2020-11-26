import onetimepass as otp
def otpcheck(my_token):
    my_secret = "JVMVAQKDJNCVIRKOINHUIRKS"
    #my_token = 662120
    is_valid = otp.valid_totp(token=my_token, secret=my_secret)
    print(is_valid)

if __name__ == '__main__':
    otpcheck("")
    
