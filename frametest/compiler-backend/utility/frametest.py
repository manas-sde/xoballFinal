import subprocess
import re
import os,json
import time
from concurrent.futures import ThreadPoolExecutor


class TestReact:
    def testReactCode(self,*args,**kwargs):
      code = kwargs['code']
      reportID = kwargs['reportID']
      executor = ThreadPoolExecutor(4)
      return executor.submit(self.testReactCode1,code=code,reportID=reportID).result()
       

       
    def testReactCode1(self,*args,**kwargs):
        t1 = time.time()
        code = kwargs['code']
        global test

        filename=kwargs['reportID']
        #print(filename)

        importStatementCodeFile = "import React, { useState } from 'react';\n"
        exportStatementCodeFile = "export default Counter;"

        importStatementTestFile = f"import App from './cand{filename}';\n"

        ttest = importStatementTestFile+test
        t2 = time.time()
        print('Till checkpoint 1 :',t2-t1)
        #print("Writing react code to .js file")
        with open(f'react-backend/src/cand{filename}.js','w') as reactJSFile:
            reactJSFile.write(importStatementCodeFile + code + exportStatementCodeFile )

        #print("Writing code to test file")
        with open(f'react-backend/src/cand{filename}.test.js','w') as reactJSTestFile:
            reactJSTestFile.write(ttest)

        reactProjectPath = 'react-backend'
        
        t3 = time.time()
        print('Till checkpoint 2 :',t3-t3)
        #print("Firing subprocess command")
        runOutput = subprocess.run(f'jest --testPathPattern=react-backend/src/cand{filename}.test.js --json --outputFile=src/candRepo{filename}.json',shell=True,cwd=reactProjectPath,capture_output=True)

        t4 = time.time()
        print('Till checkpoint 3 :',t4-t3)
        #print(runOutput.stderr.decode('utf-8'))

        # test_results = re.findall(r'(✓|✕)\s(.+)\((\d+)\sms\)', runOutput.stderr.decode('utf-8'))
        #print("test results received")
        #print(test_results)
        returnOutput = []

        # for status,description,time in test_results:
        #     returnOutput.append(f'{status} {description}')

        with open(f'react-backend/src/candRepo{filename}.json','r') as f:
          jsonDataRepo = json.load(f)

          for testres in jsonDataRepo['testResults'][0]["assertionResults"]:
            if testres["status"] == "passed":
              statusTest = '✓'
            else:
              statusTest = '✕'

            returnOutput.append(f'{statusTest} {testres["title"]}')

        t5 = time.time()
        print('Till checkpoint 4 :',t5-t4)

        print("deleting temp files")
        os.remove(f'react-backend/src/cand{filename}.js')
        os.remove(f'react-backend/src/cand{filename}.test.js')
        os.remove(f'react-backend/src/candRepo{filename}.json')
        print("Fi;e deelre")
        ##print(*returnOutput,sep="\n")
        #print("Returninig output")

        print("Total time in backend : ",time.time()-t1)
        return returnOutput


code = '''

import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  const [inputValue, setInputValue] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  function handleButtonClick() {
    setCount(count + 1);
  }

  function handleInputChange(event) {
    const value = document.getElementById('input').value;

    if (isNaN(value) || value < 0 || value > 100) {
      setErrorMessage('Please enter a number between 0 and 100.');
    } else {
      setErrorMessage('');
      setInputValue(value);
    }
  }

  return (
    <div>
      <h1 data-testid="heading">Hello World</h1>
      <button data-testid="button" onClick={handleButtonClick}>
        Increment
      </button>
      <p data-testid="counter">Count: {count}</p>
      <input
        id="input"
        data-testid="input"
        type="text"
        
      
      />
      <button data-testid="validate" onClick={handleInputChange}>
        Validate
      </button>
      <p data-testid="error">{errorMessage}</p>
      <p data-testid="input-value">{inputValue}</p>
    </div>
  );
}

export default Counter;

'''


test = '''

import React from 'react';

import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import { JSDOM } from 'jsdom';

const dom = new JSDOM();
global.document = dom.window.document;
global.window = dom.window;



describe('App', () => {
  it('renders the component', () => {
    render(<App />);
  });

  it('has the correct heading text', () => {
    const { getByTestId } = render(<App />);
    const headingElement = getByTestId('heading');
    expect(headingElement).toHaveTextContent('Hello World');
  });

  it('increments the counter when the button is clicked', () => {
    const { getByTestId } = render(<App />);
    const buttonElement = getByTestId('button');
    const counterElement = getByTestId('counter');

    expect(counterElement).toHaveTextContent('Count: 0');
    fireEvent.click(buttonElement);
    expect(counterElement).toHaveTextContent('Count: 1');
    fireEvent.click(buttonElement);
    expect(counterElement).toHaveTextContent('Count: 2');
    fireEvent.click(buttonElement);
    expect(counterElement).toHaveTextContent('Count: 3');
  });

  it('updates the input value correctly', () => {
    const { getByTestId } = render(<App />);
    const inputElement = getByTestId('input');
    fireEvent.change(inputElement, { target: { value: '50' } });
    expect(inputElement).toHaveValue('50');
  });

  it('validates the input field correctly', () => {
    const { getByTestId } = render(<App />);
    const inputElement = getByTestId('input');
    const buttonElement = getByTestId('validate');
    const errorElement = getByTestId('error');

    fireEvent.change(inputElement, { target: { value: 'abc' } });
    fireEvent.click(buttonElement);
    // console.log(errorElement.innerHTML);
    expect(errorElement).toHaveTextContent('Please enter a number between 0 and 100.');

    fireEvent.change(inputElement, { target: { value: '200' } });
    fireEvent.click(buttonElement);
    expect(errorElement).toHaveTextContent('Please enter a number between 0 and 100.');

    fireEvent.change(inputElement, { target: { value: '-1' } });
    fireEvent.click(buttonElement);
    expect(errorElement).toHaveTextContent('Please enter a number between 0 and 100.');

    fireEvent.change(inputElement, { target: { value: '50' } });
    fireEvent.click(buttonElement);
    expect(errorElement).toHaveTextContent('');
  });
});
'''
# TestReact().testReactCode(code=code,test=test)