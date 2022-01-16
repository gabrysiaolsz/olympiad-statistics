let number = 0;
let timer1 = 0;
let timer2 = 0;

function runaway() {
    $("#nag").fadeOut(500);
}

function change() {
    number = (number + 1) % 5;

    let image = document.getElementById("nag");

    switch (number) {
        case 0:
            image.src="/static/stats/img/nag/naglowek1.jpg";
            break;
        case 1:
            image.src="/static/stats/img/nag/naglowek2.jpg";
            break;
        case 2:
            image.src="/static/stats/img/nag/naglowek3.jpg";
            break;
        case 3:
            image.src="/static/stats/img/nag/naglowek4.jpg";
            break;
        case 4:
            image.src="/static/stats/img/nag/naglowek5.jpg";
            break;
    }
    $("#nag").fadeIn(500);

    timer1 = setTimeout("change()", 5000);
    timer2 = setTimeout("runaway()", 4500);
}
