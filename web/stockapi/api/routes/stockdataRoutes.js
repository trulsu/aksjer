'use strict';

module.exports = function(app) {
  var aksjedata = require('../controllers/aksjedataController');

// Aksjedata Routes
app.route('/aksjedata')
  .get(aksjedata.list_all_aksjedata);

app.route('/aksjedata/:ticker')
  .get(aksjedata.get_aksjedata);
};

