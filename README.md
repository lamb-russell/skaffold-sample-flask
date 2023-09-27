
# Hello World Flask App with Minikube and Skaffold

This project provides a simple Flask "Hello World" application that can be deployed locally using Minikube and Skaffold.

The idea is to illustrate how Skaffold can keep local code in sync with a deployed container without needed to rebuild the container.  


## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Skaffold](https://skaffold.dev/docs/install/)

## Setup and Deployment

1. **Start Minikube**:
   ```bash
   minikube start
   ```

2. **Set Docker to use Minikube's Daemon**:
   ```bash
   eval $(minikube docker-env)
   ```

3. **Run Skaffold**:
   ```bash
   skaffold dev
   ```

4. **Access the Application**:
   ```bash
   minikube service hello-world
   ```

## Troubleshooting

### Browser Hanging

- **Check Skaffold's Output**: Ensure there are no errors in Skaffold's terminal output.
  
- **Check Service and Pod Status**: Ensure the service and pod are running using `kubectl get svc hello-world` and `kubectl get pods -l app=hello-world`.

- **Access Service Manually**: Use `minikube service hello-world` to open the application in a new browser window/tab.

- **Check Application Logs**: Use `kubectl logs -l app=hello-world` to view logs for any errors or issues.

- **Network Issues**: Try accessing the application from a different browser or device on the same network.

- **Minikube Tunnel**: If using a LoadBalancer service type, ensure you have `minikube tunnel` running in a separate terminal.

- **Resource Constraints**: Ensure Minikube has enough resources allocated.

- **Recreate Minikube Cluster**: If all else fails, consider restarting Minikube using `minikube stop`, `minikube delete`, and `minikube start`.

- **Skaffold Debugging**: if you have issues running in skaffold, try running with the -vdebug flag `skaffold dev -vedbug` to see verbose output.

### Skaffold Tagging Issues

Skaffold uses Git tags or commits to tag Docker images by default. If your project directory isn't a Git repository, Skaffold might fail to generate a tag using Git but will fall back to using the `latest` tag.

To address this:

1. **Initialize a Git Repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Specify a Different Tagger in `skaffold.yaml`**: Use a datetime-based tag or always use the `latest` tag.
