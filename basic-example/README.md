
### Makefile

```shell
$ make
build                          Build the JupyterLab GPU Image
example                        Example jupyterhub_oauth2_client_secret.json config file
help                           Print list of Makefile targets
restart                        Restart the system
run                            Run the system
stop                           Stop the system
tail                           Tail the jupyterhub container logs
vscode_url_example             URL for VSCode Connection
```


### Configure

* Download google oauth client secrets into json doc
* Add a few "custom fields" to assign privileges to users in JupyterHub
* Filename: jupyterhub_oauth2_client_secret.json

```json
{
  "web": {
    "client_id": "Replaced Value",
    "project_id": "Replaced Value",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "Replaced Value",
    "redirect_uris": [
      "https://jupyter.domain.com/hub/oauth_callback"
    ],
    "javascript_origins": [
      "https://jupyter.domain.com"
    ]
  },
  "custom": {
    "admin_users": [
      "admin@domain.com"
    ],
    "allowed_users": [
      "user1@domain.com",
      "user2@domain.com"
    ]
  }
}
```

* Note: Above created with `cat jupyterhub_oauth2_client_secret.json | jq 'walk(if type == "string" then "Replaced Value" else . end)'`
