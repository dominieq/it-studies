function isEmpty(parameter) {
    if(parameter.length == 0) {
        return true;
    }
    else {
        return false;
    }
}

function isWhiteSpace(str) { 
    var ws = "\t\n\r "; 
    for (var i = 0; i < str.length; i++) { 
        var c = str.charAt(i); 
        if (ws.indexOf(c) == -1) { 
            return false; 
        } 
    } 
    return true; 
}

function checkString(parameter, message) {
    var emptiness = isEmpty(parameter);
    var spaciness = isWhiteSpace(parameter);
    if(emptiness || spaciness) {
        alert(message);
        return false;
    }
    else {
        return true;
    }  
}

function checkEmail(str) { 
    if (isWhiteSpace(str)) { 
        alert("Incorrect e-mail"); 
        return false; 
    } 
    else { 
        var at = str.indexOf("@"); 
        if (at < 1) { 
            alert("Incorrect e-mail"); 
            return false; 
        } 
        else { 
            var l = -1; 
            for (var i = 0; i < str.length; i++) { 
                var c = str.charAt(i); 
                if (c == ".") { 
                    l = i; 
                } 
            } 
            if ((l < (at + 2)) || (l == str.length - 1)) { 
                alert("Incorrect e-mail"); 
                return false; 
            } 
        } 
        return true; 
    } 
}

function checkEmailRegEx(str) { 
    var email = /[a-zA-Z_0-9\.]+@[a-zA-Z_0-9\.]+\.[a-zA-Z][a-zA-Z]+/; 
    if (email.test(str)) 
        return true; 
    else { 
        alert("Wrong e-mail address"); 
        return false; 
    } 
}

function checkZIPCodeRegEx(parameter) {
    var ZIPCode = /^\d{2}\-\d{3}$/;
    if(ZIPCode.test(parameter)) {
        document.getElementById("ZIPCode").innerHTML = "OK";
        document.getElementById("ZIPCode").className = "green";
        return false;
    }
    else {
        document.getElementById("ZIPCode").innerHTML = "WRONG";
        document.getElementById("ZIPCode").className = "red";
        return true;
    }
}


function startTimer(fName) {
    function clearError() { 
        document.getElementById(fName).innerHTML = ""; 
    }
    window.setTimeout(clearError, 5000);
}


function checkStringAndFocus(obj, msg) {
    var str = obj.value; 
    var errorFieldName = "e_" + obj.name.substr(2, obj.name.length); 
    if (isWhiteSpace(str) || isEmpty(str)) {
        document.getElementById(errorFieldName).innerHTML = msg; 
        obj.focus();
        startTimer(errorFieldName);
        return false; 
    } 
    else { 
        return true; 
    } 
}


function showElement(e) { 
    document.getElementById(e).style.visibility = 'visible'; 
}


function hideElement(e) {
    document.getElementById(e).style.visibility = 'hidden'; 
}


function validate(form) {
    var everythingOK = true;
    if(!checkStringAndFocus(form.elements["f_fname"], "First name cannot be empty!")){
        everythingOK = false;
        form.elements["f_fname"].className = "wrong";
    }
    if(!checkStringAndFocus(form.elements["f_lname"], "Last name cannot be empty!")){
        everythingOK = false;
        form.elements["f_lname"].className = "wrong";
    }
    if(checkZIPCodeRegEx(form.elements["f_zip"].value)){
        everythingOK = false;
        form.elements["f_zip"].className = "wrong";
    }
    if(!checkStringAndFocus(form.elements["f_street"], "Street name cannot be empty!")){
        everythingOK = false;
        form.elements["f_street"].className = "wrong";
    }
    if(!checkStringAndFocus(form.elements["f_city"], "City name cannot be empty!")) {
        everythingOK = false;
        form.elements["f_city"].className = "wrong";
    }
    if(!checkEmailRegEx(form.elements["f_email"].value)){
        everythingOK = false;
        form.elements["f_email"].className = "wrong";
    }
    return everythingOK; 
}


function cnt(form, msg, maxSize) { 
    if (form.value.length > maxSize) form.value = form.value.substring(0, maxSize); 
    else msg.innerHTML = maxSize - form.value.length; 
}


function alterRows(i, e) { 
    if (e) { 
        if (i % 2 == 1) { 
            e.setAttribute("style", "background-color: Aqua;"); 
        } 
        e = e.nextSibling; 
        while (e && e.nodeType != 1) { 
            e = e.nextSibling; 
        } 
        alterRows(++i, e); 
    } 
}


function nextNode(e) { 
    while (e && e.nodeType != 1) { 
        e = e.nextSibling; 
    } 
    return e; 
}


function prevNode(e) { 
    while (e && e.nodeType != 1) { 
        e = e.previousSibling; 
    } 
    return e; 
}


function swapRows(b) { 
    var tab = prevNode(b.previousSibling); 
    var tBody = nextNode(tab.firstChild); 
    var lastNode = prevNode(tBody.lastChild); 
    tBody.removeChild(lastNode); 
    var firstNode = nextNode(tBody.firstChild); 
    tBody.insertBefore(lastNode, firstNode); 
}