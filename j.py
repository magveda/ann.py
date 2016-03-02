import json

a = []
a.append({'file':'opa.jpg', 'box':[{'top': 5, 'label': ''}, {'top': 5}]})
a.append({'file': 'opapa.jpg', 'box':[]})
print a
print type(a)
print( json.dumps(a, sort_keys=True, indent=4, separators=(',', ': ')) )