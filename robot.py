import time
from utils import QUERY_LINK, TIMEOUT, N_PAGE
from paths import files_count, create_name_for_file, initial_dir


class Robot:
    def __init__(self, driver):
        self.driver = driver
        self.final_info = []
        self.links = [QUERY_LINK + str(page + 1) for page in range(N_PAGE)]

    def parse_site(self):

        for search_link in self.links:
            self.driver.get(search_link)
            breakpoint()
            articles = self.driver.find_elements_by_xpath("//*[@data-selenium-selector='title-link']")

            time.sleep(TIMEOUT)

            for link in [article.get_attribute('href') for article in articles]:
                tmp_info = {}
                self.driver.get(link)
                main = self.driver.find_element_by_class_name('fresh-paper-detail-page__header')

                #  see more button
                try:
                    main.find_element_by_class_name('more-authors-label').click()
                except:
                    pass

                tmp_info.update({
                    'title': main.find_element_by_xpath("//*[@data-selenium-selector='paper-detail-title']").text,
                    'authors': main.find_element_by_class_name('author-list').text.replace(' less', ''),
                    'number of citations':
                        main.find_element_by_xpath("//*[@data-heap-nav='citing-papers']").text.split(' ')[0],
                })

                #  not all documents have source
                try:
                    source = main.find_element_by_xpath("//*[@data-heap-id='paper-meta-journal']")
                    tmp_info.update({'source': source.text})
                except:
                    continue

                #  for example, I need only 3 docs
                if files_count() < 3:

                    #  not all documents have pdf
                    try:
                        init_dir = initial_dir()
                        self.driver.find_element_by_class_name('alternate-sources__dropdown-wrapper').click()
                        time.sleep(TIMEOUT * 2)
                        full_path = create_name_for_file(init_dir)
                    except:
                        full_path = None

                    tmp_info.update({'path_to_file': full_path})

                #  see a full description
                try:
                    main.find_element_by_class_name('mod-clickable').click()
                except:
                    continue

                #  not all documents have a description
                try:
                    description = main.find_element_by_xpath("//*[@data-selenium-selector='text-truncator-text']")
                    tmp_info.update({'description': description.text})
                except:
                    continue

                self.final_info.append(tmp_info.copy())

        return self.final_info
