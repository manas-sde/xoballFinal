# import subprocess

# # change to the root directory of your SvelteKit project
# root_dir = "/home/manas/xobin/frametest/ffrontend"

# # run npm run test command in the root directory
# subprocess.run("npm run test", shell=True, cwd=root_dir)




from babel.core import transform_string

def transpile_react_code(react_code):
    # Set up Babel configuration
    babel_config = {
        'presets': ['@babel/preset-react']
    }

    # Transpile the React code to JavaScript using Babel
    transpiled_code = transform_string(react_code, babel_config).code

    return transpiled_code

react_code = '''
    // React is loaded and is available as React and ReactDOM
// imports should NOT be used
class Message extends React.Component {
  render() {
    return (<React.Fragment>
          <a href="#">Want to buy a new car?</a>
          <p>Call +11 22 33 44 now!</p>
        </React.Fragment>);
  }
}

document.body.innerHTML = "<div id='root'></div>";
const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<Message />);
const rootElement = document.getElementById("root");
setTimeout(() => {
  console.log("Before click: " + rootElement.innerHTML);

  document.querySelector("a").click();
  setTimeout(() => {
    console.log("After click: " + rootElement.innerHTML);
  });
});
'''


print(transpile_react_code(react_code))