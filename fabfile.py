import vagrant
from fabric.api import env, task, run


# Initialize vagrant instance and set the hosts, key_filename and
# disable_known_hosts env attributes
v = vagrant.Vagrant()
v.up()
env.hosts = [v.user_hostname_port()]
env.key_filename = v.keyfile()
env.disable_known_hosts = True  # useful for when the vagrant box ip changes.


@task
def mytask():
    run('echo $USER')
