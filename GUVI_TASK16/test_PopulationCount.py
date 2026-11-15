from pages.home_page import HomePage
import time

def test_population_count(setup):

    population_page = HomePage(setup)
    try:
        while True:
            population_count=population_page.get_population()
            #population page stores homepage nd homepage inherits base page
            print("world population count: ", population_count)
            time.sleep(1)
    except KeyboardInterrupt:
        print("population stopped by user")

#For Reference
#test_PopulationCount.py::test_population_count world population count:  8,325,194,278
# world population count:  8,325,194,281
# world population count:  8,325,194,283
# world population count:  8,325,194,285
# world population count:  8,325,194,288
# population stopped by user
# PASSED