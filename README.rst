NC SSL API Client
-----------------

Command line client for communication with Namecheap SSL Api

Installation
------------
>>> pip install ncssl-api-client

General usage example
---------------------

>>> ncsslapi [command_name] [command_args] [--sandbox]

On the first run you will be requested to enter some general information required to make an api call.
This information will be stored in ``~/ncsslapi/config`` as yaml and can be easily edited.
Should you what to regenerate config, simply delete ``~/ncsslapi/config`` directory and run any command.

Environments
------------

This tool can be used in two environments:

* production (default)
* sandbox (add ``--sandbox`` flag to a command)

Available Commands
------------------

* create
* activate
* reissue
* getinfo
* retry_dcv
* renew
* revoke
* getlist
* get_email_list

Private Key and CSR generation
------------------------------

Activate and reissue commands implicitly generate private key and CSR.
All of them are stored in ``~/ncsslapi/certs/%current_year%/`` directory

Create
------
Purchases a certificate

TODO: Implement years

>>> ncsslapi create -t PositiveSSL -y 2

Activate
________
Generates CSR and activates a certificate with it

>>> ncsslapi activate -id 1111111 -cn test.example.com -e example@example.com

Should you want to create a certificate and activate it in a single command, simply add ``-new`` flag to the command

>>> ncsslapi activate -new -cn test.example.com -e example@example.com

Reissue
_______

Generates CSR and reissues a certificate with it

>>> ncsslapi reissue -id 1111111 -cn test.example.com -e example@example.com

GetInfo
_______

Shows information for a particular certificate

>>> ncsslapi getinfo -id 1111111

RetryDcv
________

Triggers domain control validation.

>>> ncsslapi retry_dcv -id 1111111

Renew
_____

Purchases a renewal certificate

>>> ncsslapi renew -id 1111111 -y 1 -t PositiveSSL

Revoke
______
Revokes a certificate

>>> ncsslapi revoke -id 1111111 -t PositiveSSL

GetList
_______
Shows list of SSL certificates in your Namecheap account

>>> ncsslapi getlist -kw example.com -f ACTIVE

GetEmailList
------------
Shows list of possible approval emails for the given domain name

>>> ncsslapi get_email_list -d example.com -t PositiveSSL




