email = input("What's your email? ").strip()
username, domain = email.split('@')

if username and ("." in domain) and (domain.endswith('.edu') or domain.endswith('.com') or domain.endswith('.com.br')):
    print('valid')
else:
    print('invalid')