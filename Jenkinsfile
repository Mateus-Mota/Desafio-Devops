pipeline {
    agent any
    
    options {
        skipDefaultCheckout(true)
    }
    environment {
        sonarToken = credentials('SonarQubeToken')
        jenkins_agent = credentials('jenkins')
        dockerHome = tool 'docker'
        scannerHome = tool 'SonarQubeScanner'
    }
    stages {
        stage('Checkout scm scripted') {
            steps {
                cleanWs()
                checkout scm
            }
        }
        
        stage ('Code Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '${scannerHome}/bin/sonar-scanner \
                    -Dsonar.projectKey=desafio-devops \
                    -Dsonar.sources=./web \
                    -Dsonar.exclusions=.*,Dockerfile,*.md,*.yml,*.conf \
                    -Dsonar.host.url=http://sonarqube:9000 \
                    -Dsonar.login=${sonarToken}'
                }
            
            }
        }
        
        stage('Build scripted') {
            steps{
                script{
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                    sh "docker build -t desafio-devops-${env.BUILD_ID} --pull -f web/Dockerfile web"
                }
            }  
        }
        
        stage('Deploy') {
            steps {
                script {
                    sh "echo ${jenkins_agent}"
                    def remote = [:]
                    remote.name = "Agent 2"
                    remote.host = "${env.AGENT_2}"
                    remote.allowAnyHosts = true
                    withCredentials([sshUserPrivateKey(credentialsId: "${jenkins_agent}", keyFileVariable: 'private_key', usernameVariable: 'sshUser')]) {
                        remote.user = sshUser
                        remote.identityFile = private_key
                        sshCommand remote: remote, command: "docker ps -a"
                    }
                }
            }
        }
        
    }
}
