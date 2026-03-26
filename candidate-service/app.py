# from flask import Flask, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# candidates = [
#     {"name":"Alice"},
#     {"name":"Bob"},
#     {"name":"Charlie"},
#     {"name":"David"},
#     {"name":"Emma"}
# ]

# @app.route("/candidates")
# def get_candidates():
#     return jsonify(candidates)


# if __name__ == "__main__":
#     app.run(port=5002, debug=True)

# # from flask import Flask, jsonify
# # from flask_cors import CORS

# # app = Flask(__name__)
# # CORS(app)

# # candidates = [
# #  {"name":"Alice"},
# #  {"name":"Bob"},
# #  {"name":"Charlie"},
# #  {"name":"David"},
# #  {"name":"Emma"}
# # ]

# # @app.route("/candidates")
# # def candidates_list():
# #     return jsonify(candidates)

# # if __name__ == "__main__":
# #     app.run(port=5002, debug=True)
# from flask import Flask, jsonify

# app = Flask(__name__)

# candidates=["Alice","Bob","Charlie","David","Emma"]

# @app.route("/")
# def home():

#     html="<h2>Candidates</h2><table border=1>"

#     for c in candidates:
#         html+=f"<tr><td>{c}</td></tr>"

#     html+="</table>"

#     return html

# @app.route("/candidates")
# def get_candidates():
#     return jsonify(candidates)

# app.run(port=5002,debug=True)
from flask import Flask, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# candidates=["Alice","Bob","Charlie","David","Emma"]

candidates = [
"Ramesh Patil - Lotus Party",
"Sanjay Deshmukh - People's Party",
"Anita Kulkarni - Development Party",
"Vikram Joshi - Independent",
"Pooja Shinde - Citizen Party"
]

html="""
<!DOCTYPE html>
<html>
<head>
<title>Candidates</title>

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

table{
width:100%;
border-collapse:collapse;
margin-top:10px;
}

th,td{
padding:12px;
border:1px solid #ddd;
text-align:center;
}

th{
background:#4facfe;
color:white;
}

tr:nth-child(even){
background:#f2f2f2;
}

</style>
</head>

<body>

<div class="container">

<h2>Candidate List</h2>

<table>

<tr>
<th>Candidate Name</th>
</tr>

""" + "".join([f"<tr><td>{c}</td></tr>" for c in candidates]) + """

</table>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

@app.route("/candidates")
def get_candidates():
    return jsonify(candidates)

app.run(port=5002,debug=True)