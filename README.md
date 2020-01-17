# check for ceph
```
./bin/ceph-health.sh
```

## metrics
```
./bin/metrics-ceph.py -e <environment name> -n client.status [-w <warning threshold of free bytes>] [-c <critical threshold of free bytes>]
```
