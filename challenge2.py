from google.cloud import compute_v1
client = compute_v1.InstancesClient()
instance = instance_client.get(project="Project_ID",zone="Zone_name",instance="instance_name")
print(instance.metadata)
