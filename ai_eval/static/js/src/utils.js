// we load Marked in a Iframe to avoid RequireJS conflicts with the Xblock runtime
function loadMarkedInIframe(html) {
  if (!window.marked && !document.getElementById("marked-iframe")) {
    const iframe = document.createElement("iframe");
    iframe.style.display = "none";
    iframe.setAttribute("id", "marked-iframe");
    iframe.srcdoc = html;
    document.body.appendChild(iframe);
  }
}
function MarkdownToHTML(text) {
  window.marked =
    window.marked ??
    document.getElementById("marked-iframe").contentWindow.marked;
  if (typeof marked !== "undefined") text = marked.parse(text);
  return text;
}

function runFuncAfterLoading(func) {
  const markedIframe = document.getElementById("marked-iframe");
  // loading is finished when Marked is available
  if (markedIframe.contentWindow.marked) {
    func();
  } else {
    markedIframe.addEventListener("load", (event) => {
      func();
    });
  }
}

function stripScriptTags(html) {
  const div = document.createElement("div");
  div.innerHTML = html;

  const scripts = div.getElementsByTagName("script");
  while (scripts.length > 0) {
    scripts[0].parentNode.removeChild(scripts[0]);
  }

  return div.innerHTML;
}
