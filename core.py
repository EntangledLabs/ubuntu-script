import subprocess

class apt():

    @classmethod
    def install(cls, program):
        subprocess.run(['apt', 'install', program, '-y'])

    @classmethod
    def remove(cls, program):
        subprocess.run(['apt', 'remove', program, '-y'])

    @classmethod
    def purge(cls, program):
        subprocess.run(['apt', 'purge', program, '-y'])

    @classmethod
    def update(cls):
        subprocess.run(['apt', 'update'])

    @classmethod
    def upgrade(cls):
        subprocess.run(['apt', 'dist-upgrade', '-y'])

    @classmethod
    def autoremove(cls):
        subprocess.run(['apt', 'autoremove', '-y'])

class systemctl():

    @classmethod
    def start(cls, service):
        subprocess.run(['systemctl', 'start', service])

    @classmethod
    def stop(cls, service):
        subprocess.run(['systemctl', 'stop', service])
    
    @classmethod
    def restart(cls, service):
        subprocess.run(['systemctl', 'restart', service])

    @classmethod
    def enable(cls, service):
        subprocess.run(['systemctl', 'enable', service])
    
    @classmethod
    def disable(cls, service):
        subprocess.run(['systemctl', 'disable', service])

class ufw():

    @classmethod
    def enable(cls):
        subprocess.run(['ufw', 'enable'])

    @classmethod
    def defaults(cls):
        subprocess.run(['ufw', 'default', 'deny', 'incoming'])
        subprocess.run(['ufw', 'default', 'allow', 'outgoing'])
    
    @classmethod
    def allow(cls, port):
        subprocess.run(['ufw', 'allow', port])

    @classmethod
    def deny(cls, port):
        subprocess.run(['ufw', 'deny', port])

    @classmethod
    def reload(cls):
        subprocess.run(['ufw', 'reload'])

class editing():

    @classmethod
    def editor(cls, path:str, changes:dict) -> None:
        f = open(path, 'r+').readlines()
        index = 0
        for line in f:
            for key,value in changes.items():
                if re.search(key, line):
                    f[index] = '{} {}\n'.format(key, value)
            index = index + 1
        open(path, 'w+').writelines(f)

    @classmethod
    def appender(cls, path:str, changes:list) -> None:
        f = open(path, 'r+').readlines()
        index = 0
        for change in changes:
            changes[index] = '{}\n'.format(change)
            index = index + 1
        f.extend(changes)
        open(path, 'w+').writelines(f)