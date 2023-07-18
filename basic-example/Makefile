.DEFAULT_GOAL := help
SHELL := /usr/bin/env bash


build:  ## Build the JupyterLab GPU Image
	docker build -f Dockerfile.gpu-jupyter -t gpu-jupyter:custom .

run: build  ## Run the system
	docker compose up -d

restart: stop run  ## Restart the system
	:

stop:  ## Stop the system
	docker compose stop

example:  ## Example jupyterhub_oauth2_client_secret.json config file
	cat jupyterhub_oauth2_client_secret.json | \
	  jq 'walk(if type == "string" then "Replaced Value" else . end)'

vscode_url_example:  ## URL for VSCode Connection
	@echo "https://jupyter.domain.com/user/email@domain.com?token=__API_TOKEN__"

tail:  ## Tail the jupyterhub container logs
	docker logs -f jupyterhub

help: ## Print list of Makefile targets
	@# Taken from https://github.com/spf13/hugo/blob/master/Makefile
	@grep --with-filename -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  cut -d ":" -f2- | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' | sort
