from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users=[]

html="""
<!DOCTYPE html>
<html>
<head>
<title>User Registration</title>

<style>

*{
box-sizing:border-box;
font-family:Arial, sans-serif;
}

body{
margin:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:linear-gradient(135deg,#4facfe,#00f2fe);
}

.container{
background:white;
padding:35px;
border-radius:12px;
box-shadow:0 10px 25px rgba(0,0,0,0.2);
width:420px;
text-align:center;
}

h2{
margin-bottom:20px;
}

input{
width:70%;
padding:10px;
border:1px solid #ccc;
border-radius:6px;
font-size:15px;
margin-right:5px;
}

button{
padding:10px 14px;
border:none;
border-radius:6px;
background:#4facfe;
color:white;
font-size:14px;
cursor:pointer;
transition:0.3s;
}

button:hover{
background:#2d8cf0;
}

.secondary{
margin-top:15px;
background:#28a745;
}

table{
width:100%;
margin-top:20px;
border-collapse:collapse;
}

th,td{
padding:10px;
border:1px solid #ddd;
text-align:center;
}

th{
background:#4facfe;
color:white;
}

</style>
</head>

<body>

<div class="container">

<h2>User Registration</h2>

<div>
<input id="name" placeholder="Enter name">
<button onclick="register()">Register</button>
</div>

<h3>Users</h3>

<button class="secondary" onclick="loadUsers()">Show Users</button>

<table id="table"></table>

</div>

<script>

function register(){

let name=document.getElementById("name").value

fetch("/register",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({name:name})
})
.then(res=>res.json())
.then(data=>{
alert(data.message)
})

}

function loadUsers(){

fetch("/users")
.then(res=>res.json())
.then(data=>{

let table=document.getElementById("table")

table.innerHTML="<tr><th>Name</th></tr>"

data.forEach(u=>{
table.innerHTML+=`<tr><td>${u.name}</td></tr>`
})

})

}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

@app.route("/register",methods=["POST"])
def register():
    data=request.json
    users.append(data)
    return jsonify({"message":"User Registered"})

@app.route("/users")
def get_users():
    return jsonify(users)

app.run(port=5001,debug=True)