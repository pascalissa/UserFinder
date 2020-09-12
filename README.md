# UserFinder
Small tool for searching users.

This tool searchs all your defined urls for the given username. It checkes for existance of an account with the given name and list them.

## Legal disclaimer
I've written this tool which is not intended to do illegal stuff. I'm not responsible if you break the law.

## Prerequisites

Python2.x

## Installation
Step 1:
```sh
git clone https://github.com/strider-paff-shell/UserFinder.git
```

Step 2:
```
python userfinder.py -h
```

## Manual
```
python userfinder.py -h
```
To show all available options

```
python userfinder.py -n <username>
```
To search the existence of an given username for all urls in the config

```
python userfinder.py -n <username> -u "<url/{u}>"
```
To search the existence of an given username for a specifc url

The pattern {u} is the placeholder for the username which the url should have.

## Configuration

The file errors.conf holds all possible error or not found messages
the file urls.conf holds all urls which you want to try when you search for a given user
The file useragents.conf holds all possible useragents which you can modify

## Add a new url
To add a new url to the urls.conf, you have to copy the desired url of an user profile and replace the username with the pattern {u}
