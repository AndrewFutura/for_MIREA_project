import yaml


data = {'version': "3.3",
        
        'services':{}}

for i in range(0, 24):
       if i < 10:
            i = f"0{i}"
       data["services"].update({f"main_{i}":{'image':  'ubuntu', 'ports': [f'59{i}:59{i}/tcp']}})

with open('docker-compose.yaml', 'w', encoding='utf-8') as file:
       yaml.dump(data, file, allow_unicode=True)

print("YAML-файл успешно создан!")