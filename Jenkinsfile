pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }
        stage('PMD Analysis') {
            steps {
                pmd canComputeNew: false, defaultEncoding: '', healthy: '', pattern: '**/src/**/*.java', unstable: '', thresholdLimit: 'normal'
            }
        }
        stage('SpotBugs Analysis') {
            steps {
                spotbugs pattern: '**/target/spotbugsXml.xml', effort: 'Max', reportLevel: 'Low'
            }
        }
        stage('FindSecurityBugs Analysis') {
            steps {
                findbugsPattern: '**/target/findbugsXml.xml', pattern: '**/target/findsecbugsXml.xml'
            }
        }
    }
    post {
        always {
            // 분석 결과 보고
            recordIssues enabledForFailure: true, tools: [pmd(), spotBugs(), findSecurityBugs()]
        }
    }
}
