// // Hello.test.js
// // import React from 'react';
// import ReactDOM from 'react-dom';
// import Hello from './cand21';

// describe('Hello component', () => {
//   it('renders a greeting message', () => {
//     const container = document.createElement('div');
//     ReactDOM.render(<Hello />, container);
//     expect(container.querySelector('h1').textContent).toBe('Hello World!');
//   });
// });


import React from 'react';

import { render, fireEvent } from '@testing-library/react';
import App from './cand21';
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
    console.log('Error Message : ',errorElement.innerHTML);
    expect(errorElement).toHaveTextContent('Please enter a number between 0 and 100.');
    console.log('Test1');

    fireEvent.change(inputElement, { target: { value: '200' } });
    fireEvent.click(buttonElement);
    
    expect(errorElement).toHaveTextContent('Please enter a number between 0 and 100.');
    console.log('Test2');


    fireEvent.change(inputElement, { target: { value: '-1' } });
    fireEvent.click(buttonElement);
    expect(errorElement).toHaveTextContent('Please enter a number between 0 and 100.');
    console.log('Test3');

    fireEvent.change(inputElement, { target: { value: '50' } });
    fireEvent.click(buttonElement);
    expect(errorElement).toHaveTextContent('');
    console.log('Test4');
  });
});
