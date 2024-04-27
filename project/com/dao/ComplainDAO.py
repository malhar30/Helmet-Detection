from  project import db
from project.com.vo.ComplainVO import ComplainVO
from project.com.vo.LoginVO import LoginVO

class ComplainDAO():

    def adminEditComplainReply(self, complainVO):
        complainList = ComplainVO.query.filter_by(complainId=complainVO.complainId).all()

        return complainList


    def adminInsertComplainReply(self, complainVO):
        db.session.merge(complainVO)
        db.session.commit()


    def adminViewComplain(self):
        complainList = db.session.query(ComplainVO, LoginVO).join(LoginVO, ComplainVO.complainFrom_LoginId == LoginVO.loginId).all()

        return complainList


    def adminDeleteComplain(self, complainVO):
        complainId = ComplainVO.query.get(complainVO.complainId)

        db.session.delete(complainId)

        db.session.commit()



    def userDeleteComplain(self, complainVO):
        complainId = ComplainVO.query.get(complainVO.complainId)

        db.session.delete(complainId)

        db.session.commit()



    def insertComplain(self, complainVO):
        db.session.add(complainVO)
        db.session.commit()
        db.session.close()


    def userViewComplain(self, complainVO):
        complainList = ComplainVO.query.filter_by(complainFrom_LoginId=complainVO.complainFrom_LoginId).all()
        return complainList


    def userViewComplainReply(self,complainVO):
        complainList = ComplainVO.query.filter_by(complainId=complainVO.complainId).all()
        return complainList
