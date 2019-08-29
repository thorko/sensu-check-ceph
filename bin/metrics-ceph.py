#!/usr/bin/python

import json
import subprocess
import argparse
import time

def main():
	parser = argparse.ArgumentParser(description='get metrics of ceph')
	parser.add_argument('-e', type=str, dest='env', required=True, help='the environment name', default='prod')
	args = parser.parse_args()

	j = subprocess.check_output(['/usr/bin/ceph', 'status', '--format=json']).replace('\n', '')
	l = json.loads(j)
	ts = int(time.time())
	print("ceph.{:s}.data_bytes {:d} {:d}".format(args.env, l['pgmap']['data_bytes'], ts))
	print("ceph.{:s}.bytes_used {:d} {:d}".format(args.env, l['pgmap']['bytes_used'], ts))
	print("ceph.{:s}.bytes_avail {:d} {:d}".format(args.env, l['pgmap']['bytes_avail'], ts))
	print("ceph.{:s}.bytes_total {:d} {:d}".format(args.env, l['pgmap']['bytes_total'], ts))
	#print("ceph.{:s}.read_bytes_sec {:d} {:d}".format(args.env, l['pgmap']['read_bytes_sec'], ts))
	print("ceph.{:s}.write_bytes_sec {:d} {:d}".format(args.env, l['pgmap']['write_bytes_sec'], ts))
	print("ceph.{:s}.read_op_per_sec {:d} {:d}".format(args.env, l['pgmap']['read_op_per_sec'], ts))
	print("ceph.{:s}.write_op_per_sec {:d} {:d}".format(args.env, l['pgmap']['write_op_per_sec'], ts))

if __name__ == '__main__':
	main()
