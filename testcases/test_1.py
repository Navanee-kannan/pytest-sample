import time

import pytest

from testcases import conftest
from testcases.gridtestwithpytest import Base



class Test_1(Base):

    # @pytest.mark.usefixtures('setup')
    @pytest.mark.run(order=1)
    def test_func1(self):
        print("starting test1")
        self.launch_browser()
        # time.sleep(5)
        print('ending test1')
        # conftest.Data.driver1=self.driver
        self.quit()



    # @pytest.mark.usefixtures('setup')
    @pytest.mark.run(order=2)
    def test_func12(self):
        print('this function func12 depends on test_func1')
        self.launch_browser()
        self.driver.get('http://google.co.in')
        time.sleep(5)
        print('ending func12')
        self.quit()