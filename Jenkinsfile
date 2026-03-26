pipeline {
    agent any

    environment {
        IMAGE_NAME = 'python-addition-app'
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/lalith900/jenkins-repo.git',
                    credentialsId: 'github-credentials'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing required packages...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running the addition program...'
                sh '''
                    . venv/bin/activate
                    python3 addition.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running test cases...'
                sh '''
                    . venv/bin/activate
                    pytest test_addition.py -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Verify Image') {
            steps {
                echo 'Verifying Docker image...'
                sh '''
                    docker images | grep ${IMAGE_NAME}
                    docker run --rm ${IMAGE_NAME}:latest
                '''
            }
        }

    }

    post {
        success {
            echo 'Docker image built successfully!'
            sh 'docker images | grep ${IMAGE_NAME}'
        }
        failure {
            echo 'Pipeline failed — check logs above.'
        }
        always {
            cleanWs()
        }
    }
}
