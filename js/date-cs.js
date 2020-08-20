// function loadCSS(filename) {
//     $("<link/>", {
//         rel: "stylesheet",
//         type: "text/css",
//         href: filename
//     }).appendTo("head");
// }

// function loadJS(filename) {
//     $("<script>", {
//         src: filename,
//         type: "text/javascript"
//     }).appendTo("head");
// }

function parseDate(date) {
    date = String(date);
    var newDate = new Date();
    newDate.setFullYear(date.substring(0, 4));
    newDate.setMonth(date.substring(4, 6) - 1);
    newDate.setDate(date.substring(6, 8));
    return newDate;
}

function ScrollToToday() {
    var dates = document.getElementsByTagName("date");
    var today = new Date();
    for (var i = 0; i < dates.length; i++) {
        var eventDate = parseDate(dates[i].getAttribute('d'));

        if ((eventDate >= (today.getTime() - (259200000))) && (eventDate <= (today.getTime() + 345600000))) {
            dates[i].id = "today";
            dates[i].scrollIntoView();
        }
    }
}

ScrollToToday();
