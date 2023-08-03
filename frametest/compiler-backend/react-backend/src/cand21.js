// import './test21.css';

// export default function Hello() {
//     return <h1>Hello World!</h1>;
//   }
//   document.body.innerHTML = "<div id='mydiv'></div>";
//   const container = document.getElementById('mydiv');
//   const root = ReactDOM.createRoot(container);
//   root.render(<Hello />)
  


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



// import React, { useState } from 'react';
// /*Do NOT use import statement. 
// //React,ReactDOM, useState are already imported.
// //Write a function with name 'Counter' of this component, which return the required output to solve this question.*/

// const Counter = () => {
//   const [counter, setCounter] = useState(0);
//   const [inputValue, setInputValue] = useState('');
//   const [errorMessage, setErrorMessage] = useState('');

//   const handleButtonClick = () => {
//     setCounter(counter + 1);
//   };

//   const handleValidateClick = () => {
//     const number = Number(inputValue);
//     if (isNaN(number) || number < 0 || number > 100) {
//       setErrorMessage('Please enter a number between 0 and 100.');
//     } else {
//       setErrorMessage('');
//       setInputValue(inputValue);
//     }
//   };

//   return (
//     <div>
//       <h1 data-testid="heading">Hello World</h1>
//       <p data-testid="counter">Count: {counter}</p>
//       <button data-testid="button" onClick={handleButtonClick}>
//         Increment Counter
//       </button>
//       <input
//         data-testid="input"
//         type="text"
//         value={inputValue}
//         onChange={(e) => setInputValue(e.target.value)}
//       />
//       <button data-testid="validate" onClick={handleValidateClick}>
//         Validate
//       </button>
//       <p data-testid="error">{errorMessage}</p>
//     </div>
//   );
// };
                      

// export default Counter;