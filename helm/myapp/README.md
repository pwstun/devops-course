myapp Helm chart

To template for dev:

  helm template . --values values.yaml

For staging:

  helm template . --values values-staging.yaml

For production:

  helm template . --values values-production.yaml


Perfect — let’s build a Kind-based Kubernetes lab from zero, the same way you’d use it with GitHub Actions and Helm later.

I’ll keep it practical so you can follow along step-by-step.

🧠 What you’re building

You’ll end up with:

Local Kubernetes cluster using Kind
kubectl configured
Helm installed
A test app deployed
⚙️ 0. Prerequisites

You need:

✅ Docker

Install:

Docker Desktop (Windows/Mac)
or Docker Engine (Linux)

Check:

docker --version
✅ kubectl

Install CLI for Kubernetes:

kubectl version --client

Install (if needed):

# Windows (choco)
choco install kubernetes-cli

# Mac
brew install kubectl

# Linux
sudo apt install kubectl
✅ Kind

Install Kind:

# Mac / Linux
brew install kind

# Windows
choco install kind

Check:

kind --version
✅ Helm (for later)

Install Helm:

brew install helm
🚀 1. Create your first cluster
kind create cluster --name dev-cluster
🔍 Verify it
kubectl cluster-info
kubectl get nodes

You should see:

NAME                 STATUS   ROLES           AGE
dev-cluster-control-plane   Ready    control-plane
🧩 2. (Optional but 🔥) Multi-node cluster

Create config file:

# kind-config.yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker

Run:

kind create cluster --name dev-cluster --config kind-config.yaml
📦 3. Deploy your first app (kubectl way)

Create a simple deployment:

kubectl create deployment hello --image=nginx

Expose it:

kubectl expose deployment hello --type=NodePort --port=80

Check:

kubectl get services
🌐 4. Access the app

Kind doesn’t expose ports by default, so:

kubectl port-forward service/hello 8080:80

Now open:

http://localhost:8080
📊 5. Inspect cluster

Useful commands:

kubectl get pods
kubectl get svc
kubectl describe pod <name>
kubectl logs <pod>
📦 6. Deploy using Helm (real-world way)

Create a chart:

helm create my-app

Install it:

helm install my-app ./my-app

Check:

helm list
kubectl get all
🔁 7. Load local Docker images into Kind

This is KEY for local dev.

If you build an image:

docker build -t my-app:local .

Kind can’t see it automatically, so:

kind load docker-image my-app:local --name dev-cluster

Then use it in your deployment:

image: my-app:local
imagePullPolicy: Never
🧪 8. Simulate CI/CD locally (very powerful)

You can mimic GitHub Actions flow:

Build image
Load into Kind
Deploy via Helm

👉 This is exactly what happens in cloud — just locally.

🧹 9. Delete cluster (when done)
kind delete cluster --name dev-cluster
🔥 Recommended project structure
project/
├── app/
│   └── Dockerfile
├── helm/
│   └── my-app/
├── k8s/ (optional raw YAMLs)
├── .github/workflows/
⚡ Pro Tips (this saves hours)
💡 Use ingress (optional advanced)

Install NGINX ingress in Kind:

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
💡 Use namespaces
kubectl create namespace dev
helm install my-app ./my-app -n dev
💡 Debug faster
kubectl get events
🧠 Mental model after this

Once this works, you already understand:

Kubernetes basics ✅
Helm deployments ✅
Image lifecycle ✅
CI/CD flow ✅

👉 Moving to Azure Kubernetes Service later becomes trivial.

🚀 If you want next step

I can help you:

Turn this into a real GitHub Actions pipeline using Kind
Add auto-deploy on push
Or build a production-ready Helm chart for your app

Just tell me what stack you're using 👍