# AppRoll
Portable Ansible role which let automate lifecycle of Java Application instances through multiple sites and environments.

## Requirements
1. Ansible (latest)
2. Identical target servers
3. Privileged user for provisioning

## Usage (Recommended to use with [AppHook](https://github.com/teymurgahramanov/AppHook))
### Deploy
1. Create manifest file as [example](https://github.com/teymurgahramanov/AppRoll/blob/main/approll/vars/main/foo.yml)
2. Add Application assests as [example](https://github.com/teymurgahramanov/AppRoll/tree/main/approll/templates/foo)
3. Deploy using Ansible (```ansible-playbook approll.yml -i approll.ini --extra-vars "app_name=%yourappname% app_env=%yourappenv% app_loc=%yourapploc" --tags "deploy"```), [AppHook](https://github.com/teymurgahramanov/AppHook)  or GitLab Pipeline
### Remove
```ansible-playbook approll.yml -i approll.ini --extra-vars "app_name=%yourappname% app_env=%yourappenv% app_loc=%yourapploc" --tags "remove"```