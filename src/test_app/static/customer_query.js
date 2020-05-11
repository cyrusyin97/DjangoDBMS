if (window.localStorage.getItem("cus_link") == null) {
	window.localStorage.setItem("cus_link", "/customerquery?");
}

var customer;
var company;

window.onload = function() {
	var customer_input = document.getElementById('cus_input').addEventListener("input", function() {
		customer = this.value;
	});

	var customer_search = document.getElementById('cus_search').addEventListener("click", function() {
		var clink = window.localStorage.getItem("cus_link") + "&name=" + customer;
		window.localStorage.setItem("cus_link", clink);
		this.href = clink;
	});




	var company_input = document.getElementById('com_input').addEventListener("input", function() {
		company = this.value;
	});

	var company_search = document.getElementById('com_search').addEventListener("click", function() {
		var clink = window.localStorage.getItem("cus_link") + "&company=" + company;
		window.localStorage.setItem("cus_link", clink);
		this.href = clink;
	});

	var ascending_income = document.getElementById('ascending').addEventListener("click", function() {
		var clink = window.localStorage.getItem("cus_link") + "&income=ascending";
		window.localStorage.setItem("cus_link", clink);
		this.href = clink;
	});

	var descending_income = document.getElementById('descending').addEventListener("click", function() {
		var clink = window.localStorage.getItem("cus_link") + "&income=descending";
		window.localStorage.setItem("cus_link", clink);
		this.href = clink;
	});

	var Back = document.getElementById('back').addEventListener("click", function() {
		window.localStorage.clear();
	});

}
