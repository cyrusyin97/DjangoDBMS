if (window.localStorage.getItem("link") == null) {
	window.localStorage.setItem("link", "/casequery?");
}
var date;
var customer;
var company;
var employee;
var product;
window.onload = function() {
	var dateinput = document.getElementById('dateinput').addEventListener("change", function() {
		date = this.value;
	});
	var datelink = document.getElementById('datelink').addEventListener("click", function() {
		var clink = window.localStorage.getItem("link") + "&timeframe=" + date;
		window.localStorage.setItem("link", clink);
		this.href = clink;
	})

	var byLatest = document.getElementById('bylatest').addEventListener("click", function() {
		var clink = window.localStorage.getItem("link") + "&time=0";
		window.localStorage.setItem("link", clink);
		this.href = clink;
	});

	var byOldest = document.getElementById('byoldest').addEventListener("click", function() {
		var clink = window.localStorage.getItem("link") + "&time=1";
		window.localStorage.setItem("link", clink);
		this.href = clink;
	});

	var statusTrue = document.getElementById('status_true').addEventListener("click", function() {
		var clink = window.localStorage.getItem("link") + "&status=True";
		window.localStorage.setItem("link", clink);
		this.href = clink;
	});

	var statusFalse = document.getElementById('status_false').addEventListener("click", function() {
		var clink = window.localStorage.getItem("link") + "&status=False";
		window.localStorage.setItem("link", clink);
		this.href = clink;
	});




	var customer_input = document.getElementById('cus_input').addEventListener("input", function() {
		customer = this.value;
	});

	var customer_search = document.getElementById('cus_search').addEventListener("click", function() {
		var clink = window.localStorage.getItem("link") + "&customer=" + customer;
		window.localStorage.setItem("link", clink);
		this.href = clink;
	});




	var company_input = document.getElementById('com_input').addEventListener("input", function() {
		company = this.value;
	});

	var company_search = document.getElementById('com_search').addEventListener("click", function() {
		var clink = window.localStorage.getItem("link") + "&company=" + company;
		window.localStorage.setItem("link", clink);
		this.href = clink;
	});

	var employee_input = document.getElementById('em_input').addEventListener("input", function() {
		employee = this.value;
	});

	var employee_search = document.getElementById('em_search').addEventListener("click", function() {
		var clink = window.localStorage.getItem("link") + "&employee=" + employee;
		window.localStorage.setItem("link", clink);
		this.href = clink;
	});

	var product_input = document.getElementById('prod_input').addEventListener("input", function() {
		product = this.value;
	});

	var product_search = document.getElementById('prod_search').addEventListener("click", function() {
		var clink = window.localStorage.getItem("link") + "&product=" + product;
		console.log(clink);
		window.localStorage.setItem("link", clink);
		this.href = clink;
	});



	var Back = document.getElementById('back').addEventListener("click", function() {
		window.localStorage.clear();
		//window.localStorage.removeItem("link");
	});
}
