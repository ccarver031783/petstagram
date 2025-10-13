import kopf
import kubernetes

def configure_k8s():
    try:
        kubernetes.config.load_incluster_config()
    except kubernetes.config.ConfigException:
        kubernetes.config.load_kube_config()

def build_deployment(name, image):
    return {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {'name': name},
        'spec': {
            'replicas': 1,
            'selector': {'matchLabels': {'app': name}},
            'template': {
                'metadata': {'labels': {'app': name}},
                'spec': {
                    'imagePullSecrets': [{'name': 'ghcr-secret'}],
                    'containers': [{
                        'name': name,
                        'image': image,
                        'ports': [{'containerPort': 8000}]
                    }]
                }
            }
        }
    }

@kopf.on.create('petbook.dev', 'v1', 'userprofileservices')
def create_fn(spec, **kwargs):
    name = spec.get('name', 'userprofile')
    image = spec.get('image')

    print(f"🚀 Creating Deployment '{name}' with image '{image}'")

    configure_k8s()
    api = kubernetes.client.AppsV1Api()
    deployment = build_deployment(name, image)
    api.create_namespaced_deployment(namespace='default', body=deployment)

@kopf.on.update('petbook.dev', 'v1', 'userprofileservices', field='spec.image')
def update_image(spec, **kwargs):
    name = spec.get('name')
    image = spec.get('image')

    print(f"🔁 Patching Deployment '{name}' to image '{image}'")

    configure_k8s()
    api = kubernetes.client.AppsV1Api()
    patch = {
        "spec": {
            "template": {
                "spec": {
                    "containers": [{
                        "name": name,
                        "image": image
                    }]
                }
            }
        }
    }
    api.patch_namespaced_deployment(name=name, namespace="default", body=patch)

# Optional: react to any spec change, not just image
# @kopf.on.update('petbook.dev', 'v1', 'userprofileservices')
# def update_any(spec, **kwargs):
#     name = spec.get('name')
#     image = spec.get('image')
#     print(f"🔁 General update: patching '{name}' to image '{image}'")
#     configure_k8s()
#     api = kubernetes.client.AppsV1Api()
#     patch = {
#         "spec": {
#             "template": {
#                 "spec": {
#                     "containers": [{
#                         "name": name,
#                         "image": image
#                     }]
#                 }
#             }
#         }
#     }
#     api.patch_namespaced_deployment(name=name, namespace="default", body=patch)
