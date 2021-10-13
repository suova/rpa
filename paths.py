import os
import pandas as pd

working_dir = os.path.dirname(os.path.realpath(__file__))
folder_for_pdf = os.path.join(working_dir, 'article_pdfs')
webdriver_path = os.path.join(working_dir, 'chromedriver')
os.environ['webdriver.chrome.driver'] = webdriver_path


def files_count():
    total_files = 0
    for base, dirs, files in os.walk(folder_for_pdf):
        for _ in files:
            total_files += 1
    return total_files


def initial_dir():
    return os.listdir(folder_for_pdf)

def create_name_for_file(init_dir):
    current_dir = os.listdir(folder_for_pdf)
    filename = list(set(current_dir) - set(init_dir))[0]
    full_path = os.path.join(folder_for_pdf, filename)
    return full_path


def create_full_file(final_info, file_name):
    df = pd.DataFrame(final_info)
    excel_path = os.path.join(working_dir, file_name)
    df.to_excel(excel_path, index=False)


def create_folder_if_not_exist():
    if not os.path.isdir(folder_for_pdf):
        os.mkdir(folder_for_pdf)
