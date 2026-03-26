# # from flask import Flask, request, jsonify
# # from flask_cors import CORS

# # app = Flask(__name__)
# # CORS(app)

# # results = {}

# # @app.route("/update", methods=["POST"])
# # def update():

# #     data = request.json
# #     candidate = data["candidate"]

# #     if candidate in results:
# #         results[candidate] += 1
# #     else:
# #         results[candidate] = 1

# #     return "ok"


# # @app.route("/results")
# # def results_data():
# #     return jsonify(results)


# # if __name__ == "__main__":
# #     app.run(port=5004, debug=True)

# from flask import Flask, request, jsonify

# app=Flask(__name__)

# results={}

# @app.route("/")
# def home():

#     html="<h2>Results</h2><table border=1><tr><th>Candidate</th><th>Votes</th></tr>"

#     for k,v in results.items():
#         html+=f"<tr><td>{k}</td><td>{v}</td></tr>"

#     html+="</table>"

#     return html

# @app.route("/update",methods=["POST"])
# def update():

#     data=request.json
#     c=data["candidate"]

#     if c in results:
#         results[c]+=1
#     else:
#         results[c]=1

#     return "ok"

# @app.route("/results")
# def get_results():
#     return jsonify(results)

# app.run(port=5004,debug=True)

from flask import Flask, request, jsonify

app=Flask(__name__)

results={}

@app.route("/")
def home():

    html="""
<!DOCTYPE html>
<html>

<head>
<title>Voting Results</title>

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

tr:nth-child(even){
background:#f2f2f2;
}

</style>
</head>

<body>

<div class="container">

<h2>Voting Results</h2>

<table>
<tr>
<th>Candidate</th>
<th>Votes</th>
</tr>
"""

    for k,v in results.items():
        html+=f"<tr><td>{k}</td><td>{v}</td></tr>"

    html+="""
</table>

</div>

</body>
</html>
"""

    return html


@app.route("/update",methods=["POST"])
def update():

    data=request.json
    c=data["candidate"]

    if c in results:
        results[c]+=1
    else:
        results[c]=1

    return "ok"


@app.route("/results")
def get_results():
    return jsonify(results)

app.run(port=5004,debug=True)