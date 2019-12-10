#!/usr/bin/python

import json
import subprocess
import argparse
import time
import sys

def main():
	parser = argparse.ArgumentParser(description='get metrics of ceph')
	parser.add_argument('-e', type=str, dest='env', required=False, help='the environment name', default='prod')
	parser.add_argument('-n', type=str, dest='name', required=True, help='the client name for auth', default='client.status')
	parser.add_argument('-k', type=str, dest='keyring', required=False, help='the client keyring file')
	args = parser.parse_args()

	if args.keyring:
		j = subprocess.check_output(['/usr/bin/ceph', '--name', args.name, '--keyring', args.keyring, 'status', '--format=json']).replace('\n', '')
	else:
		j = subprocess.check_output(['/usr/bin/ceph', '--name', args.name, 'status', '--format=json']).replace('\n', '')
	l = json.loads(j)
	ts = int(time.time())
	print("ceph.{:s}.data_bytes {:d} {:d}".format(args.env, l.get('pgmap').get('data_bytes',0), ts))
	print("ceph.{:s}.bytes_used {:d} {:d}".format(args.env, l.get('pgmap').get('bytes_used',0), ts))
	print("ceph.{:s}.bytes_avail {:d} {:d}".format(args.env, l.get('pgmap').get('bytes_avail',0), ts))
	print("ceph.{:s}.bytes_total {:d} {:d}".format(args.env, l.get('pgmap').get('bytes_total',0), ts))
	print("ceph.{:s}.read_bytes_sec {:d} {:d}".format(args.env, l.get('pgmap').get('read_bytes_sec',0), ts))
	print("ceph.{:s}.write_bytes_sec {:d} {:d}".format(args.env, l.get('pgmap').get('write_bytes_sec',0), ts))
	print("ceph.{:s}.read_op_per_sec {:d} {:d}".format(args.env, l.get('pgmap').get('read_op_per_sec',0), ts))
	print("ceph.{:s}.write_op_per_sec {:d} {:d}".format(args.env, l.get('pgmap').get('write_op_per_sec',0), ts))

if __name__ == '__main__':
	main()
