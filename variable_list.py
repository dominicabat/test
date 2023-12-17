
Recov_IP_block = ['10.10.10.0', '11.11.11.0']
src_node = 'SRC NODE A'

Alloc_IP_block = ['10.10.10.0', '11.11.11.0']
dst_node = 'DST NODE B'

mask = 21
method = 'transfer'
check_commands = ['sh users | i ','sh run | i ','sh ip local pool | i ']


#added comment

#Recov_IP_block: list of Prefixes to be recovered
#src_node: node where the IP is going to be removed 

#Alloc_IP_Block: list of Prefixes to be allocated 
#dst_node: node where the IP is going to be configured 

#mask: subnet mask
#method: could be (allocate, recover, transter, swap) - allocate when from IPAM, recover when node to IPAM, transfer when node to another node, swap when an IP from IPAM will replace an IP in node

