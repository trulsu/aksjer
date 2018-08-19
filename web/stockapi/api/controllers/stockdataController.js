'use strict';

var model = datamodelTodo();

exports.get_aksjedata = function(req,res) {
  model.find({}, function(err,aksjedata) {
    if(err) {
      res.send(err);
    }
    res.json(aksjedata);
  });
};

exports.get_aksjedata = function(req,res) {
  var ticker = req.params.ticker;
  model.findByTicker(ticker, function(err,aksjedata) {
    if(err) {
      res.send(err);
    }
    res.json(aksjedata);
  });
};

