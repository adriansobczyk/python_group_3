# ------------------------ ARCHIWIZACJA PLIKÓW ------------------------ #
import shutil

def archive_current_files():
    shutil.make_archive('archive_files/archive', 'zip', 'archive_files')
    print('Archiwizacja plików zakończona sukcesem.')

def archive_current_files_with_tar():
    shutil.make_archive('archive_files/archive_tar', 'tar', 'archive_files')
    print('Archiwizacja plików zakończona sukcesem.')

def archive_main_folder():
    shutil.make_archive('archive_files/archive_files', 'zip')
    print('Archiwizacja folderu zakończona sukcesem.')

# if __name__ == '__main__':
    # archive_current_files()
    # archive_current_files_with_tar()
    # archive_main_folder()