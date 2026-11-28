pipeline {
    agent any
    environment {
        APP_URL = 'http://127.0.0.1:5015'
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching Project from Github'
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r Requirements.txt'
            }
        }
        stage('Start Flask Application') {
            steps {
                bat '''
                    cd /d "%WORKSPACE%\\Automation_Project\\Simulator"
                    start "FlaskApp" /B python app.py
                '''
            }
        }
        stage('Execute API Test') {
            steps {
                bat '''
                    cd /d "%WORKSPACE%\\Robot_API_Project\\tests"
                    python -m robot test_2.robot
                '''
            }
        }
    }
}
