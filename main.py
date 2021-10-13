from email_me import send_an_email
from paths import create_full_file, create_folder_if_not_exist
from robot import Robot
from utils import create_webdriver, RECEIVER_ADDRESS, SUBJECT, FILE_NAME
from creds import email, password

if __name__ == '__main__':

    #  Obligatory task
    driver = create_webdriver()
    create_folder_if_not_exist()
    robot = Robot(driver)
    final_info = robot.parse_site()
    driver.quit()
    create_full_file(final_info, FILE_NAME)
    send_an_email(RECEIVER_ADDRESS, email, password, SUBJECT, FILE_NAME)

    #  Additionally task
    # Coming soon (maybe)
