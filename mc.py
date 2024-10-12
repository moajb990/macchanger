#import libraries

import subprocess
import optparse
import re

# this is a reader that will take a network interface and mac address
def get_arg():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface", dest="net_if", help="This place for network interface")
	parser.add_option("-m","--mac", dest="new_mac", help="This place for mac address")
	options, arguments = parser.parse_args()

	if not options.net_if:
		parser.error("[-] You Forgot To Put Network Interface, Type -h,--help For Usage")
	if not options.new_mac:
		parser.error("[-] You Forgot The Mac Address, Type -h,--help For Usage")
		
		
	return options

# these are sysytem command that will change the mac address for a network inter face
def mac_changer(network_interface,new_macadd):
	subprocess.call("ifconfig " + options.net_if + " down", shell=True)
	subprocess.call("ifconfig " + options.net_if + " hw ether " + options.new_mac, shell=True)
	subprocess.call("ifconfig " + options.net_if + " up", shell=True)
	print ("[+]Changing Mac Address To > " + options.new_mac)

#ifconfig for more acc that the script doing well / filtering mac address
def filtering_mac(network_interface):
	ifconfig_result = subprocess.check_output("ifconfig " + options.net_if, shell=True).decode("UTF-8")
	mac_address = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
	return mac_address[0]

options = get_arg()
mac_changer(options.net_if,options.new_mac)
mac_address = filtering_mac(options.net_if)
if mac_address == options.new_mac:
	print ("[+] mac address has been changed successfully to > " + options.new_mac)
else:
	print ("something wentworng")
