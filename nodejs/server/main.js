const WS_URL = 'ws://' + location.host.replace('8000', '6700');

let sendMessage = (message) => {
    let connection = new WebSocket(WS_URL);
    connection.onopen = () => {
        connection.send(message);
        connection.close();
    };
};

let sendQuery = (message, callback) => {
    let connection = new WebSocket(WS_URL);
    connection.onopen = () => {
        connection.send(message);
    };
    connection.onmessage = (e) => {
        callback(e.data);
    };
    setTimeout(() => {
        console.log("timeout");
        connection.close();
    }, 1000);
};

// WSに接続して、一覧を取得する
sendQuery("serif_list", (data) => {
    console.log(data);
    let $list = $('select.serif');
    let serifList = data.split(",");
    for (let serif of serifList) {
        $list.append($('<option>').val(serif).text(serif));
    }
});

$('.play-button').on('click', (e) => {
    let targetId = $(e.target).data('id');
    let serif = $(`.${targetId}`).val();
    console.log(serif);
    // WSに接続して、送信する
    sendMessage("serif," + serif);
});
