var bad_val = "Недопустивое значение";
var unreal_calc = "Невозможно вычислить";
var result = [];

function corrected_number(input_id){
	"use strict"; // для браузеров с поддержкой строгого режима

	var val = document.getElementById(input_id).value.toString();
	var testing_num = new RegExp("^([1-9][0-9]*|0|" + bad_val + "|" + unreal_calc + ")$");
	var edit_num = new RegExp("^0*?([1-9][0-9]*|0|" + bad_val + "|" + unreal_calc + ")$");
	console.log(edit_num.exec(val))

	if (!testing_num.test(val)){
		if (edit_num.test(val)){
			console.log('===', edit_num.exec(val)[1])
			document.getElementById(input_id).value = edit_num.exec(val)[1];
		} else {
			document.getElementById(input_id).value = "";
		}
	}

}

function correcting_number(input_id){
	"use strict"; // для браузеров с поддержкой строгого режима

	var val = document.getElementById(input_id).value.toString();
	var testing_num = new RegExp("^0*?([1-9][0-9]*|0)$");
	var edit_num = new RegExp("^0*?([1-9][0-9]*|0)$");
	console.log(edit_num.exec(val))
	if (!testing_num.test(val)){
		if (edit_num.test(val)){
			document.getElementById(input_id).value = edit_num.exec(val)[1];
		} else {
			document.getElementById(input_id).value = "";
		}
	}
}