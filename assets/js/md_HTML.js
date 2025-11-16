/* Load script that can parse md to html */
const markedScript = document.createElement("script");
markedScript.src = "https://cdn.jsdelivr.net/npm/marked/marked.min.js";
document.head.appendChild(markedScript);