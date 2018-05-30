def do_telnet(Host, username, password, finish, commands):
    import telnetlib

    tn = telnetlib.Telnet(Host, port=23, timeout=2)
    tn.set_debuglevel(2)

    tn.read_until(b'login: ')
    tn.write(username.encode('ascii') + '\n'.encode(''))

    tn.read_until(b'Password: ')
    tn.write(password.encode('ascii'))

    tn.read_until(finish)
    for command in commands:
        tn.write('%s\n' % command)

    tn.read_until(finish)
    tn.close()


if __name__ == '__main__':
    Host = '172.16.10.236'
    username = 'admin'
    password = '9hgame.com'
    finish = ']~$ '
    commands = ['echo "test"']
    do_telnet(Host, username, password, finish, commands)