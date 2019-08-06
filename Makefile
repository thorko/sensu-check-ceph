.PHONY: release

release:
	tar czf /tmp/sensu-check-ceph_${VERSION}_linux_amd64.tar.gz bin/ etc/ 
	sum=$$(sha512sum /tmp/sensu-check-ceph_${VERSION}_linux_amd64.tar.gz | cut -d ' ' -f 1); \
	f=$$(basename sensu-check-ceph_${VERSION}_linux_amd64.tar.gz); \
	echo $$sum $${f} > /tmp/sensu-check-ceph_${VERSION}_sha512_checksums.txt; \
	echo $$sum;
