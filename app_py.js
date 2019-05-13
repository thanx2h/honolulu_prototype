let {PythonShell} = require('python-shell');

var options = {
  mode: 'text',
  pythonPath: 'C:/Users/An/Anaconda3/envs/py36_32/Python.exe',
  pythonOptions: ['-u'],
  scriptPath: '',
  args: ['value1', 'value2', 'value3']

};

// var myVar = setInterval(callKiwoomApi, 5000);
loginKiwoomApi();

function loginKiwoomApi(){
  PythonShell.run('Honolulu_kiwoomapi/main.py', options, function (err, results) {
  	if (err) throw err;
  	console.log('results: %j', results);
  });
}

function requestHogaData() {
  
}
