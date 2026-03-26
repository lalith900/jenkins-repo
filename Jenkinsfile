pipeline {                                    // starts the jenkins pipeline
    agent any                                 // run on any available jenkins agent

    stages {                                  // all stages go inside here

        stage('Checkout') {                   // stage 1 - pull code from github
            steps {
                git branch: 'main',                                         // which branch to pull
                    url: 'https://github.com/lalith900/jenkins-repo.git',  // your github repo url
                    credentialsId: 'github-credentials'                     // credentials saved in jenkins
            }
        }

        stage('Install Dependencies') {       // stage 2 - install required packages
            steps {
                sh 'pip install pytest --break-system-packages'       // install pytest so we can run tests
            }
        }

        stage('Run App') {                    // stage 3 - run the python program
            steps {
                sh 'python3 addition.py'      // this will print Result: 30
            }
        }

        stage('Run Tests') {                  // stage 4 - test the program
            steps {
                sh 'pytest test_addition.py -v'   // -v means show detailed test results
            }
        }

        stage('Docker Build') {               // stage 5 - build docker image
            steps {
                sh 'docker build -t lalith900/python-addition-app:latest .'  // build and tag image
            }
        }

        stage('Docker Push') {                // stage 6 - push image to dockerhub
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',  // credentials saved in jenkins
                    usernameVariable: 'DOCKER_USER',         // jenkins reads username from credentials
                    passwordVariable: 'DOCKER_PASS'          // jenkins reads password from credentials
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'  // login to dockerhub
                    sh 'docker push lalith900/python-addition-app:latest'                   // push image
                    sh 'docker logout'                                                       // logout after push
                }
            }
        }

    }

    post {                                    // runs after all stages complete
        success {
            echo 'pipeline completed - image pushed to dockerhub!'   // printed if everything passed
        }
        failure {
            echo 'pipeline failed - check the red stage above!'      // printed if anything failed
        }
    }
}
