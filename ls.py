# -*- coding: utf-8 -*-

import os
import grp
import pwd

def main():

    type_it = input(" ").strip()
    
    for archive in os.listdir():

        if type_it == 'ls':
            
            print('Archive - ' + archive)

        elif type_it == 'ls -e':

            meta = os.path.splitext(archive)
            print("="*20 + "\n", meta[0], meta[1])

        elif type_it == 'ls -g':

            stat_info = os.stat("./" + archive)
            uid = stat_info.st_uid
            gid = stat_info.st_gid
            print(' UID - ' + str(uid), ' GID - ' + str(gid))
            
            user = pwd.getpwuid(uid)[0]
            group = grp.getgrgid(gid)[0]
            print(' Archive - ' + archive + '\n', 'User - ' + user + '\n', 'Group - ' + group + '\n')

        elif type_it == 'ls -h':

            print("""\n   ls -e for extensions if your program has extension

   ls -g for group belonging\n""")
            break
        
        else:

            print("\nDoes not exist!\n")
            break


main()