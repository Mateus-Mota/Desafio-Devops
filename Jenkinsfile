pipeline {
    agent any
    
    environment {
        sonarToken = credentials('SonarQubeToken')
        dockerHome = tool 'docker'
    }
    stages {
        stage('Build docker image') {
            steps {
                script {
                    checkout scm
                    def branchName = "${env.BRANCH_NAME}"
                    sh "echo ${branchName}"
                    sh "echo ${env.BRANCH_NAME}"
                    sh "echo ${env.GIT_BRANCH}"
                    if (branchName ==~ 'origin/main') {
                        sh "echo ${GIT_BRANCH}"
                        sh "echo ${GIT_COMMITTER_NAME}" 
                    }
                }
            }
        }
        
        stage('Stage 2 main declarative') {
            when {
                branch 'origin/main'
            }
            steps {
                checkout scm
                echo "${env.BRANCH_NAME}"
                echo "${env.GIT_BRANCH}"
            }
        }
        
        stage('Build scripted') {
            steps{
                script{
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                    sh "docker --version"
                    sh "echo ${dockerHome}"
                    sh "docker build -t desafio-devops-${env.BUILD_ID} --pull -f web/Dockerfile web"
                }
            }  
        }
    }
}
