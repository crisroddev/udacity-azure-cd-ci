# cd-ci-project-pipeline
![Python application test with Github Actions](https://github.com/crisroddev/cd-ci-project-pipeline/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

## Screen Shot Test Passing on Github Actions
![Alt text](screenshots/github-actions-test-passed.png?raw=true "Github Actions Test Passed")

# Overview

- Create Github Repo
- Create Cloud Shell environment
- Clone Github repo on cloud shell
- Add Github Actions to the repo
- Create Azure Pipeline

## Projet Arquitecture
![Alt text](screenshots/arq.png?raw=true "CD/CI Arquitecture")

## Instructions

* Project running on Azure App Service
- `az webapp up -n projectName`
![Alt text](screenshots/app-services.png?raw=true "AppServices")

* Project cloned into Azure Cloud Shell
- `git clone git@github.com:crisroddev/cd-ci-project-pipeline.git`
![Alt text](screenshots/clone-repo-cloud-shell.png?raw=true "Clone Repo")

* Passing tests that are displayed after running the `make all` command from the `Makefile`
- `make all`
![Alt text](screenshots/make-all-tests-passed.png?raw=true "Make All")

* Successful deploy of the project in Azure Pipelines.
- Login `https://dev.azure.com/`
- Create new pipeline
- Add code to use make lint
`
- script: |
        python -m venv antenv
        source antenv/bin/activate
        make install
        make lint
        make test
      workingDirectory: $(projectRoot)
      displayName: "Run Lint Tests"
`

* Running Azure App Service from Azure Pipelines automatic deployment


* Successful prediction from deployed flask app in Azure Cloud Shell.
![Alt text](screenshots/azure-pipelines.png?raw=true "Azure Pipelines")

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```
![Alt text](screenshots/make-predictions.png?raw=true "Prediction")

* Output of streamed log files from deployed application
`https://udacityproject.scm.azurewebsites.net/api/logs/docker`

![Alt text](screenshots/log-files.png?raw=true "Logs1")

`az webapp log tail`

![Alt text](screenshots/log-files-2.png?raw=true "Logs2")
![Alt text](screenshots/log-files-3.png?raw=true "Logs3")

## Locust
![Alt text](screenshots/locust.png?raw=true "Logs2")

## Enhancements
How I would improve the project:
- Have an Stage and Production environment
- When stage its OK passes everything then you make the commit to production with a reviewer that accepts the new commit

## Demo 
* Link to Project Demo
https://youtu.be/YHhkOw0Sfjg


