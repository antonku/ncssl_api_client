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

* :create:`create-label`
* activate
* reissue
* getinfo
* retryDcv
* renew
* revoke
* getlist
* getemailist

.. _create-label:
Create
------

Activate
________

Reissue
_______

GetInfo
_______

RetryDcv
________

Renew
_____

Revoke
______

GetList
_______

GetEmailList
------------




