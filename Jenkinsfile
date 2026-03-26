pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub...'
                git branch: 'main',
                    url: '',
                    credentialsId: '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'
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

    }

    post {
        success {
            echo 'Pipeline finished successfully — all tests passed!'
        }
        failure {
            echo 'Pipeline failed — check the logs above.'
        }
        always {
            cleanWs()
        }
    }
}
