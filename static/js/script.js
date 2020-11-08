const style = document.createElement('style');

let elapsedSeconds = 0;
let hourLabels = document.querySelectorAll(".hour-label");
let clockFace = document.getElementById('clock');
let wall = document.getElementById('wall');
let serverStatus = document.getElementById('statusdiv');
let getReportButton = document.getElementById('getreport');
let reportTable = document.getElementById('reporttable');
let timeStarted = document.getElementById('timestarted');


// default values
let dateObject = new Date('2020-11-03 12:00:00');
let wallColor = 'chocolate';
let clockColor = 'lavender';
let hourLabelColor = 'black';
let baseURL =  location.href;
let serverId = '';


style.innerHTML = `
@keyframes rotate {
    100% {
      transform: rotateZ(360deg);
    }
  }
`;



startClock();
setInterval(addElapsedTime, 5000);
getReportButton.addEventListener('click', getFullReport);



function addElapsedTime() {
  elapsedSeconds += 5;
  dateObject.setSeconds(dateObject.getSeconds() + 5);
  launchEvents();
}



function startClock(){
  fetch(baseURL + '/start', { 
    method: "GET",  
    headers: { 
        "Content-type": "application/json; charset=UTF-8"
    }
     
    }) 
    .then(response => response.json()) 
    .then(json => serverId = json['server_id']);

  document.head.appendChild(style);
}



function launchEvents() {
  let d = dateObject;
  // pad time string with zero if value is a single digit
  let timeStr = ("0" + d.getHours()).slice(-2) + ":" + ("0" + d.getMinutes()).slice(-2) + ":" + ("0" + d.getSeconds()).slice(-2);

   if(elapsedSeconds % 30 === 0 || elapsedSeconds % 40 === 0 || elapsedSeconds % 50 === 0) {
  
    let clockValues = {serverId:serverId,time:timeStr, wallColor: wallColor, clockColor:clockColor, labelColor:hourLabelColor}

    fetch(baseURL + '/runtask', { 
    method: "POST",  
    body: JSON.stringify(clockValues), 
    headers: { 
        "Content-type": "application/json; charset=UTF-8"
    }
     
    }) 
    .then(response => response.json()) 
    .then(json => setClockValues(json)); 

  }

}




function getFullReport() {
  fetch(baseURL + '/report', { 
    method: "POST",  
    body: JSON.stringify({serverId:serverId}), 
    headers: { 
        "Content-type": "application/json; charset=UTF-8"
    }
     
    }) 
    .then(response => response.json()) 
    .then(json => DisplayTable(json)); 

}

function DisplayTable(logData){
  timeStarted.innerHTML = logData.date;
  let tableHTML = `
  <tr>
      <th class="time-column">PROGRAM TIME</th>
      <th>EVENT</th>
      <th>MESSAGE</th>
      <th class="time-column">ACTUAL TIME</th>
      <th class="message-column">DISPLAY MESSAGE <span class="message-span">(sent to UI for display)</span></th>
  </tr>
  `
  logData.data.forEach(log => {

    tableHTML += `
    <tr>
        <td class="time-column">${log['program_time']}</td>
        <td>${log['event']}</td>
        <td>${log['message']}</td>
        <td class="time-column">${log['actual_time']}</td>
        <td>${log['display_message']}</td>
    </tr>
    ` 
  });

  reportTable.innerHTML = tableHTML;


}

function setClockValues(responseJson) {

  clockColor = responseJson['clock_color'];
  wallColor = responseJson['wall_color'];
  hourLabelColor = responseJson['label_color'];
  serverStatus.innerHTML = responseJson['message'];

  clockFace.style.background = clockColor;
  wall.style.background = `linear-gradient(to bottom, ${wallColor}, black)`;

  for (let i = 0; i < hourLabels.length; i++) {
    hourLabels[i].style.color = hourLabelColor;
}

}


