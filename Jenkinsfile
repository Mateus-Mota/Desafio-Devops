pipeline {
    agent any
    
    options {
        skipDefaultCheckout(true)
    }
    environment {
        sonarToken = credentials('SonarQubeToken')
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
                    def remote = [:]
                    remote.name = "Agent 2"
                    remote.host = "${env.AGENT_2}"
                    remote.allowAnyHosts = true
                    withCredentials([sshUserPrivateKey(credentialsId: 'jenkins', keyFileVariable: 'private_key', usernameVariable: 'sshUser')]) {
                        remote.user = sshUser
                        remote.identityFile = private_key
                        sshCommand remote: remote, command: "docker ps -a"
                    }
                }
            }
        }
        
        post {
            always {
                script {
                    final String url = "https://api.telegram.org/$env.TOKEN/sendMessage"
                    final String text = "<b>Job</b>: $env.JOB_NAME\n<b>Build</b>: #$env.BUILD_NUMBER - $currentBuild.currentResult - <a href=\\\"$env.BUILD_URL\\\">Link</a>\n<b>Duration</b>: $currentBuild.durationString"
                    sh(script: "echo '-s -X POST \"$url\" -d chat_id=\"-$env.CHAT_ID\" -d parse_mode=\"HTML\" -d text=\"$text\"'")
                }
            }
        }
        
    }
}
