const puppeteer = require('puppeteer');

describe('React component', () => {
  let browser, page;

  beforeAll(async () => {
    browser = await puppeteer.launch();
    page = await browser.newPage();
  });

  afterAll(async () => {
    await browser.close();
  });

  test('renders correctly', async () => {
    const html = `
      <!DOCTYPE html>
      <html>
        <head>
          <title>React Component</title>
        </head>
        <body>
          <div id="root"></div>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.min.js"></script>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/react/16.14.0/umd/react.production.min.js"></script>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/16.14.0/umd/react-dom.production.min.js"></script>
          <script type="text/babel">
            class MyComponent extends React.Component {
              constructor(props) {
                super(props);
                this.state = { count: 0 };
              }
              handleClick() {
                this.setState(prevState => ({ count: prevState.count + 1 }));
              }
              render() {
                return (
                  <div>
                    <h1>Count: {this.state.count}</h1>
                    <button onClick={() => this.handleClick()}>Increment</button>
                  </div>
                );
              }
            }
            ReactDOM.render(<MyComponent />, document.getElementById('root'));
          </script>
        </body>
      </html>
    `;

    await page.setContent(html);
    const countText = await page.$eval('h1', el => el.textContent);
    expect(countText).toBe('Count: 0');

    await page.click('button');
    const newCountText = await page.$eval('h1', el => el.textContent);
    expect(newCountText).toBe('Count: 1');
  });
});
