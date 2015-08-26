
var form_data = location.search;
var form_tokens = form_data.split('&');
var json_object = {}

for(var i = 0; i < form_tokens.length; i++){
  var key_value = form_tokens[i].split('=');
  json_object[key_value[0]] = key_value[1];
}
console.log(location.search);
console.log("\n\n"+ form_tokens);
console.log(json_object);


$.post("http://gogol-ubuntu/post-test.html", json_object, function(data, result){
    alert("Data: " + data + "\nStatus: " + status);
});
