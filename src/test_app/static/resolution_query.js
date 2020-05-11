var product;

window.onload = function() {
	var product_input = document.getElementById('pro_input').addEventListener("input", function() {
		product = this.value;
	});

	var product_search = document.getElementById('pro_search').addEventListener("click", function() {
		this.href = "/resolutionquery?product=" + product;
	});


}
