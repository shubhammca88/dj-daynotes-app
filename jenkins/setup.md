# Jenkins Setup Guide

## Prerequisites
1. Jenkins server with Docker plugin installed
2. DockerHub account
3. Docker installed on Jenkins agent

## Jenkins Configuration

### 1. Install Required Plugins
- Docker Pipeline Plugin
- Docker Plugin
- Git Plugin

### 2. Configure DockerHub Credentials
1. Go to Jenkins → Manage Jenkins → Manage Credentials
2. Add new credential:
   - Kind: Username with password
   - ID: `dockerhub-credentials`
   - Username: Your DockerHub username
   - Password: Your DockerHub password/token

### 3. Create Pipeline Job
1. New Item → Pipeline
2. Pipeline Definition: Pipeline script from SCM
3. SCM: Git
4. Repository URL: Your repository URL
5. Script Path: `Jenkinsfile`

## Environment Variables to Update
- Replace `your-dockerhub-username` in Jenkinsfile and docker-compose.yml
- Update deployment target server if needed

## Deployment Options

### Option 1: Direct Docker Run (Current)
- Deploys to same server as Jenkins
- Uses docker run commands

### Option 2: Docker Compose
```bash
docker-compose up -d
```

### Option 3: Kubernetes (Advanced)
- Use kubectl commands in deploy stage
- Requires k8s cluster setup