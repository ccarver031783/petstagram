import kopf
import kubernetes
import yaml

@kopf.on.create('petbook.dev', 'v1', 'userprofileservices')
def create_fn(spec, **kwargs):
    name = spec.get('name', 'userprofile')
    image = spec.get('image')

    # Simple logging for visibility
    print(f"Deploying {name} with image {image}")

    deployment = {
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
    
    api = kubernetes.client.AppsV1Api()
    api.create_namespaced_deployment(namespace='default', body=deployment)
    return {'message': f'{name} deployed'}
