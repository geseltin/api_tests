

class Employment:

    def __init__(self, empNumber=None,
                 category=None,
                 position=None,
                 org=None,
                 hrStatus=None,
                 workstart=None,
                 workend=None,
                 gracePeriod=None,
                 vacationType=None,
                 vacstart=None,
                 vacend=None,
                 workplacePresence=None,
                 lineManager=None,
                 funcManager=None,
                 substitute=None,
                 hrSubstitute=None,
                 hrGroup=None,
                 hrCategory=None,
                 employeeType=None,
                 integralRiskLevel=None,
                 costPlace=None,
                 vipUser=None,
                 adLogin=None,
                 sapLogin=None,
                 email=None,
                 telephoneNumber=None,
                 officeMobilePhoneNumber=None,
                 interNumber=None,
                 locality=None,
                 locationCode=None,
                 workplaceNumber=None,
                 floorNumber=None,
                 roomNumber=None,
                 candWorkPlace1=None,
                 candWorkPlace2=None,
                 candPlanStartDate=None,
                 candContactEmployee=None,
                 candPC=None,
                 candPhone=None,
                 candOwrp=None,
                 candRnst=None,
                 main=None,
                 isCandidate=None,
                 empType='штатный',
                 city='',
                 defaultEmp=False,
                 manuallyCreated=None,
                 office='',
                 status='',
                 id=None):

        self.empNumber = empNumber
        self.category = category
        self.position = position
        self.org = org
        self.hrStatus = hrStatus
        self.workstart = workstart
        self.workend = workend
        self.gracePeriod = gracePeriod
        self.vacationType = vacationType
        self.vacstart = vacstart
        self.vacend = vacend
        self.workplacePresence = workplacePresence
        self.lineManager = lineManager
        self.funcManager = funcManager
        self.substitute = substitute
        self.hrSubstitute = hrSubstitute
        self.hrGroup = hrGroup
        self.hrCategory = hrCategory
        self.employeeType = employeeType
        self.integralRiskLevel = integralRiskLevel
        self.costPlace = costPlace
        self.vipUser = vipUser
        self.adLogin = adLogin
        self.sapLogin = sapLogin
        self.email = email
        self.telephoneNumber = telephoneNumber
        self.officeMobilePhoneNumber = officeMobilePhoneNumber
        self.interNumber = interNumber
        self.locality = locality
        self.locationCode = locationCode
        self.workplaceNumber = workplaceNumber
        self.floorNumber = floorNumber
        self.roomNumber = roomNumber
        self.candWorkPlace1 = candWorkPlace1
        self.candWorkPlace2 = candWorkPlace2
        self.candPlanStartDate = candPlanStartDate
        self.candContactEmployee = candContactEmployee
        self.candPC = candPC
        self.candPhone = candPhone
        self.candOwrp = candOwrp
        self.candRnst = candRnst
        self.main = main
        self.isCandidate = isCandidate
        self.empType = empType
        self.city = city
        self.defaultEmp = defaultEmp
        self.manuallyCreated = manuallyCreated
        self.office = office
        self.status = status
        self.id=id

    def __repr__(self):

        return f'Employment --- empNumber:{self.empNumber}, ' \
               f'category: {self.category}, ' \
               f'position: {self.position}, ' \
               f'org: {self.org}, ' \
               f'hrStatus: {self.hrStatus}, ' \
               f'workstart: {self.workstart}, ' \
               f'workend: {self.workend}, ' \
               f'gracePeriod: {self.gracePeriod}, ' \
               f'vacationType: {self.vacationType}, ' \
               f'vacstart: {self.vacstart}, ' \
               f'vacend: {self.vacend}, ' \
               f'workPlacePresence: {self.workplacePresence}, ' \
               f'lineManager: {self.lineManager}, ' \
               f'funcManager: {self.funcManager}, ' \
               f'substitute: {self.substitute}, ' \
               f'hrSubstitute: {self.hrSubstitute}, ' \
               f'hrGroup: {self.hrGroup}, ' \
               f'hrCategory: {self.hrCategory}, ' \
               f'employeeType: {self.employeeType}, ' \
               f'integralRiskLevel: {self.integralRiskLevel}, ' \
               f'costPlace: {self.costPlace}, ' \
               f'vipUser: {self.vipUser}, ' \
               f'adLogin: {self.adLogin}, ' \
               f'sapLogin: {self.sapLogin}, ' \
               f'email: {self.email}, ' \
               f'telephoneNumber: {self.telephoneNumber}, ' \
               f'officeMobilePhoneNumber: {self.officeMobilePhoneNumber}, ' \
               f'interNumber: {self.interNumber}, ' \
               f'locality: {self.locality}, ' \
               f'locationCode: {self.locationCode}, ' \
               f'workplaceNumber: {self.workplaceNumber}, ' \
               f'floorNumber: {self.floorNumber}, ' \
               f'roomNumber: {self.roomNumber}, ' \
               f'candWorkPlace1: {self.candWorkPlace1}, ' \
               f'candWorkPlace2: {self.candWorkPlace2}, ' \
               f'candPlanStartDate: {self.candPlanStartDate}, ' \
               f'candContactEmployee: {self.candContactEmployee}, ' \
               f'candPC: {self.candPC}, ' \
               f'candPhone: {self.candPhone}, ' \
               f'candOwrp: {self.candOwrp}, ' \
               f'candRnst: {self.candRnst}, ' \
               f'main: {self.main}, ' \
               f'isCandidate: {self.isCandidate},' \
               f'empType: {self.empType},' \
               f'city: {self.city},' \
               f'defaultEmp: {self.defaultEmp},' \
               f'manuallyCreated: {self.manuallyCreated},' \
               f'office: {self.office},' \
               f'status: {self.status},' \
               f'id: {self.id}'

    def return_employment_data_as_json(self):

        employment_data_json = {'empNumber':self.empNumber,
                                "category": self.category,
                                "position": self.position,
                                "org": self.org,
                                "hrStatus": self.hrStatus,
                                "workstart": self.workstart,
                                "workend": self.workend,
                                "gracePeriod": self.gracePeriod,
                                "vacationType": self.vacationType,
                                "vacstart": self.vacstart,
                                "vacend": self.vacend,
                                "workPlacePresence": self.workplacePresence,
                                "lineManager": self.lineManager,
                                "funcManager": self.funcManager['id'],
                                "substitute": self.substitute,
                                "hrSubstitute": self.hrSubstitute,
                                "hrGroup": self.hrGroup,
                                "hrCategory": self.hrCategory,
                                "employeeType": self.employeeType,
                                "integralRiskLevel": self.integralRiskLevel,
                                "costPlace": self.costPlace,
                                "vipUser": self.vipUser,
                                "adLogin": self.adLogin,
                                "sapLogin": self.sapLogin,
                                "email": self.email,
                                "telephoneNumber": self.telephoneNumber,
                                "officeMobilePhoneNumber": self.officeMobilePhoneNumber,
                                "interNumber": self.interNumber,
                                "locality": self.locality,
                                "locationCode": self.locationCode,
                                "workplaceNumber": self.workplaceNumber,
                                "floorNumber": self.floorNumber,
                                "roomNumber": self.roomNumber,
                                "candWorkPlace1": self.candWorkPlace1,
                                "candWorkPlace2": self.candWorkPlace2,
                                "candPlanStartDate": self.candPlanStartDate,
                                "candContactEmployee": self.candContactEmployee,
                                "candPC": self.candPC,
                                "candPhone": self.candPhone,
                                "candOwrp": self.candOwrp,
                                "candRnst": self.candRnst,
                                "main": self.main,
                                "isCandidate": self.isCandidate,
                                "empType": self.empType,
                                "city": self.city,
                                "defaultEmp": self.defaultEmp,
                                "manuallyCreated": self.manuallyCreated,
                                "office": self.office,
                                "status": self.status,
                                "id": self.id}
        return employment_data_json


