pipeline {
    agent any 
        stages {
            stage('compile') {
                steps {
                    echo "compiled successfully"
                }
            }
            stage('JUnit') {
                steps { 
                    echo "Success "
                }
            }
            stage('Quality Gate') {
                steps{
                    echo "SonarQube Passes Succcessfully"
                }
            }
            stage('deploy') { 
                steps {
                    echo "pass"
                }
            }
        }
    
}
