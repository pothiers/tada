"""Get tables from MARS, store each in YAML files (for tada.settings via read on DQD startup)
"""

import sys
import argparse
import logging
from . import from_mars as fm

##############################################################################

def main():
    "Parse command line arguments and do the work."
    parser = argparse.ArgumentParser(
        description='Write YAML from web-service (JSON)',
        epilog='EXAMPLE: %(prog)s'
        )
    parser.add_argument('--version', action='version', version='1.0.1')
    parser.add_argument('--loglevel',
                        help='Kind of diagnostic output',
                        choices=['CRTICAL', 'ERROR', 'WARNING',
                                 'INFO', 'DEBUG'],
                        default='WARNING')
    args = parser.parse_args()

    log_level = getattr(logging, args.loglevel.upper(), None)
    if not isinstance(log_level, int):
        parser.error('Invalid log level: %s' % args.loglevel)
    logging.basicConfig(level=log_level,
                        format='%(levelname)s %(message)s',
                        datefmt='%m-%d %H:%M')

    logging.getLogger().setLevel(log_level)
    logging.debug('Debug output is enabled in %s !!!', sys.argv[0])

    fm.genPrefixTable('/etc/tada/prefix_table.yaml')
    fm.genObsTable('/etc/tada/obstype_table.yaml')
    fm.genProcTable('/etc/tada/proctype_table.yaml')
    fm.genProdTable('/etc/tada/prodtype_table.yaml')
    print("""\
Wrote TADA tables to: 
  /etc/tada/prefix_table.yaml
  /etc/tada/obstype_table.yaml
  /etc/tada/proctype_table.yaml
  /etc/tada/prodtype_table.yaml
  """)

if __name__ == '__main__':
    main()
