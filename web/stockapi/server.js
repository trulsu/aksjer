var express = require('express'),
  app = express(),
  port = process.env.PORT || 3000,
  aksjedata = require('./api/models/aksjedataModel'),
  tickers = require('./api/models/tickerModel'),
  bodyParser = require('body-parser');

var aksjeRoutes = require('./api/routes/aksjedataRoutes');
aksjeRoutes(app);

var tickerRoutes = require('./api/routes/tickerRoutes');
tickerRoutes(app);

app.listen(port);

console.log('aksjeAPI RESTful API server started on: ' + port);

