#!/bin/bash

ceph=$(which ceph)

while getopts "k:n:" opt; do
	case "$opt" in
	k)
		key=$OPTARG
		;;
	n)
		name=$OPTARG
		;;
	esac
done

if [ -z $name ]; then
	echo "Usage: $0 -n <name for auth> [-k keyring to be used]"
	exit 3
fi

if [ ! -z $key ]; then
	opts="--name $name --keyring $key"
else
	opts="--name $name"
fi

status=$($ceph $opts health detail)
echo "$status"
if [[ $status =~ HEALTH_OK ]]; then
	exit 0
else
	exit 2
fi
