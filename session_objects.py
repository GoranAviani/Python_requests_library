import requests

#####

'''
Sessions can also be used to provide default data to the request methods. 
This is done by providing data to the properties on a Session object:
'''

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
result = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(result.text)

'''
Any dictionaries that you pass to a request method will be merged with 
the session-level values that are set. The method-level parameters override
 session parameters.
'''
