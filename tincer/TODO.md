* DNS-based bastion (with associated automation) - this would improve DRY by removing an entire add_host task
* Utilize more DigitalOcean infra (firewall, floating IP, etc.) to enhance functionality/maintainability
* Future expandability of roles
* More security everywhere [avoiding root necessity due to synchronization, ssh host-key management, more lockdown, etc.]
* Scalability is a little iffy due to the way hosts are defined and how there can only be one bastion host at this time
* The virtual inventory could use some work, or possible complete replacement with dynamic inventory. I think improvements to the Ansible DO dynamic inventory provider script and/or the dopy library may be necessary to support my tag-based vision here.)
* Further honing and productionization, going along with all of the above
