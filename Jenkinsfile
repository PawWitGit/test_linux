pipeline {
    agent any
    stages {

        stage('Build') {

            withPythonEnv('python3'){
                sh 'pip install pytest'
                sh 'pytest app/test_main.py'
            }
        }
    }
}