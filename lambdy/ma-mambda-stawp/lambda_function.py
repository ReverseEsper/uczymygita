import boto3

def lambda_handler(event, context):
    try:
        # Ustawienia AWS
        ec2 = boto3.client('ec2', region_name='eu-central-1')  # Zastąp nazwę regionu swoim

        # Parametry do sprawdzenia statusu instancji EC2
        instance_id = 'i-06a670f4e0ec53431'  # Zastąp to rzeczywistym ID istniejącej instancji EC2

        # Sprawdzenie statusu instancji
        instance_status = ec2.describe_instances(InstanceIds=[instance_id])

        # Jeśli instancja jest zatrzymana, włącz ją
        if instance_status['Reservations'][0]['Instances'][0]['State']['Name'] == 'running':
            ec2.stop_instances(InstanceIds=[instance_id])
            print('Instancja EC2 wyłączona pomyślnie:', instance_id)
        elif instance_status['Reservations'][0]['Instances'][0]['State']['Name'] == 'stopping':
            print('Maszyna w trakcie zatrzymywania:', instance_id)
        elif instance_status['Reservations'][0]['Instances'][0]['State']['Name'] == 'starting':
            print('maszyna sie startuje', instance_id)
        else:
            print('Instancja EC2 jest już nie uruchomiona:', instance_id)

        return {
            'statusCode': 200,
            'body': 'Operacja zakończona sukcesem.'
        }
    except Exception as e:
        print('Wystąpił błąd:', e)

        return {
            'statusCode': 500,
            'body': 'Wystąpił błąd podczas próby wyłączenia instancji EC2.'
        }
