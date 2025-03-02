# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Configuration file for JupyterHub
import os
import json

c = get_config()  # noqa: F821

# We rely on environment variables to configure JupyterHub so that we
# avoid having to rebuild the JupyterHub container every time we change a
# configuration parameter.

# Spawn single-user servers as Docker containers
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# Spawn containers from this image
c.DockerSpawner.image = os.environ["DOCKER_NOTEBOOK_IMAGE"]

# JupyterHub requires a single-user instance of the Notebook server, so we
# default to using the `start-singleuser.sh` script included in the
# jupyter/docker-stacks *-notebook images as the Docker run command when
# spawning containers.  Optionally, you can override the Docker run command
# using the DOCKER_SPAWN_CMD environment variable.
spawn_cmd = os.environ.get("DOCKER_SPAWN_CMD", "start-singleuser.sh")
c.DockerSpawner.cmd = spawn_cmd

# Connect containers to this Docker network
network_name = os.environ["DOCKER_NETWORK_NAME"]
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name

# Explicitly set notebook directory because we'll be mounting a volume to it.
# Most `jupyter/docker-stacks` *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention.
notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/jovyan/work")
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
#   home directory in the container.  Changed from the original notebook_dir
#   because ~/.cache directories were not persisted.  This will persist
#   everything under the home directory.
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": "/home/jovyan"}

# Remove containers once they are stopped
c.DockerSpawner.remove = True

# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True

# User containers will access hub by container name on the Docker network
c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.hub_port = 8080

# Persist hub data on volume mounted inside container
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

# DEFAULTS
# Authenticate users with Native Authenticator
# c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"
# Allow anyone to sign-up without approval
# c.NativeAuthenticator.open_signup = False

# Allowed admins
# admin = "admin"
# if admin:
#     c.Authenticator.admin_users = [admin]

#####################################################################
# Nvidia
##  sudo apt-get install nvidia-container-toolkit
c.DockerSpawner.extra_host_config = {'runtime': 'nvidia'}

#####################################################################
# Google Oauth

oauth_config = json.load(open('jupyterhub_oauth2_client_secret.json'))
c.JupyterHub.authenticator_class = "google"
c.OAuthenticator.oauth_callback_url = oauth_config['web']['redirect_uris'][0]
c.OAuthenticator.client_id = oauth_config['web']['client_id']
c.OAuthenticator.client_secret = oauth_config['web']['client_secret']
c.OAuthenticator.admin_users = oauth_config['custom']['admin_users']
c.OAuthenticator.allowed_users = oauth_config['custom']['allowed_users']
c.OAuthenticator.allow_existing_users = False
