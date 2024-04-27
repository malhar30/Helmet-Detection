from flask import request, render_template, redirect, url_for
from project import app
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.DatasetVO import DatasetVO
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession

UPLOAD_FOLDER = 'project/static/adminResource/dataset/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/admin/loadDataset', methods=['GET'])
def adminLoadDataset():
    try:

        if adminLoginSession() == 'admin':
            return render_template('admin/addDataset.html')

        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/insertDataset', methods=['POST'])
def adminInsertDataset():
    try:

        if adminLoginSession() == 'admin':

            file = request.files['file']

            datasetFileName = secure_filename(file.filename)
            datasetFilePath = os.path.join(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(datasetFilePath, datasetFileName))
            datasetUploadDate = str(datetime.date(datetime.now()))
            datasetUploadTime = str(datetime.time(datetime.now()))

            datasetVO = DatasetVO()
            datasetDAO = DatasetDAO()

            datasetVO.datasetFileName = datasetFileName
            datasetVO.datasetFilePath = datasetFilePath.replace("project", "..")
            datasetVO.datasetUploadDate = datasetUploadDate
            datasetVO.datasetUploadTime = datasetUploadTime

            datasetDAO.insertDataset(datasetVO)

            return redirect(url_for('adminViewDataset'))

        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/viewDataset', methods=['GET'])
def adminViewDataset():
    try:

        if adminLoginSession() == 'admin':

            datasetDAO = DatasetDAO()
            datasetVOList = datasetDAO.viewDataset()

            return render_template('admin/viewDataset.html', datasetVOList=datasetVOList)

        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteDataset', methods=['GET'])
def adminDeleteDataset():
    try:

        if adminLoginSession() == 'admin':

            datasetVO = DatasetVO()
            datasetDAO = DatasetDAO()

            datasetId = request.args.get('datasetId')
            datasetFileName = request.args.get('datasetFileName')

            datasetVO.datasetId = datasetId

            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], datasetFileName))
            datasetDAO.deleteDataset(datasetVO)

            return redirect(url_for('adminViewDataset'))

        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)
