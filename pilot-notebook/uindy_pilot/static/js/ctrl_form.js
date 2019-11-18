$(document).ready(function(){
	// Outcome label color
	outcome = $('#outcome_body').text()
	if(outcome == "Investigation Pending"){
		$('#outcome_label').addClass("panel-danger")
	}else{
		$('#outcome_label').addClass("panel-success")
	}
	// Status Label Color
	status = $('#status_body').text()
	if(status != "Active"){
		$('#status_label').addClass("panel-danger")
	}else{
		$('#status_label').addClass("panel-success")
	}

})