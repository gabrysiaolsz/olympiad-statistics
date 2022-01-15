var number = Math.floor(Math.random()*4)+1;

var timer1 = 0;
var timer2 = 0;

function runaway()
{
    $("#nag").fadeOut(500);
}

function change()
{
    number++; 

    if (number>5)
    {
	number=1;	
    }

    switch(number)
    {

        case number:
        {
            $('#nag').html("<img src=\"img/nag/naglowek" + number + ".jpg\" class=\"slajd-naglowek\" />");
        }
        break;

    }
    $('#nag').fadeIn(500);

    timer1 = setTimeout("change()", 5000); 
    timer2 = setTimeout("runaway()", 4500);

}
