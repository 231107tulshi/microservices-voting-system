# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import requests

# app = Flask(__name__)
# CORS(app)

# @app.route("/vote", methods=["POST"])
# def vote():

#     data = request.json
#     candidate = data["candidate"]

#     requests.post(
#         "http://127.0.0.1:5004/update",
#         json={"candidate": candidate}
#     )

#     return jsonify({"message":"Vote Successful"})


# if __name__ == "__main__":
#     app.run(port=5003, debug=True)



# from flask import Flask, request, jsonify, render_template_string
# import requests

# app=Flask(__name__)

# html="""
# <h2>Vote</h2>

# <select id='candidate'></select>

# <button onclick='load()'>Load Candidates</button>
# <button onclick='vote()'>Vote</button>

# <script>

# function load(){

# fetch("http://localhost:5002/candidates")
# .then(res=>res.json())
# .then(data=>{

# let drop=document.getElementById("candidate")

# data.forEach(c=>{
# drop.innerHTML+=`<option>${c}</option>`
# })

# })

# }

# function vote(){

# let candidate=document.getElementById("candidate").value

# fetch("/vote",{
# method:"POST",
# headers:{"Content-Type":"application/json"},
# body:JSON.stringify({candidate:candidate})
# })
# .then(res=>res.json())
# .then(data=>alert(data.message))

# }

# </script>
# """

# @app.route("/")
# def home():
#     return render_template_string(html)

# @app.route("/vote",methods=["POST"])
# def vote():

#     data=request.json

#     requests.post(
#     "http://localhost:5004/update",
#     json=data
#     )

#     return jsonify({"message":"Vote Successful"})

# app.run(port=5003,debug=True)

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

html = """
<!DOCTYPE html>
<html>

<head>
<title>Vote</title>

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

select{
width:80%;
padding:10px;
border-radius:6px;
border:1px solid #ccc;
font-size:15px;
margin-bottom:15px;
}

button{
padding:10px 14px;
border:none;
border-radius:6px;
background:#4facfe;
color:white;
font-size:14px;
cursor:pointer;
margin:5px;
}

button:hover{
background:#2d8cf0;
}

.voteBtn{
background:#28a745;
}

.voteBtn:hover{
background:#218838;
}

</style>
</head>

<body>

<div class="container">

<h2>Vote for Candidate</h2>

<select id="candidate"></select>

<br>

<button onclick="load()">Load Candidates</button>
<button class="voteBtn" onclick="vote()">Vote</button>

</div>

<script>

function load(){

fetch("http://localhost:5002/candidates")
.then(res=>res.json())
.then(data=>{

let drop=document.getElementById("candidate")

drop.innerHTML=""   // clear old options

data.forEach(c=>{
drop.innerHTML+=`<option>${c}</option>`
})

})

}

function vote(){

let candidate=document.getElementById("candidate").value

fetch("/vote",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({candidate:candidate})
})
.then(res=>res.json())
.then(data=>alert(data.message))

}

</script>

</body>

</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

@app.route("/vote", methods=["POST"])
def vote():

    data = request.json

    requests.post(
        "http://localhost:5004/update",
        json=data
    )

    return jsonify({"message":"Vote Successful"})

app.run(port=5003, debug=True)