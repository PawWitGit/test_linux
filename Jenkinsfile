podTemplate(inheritFrom: 'k8s-slave', containers: [
    containerTemplate(name: 'py38', image: 'python:3.8.4-slim-buster', ttyEnabled: true, command: 'cat')
  ])
{
    node(POD_LABEL) {

        stage('Checkout') {
            checkout scm
            sh 'ls -lah'
        }

        container('py38') {
            stage('Poetry Configuration') {
                sh 'apt-get update && apt-get install -y curl'
                sh "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python"
                sh "$HOME/.poetry/bin/poetry install --no-root"
            }

            stage('Lint') {
                sh "$HOME/.poetry/bin/poetry run 'pre-commit install'"
                sh "$HOME/.poetry/bin/poetry run 'pre-commit run --all'"
            }
        }
    }
}

pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            steps {
                sh 'python app/test_main.py'
            }
        }

    }
}