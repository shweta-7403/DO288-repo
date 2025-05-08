# 🚀 DO288 - Red Hat OpenShift Developer II: Building and Deploying Cloud-native Applications

### 🎯 Goal

* Deploy simple applications using:

   * The **Red Hat OpenShift Web Console**
   * The **`oc` and `odo` CLI tools**


### ✏️ Navigating the Red Hat OpenShift Web Console

* Understand **Web Console perspectives**:

  * 👨‍💼 *Administrator*: Focus on cluster resources
  * 👨‍💻 *Developer*: Focus on app development
* Use the **Topology view** for an interactive overview
* Access console via:

  ```bash
  oc whoami --show-console
  ```
---

### ⚖️ Deploying via the Web Console

* Deploy apps using:

  * 💻 Git Repositories
  * 🌁 Container Images
  * 🌐 Helm Charts or Developer Catalog

---

### 🛠️ Deploying via `oc` and `odo`

* **`oc` CLI** for YAML-based deployments

  ```bash
  oc apply -f app.yaml
  oc logs bc/my-app
  ```
* **`odo` CLI** for streamlined dev experience

  ```bash
  odo create nodejs
  odo push
  ```
---
## 🔗 Key Concepts Cheat Sheet

| Concept            | Description                              |
| ------------------ | ---------------------------------------- |
| 📦 Pod             | Basic unit: 1+ containers                |
| 👥 ReplicaSet      | Maintains pod count                      |
| 🚀 Deployment      | Declarative updates                      |
| 🔗 Service         | Internal access to pods                  |
| 📣 Route/Ingress   | External access to apps                  |
| 📂 PVC/PV          | Persistent storage for pods              |
| 🌐 Helm            | Package manager for Kubernetes/OpenShift |
| 🧰 odo             | Simplified CLI for developers            |
| 👤 Service Account | Auth identity for processes              |

---




