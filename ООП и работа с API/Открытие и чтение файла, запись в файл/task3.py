import os


def file_sorting(path_to_folder):
    content = {}
    for file_name in os.listdir(f'{path_to_folder}'):
        with open(f'folder/{file_name}', 'r', encoding='utf-8') as file:
            content[file_name] = {'row_count': len(file.readlines())}
            file.seek(0)
            content[file_name]['text'] = file.read()
    return {k: v for k, v in sorted(content.items(), key=lambda x: x[1]['row_count'])}


def save_info_about_files(info, path_to_folder):
    with open(f'{path_to_folder}/file_info.txt', 'w', encoding='utf-8') as file:
        for item in info.items():
            file.write(item[0] + '\n' + str(item[1]['row_count']) + '\n' + item[1]['text'] + '\n')


if __name__ == '__main__':
    save_info_about_files(file_sorting('folder'), 'folder')
