#!/bin/bash

ceph=$(which ceph)
$ceph health
rc=$?
exit $?
