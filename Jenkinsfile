pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/00xxxx/test.git'
            }
        }
        stage('CodeQL Analysis') {
            steps {
                script {
                    // CodeQL 데이터베이스 생성
                    sh 'codeql database create my-db --language=python'
                    // CodeQL 분석 실행
                    sh 'codeql analyse my-db --format=sarif-latest --output=results.sarif'
                }
            }
        }
        stage('Publish Results') {
            steps {
                script {
                    // 결과를 저장하고 Jenkins의 UI에서 확인할 수 있도록 설정
                    // SARIF 결과 리포트를 파악할 수 있는 방법을 추가
                    // 예를 들어, 다른 플러그인을 사용해 SARIF 결과를 보일 수 있습니다.
                }
            }
        }
    }
}
