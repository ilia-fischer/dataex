'use strict'

module.exports = function(app) {
	var dex = require('../controllers/dexController')

	app.route("/")
		.get(dex.overview);

	//Data Exchange Platform API
	app.route('/dataset')
		.post(dex.addDataSet);

	app.route('/querydataset')
		.post(dex.queryDataSet);

	app.route('/accessdataset')
		.post(dex.accessDataSet);

	app.route('/dataset/:datasetId')
		.get(dex.getDataSet)
		.post(dex.updateDataSet)
		.delete(dex.deleteDataSet);

	app.route('/account')
		.post(dex.queryAccount);

		//query transactions
		//smart contract
};