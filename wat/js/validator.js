function addErrorElement(txt,xnum) {
	var ni = document.getElementById('form_err');
	var numi = document.getElementById('theValue');
	var num = (document.getElementById('theValue').value -1)+ 2;
	numi.value = num;
	var newdiv = document.createElement('div');
	var divIdName = 'my'+num+'Div';
	newdiv.setAttribute('id',divIdName);
	newdiv.innerHTML = "<font color=\"red\>" + xnum + ". Please enter a "+ txt + ".";
	ni.appendChild(newdiv);
}

function validate_form()
{
	//alert('check');
	valid = true;
	var i=1;
	var err = document.getElementById("form_err");
	err.innerHTML="";
	if (document.coolForm.f2fheight.value == "" )
	{
		addErrorElement("floor to floor height",i);
		i=i+1;
		valid = false;
	}
	if (isNaN(document.coolForm.f2fheight.value) || parseInt(document.coolForm.f2fheight.value) > 20 || parseInt(document.coolForm.f2fheight.value) < .01)
	{
		addErrorElement("valid ( .01m < ; < 20m) floor to floor height",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.num_floor.value == "" )
	{
		addErrorElement("number of floors",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.num_floor.value) || parseInt(document.coolForm.num_floor.value) > 80 ||  parseInt(document.coolForm.num_floor.value) < 1)
	{
		addErrorElement("valid ( 1 < ; < 80) number of floor(s)",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.len.value == "" )
	{
		addErrorElement("length",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.len.value) || parseInt(document.coolForm.len.value) > 10000 || parseInt(document.coolForm.len.value) < 1)
	{
		addErrorElement("valid ( 1m < ; < 10000m) length",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.breadth.value == "" )
	{
		addErrorElement("breadth",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.breadth.value) || parseInt(document.coolForm.breadth.value) > 10000 || parseInt(document.coolForm.breadth.value) < 1)
	{
		addErrorElement("valid ( 1m < ; < 10000m) breadth",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.epdForm.value == "" )
	{
		addErrorElement("EPD",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.epdForm.value) ||  parseInt(document.coolForm.epdForm.value) < .001)
	{
		addErrorElement("valid ( .001m < ; ) EPD",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.ppdForm.value == "" )
	{
		addErrorElement("PPD",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.ppdForm.value) ||  parseInt(document.coolForm.ppdForm.value) < .001)
	{
		addErrorElement("valid ( .001m < ; ) PPD",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.lpdForm.value == "" )
	{
		addErrorElement("LPD",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.lpdForm.value) ||  parseInt(document.coolForm.lpdForm.value) < .001)
	{
		addErrorElement("valid ( .001m < ; ) LPD",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.Lglaze.value == "" )
	{
		addErrorElement("Left Glazing",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.Lglaze.value) ||  parseInt(document.coolForm.Lglaze.value) < 0 || parseInt(document.coolForm.Lglaze.value) > 95)
	{
		addErrorElement("valid ( 0% < ; < 95%) left glazing",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.Bglaze.value == "" )
	{
		addErrorElement("Back Glazing",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.Bglaze.value) ||  parseInt(document.coolForm.Bglaze.value) < 0 || parseInt(document.coolForm.Bglaze.value) > 95)
	{
		addErrorElement("valid ( 0% < ; < 95%) back glazing",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.Rglaze.value == "" )
	{
		addErrorElement("Right Glazing",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.Rglaze.value) ||  parseInt(document.coolForm.Rglaze.value) < 0 || parseInt(document.coolForm.Rglaze.value) > 95)
	{
		addErrorElement("valid ( 0% < ; < 95%) right glazing",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.Fglaze.value == "" )
	{
		addErrorElement("Front Glazing",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.Fglaze.value) ||  parseInt(document.coolForm.Fglaze.value) < 0 || parseInt(document.coolForm.Fglaze.value) > 95)
	{
		addErrorElement("valid ( 0% < ; < 95%) front glazing",i);
		i=i+1;
		valid = false;
	}
	if (document.coolForm.copForm.value == "" )
	{
		addErrorElement("COP",i);
		valid = false;
		i=i+1;
	}
	if (isNaN(document.coolForm.copForm.value) ||  parseInt(document.coolForm.copForm.value) < 1)
	{
		addErrorElement("valid ( 1 < ;) COP",i);
		i=i+1;
		valid = false;
	}


	return valid;
}



