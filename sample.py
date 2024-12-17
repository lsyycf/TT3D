import os
import shutil
import random


def clear_directory(directory, except_file):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not any(file == except_file for file in os.listdir(dir_path)):
                shutil.rmtree(dir_path)
        for file_name in files:
            if file_name != except_file:
                os.remove(os.path.join(root, file_name))


def get_subdirectories(path):
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


def copy_files_to_new_folders(src_dirs, dest_base_dir):
    for i, src_dir in enumerate(src_dirs):
        new_folder = os.path.join(dest_base_dir, f'object_{i + 1}')
        os.makedirs(new_folder, exist_ok=True)
        for root, dirs, files in os.walk(src_dir):
            relative_path = os.path.relpath(root, src_dir)
            dest_root = os.path.join(new_folder, relative_path)
            os.makedirs(dest_root, exist_ok=True)
            for file_name in files:
                src_file = os.path.join(root, file_name)
                dest_file = os.path.join(dest_root, file_name)
                shutil.copy(src_file, dest_file)


def main():
    dataset_dir = r'dataset'
    clear_directory(dataset_dir, 'imagenet-simple-labels.json')
    gmfool_dir = r'TT3D-dataset\dataset1'
    train_data_dir = r'TT3D-dataset\dataset2'
    gmfool_subdirs = get_subdirectories(gmfool_dir)
    train_data_subdirs = get_subdirectories(train_data_dir)
    all_subdirs = gmfool_subdirs + train_data_subdirs
    selected_subdirs = random.sample(all_subdirs, 100)
    copy_files_to_new_folders(selected_subdirs, dataset_dir)


if __name__ == '__main__':
    main()
