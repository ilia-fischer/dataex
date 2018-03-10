var express = require('express'),
	app = express(),
	port = 3001;

var cors = require('cors')
app.use(cors())

bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

var routes = require('./api/routes/dexRoutes');
routes(app);

app.listen(port);

console.log("Blockchain Secured Data Exchange RESTful API started on: " + port)

