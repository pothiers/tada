"All use of iRODS by TADA is done through these functions"

import subprocess
import logging
import os

def irods_put331(local_fname, irods_fname):
    "Copy local_fname to irods_fname, creating dirs if needed."
    logging.debug('irods_put331({}, {})'.format(local_fname, irods_fname))
    #!logging.debug('   irods_put331 env:{})'.format(os.environ))
    icmdpath = ('/usr/local/share/applications/irods3.3.1/iRODS/clients'
                '/icommands/bin')
    try:
        subprocess.check_output([os.path.join(icmdpath, 'imkdir'),
                                 '-p',
                                 os.path.dirname(irods_fname)])
                                #! start_new_session=True)
        subprocess.check_output([os.path.join(icmdpath, 'iput'),
                                 '-f', '-K', local_fname, irods_fname])
    except subprocess.CalledProcessError as ex:
        logging.error('Execution failed: {}; {}'
                      .format(ex, ex.output.decode('utf-8')))
        raise

def irods_get331( irods_fname, local_fname):
    "Copy irods_fname to local_fname."
    logging.debug('irods_get331({}, {})'.format(irods_fname, local_fname))
    icmdpath = ('/usr/local/share/applications/irods3.3.1/iRODS/clients'
                '/icommands/bin')
    try:
        subprocess.check_output([os.path.join(icmdpath, 'iget'),
                                 '-f', '-K', local_fname, irods_fname])
    except subprocess.CalledProcessError as ex:
        return False
    
    return True


def irods_remove331(irods_fname):
    "Remove irods_fname from irods"
    logging.debug('irods_remove331({})'.format(irods_fname))
    icmdpath = ('/usr/local/share/applications/irods3.3.1/iRODS/clients'
                '/icommands/bin')
    try:
        subprocess.check_output([os.path.join(icmdpath, 'irm'),
                                 '-f', irods_fname])
    except subprocess.CalledProcessError as ex:
        logging.error('Execution failed: {}; {}'
                      .format(ex, ex.output.decode('utf-8')))
        raise

