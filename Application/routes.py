from Application import app
from flask import render_template, request,json,Response
# from Application.models import Course,User,Enrollment
# from flask_restplus import Resource

courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]

# #################################################
# @api.route('/api', '/api/')
# class GetAndPost(Resource):
#     def get(self):
#         return jsonify(courseData)
    
# @api.route('/api/<idx>')
# class GetUpdateDelete(Resource):
#     def get(self, idx):
#         return jsonify(courseData)

 

################################################

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):


    return render_template("courses.html", courseData=courseData, courses=True ,term=term)

@app.route("/register")
def register():
    return render_template("register.html",register=True)

@app.route("/enrollment",methods=["GET","POST"])
def enrollment():
    id=request.form.get("courseID")
    title=request.form.get("title")
    term=request.form.get("term")
    return render_template("enrollment.html",enrollment=True,data={"id":id,"title":title,"term":term})

@app.route("/api/")
@app.route("/api/<idx>")

def api(idx=None):
    if(idx == None):
       jdata =courseData
    else:
        jdata = courseData[int(idx)]

    return Response(json.dumps(jdata), mimetype="Application/json")



# @app.route("/user")
# def user():
#     # User(user_id=1,first_name="John",last_name="Doe",email="h9u2K@example.com",password="1234").save()
#     # User(user_id=2,first_name="Mary",last_name="Jane",email="h8u2K@example.com",password="1234abc").save()
#     users = User.objects.all()
#     return render_template("user.html",users=users)
