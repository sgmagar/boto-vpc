# boto-vpc
This is the script for creation for vpc as well as vpc peering connection from command line.

## Requirements
1. Python 2.7
2. Boto3

## Usage
1. View list of command arguments:  
  *Run*: `python boto.py -h`  
  This will show list of command line arguments for required for vpc as well as peer vpc creation.
2. Arguments necessary for vpc creation:
  * `--access_key`  AWS Access key Id 
  * `--secret_key` AWS Secret Access Key
  * `--region` AWS Region Name
  * `--cidr_block` AWS cidr block
  
3. Arguments necessary for vpc peer connection:
  * `--access_key`  AWS Access key Id 
  * `--secret_key` AWS Secret Access Key
  * `--region` AWS Region Name
  * `--peer` Args to identify peer connection or vpc creation. Pass this for peer connection.
  * `--peer_owner_id` AWS Account Id of accepter VPC
  * `--peer_vpc_id` The ID of the VPC with which you are creating the VPC peering connection
  * `--vpc_id` The ID of the requester VPC
  * `--peer_region` The region code for the accepter VPC
  
  To create VPC or VPC Peer Connection, *Run*: `python boto.py ` and pass those arguments.
