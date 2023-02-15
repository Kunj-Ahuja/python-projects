import files_types

link_input = input('Enter yt link: ')
file_type_input = input('Which file do you want: (mp3,mp4): ')

while file_type_input not in ['mp3','mp4']:
    print('Wrong File type!!\nSelect Again!!\n')
    file_type_input = input('>> ')

match file_type_input:
    case 'mp3':
        files_types.mp3(link_input)
    case 'mp4':
        files_types.mp4(link_input)