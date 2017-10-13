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
Should you what to regenerate config, simply delete ``~/ncsslapi/config`` directory and run any ``ncsslapi`` command.

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

>>> ncsslapi create -t EssentialSSL
>>> ncsslapi create -t PositiveSSL -y 2

**Arguments**

+----------+-----------+--------------------------------------------------------------------------+----------+
| ShortCut | Full Name | Description                                                              | Required |
+----------+-----------+--------------------------------------------------------------------------+----------+
| -t       | --type    | Certificate Type. See list of available options in the dedicated section | Yes      |
+----------+-----------+--------------------------------------------------------------------------+----------+
| -y       | --years   | The number of year to purchase certificate for. Default is 1.            | No       |
+----------+-----------+--------------------------------------------------------------------------+----------+

Activate
________
Generates CSR and activates a certificate with it

>>> ncsslapi activate -id 1111111 -cn test.example.com -e admin@example.com

Should you want to create a certificate and activate it in a single command, simply add ``-new`` flag to the command

>>> ncsslapi activate -new -cn test.example.com -e admin@example.com

There are three possible options for domain control validation (DCV):

* Email DCV: ``ncsslapi activate -id 1111111 -cn test.example.com -e admin@example.com``
* HTTP DCV: ``ncsslapi activate -id 1111111 -cn test.example.com -http``
* DNS DCV: ``ncsslapi activate -id 1111111 -cn test.example.com -dns``


**Arguments**

+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| ShortCut | Full Name    | Description                                                                                             | Required      |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| -cn      | --common_name| Namecheap certificate ID to activate. Should be skipped if ``-new`` parameter is specified              | Yes           |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| -id      | --id         | Namecheap certificate ID to activate. Should be skipped if ``-new`` parameter is specified              | Conditionally |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| -new     | --new        | If added, certificate will be purchased prior to activation. This argument must be used without a value | Conditionally |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| -e       | --email      | Approver email address. Must be specified unless DNS or HTTP dcv is preferred                           | Conditionally |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| -http    | --http_dcv   | Sets domain control validation to HTTP method. This argument must be used without a value               | Conditionally |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| -dns     | --dns_dcv    | Sets domain control validation to DNS (CNAME) method. This argument must be used without a value        | Conditionally |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| -enc     | --ecnrypt    | If set, private key will be encrypted with a passphrase. This argument must be used without a value     | No            |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| -t       | --type       | Certificate Type. See list of available options in the dedicated section                                | Yes           |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+
| -y       | --years      | The number of year to purchase certificate for. Default is 1.                                           | No            |
+----------+--------------+---------------------------------------------------------------------------------------------------------+---------------+


Reissue
_______

Generates CSR and reissues a certificate with it

>>> ncsslapi reissue -id 1111111 -cn test.example.com -e admin@example.com
>>> ncsslapi reissue -id 1111111 -cn test.example.com -http
>>> ncsslapi reissue -id 1111111 -cn test.example.com -dns -enc

**Arguments**

+----------+---------------+-----------------------------------------------------------------------------------------------------+---------------+
| ShortCut | Full Name     | Description                                                                                         | Required      |
+----------+---------------+-----------------------------------------------------------------------------------------------------+---------------+
| -cn      | --common_name | Common name to reissue certificate for                                                              | Yes           |
+----------+---------------+-----------------------------------------------------------------------------------------------------+---------------+
| -id      | --id          | Namecheap certificate ID to reissue.                                                                | Yes           |
+----------+---------------+-----------------------------------------------------------------------------------------------------+---------------+
| -e       | --email       | Approver email address. Must be specified unless DNS or HTTP dcv is preferred                       | Conditionally |
+----------+---------------+-----------------------------------------------------------------------------------------------------+---------------+
| -http    | --http_dcv    | Sets domain control validation to HTTP method. This argument must be used without a value           | Conditionally |
+----------+---------------+-----------------------------------------------------------------------------------------------------+---------------+
| -dns     | --dns_dcv     | Sets domain control validation to DNS (CNAME) method. This argument must be used without a value    | Conditionally |
+----------+---------------+-----------------------------------------------------------------------------------------------------+---------------+
| -enc     | --ecnrypt     | If set, private key will be encrypted with a passphrase. This argument must be used without a value | No            |
+----------+---------------+-----------------------------------------------------------------------------------------------------+---------------+

GetInfo
_______

Shows information for a particular certificate

>>> ncsslapi getinfo -id 1111111

**Arguments**

+----------+---------------+---------------------------------------------------------------+----------+
| ShortCut | Full Name     | Description                                                   | Required |
+----------+---------------+---------------------------------------------------------------+----------+
| -id      | --id          | Namecheap certificate ID to show information for              | Yes      |
+----------+---------------+---------------------------------------------------------------+----------+
| -rc      | --return_certs| Show certificates in response                                 | No       |
+----------+---------------+---------------------------------------------------------------+----------+

