from locust import HttpUser,task,between
import random

class LoadTestUser(HttpUser):

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
    let value = inputValue;
    console.log('Value : ',value,typeof value);

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
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        
      
      />
      <button data-testid="validate" onClick={handleInputChange}>
        Validate
      </button>
      <p data-testid="error">{errorMessage}</p>
      {/* <p data-testid="input-value">{inputValue}</p> */}
    </div>
  );
}

export default Counter;
    '''
    
    @task
    def compile(self):
        #print(random.randint(1,1000))
        self.client.post("/frametest/compile-and-evaluate",json={"code":self.code, "questionType":"react","reportID":random.randint(1,10000)})
        #self.client.get('/')
        