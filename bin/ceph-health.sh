#!/bin/bash

ceph=$(which ceph)
status=$($ceph health)
if [[ $stats =~ HEALTH_OK ]]; then
  echo $status
	exit 0
else
  echo $status
	exit 2
fi
