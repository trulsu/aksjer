'use strict';

const sqlite3 = require('sqlite3').verbose();

function opendb(name) {
	let db = new sqlite3.Database('../data/AKER.sqlite3', (err) => {
		if(err) {
			return console.error(err.message);
		}
		console.log('connected to database');
	});
};

let sql = 'SELECT * FROM data';

db.all(sql, [], (err,rows) => {
	if(err) {
		throw err;
	}
	rows.forEach((row) => {
		console.log(row.date);
	});
});

db.get(sql, [ticker], (err,row) => {
	if(err) {
		return err;
	}
	return row
	  ? row
	  : err;
});

db.close((err) => {
	if(err) {
		return console.error(err.message);
	}
	console.log('database connection closed');
});
