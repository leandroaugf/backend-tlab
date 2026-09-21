document.querySelector("#start_chat").addEventListener("click", (event) => {

    const socket = io();

    const chat_help = document.getElementById("chat_help");
    chat_help.style.display = "none";

    const chat_support = document.getElementById("chat_support");
    chat_support.style.display = "block";

    const email = document.getElementById("email").value;
    const text = document.getElementById("txt_help").value;

    socket.on("connect", () => {
        const params = {
            email, 
            text
        }
        socket.emit("client_first_access", params, (call, err) => {
            if (err) console.log(err);
            else console.log(call);
        })
    })

});
/*console.log("CHAT.JS FOI CARREGADO");

const button = document.querySelector("#start_chat");

console.log("BOTÃO:", button);

button.addEventListener("click", () => {
    console.log("CLIQUEI EM INICIAR CHAT");

    const socket = io();

    socket.on("connect", () => {
        console.log("CONECTADO:", socket.id);
    });
});*/