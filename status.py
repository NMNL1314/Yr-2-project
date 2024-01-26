import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class PlayerStatusPage(QWidget):
    def __init__(self, parent=None):
        super(PlayerStatusPage, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.label_title = QLabel('Player Status')

        self.group_box_player_info = QGroupBox('Player Info')
        self.label_player_name = QLabel('Player: John Doe')
        self.label_icon = QLabel()

        self.group_box_game_stats = QGroupBox('Game Stats')
        self.label_total_play_time = QLabel('Total Play Time: 0 hours')
        self.label_current_streak = QLabel('Current Streak: 0 games')
        self.label_longest_streak = QLabel('Longest Streak: 0 games')
        self.label_score = QLabel('Score: 0')
        self.label_time = QLabel('Time: 0 seconds')

        self.button_back = QPushButton('Back to Main Menu')
        self.button_back.clicked.connect(self.close)

        # Set up shadow effect for the title
        title_shadow = QGraphicsDropShadowEffect()
        title_shadow.setBlurRadius(5)
        title_shadow.setColor(Qt.gray)
        title_shadow.setOffset(2)
        self.label_title.setGraphicsEffect(title_shadow)

        # Create layouts
        layout = QVBoxLayout()

        player_info_layout = QVBoxLayout()
        player_info_layout.addWidget(self.label_player_name)
        player_info_layout.addWidget(self.label_icon, alignment=Qt.AlignCenter)
        self.group_box_player_info.setLayout(player_info_layout)

        game_stats_layout = QVBoxLayout()
        game_stats_layout.addWidget(self.label_total_play_time)
        game_stats_layout.addWidget(self.label_current_streak)
        game_stats_layout.addWidget(self.label_longest_streak)
        game_stats_layout.addWidget(self.label_score)
        game_stats_layout.addWidget(self.label_time)
        self.group_box_game_stats.setLayout(game_stats_layout)

        layout.addWidget(self.label_title, alignment=Qt.AlignCenter)
        layout.addWidget(self.group_box_player_info)
        layout.addWidget(self.group_box_game_stats)
        layout.addWidget(self.button_back, alignment=Qt.AlignCenter)

        # Set the layout
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle('Player Status')
        self.setGeometry(100, 100, 400, 300)

    def update_status(self, player_name, icon_path, total_play_time, current_streak, longest_streak, score, time):
        # Update labels with player status
        self.label_player_name.setText(f'Player: {player_name}')
        self.label_icon.setPixmap(QPixmap(icon_path).scaled(50, 50, Qt.KeepAspectRatio))
        self.label_total_play_time.setText(f'Total Play Time: {total_play_time} hours')
        self.label_current_streak.setText(f'Current Streak: {current_streak} games')
        self.label_longest_streak.setText(f'Longest Streak: {longest_streak} games')
        self.label_score.setText(f'Score: {score}')
        self.label_time.setText(f'Time: {time} seconds')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player_status_page = PlayerStatusPage()
    player_status_page.show()
    main_menu_screen = MainMenuScreen(name)
    sys.exit(app.exec_())
