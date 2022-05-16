import secrets
print('Printing integer from secrets module')
passwordresetLink = "http://khinezarthwe.com/supergenius/reset="
passwordresetLink+=secrets.token_urlsafe(32)
print('Result is ',passwordresetLink)