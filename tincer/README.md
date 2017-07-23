# tincer
An Ansible experiment to auto-provision a mesh secured overlay network with bastion access

Steps to run this playbook:
1. Create a symlink or copy your identity file to `roles/digitalocean/files/identity.pub`
2. `export DO_API_TOKEN=$token`, replacing `$token` with your DigitalOcean API token
3. If this the first time provisioning a set of machines, you'll need to temporarily disable host key checking.
via `export ANSIBLE_HOST_KEY_CHECKING="False"`. It should be `unset` subsequent to initial provisioning in order to help prevent the possibility of a MITM attack.
4. Execute the playbook with `ansible-playbook playbook.yml`
5. To test the functionality of the machines, SSH to the IP address of the bastion host and attempt a ping of one of the other machines defined in the main playbook's vars.

The included ansible-tinc role is a submodule pointing to a specific version of ansible-tinc that contains some bugfixes that are necessary to run this playbook. This playbook is fully idempotent, so it is safe to re-run in the event of failure.

The Droplets will be autoprovisioned with a tun0 device that is attached to the network 192.168.1.0/24. This network is secured via tinc's encryption subsystems, and should be used for any inter-host traffic, with the exceptions of the tinc protocol itself and SSH.
To further expand the number of droplets that are autoprovisioned and added to the mesh, add another hash describing a droplet to the `droplets` list in the main playbook. Currently limited in size to the equivalent of a CIDR `/24`.

Unwanted incoming traffic on the secured host WAN interfaces is dropped via `iptables` to prevent communication with the outside world.
