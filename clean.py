from os import listdir, path as osp
from shutil import rmtree

USERNAME = 'mkaminski5'

LIBRARIES_PATHS = ['/Library', '/Users/{}/Library'.format(USERNAME)]

APPS_TO_REMOVE = ['to-delete']


def ishidden(name: str) -> bool:
    return name.startswith('.')


def success_message(path: str):
    print('\nDELETED: {}\n'.format(path))


def paths_from_dir_gen(base_path: str):
    if osp.isfile(base_path):
        return []
    else:
        return (fp for fp in listdir(base_path) if not ishidden(fp))


def deleted(path: str) -> bool:
    if input('Delete {} ? (y/n) '.format(path)) == 'y':
        rmtree(path)
        return True
    else:
        return False


def cleaned(path: str) -> bool:
    for to_remove in APPS_TO_REMOVE:
        if to_remove.upper() in path.upper():
            return True if deleted(path) else False
    return False


def clean_dir(base_path: str) -> bool:
    path = None

    for fp in paths_from_dir_gen(base_path):
        try:
            path = '{}/{}'.format(base_path, fp)
            if cleaned(path):
                success_message(path)
            else:
                clean_dir(path)
        except OSError:
            print('Not permitted:', path)


def main():
    for library_path in LIBRARIES_PATHS:
        clean_dir(library_path)


if __name__ == "__main__":
    main()
