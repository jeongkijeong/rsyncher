import pexpect
import logging


def call_rsync(source, target, password):
    cmd = 'rsync -arvP --delete {} {}'.format(source, target)
    logging.info(cmd)

    try:
        rsyncher = pexpect.spawn(cmd, timeout=5)
        i = rsyncher.expect(['password:', 'continue connecting (yes/no)'], timeout=5)

        if i == 1:
            rsyncher.sendline('yes')
            rsyncher.expect('password:', timeout=5)
        rsyncher.sendline(password)
        buffer = rsyncher.read()

        rsyncher.close()

        logging.info(buffer)
    except Exception as e:
        pass
