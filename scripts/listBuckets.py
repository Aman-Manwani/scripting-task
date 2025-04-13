import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    for bucket in response.get('Buckets', []):
        print(bucket['Name'])

def count_objects_in_bucket(bucket_name):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    total = 0

    try:
        for page in paginator.paginate(Bucket=bucket_name):
            total += len(page.get('Contents', []))
        print(f"Total objects in '{bucket_name}': {total}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    list_s3_buckets()
    name = input("Enter bucket name to count objects: ").strip()
    count_objects_in_bucket(name)
