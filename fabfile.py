import vagrant
from fabric.api import env, task, run, sudo


# Initialize vagrant instance and set the hosts, key_filename and
# disable_known_hosts env attributes
v = vagrant.Vagrant()
v.up()
env.hosts = [v.user_hostname_port()]
print(env.hosts)
env.key_filename = v.keyfile()
env.disable_known_hosts = True  # useful for when the vagrant box ip changes.


@task
def mytask():
    run('echo $USER')


@task
def invoke(command):
    """
    Invoke an arbitrary command
    """
    sudo(command)


@task
def host_type():
    run('uname -s')
