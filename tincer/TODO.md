* Figure out some ways to avoid root access (synchronization useful for Tinc applies)
* DNS-based bastion (with associated automation) - this would improve DRY by removing an entire add_host task
* Future expandability of roles
* More security everywhere (see first bullet)
* Scalability is a little iffy due to the way hosts are defined and how there can only be one bastion host at this time
