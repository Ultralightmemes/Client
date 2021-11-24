import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
import matplotlib.pyplot
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from Client import Client
import json
from User import User


class Enterance(QDialog):
    def __init__(self):
        super(Enterance, self).__init__()
        loadUi('enterance.ui', self)
        self.admin.clicked.connect(self.admin_login)
        self.user.clicked.connect(self.user_login)

    def user_login(self):
        log = Login()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def admin_login(self):
        admin_log = AdminLog()
        widget.addWidget(admin_log)
        widget.setCurrentIndex(widget.currentIndex()+1)


class AdminLog(QDialog):
    def __init__(self):
        super(AdminLog, self).__init__()
        loadUi('admin_login.ui', self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_admin)
        self.exit_button.clicked.connect(self.exit_to_entr)

    def login_admin(self):
        message = {}
        message["type"] = "admin"
        message["login"] = self.log_in.text()
        message["password"] = self.password.text()
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        print(parsed_data)
        if parsed_data["access"] == "yes":
            print('Yes')
            adm = AdminMenu()
            widget.addWidget(adm)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            QMessageBox.information(None, 'Ошибка!', "Проверьте правильность введённых данных")

    def exit_to_entr(self):
        entrance = Enterance()
        widget.addWidget(entrance)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('login.ui', self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.login_button.clicked.connect(self.login_user)
        self.exit_button.clicked.connect(self.exit_to_entr)

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def login_user(self):
        message = {}
        message["type"] = "user"
        message["login"] = self.log_in.text()
        message["password"] = self.password.text()
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        print(parsed_data)
        if parsed_data["access"] == "yes":
            user.login = self.log_in.text()
            user.password = self.password.text()
            if parsed_data["employee"] == "yes":
                user.is_employee = True
                user.employee_id = parsed_data["id"]
            else:
                user.is_employee = False
            print("Yes")
            menu = UserMenu()
            widget.addWidget(menu)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            QMessageBox.information(None, 'Ошибка!', "Проверьте правильность введённых данных")

    def exit_to_entr(self):
        entrance = Enterance()
        widget.addWidget(entrance)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi('signup.ui', self)
        self.signup_button.clicked.connect(self.createaccfunction)
        self.exit_button.clicked.connect(self.goto_menu)

    def createaccfunction(self):
        message = {}
        message["type"] = "addUser"
        message["login"] = self.log_in.text()
        message["password"] = self.password.text()
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        print(parsed_data)
        if parsed_data["access"] == "yes":
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
            QMessageBox.information(None, 'Уведомление', "Аккаунт успешно создан")
        else:
            QMessageBox.information(None, 'Ошибка!', "Пользователь с таким менем уже существует")

    def goto_menu(self):
        entrance = Enterance()
        widget.addWidget(entrance)
        widget.setCurrentIndex(widget.currentIndex()+1)


class UserMenu(QDialog):
    def __init__(self):
        super(UserMenu, self).__init__()
        loadUi("user_menu.ui", self)
        self.quality_menu.clicked.connect(self.goto_quality)
        self.profile.clicked.connect(self.goto_profile)
        self.exit.clicked.connect(self.goto_enterance)

    def goto_quality(self):
        quality = Quality()
        widget.addWidget(quality)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_profile(self):
        profile = Profile()
        widget.addWidget(profile)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_enterance(self):
        entrance = Enterance()
        widget.addWidget(entrance)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AdminMenu(QDialog):
    def __init__(self):
        super(AdminMenu, self).__init__()
        loadUi("admin_menu.ui", self)
        self.clients_menu.clicked.connect(self.goto_clients)
        self.accounts.clicked.connect(self.goto_accounts)
        self.products_menu.clicked.connect(self.goto_products)
        self.exit.clicked.connect(self.goto_enterance)

    def goto_clients(self):
        clients = ClientsMenu()
        widget.addWidget(clients)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_accounts(self):
        account = AccountMenu()
        widget.addWidget(account)
        widget.setFixedWidth(600)
        widget.setFixedHeight(700)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_products(self):
        products = ProductsMenu()
        widget.addWidget(products)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_enterance(self):
            entrance = Enterance()
            widget.addWidget(entrance)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class Profile(QDialog):
    def __init__(self):
        super(Profile, self).__init__()
        loadUi("profile.ui", self)
        self.change_password.clicked.connect(self.goto_change)
        self.delete_account.clicked.connect(self.goto_delete)
        self.back.clicked.connect(self.goto_menu)

    def goto_change(self):
        change = Change()
        widget.addWidget(change)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_delete(self):
        delete = Delete()
        widget.addWidget(delete)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu(self):
        menu = UserMenu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Quality(QDialog):
    def __init__(self):
        super(Quality, self).__init__()
        loadUi("user_work.ui", self)
        self.add_mark.clicked.connect(self.goto_add)
        self.show_marks.clicked.connect(self.goto_show)
        self.show_chart.clicked.connect(self.goto_chart)
        self.back.clicked.connect(self.goto_menu)

    def goto_add(self):
        if user.is_employee:
            add_mark = AddMark()
            widget.addWidget(add_mark)
            widget.setFixedHeight(600)
            widget.setFixedWidth(700)
            widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_show(self):
        show_marks = ShowMarks()
        widget.addWidget(show_marks)
        widget.setFixedHeight(600)
        widget.setFixedWidth(700)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_chart(self):
        chart = Chart()
        widget.addWidget(chart)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu(self):
        menu = UserMenu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Chart(QDialog):
    def __init__(self):
        super(Chart, self).__init__()
        loadUi("chart.ui", self)
        self.mark_chart.clicked.connect(self.employee)
        self.product_chart.clicked.connect(self.product)
        self.client_chart.clicked.connect(self.client)
        self.back.clicked.connect(self.goto_menu)

    def employee(self):
        message = {}
        message["type"] = "EmployeeMarks"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        print(parsed_data)
        num_list = []
        for a in parsed_data:
            num_list.append(int(parsed_data[a]))
        print(num_list)
        ppl = matplotlib.pyplot
        ppl.title("Оценки работников")
        ppl.bar(parsed_data.keys(), num_list)
        ppl.legend()
        ppl.show()

    def product(self):
        message = {}
        message["type"] = "ProductsHaveMarks"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        print(parsed_data)
        nums = []
        for a in parsed_data:
            nums.append(int(a))
        for a in parsed_data:
            nums.append((parsed_data[a]))
        ppl = matplotlib.pyplot
        labels = ["С оценкой", "Без оценки"]
        fig1, ax1 = ppl.subplots()
        ppl.title("Процент продуктов с оценками")
        ax1.pie(nums, labels=labels)
        ppl.legend()
        ppl.show()

    def client(self):
        message = {}
        message["type"] = "ClientHaveProducts"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        print(parsed_data)
        num_list = []
        for a in parsed_data:
            num_list.append(int(parsed_data[a]))
        print(num_list)
        ppl = matplotlib.pyplot
        ppl.title("Продукты клиентов")
        ppl.bar(parsed_data.keys(), num_list)
        ppl.legend()
        ppl.show()

    def goto_menu(self):
        quality = Quality()
        widget.addWidget(quality)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Change(QDialog):
    def __init__(self):
        super(Change, self).__init__()
        loadUi("change_password.ui", self)
        self.login_button.clicked.connect(self.change_password)
        self.exit_button.clicked.connect(self.goto_menu)

    def change_password(self):
        if self.password.text() == user.password:
            message = {}
            message["type"] = "changeUserPassword"
            message["login"] = user.login
            message["password"] = self.new_password.text()
            data = json.dumps(message)
            client.sending(data)
        else:
            QMessageBox.information(None, 'Ошибка!', "Проверьте правильность введёных данных!")

        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            user.password = self.new_password.text()
            profile = Profile()
            widget.addWidget(profile)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            QMessageBox.information(None, 'Ошибка!', "Проверьте правильность введёных данных!")

    def goto_menu(self):
        user_menu = UserMenu()
        widget.addWidget(user_menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Delete(QDialog):
    def __init__(self):
        super(Delete, self).__init__()
        loadUi("delete_account.ui", self)
        self.delete_user.clicked.connect(self.delete_account)
        self.exit_button.clicked.connect(self.goto_menu)

    def delete_account(self):
        if self.password.text() == self.dublicate_password.text() == user.password:
            message = {}
            message["type"] = "deleteUser"
            message["login"] = user.login
            data = json.dumps(message)
            client.sending(data)
        else:
            QMessageBox.information(None, 'Ошибка!', "Проверьте правильность введёных данных!")

        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            user.password = None
            user.login = None
            entrance = Enterance()
            widget.addWidget(entrance)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")

    def goto_menu(self):
        user_menu = UserMenu()
        widget.addWidget(user_menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ClientsMenu(QDialog):
    def __init__(self):
        super(ClientsMenu, self).__init__()
        loadUi("clients_menu.ui", self)
        self.add_client.clicked.connect(self.goto_add)
        self.manage_clients.clicked.connect(self.goto_manage)
        self.exit.clicked.connect(self.goto_menu)

    def goto_add(self):
        add_client = AddClient()
        widget.addWidget(add_client)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_manage(self):
        manage_clients = ManageClients()
        widget.addWidget(manage_clients)
        widget.setFixedWidth(700)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_menu(self):
        admin_menu = AdminMenu()
        widget.addWidget(admin_menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ProductsMenu(QDialog):
    def __init__(self):
        super(ProductsMenu, self).__init__()
        loadUi("products_menu.ui", self)
        self.add_product.clicked.connect(self.goto_add)
        self.manage_products.clicked.connect(self.goto_manage)
        self.exit.clicked.connect(self.goto_menu)

    def goto_add(self):
        add_product = AddProduct()
        widget.addWidget(add_product)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_manage(self):
        manage_products = ManageProducts()
        widget.addWidget(manage_products)
        widget.setFixedWidth(700)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goto_menu(self):
        admin_menu = AdminMenu()
        widget.addWidget(admin_menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AddClient(QDialog):
    def __init__(self):
        super(AddClient, self).__init__()
        loadUi("add_client.ui", self)
        self.add_button.clicked.connect(self.add_client)
        self.exit.clicked.connect(self.goto_menu)

    def add_client(self):
        message = {}
        message["type"] = "addClient"
        message["id"] = self.id.text()
        message["name"] = self.name.text()
        message["director"] = self.director_2.text()
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            self.message_label.setText("Запись добавлена!")
        else:
            self.message_label.setText("Повторите попытку")
            QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")

    def goto_menu(self):
        clients_menu = ClientsMenu()
        widget.addWidget(clients_menu)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ManageClients(QDialog):
    def __init__(self):
        super(ManageClients, self).__init__()
        loadUi("show_clients.ui", self)
        self.client_table.setColumnWidth(0, 90)
        self.client_table.setColumnWidth(1, 269)
        self.client_table.setColumnWidth(2, 280)
        # self.client_table.cellClicked.connect(self.OnClicked)
        self.delete_button.clicked.connect(self.delete_client)
        self.edit_button.clicked.connect(self.edit_client)
        self.exit.clicked.connect(self.goto_menu)
        self.load_data()

    def load_data(self):
        message = {}
        message["type"] = "showClients"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            self.client_table.setRowCount(int(parsed_data["count"]))
            print(parsed_data)
            for number in range(0, int(parsed_data["count"])):
                self.client_table.setItem(number, 0, QtWidgets.QTableWidgetItem(parsed_data["id" + str(number)]))
                self.client_table.setItem(number, 1, QtWidgets.QTableWidgetItem(parsed_data["name" + str(number)]))
                self.client_table.setItem(number, 2, QtWidgets.QTableWidgetItem(parsed_data["director" + str(number)]))

    def delete_client(self):
        message = {}
        message["type"] = "deleteClient"
        row = self.client_table.currentItem().row()
        message["id"] = self.client_table.item(row, 0).text()
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            self.client_table.removeRow(row)
        else:
            QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")

    def edit_client(self):
        self.edit_window = EditClient(self.client_table.item(self.client_table.currentItem().row(), 0).text())
        self.edit_window.show()

    def goto_menu(self):
        clients_menu = ClientsMenu()
        widget.addWidget(clients_menu)
        widget.setFixedWidth(600)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # def OnClicked(self):
    #     self.client_table.clearSelection()
    #     self.client_table.setSelectionMode(QAbstractItemView.MultiSelection)
    #     row_num = self.client_table.currentRow()
    #     self.client_table.selectRow(row_num)
    #     self.client_table.setCurrentIndex(row_num)


class EditClient(QDialog):
    def __init__(self, client_id):
        super(EditClient, self).__init__()
        loadUi("edit_client.ui", self)
        self.client_id = client_id
        self.edit_button.clicked.connect(self.edit_client)
        self.cancel.clicked.connect(self.goto_close)

    def edit_client(self):
        message = {}
        message["type"] = "editClient"
        message["id"] = self.client_id
        message["name"] = self.name.text()
        message["director"] = self.director_2.text()
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            self.close()
            manage_clients = ManageClients()
            widget.addWidget(manage_clients)
            widget.setFixedWidth(700)
            widget.setFixedHeight(600)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            self.message_label.setText("Повторите попытку")
            QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")

    def goto_close(self):
        self.close()


class AddProduct(QDialog):
    company_item = {}
    def __init__(self):
        super(AddProduct, self).__init__()
        loadUi("add_product.ui", self)
        self.add_button.clicked.connect(self.goto_add)
        self.exit.clicked.connect(self.goto_menu)
        self.load_data()

    def goto_add(self):
        message = {}
        message["type"] = "addProduct"
        message["id"] = self.id.text()
        message["name"] = self.name.text()
        message["company"] = self.companyBox.currentText()
        print(self.company_item[self.companyBox.currentText()])
        message["companyId"] = str(self.company_item[self.companyBox.currentText()])
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            self.message_label.setText("Запись добавлена!")
        else:
            self.message_label.setText("Повторите попытку")
            QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")

    def goto_menu(self):
        products_menu = ProductsMenu()
        widget.addWidget(products_menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def load_data(self):
        message = {}
        message["type"] = "getClientsNames"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        print(parsed_data)
        if parsed_data["access"] == "yes":
            for number in range(0, int(parsed_data["count"])):
                self.company_item[parsed_data["name" + str(number)]] = parsed_data["id" + str(number)]
                print(parsed_data["name" + str(number)])
                self.companyBox.addItem(parsed_data["name" + str(number)])

class ManageProducts(QDialog):
    def __init__(self):
        super(ManageProducts, self).__init__()
        loadUi("show_products.ui", self)
        self.product_table.setColumnWidth(0, 50)
        self.product_table.setColumnWidth(1, 209)
        self.product_table.setColumnWidth(2, 200)
        self.product_table.setColumnWidth(3, 180)
        # self.product_table.cellClicked.connect(self.OnClicked)
        self.delete_button.clicked.connect(self.delete_product)
        self.edit_button.clicked.connect(self.edit_product)
        self.exit.clicked.connect(self.goto_menu)
        self.load_data()

    def load_data(self):
        message = {}
        message["type"] = "showProducts"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        secondary_message = {}
        secondary_message["type"] = "getClientProduct"
        secondary_data = json.dumps(secondary_message)
        client.sending(secondary_data)
        secondary_text = client.receive()
        parsed_secondary = json.loads(secondary_text)
        if parsed_data["access"] == "yes":
            self.product_table.setRowCount(int(parsed_data["count"]))
            print(parsed_data)
            print(parsed_secondary)
            for number in range(0, int(parsed_data["count"])):
                self.product_table.setItem(number, 0, QtWidgets.QTableWidgetItem(parsed_data["id" + str(number)]))
                self.product_table.setItem(number, 1, QtWidgets.QTableWidgetItem(parsed_data["name" + str(number)]))
                self.product_table.setItem(number, 2, QtWidgets.QTableWidgetItem(parsed_data["mark" + str(number)]))
                self.product_table.setItem(number, 3, QtWidgets.QTableWidgetItem(parsed_secondary[parsed_data["id" + str(number)]]))

    def delete_product(self):
        message = {}
        message["type"] = "deleteProduct"
        row = self.product_table.currentItem().row()
        message["id"] = self.product_table.item(row, 0).text()
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            self.product_table.removeRow(row)
        else:
            QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")

    def edit_product(self):
        self.edit_window = EditProduct(self.product_table.item(self.product_table.currentItem().row(), 0).text())
        self.edit_window.show()

    def goto_menu(self):
        products_menu = ProductsMenu()
        widget.addWidget(products_menu)
        widget.setFixedWidth(600)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # def OnClicked(self):
    #     self.client_table.clearSelection()
    #     self.client_table.setSelectionMode(QAbstractItemView.MultiSelection)
    #     row_num = self.client_table.currentRow()
    #     self.client_table.selectRow(row_num)
    #     self.client_table.setCurrentIndex(row_num)


class EditProduct(QDialog):
    company_item = {}
    def __init__(self, product_id):
        super(EditProduct, self).__init__()
        loadUi("edit_product.ui", self)
        self.product_id = product_id
        self.edit_button.clicked.connect(self.edit_client)
        self.cancel.clicked.connect(self.goto_close)
        self.load_data()

    def edit_client(self):
        message = {}
        message["type"] = "editProduct"
        message["id"] = self.product_id
        message["name"] = self.name.text()
        message["company"] = self.clientBox.currentText()
        message["companyId"] = str(self.company_item[self.clientBox.currentText()])
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            self.close()
            manage_products = ManageProducts()
            widget.addWidget(manage_products)
            widget.setFixedWidth(700)
            widget.setFixedHeight(600)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            self.message_label.setText("Повторите попытку")
            QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")

    def goto_close(self):
        self.close()

    def load_data(self):
        message = {}
        message["type"] = "getClientsNames"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        print(parsed_data)
        if parsed_data["access"] == "yes":
            for number in range(0, int(parsed_data["count"])):
                self.company_item[parsed_data["name" + str(number)]] = parsed_data["id" + str(number)]
                print(parsed_data["name" + str(number)])
                self.clientBox.addItem(parsed_data["name" + str(number)])


class AccountMenu(QDialog):
    def __init__(self):
        super(AccountMenu, self).__init__()
        loadUi("show_accounts.ui", self)
        self.exit.clicked.connect(self.goto_menu)
        self.change_button.clicked.connect(self.change_type)
        self.load_data()

    def goto_menu(self):
        admin_menu = AdminMenu()
        widget.addWidget(admin_menu)
        widget.setFixedWidth(600)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def load_data(self):
        message = {}
        message["type"] = "getEmployeesLogin"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        employees_data = json.loads(text)
        message["type"] = "getUsers"
        data_user = json.dumps(message)
        client.sending(data_user)
        text = client.receive()
        users_data = json.loads(text)
        if employees_data["access"] == "yes" and users_data["access"] == "yes":
            rows = int(users_data["count"])
            self.acc_table.setRowCount(rows)
            print(employees_data)
            print(users_data)
            for number in range(0, rows):
                self.acc_table.setItem(number, 0, QtWidgets.QTableWidgetItem(users_data["login" + str(number)]))
                if users_data["login" + str(number)] in employees_data:
                    self.acc_table.setItem(number, 1, QtWidgets.QTableWidgetItem("Работник"))
                    self.acc_table.setItem(number, 2, QtWidgets.QTableWidgetItem(employees_data["name" + employees_data[users_data["login" + str(number)]]]))
                    self.acc_table.setItem(number, 3, QtWidgets.QTableWidgetItem(employees_data["education" + employees_data[users_data["login" + str(number)]]]))
                    self.acc_table.setItem(number, 4, QtWidgets.QTableWidgetItem(employees_data["id" + employees_data[users_data["login" + str(number)]]]))
                else:
                    self.acc_table.setItem(number, 1, QtWidgets.QTableWidgetItem("Пользователь"))

    def change_type(self):
        row = self.acc_table.currentItem().row()
        if self.acc_table.item(row, 1).text() == "Работник":
            message = {}
            message["type"] = "deleteEmployee"
            message["login"] = self.acc_table.item(row, 0).text()
            data = json.dumps(message)
            client.sending(data)
            text = client.receive()
            parsed_data = json.loads(text)
            if parsed_data["access"] == "yes":
                account_menu = AccountMenu()
                widget.addWidget(account_menu)
                widget.setFixedWidth(700)
                widget.setFixedHeight(600)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")
        else:
            self.add_employee = AddEmployee(self.acc_table.item(row, 0).text())
            self.add_employee.show()


class AddEmployee(QDialog):
    def __init__(self, login):
        super(AddEmployee, self).__init__()
        self.login = login
        loadUi("add_employee.ui", self)
        self.exit.clicked.connect(self.goto_menu)
        self.add_button.clicked.connect(self.goto_add)

    def goto_menu(self):
        self.close()

    def goto_add(self):
        message = {}
        message["type"] = "addEmployee"
        message["login"] = self.login
        message["id"] = self.id.text()
        message["education"] = self.education.text()
        message["name"] = self.name.text()
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            self.close()
            account_menu = AccountMenu()
            widget.addWidget(account_menu)
            widget.setFixedWidth(700)
            widget.setFixedHeight(600)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            self.message_label.setText("Повторите попытку")
            QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")


class AddMark(QDialog):
    def __init__(self):
        super(AddMark, self).__init__()
        loadUi("products_empty.ui", self)
        self.product_table.setColumnWidth(0, 150)
        self.product_table.setColumnWidth(1, 250)
        self.product_table.setColumnWidth(2, 250)
        self.load_table()
        self.exit.clicked.connect(self.goto_menu)
        self.give_mark.clicked.connect(self.goto_mark)

    def goto_mark(self):
        row = self.product_table.currentItem().row()
        message = {}
        message["type"] = "addMark"
        message["id"] = self.product_table.item(row, 0).text()
        message["mark"] = self.markBox.currentText()
        message["employee_id"] = user.employee_id
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        if parsed_data["access"] == "yes":
            add_mark = AddMark()
            widget.addWidget(add_mark)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            QMessageBox.information(None, 'Ошибка!', "Произошла ошибка!")

    def load_table(self):
        message = {}
        message["type"] = "showProducts"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        secondary_message = {}
        secondary_message["type"] = "getClientProduct"
        secondary_data = json.dumps(secondary_message)
        client.sending(secondary_data)
        secondary_text = client.receive()
        parsed_secondary = json.loads(secondary_text)
        if parsed_data["access"] == "yes":
            self.product_table.setRowCount(int(parsed_data["count"]))
            print(parsed_data)
            print(parsed_secondary)
            mark_empty = 0
            for number in range(0, int(parsed_data["count"])):
                if parsed_data["mark" + str(number)] == "NULL":
                    parsed_data["table" + str(number)] = "true"
                    mark_empty += 1
                else:
                    parsed_data["table" + str(number)] = "false"
            self.product_table.setRowCount(mark_empty)
            table_count = 0
            for number in range(0, int(parsed_data["count"])):
                if parsed_data["table" + str(number)] == "true":
                    print(parsed_data["table" + str(number)])
                    self.product_table.setItem(table_count, 0, QtWidgets.QTableWidgetItem(parsed_data["id" + str(number)]))
                    self.product_table.setItem(table_count, 1, QtWidgets.QTableWidgetItem(parsed_data["name" + str(number)]))
                    self.product_table.setItem(table_count, 2, QtWidgets.QTableWidgetItem(
                        parsed_secondary[parsed_data["id" + str(number)]]))
                    table_count += 1
        for number in range(1, 11):
            self.markBox.addItem(str(number))

    def goto_menu(self):
        quality = Quality()
        widget.addWidget(quality)
        widget.setFixedWidth(600)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(widget.currentIndex()+1)


class ShowMarks(QDialog):
    def __init__(self):
        super(ShowMarks, self).__init__()
        loadUi("all_products.ui", self)
        self.load_table()
        self.exit.clicked.connect(self.goto_menu)
        self.edit_mark.clicked.connect(self.goto_edit)

    def load_table(self):
        message = {}
        message["type"] = "showProducts"
        data = json.dumps(message)
        client.sending(data)
        text = client.receive()
        parsed_data = json.loads(text)
        secondary_message = {}
        secondary_message["type"] = "getClientProduct"
        secondary_data = json.dumps(secondary_message)
        client.sending(secondary_data)
        secondary_text = client.receive()
        parsed_secondary = json.loads(secondary_text)
        if parsed_data["access"] == "yes":
            self.product_table.setRowCount(int(parsed_data["count"]))
            print(parsed_data)
            print(parsed_secondary)
            for number in range(0, int(parsed_data["count"])):
                self.product_table.setItem(number, 0, QtWidgets.QTableWidgetItem(parsed_data["id" + str(number)]))
                self.product_table.setItem(number, 1, QtWidgets.QTableWidgetItem(parsed_data["name" + str(number)]))
                self.product_table.setItem(number, 2, QtWidgets.QTableWidgetItem(
                        parsed_secondary[parsed_data["id" + str(number)]]))
                self.product_table.setItem(number, 3, QtWidgets.QTableWidgetItem(parsed_data["mark" + str(number)]))
        for number in range(1, 11):
            self.markBox.addItem(str(number))

    def goto_edit(self):
        row = self.product_table.currentItem().row()
        message = {}
        if self.product_table.item(row, 3).text() == "NULL":
            QMessageBox.information(None, 'Ошибка!', "Вы не можете редактировать несуществующую оценку")
        else:
            message["type"] = "editMark"
            message["id"] = self.product_table.item(row, 0).text()
            message["employee_id"] = user.employee_id
            message["mark"] = self.markBox.currentText()
            data = json.dumps(message)
            client.sending(data)
            text = client.receive()
            parsed_data = json.loads(text)
            if parsed_data["access"] == "yes":
                show_marks = ShowMarks()
                widget.addWidget(show_marks)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                QMessageBox.information(None, 'Ошибка!',
                                        "Вы не можете редактировать оценку поставленную другим работником")


    def goto_menu(self):
        quality = Quality()
        widget.addWidget(quality)
        widget.setFixedWidth(600)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QApplication(sys.argv)
mainwindow = Enterance()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(600)
widget.setFixedHeight(500)
widget.setWindowTitle('Курсовая работа')
# widget.setWindowIcon(QIcon('kurs_project.ico'))
client = Client()
user = User()


# login = {}
# login["login"] = "login"
# login["password"] = "password"
# print(login)
# data = json.dumps(login)
# client.sending(data)
# print(type(data))

# text = client.receive()
# parsed_data = json.loads(text)
# print(text)

widget.show()
app.exec_()
