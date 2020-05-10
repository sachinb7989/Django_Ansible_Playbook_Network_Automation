$("#MyForm").submit(function (event){
	event.preventDefault();
	var form = $(this),
		url = form.attr('action'),
		device_name = form.find('select[name="hostname"]').val(),
                Command = form.find('input[name="Command"]').val(),
		csrfmiddlewaretoken = form.find('input[name="csrfmiddlewaretoken"]').val(),
		error_div = form.find('div[class="invalid-feedback"]'),
		success_div = form.find('div[class="valid-feedback"]');

	error_div.hide();
	success_div.hide();

	$.ajax({
		url: url,
		method: 'POST',
		headers: {
			'X-CSRFToken': csrfmiddlewaretoken
		},
		data: {
			'hostname': device_name,
                        'command': Command,
		},
		success: function (data) {
			//error_div.show();
			//alert('Ping Successful');
			success_div.show();
			console.log(data);
var dataStr = JSON.stringify(data)
if(dataStr.length <=0)
{
	alert("Error");
}
if(data.plays[0].tasks.length>1){
	var s=data.plays[0].tasks[1].hosts;
	var str = JSON.stringify(s)
	if(str.length>0)
		alert("success")
$('#outputtable').append("<tr><td>1</td><td>"+Command+"</td><td>"+device_name+"</td><td>"+str+"</td><td>"+new Date()+"</td></tr>");
}
else
{
$('#outputtable').append("<tr><td>1</td><td>"+Command+"</td><td>"+device_name+"</td><td>"+JSON.stringify(data)+"</td><td>"+new Date()+"</td></tr>");
 alert("Error while executing command");
}

		}

	})
});
