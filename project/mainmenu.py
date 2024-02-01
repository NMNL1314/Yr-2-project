import sys
from words import *


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from status import PlayerStatusPage

wordle_game = ''


class MainMenuScreen(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name
        self.init_ui()
        # self.loginstate = False
        # self.login_screen = LoginScreen()
        # self.login_screen.exec()

    def init_ui(self):
        self.setWindowTitle('Main Menu')
        self.setGeometry(100, 100, 400, 300)

        welcome_label = QLabel(f'Welcome, {self.name}!')
        status_button = QPushButton('Player Status', self)
        play_wordle_button = QPushButton('Play Wordle', self)
        logout_button = QPushButton('Logout', self)

        status_button.clicked.connect(self.show_player_status)
        play_wordle_button.clicked.connect(self.show_play_wordle)
        logout_button.clicked.connect(self.logout)

        vbox = QVBoxLayout()
        vbox.addWidget(welcome_label)
        vbox.addWidget(status_button)
        vbox.addWidget(play_wordle_button)
        vbox.addWidget(logout_button)

        self.setLayout(vbox)

    def show_player_status(self):
        status_screen.show()
        self.close()

        print('Show Player Status')  

    def show_play_wordle(self):
        
        print('Show Play Wordle')
        try :
            import main2 as m2
            pygame.quit()
            self.run()

        except Exception as e:
            print(f"Error:{str(e)}")

        
        self.close()

    def logout(self):
        # self.name = ''
        # self.loginstate = True
        # self.close()
        
        

        print('Logout')  

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_menu_screen = MainMenuScreen('User123')
    status_screen = PlayerStatusPage()
    # main_menu_screen.show()
    
    
    sys.exit(app.exec_())
