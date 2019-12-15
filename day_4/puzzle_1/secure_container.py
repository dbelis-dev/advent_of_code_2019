import sys
import os
import array

def main():
    start = 138241
    end = 674034
    hold_list = []
    for current_passwd in range( start, end, 1 ):
        if has_duplicates( current_passwd ) and is_ascending( current_passwd ):
            hold_list.append( current_passwd )

    print('Hold List size: {}'.format(len(hold_list)))

def has_duplicates( current_passwd ):
    password_str = str(current_passwd)
    for i in range( 1, len( password_str) ):
        if password_str[ i ] == password_str[ i - 1 ]:
            return True
    return False

def is_ascending( current_passwd ):
    password_str = str(current_passwd)
    for i in range( 1, len( password_str) ):
        if ord(password_str[ i ]) >= ord(password_str[ i - 1 ]):
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    main()
