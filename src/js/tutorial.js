$(function() {
	editor = CodeMirror.fromTextArea(document.getElementById("code"), {
		lineNumbers: true,
		matchBrackets: true,
		mode: "text/javascript"
	});
	editor2 = CodeMirror.fromTextArea(document.getElementById("output"), {
		lineNumbers: true,
		matchBrackets: true,
		mode: "text/javascript"
	});
});