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
    dup_counter = 0
    dup_2_digit = False
    for i in range( 1, len( password_str) ):
        if password_str[ i ] == password_str[ i - 1 ]:
            dup_counter += 1
        else:
            if dup_counter == 1:
                dup_2_digit = True
            dup_counter = 0
    if dup_counter == 1:
        dup_2_digit = True
    return dup_2_digit

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
