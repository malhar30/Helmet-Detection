from flask import render_template, request, redirect, url_for, session
from project import app
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO



@app.route('/')
def adminLoadLogin():
    try:
        session.clear()
        return render_template('admin/Login.html')

    except Exception as ex:
        print(ex)


@app.route('/admin/validateLogin', methods=['POST'])
def adminValidateLogin():
    try:
        loginUsername = request.form['loginUsername']
        loginPassword = request.form['loginPassword']

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginStatus = "active"

        loginVOList = loginDAO.validateLogin(loginVO)

        loginDictList = [i.as_dict() for i in loginVOList]

        lenLoginDictList = len(loginDictList)

        if lenLoginDictList == 0:

            msg = 'Username Or Password is Incorrect !'

            return render_template('admin/login.html', error=msg)

        else:
            for row1 in loginDictList:

                loginId = row1['loginId']
                loginUsername = row1['loginUsername']
                loginRole = row1['loginRole']

                session['session_loginId'] = loginId
                session['session_loginUsername'] = loginUsername
                session['session_loginRole'] = loginRole

                session.permanent = True

                if loginRole == 'admin':
                    return redirect(url_for('adminLoadDashboard'))

                else:
                    return redirect(url_for('userLoadDasboard'))

    except Exception as ex:
        print(ex)


@app.route('/admin/loadDashboard', methods=['GET'])
def adminLoadDashboard():
    try:

        if adminLoginSession() == 'admin':
            return render_template('admin/index.html')

        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/user/loadDashboard', methods=['GET'])
def userLoadDasboard():
    try:

        if adminLoginSession() == 'user':
            return render_template('user/index.html')

        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/loginSession')
def adminLoginSession():
    try:

        if 'session_loginId' and 'session_loginRole' in session:

            if session['session_loginRole'] == 'admin':
                return 'admin'

            else:
                return 'user'

        else:
            return False

    except Exception as ex:
        print(ex)


@app.route('/admin/logoutSession')
def adminLogoutSession():
    try:
        session.clear()
        return render_template('admin/login.html')

    except Exception as ex:
        print(ex)



