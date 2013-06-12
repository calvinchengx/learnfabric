import vagrant
from fabric.api import env, task, run, sudo
from fabric.operations import local


# Initialize vagrant instance and set the hosts, key_filename and
# disable_known_hosts env attributes
v = vagrant.Vagrant()
v.up()
env.hosts = [v.user_hostname_port()]
env.key_filename = v.keyfile()
env.disable_known_hosts = True  # useful for when the vagrant box ip changes.

env.roledefs = {
    'all': ['localhost', v.user_hostname_port()],
    'vag': [v.user_hostname_port()],
    'local': ['localhost']
}


@task
def mytask():
    command = 'echo $USER'
    if env.host == 'localhost':
        local(command)
    else:
        run(command)


@task
def invoke(command):
    """
    Invoke an arbitrary command
    """
    sudo(command)


@task
def host_type():
    command = 'uname -s'
    if env.host == 'localhost':
        local(command)
    else:
        run(command)
