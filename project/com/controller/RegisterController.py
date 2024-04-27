from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template, request, redirect, url_for
from project import app
import random
import smtplib
import string
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession


@app.route('/user/loadRegister')
def adminLoadUser():
    try:
        return render_template('user/register.html')

    except Exception as ex:
        print(ex)


@app.route('/user/insertRegister', methods=['POST'])
def adminInsertRegister():
    try:

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        registerVO = RegisterVO()
        registerDAO = RegisterDAO()

        loginUsername = request.form['loginUsername']

        registerFirstname = request.form['registerFirstname']
        registerLastname = request.form['registerLastname']
        registerGender = request.form['registerGender']
        registerContactNumber = request.form['registerContactNumber']

        loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))

        sender = "automatesurveillancesystem@gmail.com"

        receiver = loginUsername

        msg = MIMEMultipart()

        msg['From'] = sender

        msg['To'] = receiver

        msg['Subject'] = "LOGIN PASSWORD"

        msg.attach(MIMEText(loginPassword, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender, "m@lh@r3003")

        text = msg.as_string()

        server.sendmail(sender, receiver, text)

        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginRole = "user"
        loginVO.loginStatus = "active"

        loginDAO.insertLogin(loginVO)

        registerVO.registerFirstname = registerFirstname
        registerVO.registerLastname = registerLastname
        registerVO.registerGender = registerGender
        registerVO.registerContactNumber = registerContactNumber

        registerVO.register_LoginId = loginVO.loginId

        registerDAO.insertRegister(registerVO)

        server.quit()

        return render_template('admin/login.html')

    except Exception as ex:
        print(ex)


@app.route('/admin/viewUser')
def adminViewUser():
    try:
        if adminLoginSession() == "admin":
            registerDAO = RegisterDAO()
            registerVOList = registerDAO.viewUser()

            return render_template("admin/viewUser.html", registerVOList=registerVOList)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/blockUser', methods=['GET'])
def adminBlockUser():
    try:
        if adminLoginSession() == 'admin':
            loginDAO = LoginDAO()
            loginVO = LoginVO()
            loginId = request.args.get('loginId')
            loginStatus = 'deactive'

            loginVO.loginId = loginId
            loginVO.loginStatus = loginStatus

            loginDAO.blockUser(loginVO)

            return adminViewUser()
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)