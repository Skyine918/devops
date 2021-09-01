pipeline {
    agent {
        docker {
            image 'python:3.8-slim'
        }
    }
    stages {
        stage('Setup Python') {
            steps {
                echo "Setup Python:"
                sh 'python pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Linters'){
            steps {
                echo "Running pylint:"
                sh "cd app_python"
                sh "pylint ."
            }
        }
        stage('Unit Test'){
            steps {
                echo "Running django tests:"
                sh "cd app_python"
                sh "python3 manage.py test"
            }
        }
    }
}