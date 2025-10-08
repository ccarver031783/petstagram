import kopf
import kubernetes
import yaml

@kopf.on.create('petbook.dev', 'v1', 'userprofileservices')
def create_fn(spec, **kwargs):
    name = spec.get('name', 'userprofile')
    image = spec.get('image', 'ghcr.io/your-org/userprofile:v0.1')

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
