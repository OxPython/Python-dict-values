'''
Created on Jul 2, 2014

@author: viejoemer

How I can get the values ​​from a dictionary in Python?

¿Cómo puedo obtener los valores de un diccionario en Python?

The method values() returns a list of all the values 
available in a given dictionary.
'''

#dict with three values and keys
d = {'Name': 'Emerson', 'Age': 27,'Sex': 'Male' }
print(d)

#get the values from a dict
d_values = d.values()
print (d_values)
print(d)
