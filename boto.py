import boto3
import sys
import argparse

parser = argparse.ArgumentParser(description='VPC configuration args')
parser.add_argument('--access_key', help='AWS Access key id')
parser.add_argument('--secret_key', help='AWS Secret Access Key')
parser.add_argument('--region', help='AWS region name ')
parser.add_argument('--cidr_block', help='VPC IP range in format 10.0.0.0/16')
parser.add_argument('--peer', help='Set this args to start peer vpc connection')
parser.add_argument('--peer_owner_id', help='Aws account id of accepter VPC')
parser.add_argument('--peer_vpc_id', help='The ID of the VPC with which you are creating the VPC peering connection')
parser.add_argument('--vpc_id', help='The ID of the requester VPC')
parser.add_argument('--peer_region', help='The region code for the accepter VPC')

args = parser.parse_args()
args = vars(args)

if all (k in args for k in ('access_key', 'secret_key', 'region'):
    sys.exit('You have to provide both aws access_key, secret key, cidr_block and region')

client = boto3.client(
	'ec2', region_name=args.get('region'), aws_access_key_id=args.get('access_key'), 
	aws_secret_access_key=args.get('secret_key'))

if args.get('peer'):
	if all (k in foo for k in ('peer_owner_id', 'peer_vpc_id', 'vpc_id', 'peer_region'):
		create_peer_vpc_connection(args)
	else:
		sys.exit('You have to pass peer_owner_id, peer_vpc_id, vpc_id, peer_region as args to create vpc peering commection')
	
else:
	if args.get('cidr_block'):
		cidr_block = args.get('cidr_block')
		create_vpc(cidr_block):
	else:
		sys.exit('You have to pass cidr_block as args to create vpc')
	


def create_vpc(cidr_block)
	response = client.create_vpc(
    	CidrBlock='10.0.0.0/16',
	)
	if response.get('Vpc') and response.get('Vpc').get('VpcId'):
		vpc_id = (response.get('Vpc').get('VpcId')
		with open('vpc.txt', 'a') as f:
			f.write('VPC_ID: {}'.format(vpc_id))
		print('VPC creation successfull with ID: {}'.format(vpc_id))
	else:
		print('Failed to create VPC')


def create_peer_vpc_connection(data):
	peer_owner_id = data.get('peer_owner_id')
	peer_vpc_id = data.get('peer_vpc_id')
	vpc_id = data.get('vpc_id')
	peer_region = data.get('peer_region')
	response = client.create_vpc_peering_connection(
	    PeerOwnerId=peer_owner_id,
	    PeerVpcId=peer_vpc_id,
	    VpcId=vpc_id,
	    PeerRegion=peer_region
	)
	if response.get('VpcPeeringConnection') and response.get('VpcPeeringConnection').get('VpcPeeringConnectionId'):
		vpc_peer_commecction_id = response.get('VpcPeeringConnection').get('VpcPeeringConnectionId')
		with open('vpc.txt', 'a') as f:
			f.write('VPC_PEER_CONNECTION_ID: {}, with vpc_id={} and peer_vpc_id={}'.format())
		print('VPC peer connection creation successfull with connection_id: {}'.format(vpc_peer_commecction_id))
	else:
		print("Failed to create vpc peering connection")