from flask import request, render_template, redirect, url_for
from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession






@app.route('/user/viewPackage')
def userViewPackage():
    try:
        if adminLoginSession() == "user":
            return render_template('user/viewPackage.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/viewPurchasePackage')
def userViewPurchasePackage():
    try:
        if adminLoginSession() == "user":
            return render_template('user/viewPurchasePackage.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/loadVideo')
def userLoadVideo():
    try:
        if adminLoginSession() == "user":
            return render_template('user/addVideo.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/viewVideo')
def userViewVideo():
    try:
        if adminLoginSession() == "user":
            return render_template('user/viewVideo.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)




        # Admin


@app.route('/admin/loadDashboard')
def adminloadDashboard():
    try:
        if adminLoginSession() == "admin":
            return render_template('admin/index.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewPurchasePackage')
def adminViewPurchasePackage():
    try:
        if adminLoginSession() == "admin":
            return render_template('admin/viewPurchasePackage.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewVideo')
def adminViewVideo():
    try:
        if adminLoginSession() == "admin":
            return render_template('admin/viewVideo.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewDetection')
def adminViewDetection():
    try:
        if adminLoginSession() == "admin":
            return render_template('admin/viewDetection.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


