import unittest

PATH = "C:\Program Files (x86)\chromedriver.exe"

def main():
    #test view salary
    from ViewSalary import PythonOrgSearch
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
