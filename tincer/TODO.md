* DNS-based bastion (with associated automation) - this would improve DRY by removing an entire add_host task
* Utilize more DigitalOcean infra (firewall, floating IP, etc.) to enhance functionality/maintainability
* Future expandability of roles
* More security everywhere [avoiding root necessity due to synchronization, ssh host-key management, more lockdown, etc.]
* Better system for host-key management
* Scalability is a little iffy due to the way hosts are defined and how there can only be one bastion host at this time
