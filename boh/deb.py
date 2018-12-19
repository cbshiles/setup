def install(args):
        subprocess.run(['apt-get','install']+args)

deb = {
    'install': install
    }
