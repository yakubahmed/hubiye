import os

from flask import *
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
import json
from city import addCity
from flask_mail import Mail,Message
from Authenticate import login_required
import string, random, datetime, random
from flask_qrcode import QRcode
import pyqrcode

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
qrcode = QRcode(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mail  = Mail(app)
app.config['MAIL_SERVER']='mail.covid19-so.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'hubiye@covid19-so.com'
app.config['MAIL_PASSWORD'] = 'Me.Yakub@2019'
mail  = Mail(app)

# Check for environment variable
#if not os.getenv("DATABASE_URL"):
    #raise RuntimeError("DATABASE_URL is not set")

# onfigure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
Session(app)

# Set up databas
engine = create_engine('postgres://ecscjmaijmcnqj:ed862132500d08d40921acc54abb57c148370e89d6ec9d89ff2beed7136bbddd@ec2-54-165-36-134.compute-1.amazonaws.com:5432/d5jspseqo3dpsu')
db = scoped_session(sessionmaker(bind=engine))

#function that allows to generate radom text
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@app.route('/')
def index():
    return  render_template('login.html')


@app.route('/admin')
@login_required
def admin():
    return  render_template('admin-index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        uname = request.form.get('Username')
        pwd  =  request.form.get('Password')
        login =  db.execute('SELECT * FROM tbl_login WHERE usename=:uname and password =:pwd', {'uname':uname, 'pwd':pwd}).fetchone()
        if login is not None:
            session['user_id'] = login['user_id']
            session['fname'] = login['fullname']
            session['mail'] = login['email_address']
            session['uname'] = login['usename']
            session['pimage'] = login['profile_image']
            session['comp_id'] = login['acc_id']
            session['user_type'] = login['user_type']
            return redirect(url_for('admin'))
        else:
            flash('invalid username or password')
    return  render_template('login.html')

#This section is the company type section
@app.route('/admin/company/type', methods=['POST', 'GET'])
@login_required
def company_type():
    cname = request.form.get('comp_type_name')
    companies_t = db.execute("SELECT * FROM tbl_company_type")
    if request.method == "POST":
        if db.execute("SELECT * FROM tbl_company_type WHERE name=:name",{"name":cname}).fetchone():
            flash("SORRY you can not add same category name twice. try another one.")
            return redirect(url_for('company_type'))
        else:
            company = db.execute("INSERT INTO tbl_company_type (name) VALUES (:ctname)", {"ctname":cname})
            db.commit()
            if company is not None:
                flash("Successfully added")
                return redirect(url_for('company_type'))
            else:
                flash("Failed to add. please try again")
                return render_template('company-type.html')
    return render_template('company-type.html', companies_t=companies_t)

@app.route('/admin/company/delete<int:id>')
@login_required
def delete_com_type(id):
   if db.execute('DELETE FROM tbl_company_type WHERE com_type_id=:ctid', {"ctid":id}):
       db.commit()
       flash("Deleted successfully")
       return redirect(url_for('company_type'))

@app.route('/admin/company-type/update/<int:id>', methods=['POST','GET'])
@login_required
def updat_com_type(id):
    ctypes  = db.execute("SELECT * FROM tbl_company_type")
    ctype = db.execute("SELECT * FROM tbl_company_type WHERE com_type_id=:id", {"id":id}).fetchone()
    if request.method == "POST":
        ctname = request.form.get('comp_type_name')
        if db.execute("UPDATE tbl_company_type SET name=:name WHERE com_type_id=:id", {"name":ctname, "id":id}):
            db.commit()
            flash("Updated succesfully")
            return redirect(url_for('company_type'))
    return render_template('edite-company-type.html', c=ctype, ctypes=ctypes)
       
#....end of company type

@app.route('/admin/product', methods=['POST', 'GET'])
@login_required
def product():
    cid = session.get("comp_id")
    #companies = db.execute("SELECT * FROM tbl_company").fetchall()
    products = db.execute("SELECT * FROM view_product WHERE comp_id=:id", {'id':cid}).fetchall()

    if request.method == "POST":
        com_id = session.get("comp_id")
        pname = request.form.get('pname')
        pdesc = request.form.get('pdesc')
        edate = request.form.get('expdate')
        mdate = request.form.get('expdate')
        pcode = random.randint(10,5000000000000000)
        #QR CODE
        #qrgen(tex)
        code = "https://hubiye.herokuapp.com/product-description/"+str(pcode)+edate
        qr = pyqrcode.create(code)
        qr.png('static/images/'+pname+str(pcode)+'.png',scale = 2)

        filename = 'static/images/'+pname+str(pcode)+'.png'
        #return send_file(filename,as_attachment=True)

        status='active'
        if db.execute("INSERT INTO tbl_product (product_name, comp_id, description, man_date, exp_date, status, product_code, code ) VALUES(:pname, :cid, :des, :mdate, :edate, :status, :pcode, :c)",{"pname":pname, "cid":com_id, "des":pdesc, "mdate":mdate, "edate":edate, "status":status, "pcode":pname+str(pcode)+'.png', 'c':str(pcode)+edate}):
            db.commit()
            send_file(filename,as_attachment=True)
            flash('Product added successfully')
            return redirect(url_for('product'))

        
    return render_template('add-new-product.html',  products=products)

@app.route('/admin/product/barcode/<int:id>', methods=['POST','GET'])
def product_barcode(id):
    product = db.execute("SELECT * FROM tbl_product WHERE product_id=:id", {'id':id}).fetchone()

    return render_template('barcode.html', product=product)


#This section contains all thinks about City
@app.route('/admin/city', methods = ['POST', 'GET'])
@login_required
def add_manage_city():
    if request.method == "POST":
        addCity()
    cities = db.execute('SELECT * FROM  tbl_city ').fetchall()
    return render_template('cities.html', cities=cities)



#this function is the function that allows to delete cities
@app.route('/admin/city/delete/<int:id>')
@login_required
def delete_city(id):
    if db.execute("SELECT * FROM tbl_city WHERE city_id=:cid", {"cid":id}).fetchall():
        if db.execute("DELETE FROM tbl_city WHERE city_id=:cid", {"cid":id}):
            db.commit()
            flash("Deleted successfully")
            return redirect(url_for('add_manage_city'))
    else:
        flash("The city you are trying to delete is not found")
        return redirect(url_for('add_manage_city'))

##############################################
@app.route('/admin/city/edite/<int:id>', methods=['POST','GET'])
@login_required
def update_city(id):
    city = db.execute("SELECT * FROM tbl_city WHERE city_id=:cid", {"cid":id}).fetchone()
    cities = db.execute("SELECT * FROM tbl_city  ").fetchall()
    if request.method == "POST":
        cityname = request.form.get('cityname')
        if db.execute("SELECT * FROM tbl_city WHERE city_id=:cid", {"cid":id}).fetchall():
            if db.execute("UPDATE tbl_city set city_name=:cname WHERE city_id=:cid", {"cid":id, "cname":cityname}):
                db.commit()
                flash("Updated successfully")
                return redirect(url_for('add_manage_city'))
            else:
                flash("SOmething is wrong please try again")
                return redirect(url_for('add_manage_city'))
        else:
            flash("The city that you are trying to update is not found")
            return redirect(url_for('add_manage_city'))
    
    return render_template('edite-city.html', city=city, id=id, c=cities)

#..../end city section

@app.route('/admin/user-setting')
@login_required
def user_setting():
    fname = session.get("fname")
    userid  = session.get('mail')
    image  = session.get('pimage')
    uname  = session.get('uname')

    return render_template('user-setting.html')

@app.route('/admin/company/add', methods=['POST','GET'])
@login_required
def add_new_comp():
    ctype = db.execute("SELECT * FROM tbl_company_type")
    City = db.execute("SELECT * FROM tbl_city")
    if request.method == "POST":
        cname = request.form.get('com_name')
        ctid = request.form.get('com_type_id')
        cid = request.form.get('city_id')
        desc = request.form.get('com_desc')
        addr = request.form.get('com_addr')
        cphone = request.form.get('com_phone')
        rfname = request.form.get('rfname')
        remail = request.form.get('email')
        rusername = request.form.get('rusername')
        rphone = request.form.get('rphone')
        currdate = datetime.date.today()
        status = 'active'

        #Check if the company is already registered
        if db.execute('SELECT * FROM tbl_company WHERE comp_name=:cname', {'cname':cname}).fetchone():
            flash('A company with this name: ' + cname + ' is allready is registered')
        elif db.execute('SELECT * FROM tbl_login WHERE email_address=:mail', {"mail":remail}).fetchone():
            flash('This is email: ' + remail + " is allready registered. try another one.")
        elif db.execute('SELECT * FROM tbl_login WHERE usename=:user', {"user":rusername}).fetchone():
            flash('This is email: ' + remail + " is allready registered. try another one.")
        else:
            #Inserting company details to the database
            company = db.execute('INSERT INTO tbl_company (comp_name, com_type_id, comp_description, city_id, comp_address, \
                comp_phone, rep_phone, reg_date, status) \
                    VALUES(:cname, :ctid, :cdesc, :cid, :caddr, :cphone, :rphone, :rdate, :status) \
                    ', {"cname":cname, "ctid":ctid, "cdesc":desc, "cid":cid, "caddr":addr, "cphone":cphone,  "rphone": rphone,  "rdate": currdate, "status":status})
            db.commit()
            code =  randomString(10)
            c = db.execute("SELECT * FROM tbl_company WHERE comp_name=:name",{"name":cname}).fetchone()
            user = db.execute("INSERT INTO tbl_login (fullname, email_address, user_type, acc_id, ver_code) \
                VALUES(:fname, :ema, :type, :uid, :code)", {"fname":rfname, "ema":remail,  "type":'company', "uid":c.comp_id, "code":code})
            db.commit()
            if company:
                msg = Message("Welcome to Hubiye",
                sender=('Hubiye', "hubiye@covid19-so.com"),
                recipients=[remail])
                msg.body = "Welcome to Hubiye"
                msg.html = "Asc <b>" + cname +"</b>, ku soo dhawaaw hubiye app. si aad isku diiwan geliso fur lifaaqa hoose. \
                <br> <a  href='https://hubiye.herokuapp.com/new-user/"  + code + "'>Click here<a>"
                mail.send(msg)

                flash("Company added successfully")
                return redirect(url_for('add_new_comp'))
            else:
                flash('Fialed to add')
        
    return render_template('addCompany.html', ctypes=ctype, city=City)

@app.route('/admin/edit-company/<int:id>', methods=['POST','GET'])
def edit_comp(id):
    company = db.execute("SELECT * FROM tbl_company WHERE comp_id=:id", {'id':id}).fetchone()
    user = db.execute("SELECT * FROM tbl_login WHERE acc_id=:id", {'id':id}).fetchone()
    ctype = db.execute("SELECT * FROM tbl_company_type")
    City = db.execute("SELECT * FROM tbl_city")
    if request.method == "POST":
        cname = request.form.get('com_name')
        ctid = request.form.get('com_type_id')
        cid = request.form.get('city_id')
        desc = request.form.get('com_desc')
        addr = request.form.get('com_addr')
        cphone = request.form.get('com_phone')
        rfname = request.form.get('rfname')
        remail = request.form.get('email')
        rusername = request.form.get('rusername')
        rphone = request.form.get('rphone')
        currdate = datetime.date.today()
        status = 'active'
        #Check if the company is already registered
        #Inserting company details to the database
        company = db.execute('UPDATE tbl_company SET comp_name=:cname,  com_type_id=:ctid, comp_description=:cdesc, city_id=:cid, comp_address=:caddr, \
            comp_phone=:cphone, rep_phone=:rphone, reg_date=:rdate WHERE comp_id=:id \
                ', {"cname":cname, "ctid":ctid, "cdesc":desc, "cid":cid, "caddr":addr, "cphone":cphone,  "rphone": rphone,  "rdate": currdate,  'id':id})
        db.commit()
        #c = db.execute("SELECT * FROM tbl_company WHERE comp_name=:name",{"name":cname}).fetchone()
        use = db.execute("UPDATE tbl_login SET fullname=:fname, email_address=:ema, usename=:uname WHERE acc_id=:aid ", {"fname":rfname, "ema":remail, "uname":rusername, 'aid':user.acc_id})
        db.commit()
        flash('Info Updated successfully')
        return redirect(url_for('manage_company'))
            
            

    return render_template('edit-company.html', id=id, ctypes=ctype, city=City, company=company, user=user)

@app.route('/admin/manage-company')
def manage_company():
    company = db.execute("SELECT * FROM view_company").fetchall()
    return render_template('manage-company.html', companies=company)
@app.route('/admin/delete-company/<int:id>')
def delete_comp(id):
    if db.execute("DELETE FROM tbl_company WHERE comp_id=:id", {'id':id}):
        db.commit()
        flash('Successfully deleted..')
        return redirect(url_for('manage_company'))
    else:
        flash('Failed to delete. try aain')
        return redirect(url_for('manage_company'))

@app.route('/admin/company-detail/<int:id>')
def comp_detail(id):
    row = db.execute('SELECT * FROM view_company WHERE comp_id=:id', {'id':id}).fetchone()
    return render_template('single-company.html',row=row)
   

@app.route('/admin/users', methods =['POST','GET'])
def users():
    fullname =  request.form.get('fname')
    email = request.form.get('email')
    id = session['user_id']
    users  =  db.execute("SELECT * FROM tbl_login WHERE user_id !=:id",{"id":id}).fetchall()
    if request.method == "POST":
        if db.execute("SELECT * FROM tbl_login WHERE email_address=:email",{"email":email}).fetchone():
            flash('The email that you entered is already taken please try another one')
            return render_template('add-manage-user.html')
        else:
            code =  randomString(10)
            db.execute("INSERT INTO tbl_login (fullname,email_address, ver_code, status, user_type) VALUES (:fname,:mail,:vcode, 'active', 'admin')", {"fname":fullname,"mail":email, "vcode":code})
            db.commit()
            msg = Message("Welcome to Hubiye",
                sender=('Hubiye', "hubiye@covid19-so.com"),
                recipients=[email])
            msg.body = "Welcome to Hubiye"
            msg.html = "Asc <b>" + fullname +"</b>, ku soo dhawaaw hubiye app. si aad isku diiwan geliso fur lifaaqa hoose. \
                <br> <a href='https://hubiye.herokuapp.com/new-user/' + code + "' > Click </a>"
            mail.send(msg)
         
            #Here is place to send an email to the user
            flash('User added successfully, we sent insturctions through this email: ' + email + '.')
            return redirect(url_for('users'))
    return render_template('add-manage-user.html', users=users)

@app.route('/new-user/<key>', methods=['POST','GET'])
def new_user(key):
    if not db.execute('SELECT * FROM tbl_login WHERE ver_code=:c', {'c':key}).fetchone():
        return redirect(url_for('login'))
    if request.method == "POST":
        username = request.form.get('Username')
        pwd = request.form.get('Password')
        cpwd = request.form.get('cpassword')
        if db.execute("SELECT * FROM tbl_login WHERE usename=:u", {'u':username}).fetchone():
            flash('This username is already taken please try another one')
        elif pwd != cpwd:
            flash('Password and confirm password does not match')
        else:
            uimage = request.files['uimage']
            image = request.form.get('uimage')
            if db.execute("UPDATE tbl_login SET usename=:u, password=:p, profile_image=:img WHERE ver_code=:code", {'u':username, 'p':pwd, 'img':uimage.filename, 'code':key}):
                db.commit()
                file = request.files['uimage']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(UPLOAD_FOLDER, filename))
                    if db.execute("UPDATE tbl_login SET ver_code='' WHERE usename=:u", {'u':username}):
                        db.commit()
                        flash('your account is created succesfully, know you can login')
                        return redirect('logout')
            

    return render_template('new-user.html', code=key)

@app.route('/admin/delete/user/<int:id>')
@login_required
def delete_user(id):
   if db.execute("DELETE FROM tbl_login WHERE user_id =:uid", {'uid':id}):
       db.commit()
       flash("User deleted successfully")
       return redirect(url_for('users'))

@app.route("/logout")
@login_required
def logout():
    session.pop("user_id",None)
    session.pop("fname",None)
    session.pop("mail",None)
    session.pop("uname",None)
    session.pop("pimage",None)
    return redirect(url_for('login'))

#Allowed image file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/admin/profile/update-detail',methods=['POST'])
def update_user():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        fname = request.form.get('fname')
        id = session['user_id']
        if db.execute("UPDATE tbl_login SET usename=:u,email_address=:e, fullname=:f WHERE user_id=:id", {'u':username, 'e':email, 'f':fname, 'id':id}):
            db.commit()
            flash('Detail upated successfully')
            return redirect(url_for('logout'))


@app.route('/admin/profile/update-password' ,methods=['POST'])
def update_pwd():
    if request.method == "POST":
        cpwd = request.form.get('currpwd')
        npwd = request.form.get('newpwd')
        cnpwd = request.form.get('cnewpwd')
        id = session['user_id']

        if db.execute("SELECT * FROM tbl_login WHERE password=:p and user_id=:uid", {'p':cpwd, 'uid':id}).fetchone():
            if npwd == cnpwd:
                if db.execute("UPDATE tbl_login SET password=:p WHERE user_id =:id", {'p':npwd, 'id':id}):
                    db.commit()
                    flash('Password has changes successfully')
                    return redirect(url_for('logout'))
            else:
                flash('New password and confirm password does not match')
        else:
            flash('invalid password')
    return render_template('user-setting.html')
    
@app.route('/product-description/<p_code>')
def pro_des(p_code):
    product = db.execute("SELECT * FROM view_product WHERE code=:pc", {'pc':p_code}).fetchone()
    return render_template('index.html', product=product)   
                
@app.route('/admin/profile/change-image', methods=['POST'])
def change_image():
    if request.method == "POST":
        uimage = request.files['pimage']
        image = request.form.get('pimage')
        id = session['user_id']
        
        if db.execute("UPDATE tbl_login SET profile_image=:p WHERE user_id=:id", {'p':uimage.filename, 'id':id}):
            flash('Profile updated successfully')
            return redirect(url_for('logout'))
        file = request.files['pimage']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

    return ""

@app.route('/forgot/username', methods=['POST','GET'])
def forgot_username():
    if request.method == "POST":
        email = request.form.get('email')
        user = db.execute('SELECT * FROM tbl_login WHERE email_address=:e', {'e':email}).fetchone()
        if user is not None:
            msg = Message("Username reset request",
            sender=('Hubiye', "hubiye@covid19-so.com"),
            recipients=[email])
            msg.body = "Username reset Hubiye"
            msg.html = "Hello  <b>" + user.fullname +"</b>, you requested username reset. <br> \
                your username is <b> " + user.usename +"</b>. "
            mail.send(msg)
            flash('Check your email. ')
            return redirect(url_for('login'))
        else:
            flash('Email not found.')
    
    return render_template('forgot-username.html')

@app.route('/forgot-password', methods=['POST','GET'])
def forgot_password():
    if request.method == "POST":
        email = request.form.get('email')
        user = db.execute('SELECT * FROM tbl_login WHERE email_address=:e', {'e':email}).fetchone()
        vcode =  randomString(10)


        if user is not None:
            code = db.execute("UPDATE tbl_login SET ver_code=:vcode WHERE email_address=:e", {'vcode':vcode,'e':email})
            db.commit()
            msg = Message("Password reset request",
            sender=('Hubiye', "hubiye@covid19-so.com"),
            recipients=[email])
            msg.body = "Password reset Hubiye"
            msg.html = "Hello  <b>" + user.fullname +"</b>, you requested password reset. <br> \
              to recover your password click link below. <br> https://hubiye.herokuapp.com/new-password/" + vcode + "' "
            mail.send(msg)
            flash('Check your email. we sent you instructions ')
            return redirect(url_for('forgot_password'))
        else:
            flash('Email not found.')
    return render_template('forgot-password.html')

@app.route('/new-password/<key>', methods=['POST','GET'])
def new_password(key):
    password = request.form.get('password')
    cpassword = request.form.get('cpassword')
    if not db.execute('SELECT * FROM tbl_login WHERE ver_code=:v',{'v':key}).fetchone():
        flash('you dont have access to this page')
        return redirect(url_for('login'))
    if request.method == "POST":
        user = db.execute("SELECT * FROM tbl_login WHERE ver_code=:v",{'v':key}).fetchone()
        if password != cpassword:
            flash('Password and confirm password does not match')
        else:
            if db.execute('UPDATE tbl_login SET password=:p WHERE ver_code=:vcode',{'p':password, 'vcode':key}):
                db.commit()
            if db.execute("UPDATE tbl_login SET ver_code='' WHERE email_address=:e", {'e':user.email_address}):
                db.commit()
            flash('your password is changes successfully')
            return redirect(url_for('login'))

    return render_template('new-password.html', key=key)

if __name__ == "__main__":
    app.run(debug=True)

