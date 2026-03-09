// async function generateBlog() {

//     const topic = document.getElementById("topic").value;

//     const response = await fetch("http://127.0.0.1:8000/generate-blog", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({
//             topic: topic
//         })
//     });

//     const data = await response.json();

//     document.getElementById("result").innerText = data.result;
// }

async function generateBlog() {

    const topicInput = document.getElementById("topic");
    const topic = topicInput.value;

    if(!topic) return;

    const chat = document.getElementById("chat");

    /* USER MESSAGE */

    const userMsg = document.createElement("div");
    userMsg.className = "message user";
    userMsg.innerText = topic;
    chat.appendChild(userMsg);

    /* BOT MESSAGE */

    const botMsg = document.createElement("div");
    botMsg.className = "message bot";
    chat.appendChild(botMsg);

    topicInput.value = "";

    chat.scrollTop = chat.scrollHeight;

    const response = await fetch("http://127.0.0.1:8000/generate-blog",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({topic:topic})
    });

    const data = await response.json();

    const text = data.result;

    streamMarkdown(text, botMsg);

}

/* Streaming Markdown */

function streamMarkdown(text, element){

    let i = 0;

    const interval = setInterval(()=>{

        element.innerHTML = marked.parse(text.slice(0,i));

        i++;

        if(i >= text.length){
            clearInterval(interval);
        }

        element.parentElement.scrollTop = element.parentElement.scrollHeight;

    },10);

}