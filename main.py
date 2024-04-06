import hashlib as aarti
from pyscript import document


def sha224_converter(event):      
    pwd = document.getElementById('sha224_input').value
    akhilesh = aarti.sha224(pwd.encode('utf-8'))
    suyash = akhilesh.hexdigest()
    print(suyash)
    output_div = document.getElementById('sha224_output')
    output_div.innerText = suyash
   