RetryDcv
________

Triggers domain control validation.

>>> ncsslapi retry_dcv -id 1111111

**Arguments**

+----------+-----------+---------------------------------------------------------------+----------+
| ShortCut | Full Name | Description                                                   | Required |
+----------+-----------+---------------------------------------------------------------+----------+
| -id      | --id      | Namecheap certificate ID to retry DCV for                     | Yes      |
+----------+-----------+---------------------------------------------------------------+----------+

Renew
_____

Purchases a renewal certificate

>>> ncsslapi renew -id -t EssentialSSL
>>> ncsslapi renew -id 1111111 -y 1 -t PositiveSSL

**Arguments**

+----------+-----------+-------------------------------------------------------------------------------------+----------+
| ShortCut | Full Name | Description                                                                         | Required |
+----------+-----------+-------------------------------------------------------------------------------------+----------+
| -id      | --id      | Namecheap certificate ID of an expiring certificate                                 | Yes      |
+----------+-----------+-------------------------------------------------------------------------------------+----------+
| -t       | --type    | Type of certificate. See the list the of available options in the dedicated section | Yes      |
+----------+-----------+-------------------------------------------------------------------------------------+----------+
| -y       | --years   | Number of years to purchase renewal for. Default is 1.                              | No       |
+----------+-----------+-------------------------------------------------------------------------------------+----------+

Revoke
______
Revokes a certificate

>>> ncsslapi revoke -id 1111111 -t PositiveSSL

**Arguments**

+----------+-----------+---------------------------------------------------------------------------------------------+----------+
| ShortCut | Full Name | Description                                                                                 | Required |
+----------+-----------+---------------------------------------------------------------------------------------------+----------+
| -id      | --id      | Namecheap certificate ID to revoke                                                          | Yes      |
+----------+-----------+---------------------------------------------------------------------------------------------+----------+
| -t       | --type    | Type of revoked certificate. See the list the of available options in the dedicated section | Yes      |
+----------+-----------+---------------------------------------------------------------------------------------------+----------+

GetList
_______
Shows list of SSL certificates in your Namecheap account

>>> ncsslapi getlist -kw
>>> ncsslapi getlist -kw example.com -f ACTIVE -s PURCHASEDATE

**Arguments**

+----------+------------+-----------------------------------------------------------------------------------------------------+---------------+
| ShortCut | Full Name  | Description                                                                                         | Required      |
+----------+------------+-----------------------------------------------------------------------------------------------------+---------------+
| -kw      | --keyword  | Show only items that match the key word, can be a domain for example                                | No            |
+----------+------------+-----------------------------------------------------------------------------------------------------+---------------+
| -f       | --filter   | Filters the result, see the list of available options in the dedicated section                      | No            |
+----------+------------+-----------------------------------------------------------------------------------------------------+---------------+
| -s       | --sort_by  | Sorts the result, see the list of available options in the dedicated section                        | No            |
+----------+------------+-----------------------------------------------------------------------------------------------------+---------------+

GetEmailList
------------
Shows list of possible approval emails for the given domain name

>>> ncsslapi get_email_list -d example.com -t PositiveSSL

**Arguments**

+----------+-----------+-------------------------------------------------------------------------------------+----------+
| ShortCut | Full Name | Description                                                                         | Required |
+----------+-----------+-------------------------------------------------------------------------------------+----------+
| -d       | --domain  | Domain name to gather approver emails for                                           | Yes      |
+----------+-----------+-------------------------------------------------------------------------------------+----------+
| -t       | --type    | Type of certificate. See the list the of available options in the dedicated section | Yes      |
+----------+-----------+-------------------------------------------------------------------------------------+----------+

Enumerables
___________

**Certificate Types**

* PositiveSSL
* EssentialSSL
* PositiveSSL Wildcard
* EssentialSSL Wildcard
* PositiveSSL Multi Domain
* InstantSSL
* InstantSSL Pro
* PremiumSSL
* PremiumSSL Wildcard
* Multi Domain SSL
* Unified Communications
* EV SSL
* EV Multi Domain SSL

**Sorters**

* PURCHASEDATE
* PURCHASEDATE_DESC
* SSLTYPE
* SSLTYPE_DESC
* EXPIREDATETIME
* EXPIREDATETIME_DESC
* Host_Name
* Host_Name_DESC

**Filters**

* Processing
* EmailSent
* TechnicalProblem
* InProgress
* Completed
* Deactivated
* Active
* Cancelled
* NewPurchase
* NewRenewal

