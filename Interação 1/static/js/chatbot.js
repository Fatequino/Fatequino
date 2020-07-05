const URL = "http://127.0.0.1:5000/";

function getBotResponse() {
    
    let rawText = jQuery("#textInput").val();
    let userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
    
    jQuery("#textInput").val("");
    jQuery("#chatbox").append(userHtml);
    document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});

   let ajax = new XMLHttpRequest();
   ajax.open("GET", `${URL}get?msg=${encodeURI(rawText)}`, true);
   ajax.send();
   
   ajax.onreadystatechange = function() {

    if (ajax.readyState == 4 && ajax.status == 200) {
        let data = ajax.responseText;
        let botHtml = `<p class="botText">
                            <img class="avatar" src="https://fatequino.com.br/wp-content/uploads/fatequino-avatar2.png" alt="avatar"/>
                            <span>${data}</span>
                       </p>`;
        jQuery("#chatbox").append(botHtml);
        document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
        console.log(data);
    }
  }

}

jQuery("#textInput").keypress(function(e) {
    if(e.which == 13) {
        getBotResponse();
    }
});

jQuery("#buttonInput").click(function() {
    getBotResponse();
})
