import sys
import pyodbc
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from mainmenu import MainMenuScreen


class RegisterScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def openmainwindow(self,name):
        self.window = MainMenuScreen(name)
        self.window.show()

    def init_ui(self):
        self.setWindowTitle('Register Screen')
        self.setGeometry(100, 100, 600, 400)

        self.first_name_label = QLabel('First Name:')
        self.first_name_entry = QLineEdit()

        self.last_name_label = QLabel('Last Name:')
        self.last_name_entry = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton('Register', self)
        self.register_button.clicked.connect(self.register)

        self.back_button = QPushButton('Back', self)
        self.back_button.clicked.connect(self.back)

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.first_name_label)
        hbox1.addWidget(self.first_name_entry)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.last_name_label)
        hbox2.addWidget(self.last_name_entry)
        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.password_label)
        hbox3.addWidget(self.password_entry)
        vbox.addLayout(hbox3)

        vbox.addWidget(self.register_button)
        vbox.addWidget(self.back_button)

        self.setLayout(vbox)

    def register(self):
        first_name = self.first_name_entry.text()
        last_name = self.last_name_entry.text()
        password = self.password_entry.text()

        if not first_name or not last_name or not password:
            self.show_error('Error', 'Please fill in all fields.')
        elif len(first_name) > 10 or len(last_name) > 10:
            self.show_error('Error', 'Maximum number of characters for first name or last name must be within 10 characters.') 
        elif not first_name.isalpha() or not last_name.isalpha():
            self.show_error('Error', 'First name and last name should contain only alphabetic characters.') 
        elif len(password) > 10 :
            self.show_error('Error', 'Password should be at most 10 characters long.')

 

        else:
            name = first_name + last_name
            print(name)
            self.hide()
            self.openmainwindow(name)
            self.hide()  # Hide the login screen
            # main_menu_screen = MainMenuScreen(name)
            # main_menu_screen.show()  # Show the main menu screen
            statementSQL = "INSERT INTO PLAYERS (USERNAME,PASSWORD)VALUES('name',password)"
            
            
            cursor = None
            
            try:
                connection = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=svr-cmp-01;"
                "Database=22YauK046;"
                "Trusted_Connection=yes;"
                "UID=COLLYERS\22YauK046"
                "pwd=SY222046"
                )

                print("Connected")

                cursor = connection.cursor()

                # Insert data into the database
                cursor.execute("INSERT INTO Players (Username, Pass) VALUES (?, ?)", name, password)
                connection.commit()

                self.show_info('Success', f'Registered: {first_name} {last_name}, Password: {password}')
                self.switch_to_login_screen()

            except pyodbc.Error as ex:
                print("Error:", ex)
                self.show_error('Error', 'Failed to register. Please try again.')

            finally:
                # Close the database connection
                cursor.close()
                connection.close()





            # Add database registration logic here (simulate for now)
            self.show_info('Success', f'Registered: {first_name} {last_name}, Password: {password}')
            # You can include logic to save the data to your database here
            self.switch_to_login_screen()

    def back(self):
        self.switch_to_login_screen()

    def switch_to_login_screen(self):
        login_screen.show()
        self.close()

    def show_error(self, title, message):
        QMessageBox.critical(self, title, message, QMessageBox.Ok)

    def show_info(self, title, message):
        QMessageBox.information(self, title, message, QMessageBox.Ok)


class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def openmainwindow(self,name):
        self.window = MainMenuScreen(name)
        self.ui =  MainMenuScreen(name)
        # self.ui.init_ui(self.window)
        self.window.show()

    def init_ui(self):
        self.setWindowTitle('Login Screen')
        self.setGeometry(100, 100, 600, 400)

        self.username_label = QLabel('Username:')
        self.username_entry = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login)

        self.switch_to_register_button = QPushButton('Switch to Register', self)
        self.switch_to_register_button.clicked.connect(self.switch_to_register_screen)

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.username_label)
        hbox1.addWidget(self.username_entry)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.password_label)
        hbox2.addWidget(self.password_entry)
        vbox.addLayout(hbox2)

        vbox.addWidget(self.login_button)
        vbox.addWidget(self.switch_to_register_button)

        self.setLayout(vbox)

    def login(self):
        name = self.username_entry.text()
        password = self.password_entry.text()

        if not name or not password:
            self.show_error('Error', 'Please fill in all fields.')
        else:
            cursor = None
            
            try:
                connection = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=svr-cmp-01;"
                "Database=22YauK046;"
                "Trusted_Connection=yes;"
                "UID=COLLYERS\22YauK046"
                "pwd=SY222046"
                )

                print("Connected")

                cursor = connection.cursor()




                #query = f"SELECT * FROM Players WHERE Username = '"+name+"'"
                

                #user = cursor.fetchone()

                query = f"select username, password from players where username = '{name}'"
                cursor.execute(query)
                connection.commit()
                details = cursor.fetchall()[0]
                username = details[0]
                pass_ = details[1]



                if (username == name) and (password == pass_):
                    print("LOGGED IN")
                else:
                    print("not logged in")
                # if user:
                #     stored_password = user.Pass

                #     if stored_password == Pass:
                #         print("Login successful")
                #         self.show_info('Success', f'Welcome {name}')
                #         self.hide()
                #         self.openmainwindow(name)  # Hide the login screen
                #     else:
                #         self.show_info('Login faliled', 'Incorrect password')
                #         print("Incorrect password. Login failed")
                # else:
                #     self.show_info('Login faliled', 'User not found')
                #     print("Username not found,login failed")

            finally:
                # Close the database connection
                cursor.close()
                connection.close()



    def switch_to_register_screen(self):
        register_screen.show()
        self.close()

    def show_error(self, title, message):
        QMessageBox.critical(self, title, message, QMessageBox.Ok)

    def show_info(self, title, message):
        QMessageBox.information(self, title, message, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    register_screen = RegisterScreen()
    login_screen = LoginScreen()

    login_screen.show()

    sys.exit(app.exec_())




