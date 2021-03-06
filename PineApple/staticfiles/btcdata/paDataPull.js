var jsonFileNames = ["parsedusdbtcdata1519320470.224996.json","parsedusdbtcdata1519512115.416004.json","parsedusdbtcdata1519151517.2418811.json","parsedusdbtcdata1519151518.274397.json","parsedusdbtcdata1519151537.124332.json","parsedusdbtcdata1519151551.594238.json","parsedusdbtcdata1519151912.206002.json","parsedusdbtcdata1519152669.048627.json","parsedusdbtcdata1519152881.957901.json","parsedusdbtcdata1519152895.836216.json","parsedusdbtcdata1519152939.631706.json","parsedusdbtcdata1519152944.231408.json","parsedusdbtcdata1519153002.767909.json","parsedusdbtcdata1519153005.672537.json","parsedusdbtcdata1519153008.2082071.json","parsedusdbtcdata1519153019.840377.json","parsedusdbtcdata1519153053.9101639.json","parsedusdbtcdata1519153055.49937.json","parsedusdbtcdata1519153136.231906.json","parsedusdbtcdata1519153136.2894871.json","parsedusdbtcdata1519175293.2648902.json","parsedusdbtcdata1519175305.928298.json","parsedusdbtcdata1519175441.817842.json","parsedusdbtcdata1519175483.6735628.json"]; //array of all the historical json files of btc data, to be used to read json info for frontend display

var historicalJSON = [{
  "time": 1519151517.2418811,
  "bitfinex:btcusd": 11673,
  "bitflyer:btcusd": 11665,
  "bitsquare:btcusd": 11383.77,
  "bitstamp:btcusd": 11671.25,
  "btce:btcusd": 11631.01,
  "cexio:btcusd": 11930.2,
  "gdax:btcusd": 11684.14,
  "gemini:btcusd": 11679.99,
  "kraken:btcusd": 11688,
  "okcoin:btcusd": 12354.36,
  "quadriga:btcusd": 11600.01,
  "quoine:btcusd": 11676
},{"time": 1519151518.274397,
	 "bitfinex:btcusd": 11673,
	 "bitflyer:btcusd": 11665,
	 "bitsquare:btcusd": 11383.77,
	 "bitstamp:btcusd": 11671.25,
	 "btce:btcusd": 11631.01,
	 "cexio:btcusd": 11930.2,
	 "gdax:btcusd": 11684.14,
	 "gemini:btcusd": 11679.99,
	 "kraken:btcusd": 11688,
	 "okcoin:btcusd": 12354.36,
	 "quadriga:btcusd": 11600.01,
	 "quoine:btcusd": 11676
	},{"time": 1519151537.124332,
		 "bitfinex:btcusd": 11677,
		 "bitflyer:btcusd": 11665,
		 "bitsquare:btcusd": 11383.77,
		 "bitstamp:btcusd": 11678.7,
		 "btce:btcusd": 11658,
		 "cexio:btcusd": 11939.9,
		 "gdax:btcusd": 11684.14,
		 "gemini:btcusd": 11679.17,
		 "kraken:btcusd": 11685,
		 "okcoin:btcusd": 12354.36,
		 "quadriga:btcusd": 11600.01,
		 "quoine:btcusd": 11676},{
  "time": 1519151551.594238,
  "bitfinex:btcusd": 11674,
  "bitflyer:btcusd": 11665,
  "bitsquare:btcusd": 11383.77,
  "bitstamp:btcusd": 11678.7,
  "btce:btcusd": 11658,
  "cexio:btcusd": 11939.9,
  "gdax:btcusd": 11684.13,
  "gemini:btcusd": 11677.21,
  "kraken:btcusd": 11685,
  "okcoin:btcusd": 12354.36,
  "quadriga:btcusd": 11600.01,
  "quoine:btcusd": 11676
},{"time": 1519151912.206002,
	 "bitfinex:btcusd": 11678,
	 "bitflyer:btcusd": 11664.9,
	 "bitsquare:btcusd": 11383.77,
	 "bitstamp:btcusd": 11690,
	 "btce:btcusd": 11660,
	 "cexio:btcusd": 11922.7,
	 "gdax:btcusd": 11675.09,
	 "gemini:btcusd": 11684.99,
	 "kraken:btcusd": 11685.1,
	 "okcoin:btcusd": 12361.22,
	 "quadriga:btcusd": 11600.01,
	 "quoine:btcusd": 11676
	},{"time": 1519152669.048627,
		 "bitfinex:btcusd": 11676,
		 "bitflyer:btcusd": 11706.2,
		 "bitsquare:btcusd": 11383.77,
		 "bitstamp:btcusd": 11670.89,
		 "btce:btcusd": 11682.501,
		 "cexio:btcusd": 11942.9,
		 "gdax:btcusd": 11690,
		 "gemini:btcusd": 11680.98,
		 "kraken:btcusd": 11699.4,
		 "okcoin:btcusd": 12361.22,
		 "quadriga:btcusd": 11600.01,
		 "quoine:btcusd": 11686.56},{
  "time": 1519152881.957901,
  "bitfinex:btcusd": 11676,
  "bitflyer:btcusd": 11678.35,
  "bitsquare:btcusd": 11383.77,
  "bitstamp:btcusd": 11665.83,
  "btce:btcusd": 11704.35,
  "cexio:btcusd": 11910,
  "gdax:btcusd": 11665.26,
  "gemini:btcusd": 11668.37,
  "kraken:btcusd": 11672.1,
  "okcoin:btcusd": 12453.16,
  "quadriga:btcusd": 11600.01,
  "quoine:btcusd": 11669.852
},{
  "time": 1519152895.836216,
  "bitfinex:btcusd": 11673,
  "bitflyer:btcusd": 11678.35,
  "bitsquare:btcusd": 11383.77,
  "bitstamp:btcusd": 11665.83,
  "btce:btcusd": 11704.37,
  "cexio:btcusd": 11916.6,
  "gdax:btcusd": 11665.25,
  "gemini:btcusd": 11674.09,
  "kraken:btcusd": 11685,
  "okcoin:btcusd": 12453.16,
  "quadriga:btcusd": 11600.01,
  "quoine:btcusd": 11674.525
},{
  "time": 1519152939.631706,
  "bitfinex:btcusd": 11676,
  "bitflyer:btcusd": 11676.95,
  "bitsquare:btcusd": 11383.77,
  "bitstamp:btcusd": 11663.79,
  "btce:btcusd": 11704.37,
  "cexio:btcusd": 11915,
  "gdax:btcusd": 11673.8,
  "gemini:btcusd": 11678.62,
  "kraken:btcusd": 11677.6,
  "okcoin:btcusd": 12453.16,
  "quadriga:btcusd": 11600.01,
  "quoine:btcusd": 11669.852
},{"time": 1519152944.231408,
	 "bitfinex:btcusd": 11675,
	 "bitflyer:btcusd": 11676.95,
	 "bitsquare:btcusd": 11383.77,
	 "bitstamp:btcusd": 11663.79,
	 "btce:btcusd": 11704.37,
	 "cexio:btcusd": 11915,
	 "gdax:btcusd": 11673.8,
	 "gemini:btcusd": 11674.3,
	 "kraken:btcusd": 11679.8,
	 "okcoin:btcusd": 12453.16,
	 "quadriga:btcusd": 11600.01,
	 "quoine:btcusd": 11669.852}
];



