# from flask import render_template, redirect, request, session, flash
# from models.user_model import User
# from models.business_model import Business

# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

# @app.route('/')
# def index():
#     return redirect("/")

# @app.route('/login')
# def login():
#     return render_template("login.html")	

# @app.route('/logout')
# def logout():
#     session.clear()
#     print("This user's session has been cleared.")
#     return redirect('/')




# @app.route('/dashboard')
# def dashboard():
#     if "user_id" in session:
#         return render_template("dashboard.html", user = User.get_one({"id": session['user_id']}), 
#     all_sightings = Business.get_all_businesses_with_user())
#     else:
#         return redirect('/')