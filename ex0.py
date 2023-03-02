import requests

def get_url():
    url = input("Παρακαλώ εισάγετε ένα URL: ")
    return url

url = get_url()

response = requests.get(url)

print("Οι κεφαλίδες είναι:")
for header, value in response.headers.items():
    print(header + ": " + value)


#Για τον server που χρησιμοποιω:
print("Το λογισμικο του web server είναι: {}".format(response.headers['Server']))

#Για τα cookies
A = response.headers['Set-Cookie'].split(';')
for i in range(len(A)):
    if 'expires' in A[i]:
        print("Τo cookie {} , {}".format(A[i-1],A[i]))


