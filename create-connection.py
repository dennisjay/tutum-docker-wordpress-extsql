import boto.ec2
conn=boto.ec2.connect_to_region("eu-west-1")
reservations = conn.get_all_instances()
for res in reservations:
    for inst in res.instances:
        if 'type' in inst.tags:
            if inst.tags['type'] == 'db':
                print inst.ip_address()