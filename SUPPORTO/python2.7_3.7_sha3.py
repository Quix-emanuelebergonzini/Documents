py 3.7
chain = ['idCZOCQ77gVnCWd1T77R1w', '20200121093144', '66-8ac3-8b0bd50b409227BJ982CRB0X']
chain = ''.join(chain)
encoded_str = chain.encode()
hashlib.sha3_512(encoded_str).hexdigest().upper()

py 2.7 --> dove sha3 è un file sha3.py
import sha3
/Library/Python/2.7/site-packages/pysha3-1.0.2-py2.7-macosx-10.13-intel.egg/_pysha3.py:3: UserWarning: Module _pysha3 was already imported from /Library/Python/2.7/site-packages/pysha3-1.0.2-py2.7-macosx-10.13-intel.egg/_pysha3.pyc, but /Users/emanuelebergonzini/Downloads/pysha3-1.0.2 is being added to sys.path
new = sha3.sha3_512()
new.update('idCZOCQ77gVnCWd1T77R1w2020012109314466-8ac3-8b0bd50b409227BJ982CRB0X')
 new.hexdigest()
'a24e0e3988e028d75381d0b8f0aa53a10c930c03e7ce12171be834866817959104651c7df614a2a99043910e44bd3ba4acd7d09a089481a6fee9a36bfa12ae1e'
