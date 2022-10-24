pipeline {
    agent any
    stages {
        
        stage('Code Analysis') {
            environment {
                scannerHome = tool 'SonarQubeScanner'
            }    
            steps {
                checkout scm
                withSonarQubeEnv('SonarQube') {
                    sh '${scannerHome}/bin/sonar-scanner \
                    -Dsonar.projectKey=Desafio-DevOps \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=https://sonar.frexco.com.br \
                    -Dsonar.login=${env.sonarToken}'
                }

                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        
        stage('Stage 1 main 2') {
            when {
                branch 'main'
            }
            steps {
                echo "${some_ip}"
            }
        }
    }
}
