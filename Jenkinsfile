pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'your-dockerhub-username/daynotes-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://registry-1.docker.io', 'dockerhub-credentials') {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    sh '''
                        docker stop daynotes-app || true
                        docker rm daynotes-app || true
                        docker run -d --name daynotes-app -p 8000:8000 ${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }
    }
    
    post {
        always {
            sh 'docker system prune -f'
        }
    }
}