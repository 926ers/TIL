import os

def list_files_recursive(directory, level=0):
    # 현재 디렉토리의 내용을 가져옴
    with os.scandir(directory) as entries:
        for entry in entries:
            # 현재 항목의 이름을 출력
            if entry.is_file and (entry.name.endswith('md') or entry.name.endswith('txt')) and directory.split("/")[-1] == 'kbs' :
                print(directory.split("/")[1], '    ' * level + entry.name)
                kbs_md_list.append(directory.split("/")[1] + '    ' * level + entry.name)
            # 항목이 디렉토리인 경우, 재귀적으로 탐색
            if entry.is_dir():
                list_files_recursive(entry.path, level + 1)

# 탐색할 디렉토리 경로 (상대 경로)
start_directory = '.'

readme_path = os.path.join(start_directory, 'kbs index.md')
kbs_md_list = []
list_files_recursive(start_directory)

with open(readme_path, 'w') as readme_file:
    readme_file.write('# KBS INDEX \n')
    readme_file.write('\n'.join(kbs_md_list))