function aggregateFunction(){
	var data = {}
	var latestTime = 0;
	var averagePrice = 0;
	var totalPrice = 0;
	var marketCount = 0;

	for (var i=0; i<historicalJSON.length; i++){
		if (historicalJSON[i].time > latestTime){
			data = historicalJSON[i];
			latestTime = historicalJSON[i].time;
		}
	}
	var marketsTable = document.getElementById("marketsTableBody");
	console.log(data);
	dataObjects = Object.entries(data);
	for (var j=1; j<dataObjects.length; j++){
		totalPrice+=dataObjects[j][1];
		var newName = dataObjects[j][0];
		var loc = newName.search(":btcusd");
		newName = newName.slice(0,loc);
		dataObjects[j][0] = newName;
	}
	marketCount = (dataObjects.length) - 1;
	averagePrice = totalPrice/marketCount;
	console.log(averagePrice);

	for (var l= 1; l<dataObjects.length; l++){
		var difference = (dataObjects[l][1]/averagePrice) - 1.00;
		var compare = "";
		var compareID = ""

		if (difference > 0){
			compare = "above (+" + difference.toFixed(3)+")";
			compareID = "above";
		}
		else{
			compare = "below (" + difference.toFixed(3)+")";
			compareID = "below";
		}
		var newelement1 = document.createElement("tr");
		newelement1.innerHTML = "<td>"+String(dataObjects[l][0]).toUpperCase()+"</td><td>$"+String(dataObjects[l][1]) + "</td><td " + "id='"+compareID + "'>"+ compare + "</td>";
		marketsTable.appendChild(newelement1);
		//console.log(newelement1);
	}
}

function populateChart(form){
	var market1 = document.getElementById("exampleSelect1").value;
	var market2 = document.getElementById("exampleSelect2").value;
	var times = [];
	var market1Data = [];
	var market2Data = [];

	//var utcSeconds = 1234567890;
	//var d = new Date(0); // The 0 there is the key, which sets the date to the epoch
	//d.setUTCSeconds(utcSeconds);
	//d is now a date (in my time zone) set to Fri Feb 13 2009 18:31:30 GMT-0500 (EST)

	for (var i=0; i < historicalJSON.length; i++){
		var itime = historicalJSON[i].time;
		var market1point = historicalJSON[i][market1];
		var market2point = historicalJSON[i][market2];
		var date = new Date(0);
		date.setUTCSeconds(itime);
		var datestring = String(date.getHours())+":"+String(date.getMinutes());
		times.push(datestring);
		market1Data.push(market1point);
		market2Data.push(market2point);
	}
	console.log(market1Data);

	var ctx = document.getElementById("myChart");
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: times,
          datasets: [{
            data: market1Data,
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#ff0000',
            borderWidth: 4,
            pointBackgroundColor: '#ff0000'
          },{
            data: market2Data,
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#007bff',
            borderWidth: 4,
            pointBackgroundColor: '#007bff'
          }]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: false
              }
            }]
          },
          legend: {
            display: false,
          }
        }
      });
}
