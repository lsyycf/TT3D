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


def get_all_subdirectories(nums):
    base_path = r'/mnt/data/lhl/TT3D-dataset'
    all_subdirs = []
    for num in nums:
        dataset_dir = os.path.join(base_path, f'dataset{num}')
        if os.path.exists(dataset_dir):
            subdirs = get_subdirectories(dataset_dir)
            all_subdirs.extend(subdirs)
        else:
            print(f'Dataset directory {dataset_dir} does not exist.')
    return all_subdirs


def main():
    dataset_dir = r'/mnt/data2/lhl/dataset'
    clear_directory(dataset_dir, 'imagenet-simple-labels.json')
    all_subdirs = get_all_subdirectories([1, 2, 5])
    selected_subdirs = random.sample(all_subdirs, 100)
    copy_files_to_new_folders(selected_subdirs, dataset_dir)


if __name__ == '__main__':
    main()
