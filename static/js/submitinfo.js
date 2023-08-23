function submitinfo() {
    var name_ = document.getElementById("name").value;
    var wechat_id = document.getElementById("wechat-id").value;
    var experience = document.getElementById("experience").value;
    if (name_ == "" || wechat_id == "" || experience == "") {
        alert("麻烦填好信息再来提交嘛")
    } else {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
          if (xhr.readyState == 4 && xhr.status == 200) {
            alert("提交成功！")
          }
        }
        xhr.open("POST", "/submitinfo", true)
        xhr.send(JSON.stringify({'name': name_, 'wechat-id': wechat_id, 'experience': experience}))
    }
}