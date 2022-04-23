const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data)
    const div = document.createElement('div');
    div.className = 'message_item';
    div.innerHTML = `
    <h3 class="message_author">${data.username} <small>${Date(data.timestamp * 1000).slice(0, 24)}</small></h3>
    <div class="message_content">${data.message}</div>
    `;
    if(data.username == username){
        div.classList.add("my-message");
    }
    document.getElementById('message_part').appendChild(div);
    var objDiv = document.getElementById("message_part");
    objDiv.scrollTop = objDiv.scrollHeight;
};

chatSocket.onclose = function(e) {
    // $('#LostModal').modal('show');
    var myModal = new bootstrap.Modal(document.getElementById('LostModal'))
    myModal.show()
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': username,
        'timestamp': Date.now(),
        'room_id': room_id

    }));
    messageInputDom.value = '';
};