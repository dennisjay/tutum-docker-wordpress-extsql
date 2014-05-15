import boto.ec2
import yaml 

conn=boto.ec2.connect_to_region("eu-west-1")
reservations = conn.get_all_instances()
for res in reservations:
    for inst in res.instances:
        if 'type' in inst.tags:
            if inst.tags['type'] == 'db':
                print inst.ip_address
                
                with open("fig.yml") as f:
                    dataMap = yaml.safe_load(f)
                    print(dataMap)
                    
                dataMap['wordpress']['environment']['WORDPRESS_DB_IP'] = str(inst.ip_address)   
                
                with open("fig.yml", "w") as f:
                    yaml.dump(dataMap, f)
                    