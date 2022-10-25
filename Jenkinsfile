pipeline {
    agent any

    stages {
        stage('Hello') {

                withPythonEnv('python') {
                    sh 'pip install pytest'
                    sh 'pytest app/test_main.py'
                    }


        }
    }
}