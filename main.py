from fingerprint_creating import fing_creat
from distance_counting import diff_counting, distance_plots
from excel_io import save_to_excel, load_from_excel

def main():
    menu = {
        1: '1 - Create reference fingerprint.',
        2: '2 - Create test fingerprint.',
        3: '3 - Calculate difference between referance and test fingerprints.',
        4: '4 - Plot distance.',
        5: '5 - Options.',
        6: '6 - Save reference fingerprint.',
        7: '7 - Load reference fingerprint.',
        8: '8 - Quit program.'
        }
    print('Welcome to audio quality verification system.')
    print('Default settings\nWindow size: 1024\nOffset: 512\nDisplay parameter plots: no')

    ref_fing_l = None
    ref_fing_r = None
    test_fing_l = None
    test_fing_r = None

    ref_path = None
    test_path = None

    window_size = 1024
    offset = 512
    debug = 'n'

    if debug.lower() == 'y':
        debug_mode = True
    elif debug.lower() == 'n':
        debug_mode = False

    while True:
        print(f'Main menu:')

        for value in menu:
            print(f'{menu[value]}')
        user_input = int(input('Type number to navigate: '))

        if user_input == 1:
            print('To create reference fingerprint from audio file type path to the audio file or filename:\n')
            ref_path = input()
            print('Creating reference fingerprint...')
            ref_fing_l, ref_fing_r, ref_time = fing_creat(ref_path, window_size=window_size, offset=offset,
                                                          debug_mode=debug_mode)
        elif user_input == 2:
            print('Type path to the audio file or filename to compare with reference:\n')
            test_path = input()
            print('Creating test fingerprint...')
            test_fing_l, test_fing_r, test_time = fing_creat(test_path, window_size=window_size, offset=offset,
                                                          debug_mode=debug_mode)
        elif user_input == 3:
            try:
                ref_fing_l
                ref_fing_r
                test_fing_l
                test_fing_r
            except NameError:
                ref_fing_l = None
                ref_fing_r = None
                test_fing_l = None
                test_fing_r = None

            if ref_fing_l is None or ref_fing_r is None or test_fing_l is None or test_fing_r is None:
                print('\nCreate both fingeprints first.\n')
            else:
                # calculate difference between fingerprints
                dst_l, average_dst_l, dst_r, average_dst_r, dst_dict = diff_counting(ref_fing_l, ref_fing_r,
                                                                           test_fing_l, test_fing_r)
                print(f'Average distance between files in channel left equals {average_dst_l}.\n'
                      f'Average distance between files in channel right equals {average_dst_r}.')

        elif user_input == 4:
            try:
                dst_l
                dst_dict
            except NameError:
                dst_l = None
                dst_dict = None

            if dst_l is None or dst_dict is None:
                print('\nCalculate distance first.')
            else:
                distance_plots(dst_l, dst_r, dst_dict, time=ref_time)

        elif user_input == 5:
            print(f'Current settings:\n'
                  f'Window size: {window_size} samples\n'
                  f'Window offset: {offset} samples')

            if debug_mode:
                print('Plot parameters: yes')
            else:
                print('Plot parameters: no')

            options_menu = {
                1: '1 - Window size.',
                2: '2 - Window offset.',
                3: '3 - Plot parameters.',
                4: '4 - Back.'
            }

            while True:
                for value in options_menu:
                    print(f'{options_menu[value]}')

                options_input = int(input('Select option: '))

                if options_input == 1:
                    window_size = int(input('Set window size in samples(must be power of 2): '))
                elif options_input == 2:
                    offset = int(input('Set window overlap in samples(must be power of 2 and less than window size): '))
                elif options_input == 3:
                    debug = input('Display parameter plots while creating fingerprint? y/n: ')
                    if debug.lower() == 'y':
                        debug_mode = True
                    elif debug.lower() == 'n':
                        debug_mode = False
                    else:
                        print('There is no such option.\nSet to \'no\'')
                        debug_mode = False
                elif options_input == 4:
                    break
                else:
                    print('There is no such option.')

        elif user_input == 6:
            print('Saving reference fingerprint to excel file...')
            save_to_excel(f'{ref_path}', fp_left=ref_fing_l, fp_right=ref_fing_r)
        
        elif user_input == 7:
            print('Enter filename or path to saved reference fingerprint')
            load_from_excel(input())

        elif user_input == 8:
            print('Bye bye.')
            break
        else:
            print('There is no such option.')


main()

