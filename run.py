import unittest

PATH = ".\chromedriver.exe"

def main():
    if PATH == "":
        raise Exception("Please input the path to your Chrome driver")

    #test view salary
    # from ViewSalary import PythonOrgSearch
    # suite = unittest.makeSuite(PythonOrgSearch)
    # test(suite)

    #test log in
    # from LogIn import PythonOrgSearch
    # suite = unittest.makeSuite(PythonOrgSearch)
    # test(suite)   

    #test register
    from Register import PythonOrgSearch
    suite = unittest.makeSuite(PythonOrgSearch)
    test(suite)   

    from JobSearch import PythonOrgSearch
    suite = unittest.makeSuite(PythonOrgSearch)
    test(suite)

def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())


if __name__ == "__main__":
   main()
