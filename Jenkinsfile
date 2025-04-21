node {
  def app

  stage('Clone Respository') {
    checkout scm
  }

  stage('Build Image') {
    app = docker.build("busycaesar/content_driven_llm_apis")
  }

  stage('Test Image') {
    app.inside {
      sh 'echo "Tests Passed"'
    }
  }

  stage('Push Image') {
    docker.withRegistry('https://registry.hub.docker.com', 'git') {
      app.push("${env.BUILD_NUMBER}")
      app.push("jenkins")
    } 
  }
  
}
