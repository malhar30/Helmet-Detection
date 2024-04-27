from project import app
from flask import render_template, request, session,redirect,url_for
from project.com.vo.ComplainVO import ComplainVO
from project.com.dao.ComplainDAO import ComplainDAO
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession


@app.route('/admin/viewComplain')
def adminViewComplain():
    try:
        if adminLoginSession() == "admin":

            complainDAO = ComplainDAO()
            complainVOList = complainDAO.adminViewComplain()

            return render_template('admin/viewComplain.html', complainVOList=complainVOList)

        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/loadComplainReply', methods=['GET'])
def adminloadComplainReply():
    try:
        if adminLoginSession() == "admin":

            complainDAO = ComplainDAO()
            complainVO = ComplainVO()

            complainId = request.args.get('complainId')

            complainVO.complainId = complainId

            complainVOList = complainDAO.adminEditComplainReply(complainVO)


            return render_template('admin/addComplainReply.html', complainVOList = complainVOList)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/insertComplainReply', methods=['POST'])
def adminInsertComplainReply():
    try:
        if adminLoginSession() == "admin":

            complainDAO = ComplainDAO()
            complainVO = ComplainVO()

            complainId = request.form['complainId']
            replySubject = request.form['replySubject']
            replyMessage = request.form['replyMessage']

            replyDate = str(datetime.date(datetime.now()))
            replyTime = str(datetime.time(datetime.now()))

            complainStatus = 'Replied'

            complainTo_LoginId = session['session_loginId']

            file = request.files['file']

            replyFileName = secure_filename(file.filename)

            replyFilePath = os.path.join(app.config['UPLOAD_FOLDER'])

            file.save(os.path.join(replyFilePath, replyFileName))

            complainVO.complainId = complainId
            complainVO.replySubject = replySubject
            complainVO.replyMessage = replyMessage
            complainVO.replyFileName = replyFileName
            complainVO.replyFilePath = replyFilePath.replace('project', '..')
            complainVO.replyDate = replyDate
            complainVO.replyTime = replyTime
            complainVO.complainTo_LoginId = complainTo_LoginId
            complainVO.complainStatus = complainStatus

            complainDAO.adminInsertComplainReply(complainVO)

            return redirect (url_for('adminViewComplain'))

        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteComplain', methods=['GET'])
def adminDeleteComplain():
    try:
        if adminLoginSession() == "admin":

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainId = request.args.get('complainId')
            complainFileName = request.args.get('complainFileName')

            complainVO.complainId = complainId
            complainVO.complainFileName = complainFileName

            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], complainFileName))
            complainDAO.adminDeleteComplain(complainVO)

            return redirect(url_for('adminViewComplain'))

    except Exception as ex:
        print(ex)


#user

@app.route('/user/loadComplain')
def userLoadComplain():
    try:
        if adminLoginSession() == "user":
            return render_template('user/addComplain.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/insertComplain', methods=['POST'])
def userInsertComplain():
    try:
        if adminLoginSession() == "user":

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainVO.complainSubject = request.form['complainSubject']
            complainVO.complainDescription = request.form['complainDescription']

            UPLOAD_FOLDER = 'project/static/adminResource/complainAttach/'

            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            file = request.files['file']
            print(file)

            complainFileName = secure_filename(file.filename)
            print(complainFileName)

            complainFilePath = os.path.join(app.config['UPLOAD_FOLDER'])
            print(complainFilePath)

            file.save(os.path.join(complainFilePath, complainFileName))

            complainDate = str(datetime.date(datetime.now()))
            complainTime = str(datetime.time(datetime.now()))
            complainFrom_LoginId = session['session_loginId']

            complainVO.complainFileName = complainFileName
            complainVO.complainFilePath = complainFilePath.replace("project", "..")
            complainVO.complainDate = complainDate
            complainVO.complainTime = complainTime
            complainVO.complainFrom_LoginId = complainFrom_LoginId
            complainVO.complainStatus = "pending"

            complainDAO.insertComplain(complainVO)

            return redirect(url_for('userViewComplain'))

        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/user/viewComplain', methods=['GET'])
def userViewComplain():
    try:
        if adminLoginSession() == "user":

            complainVO = ComplainVO()
            compainDAO = ComplainDAO()

            complainVO.complainFrom_LoginId = session['session_loginId']

            complainVOList = compainDAO.userViewComplain(complainVO)

            return render_template('user/viewComplain.html', complainVOList=complainVOList)


        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)



@app.route('/user/deleteComplain', methods=['GET'])
def userDeleteComplain():
    try:
        if adminLoginSession() == "user":

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainId = request.args.get('complainId')
            complainFileName = request.args.get('complainFileName')

            complainVO.complainId = complainId
            complainVO.complainFileName = complainFileName

            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], complainFileName))
            complainDAO.userDeleteComplain(complainVO)

            return redirect(url_for('userViewComplain'))

    except Exception as ex:
        print(ex)



@app.route('/user/viewComplainReply')
def userViewComplainReply():
    try:
        if adminLoginSession() == "user":

            complainDAO = ComplainDAO()
            complainVO = ComplainVO()

            complainId = request.args.get('complainId')

            complainVO.complainId = complainId

            complainVOList = complainDAO.userViewComplainReply(complainVO)


            return render_template('user/viewComplainReply.html', complainVOList = complainVOList)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


