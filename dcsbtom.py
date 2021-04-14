import sys, socket

new_domains = []

if len(sys.argv) < 2:
	print(
"""Using:
	python3 dcsbtom.py [domain]

   Example:
	python3 dcsbtom.py google.com
"""
)
else:
	domain = sys.argv[1]
	with open("subdomains.txt",'r') as file_object:
		subdomains = file_object.readlines()
	for subdomain in subdomains:
		DNS = subdomain.strip("\n") + domain
		try:
			full_DNS = DNS + ":    " + socket.gethostbyname(DNS)
			print(full_DNS)
			new_domains.append(str(full_DNS) + "\n")
		except socket.gaierror:
			pass
	print("\nFinalized")
	opt = input("\nDo you want to save domains in a file (Y/N)? ")
	if opt == "Y" or opt == "y":
		with open("new_domains.txt",'w') as file_obj:
			file_obj.writelines(new_domains)
		print("\nSaved")
