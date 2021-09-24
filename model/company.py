import random


class Company:

    def __init__(self,
                 actualAddress=None,
                 address=None,
                 bukrs=None,
                 country=None,
                 fullName=None,
                 globalId=None,
                 hr_obj_id=None,
                 inn=None,
                 kpp=None,
                 legalAddress=None,
                 ogrn=None,
                 orgLegalForm=None,
                 parentCompanyRef=None,
                 region=None,
                 shortName=None,
                 town=None,
                 oid=None):

        random_name = self._pick_random_name()

        self.actualAddress = actualAddress
        self.address = address
        self.bukrs = bukrs
        self.country = country
        self.fullName = fullName or random_name[1]
        self.globalId = globalId
        self.hr_obj_id = hr_obj_id
        self.inn = inn or self._generate_inn()
        self.kpp = kpp or self._generate_kpp()
        self.legalAddress = legalAddress
        self.ogrn = ogrn or self._generate_ogrn()
        self.orgLegalForm = orgLegalForm or self._generate_org_legal_form()
        self.parentCompanyRef = parentCompanyRef
        self.region = region
        self.shortName = shortName or random_name[0]
        self.town = town or self._generate_town()
        self.oid = oid

    def _pick_random_name(self):
        name_dictionary = {'Австралия': 'Австралийский Союз', 'Австрия': 'Австрийская Республика',
                           'Азербайджан': 'Азербайджанская Республика',
         'Албания': 'Республика Албания', 'Алжир': 'Алжирская Народная Демократическая Республика',
                           'Ангола': 'Республика Ангола',
         'Андорра': 'Княжество Андорра', 'Аргентина': 'Аргентинская Республика', 'Армения': 'Республика Армения',
                           'Афганистан': 'Исламская Республика Афганистан',
         'Багамы': 'Содружество Багамских Островов', 'Бангладеш': 'Народная Республика Бангладеш',
                           'Бахрейн': 'Королевство Бахрейн',
         'Белоруссия': 'Республика Беларусь', 'Бельгия': 'Королевство Бельгия', 'Бенин': 'Республика Бенин',
                           'Болгария': 'Республика Болгария',
         'Боливия': 'Многонациональное Государство Боливия', 'Ботсвана': 'Республика Ботсвана',
                           'Бразилия': 'Федеративная Республика Бразилия',
         'Бруней': 'Государство Бруней-Даруссалам', 'Бурунди': 'Республика Бурунди', 'Бутан': 'Королевство Бутан',
         'Вануату': 'Республика Вануату', 'Великобритания': 'Соединённое Королевство Великобритании и Северной Ирландии',
         'Венесуэла': 'Боливарианская Республика Венесуэла',
                           'Восточный Тимор': 'Демократическая Республика Восточный Тимор',
         'Вьетнам': 'Социалистическая Республика Вьетнам', 'Габон': 'Габонская Республика', 'Гаити': 'Республика Гаити',
         'Гайана': 'Кооперативная Республика Гайана',  'Гамбия': 'Республика Гамбия', 'Гана': 'Республика Гана',
         'Гватемала': 'Республика Гватемала', 'Гвинея': 'Гвинейская Республика',
                           'Гвинея-Бисау': 'Республика Гвинея-Бисау',
         'Германия': 'Федеративная Республика Германия'}
        name_dictionary_list = list(name_dictionary.items())
        random_name = random.choice(name_dictionary_list)

        return random_name

    def _generate_org_legal_form(self):
        orgLegalForm = random.choice(['ПАО', 'НАО', 'ООО', 'ГУП'])
        return orgLegalForm

    def _generate_town(self):
        random_town = random.choice(['Москва', 'Санкт-Петербург', 'Смоленск', 'Самара', 'Саратов', 'Екатеринбург',
                                     'Ростов-на-Дону', 'Егорьевск', 'Калуга', 'Чехов'])

    def _generate_inn(self):
        inn = ''
        for i in range(10):
            inn += str(random.randint(0,9))
        return inn

    def _generate_ogrn(self):
        ogrn = ''
        for i in range(13):
            ogrn += str(random.randint(0,9))
        return ogrn

    def _generate_kpp(self):
        kpp = ''
        for i in range(9):
            kpp += str(random.randint(0,9))
        return kpp

    def return_company_data_as_json(self):
        json_data = {'actualAddress': self.actualAddress,
                     'address': self.address,
                     'bukrs': self.bukrs,
                     'country': self.country,
                     'fullName': self.fullName,
                     'globalId': self.globalId,
                     'hr_obj_id': self.hr_obj_id,
                     'inn': self.inn,
                     'kpp': self.kpp,
                     'legalAddress': self.legalAddress,
                     'ogrn': self.ogrn,
                     'orgLegalForm': self.orgLegalForm,
                     'parentCompanyRef': self.parentCompanyRef,
                     'region': self.region,
                     'shortName': self.shortName,
                     'town': self.town}
        return json_data



    def __repr__(self):
        return f'oid: {self.oid}, actualAddress: {self.actualAddress}, address: {self.address}, bukrs: {self.bukrs}, ' \
               f'country: {self.country}, fullName: {self.fullName}, globalId: {self.globalId}, ' \
               f'hr_obj_id: {self.hr_obj_id}, inn: {self.inn}, kpp: {self.kpp }, legalAddress: {self.legalAddress}, ' \
               f'ogrn: {self.ogrn}, orgLegalForm: {self.orgLegalForm}, parentCompanyRef: {self.parentCompanyRef}, ' \
               f'region: {self.region}, shortName: {self.shortName}, town: {self.town}'

    def __eq__(self, other):
        return (self.actualAddress, self.address, self.bukrs, self.country, self.fullName, self.globalId,
                self.hr_obj_id, self.inn, self.kpp, self.legalAddress, self.ogrn, self.orgLegalForm,
                self.parentCompanyRef, self.region, self.shortName, self.town) == (other.actualAddress,
                                                                                   other.address, other.bukrs,
                                                                                   other.country, other.fullName,
                                                                                   other.globalId, other.hr_obj_id,
                                                                                   other.inn, other.kpp,
                                                                                   other.legalAddress, other.ogrn,
                                                                                   other.orgLegalForm,
                                                                                   other.parentCompanyRef, other.region,
                                                                                   other.shortName, other.town)


