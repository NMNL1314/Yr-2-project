import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
# import pyodbc


class PlayerStatusPage(QWidget):
    def __init__(self, parent=None):
        super(PlayerStatusPage, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Player Status')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label_title = QLabel('<h2>Player Status</h2>')
        self.label_player_name = QLabel()
        self.label_total_play_time = QLabel()
        self.label_current_streak = QLabel()
        self.label_longest_streak = QLabel()

        self.table_players = QTableWidget()
        self.table_players.setColumnCount(2)
        self.table_players.setHorizontalHeaderLabels(['Player', 'Score'])

        self.button_back = QPushButton('Back to Main Menu')
        self.button_back.clicked.connect(self.back_to_main_menu)

        layout.addWidget(self.label_title)
        layout.addWidget(self.label_player_name)
        layout.addWidget(self.label_total_play_time)
        layout.addWidget(self.label_current_streak)
        layout.addWidget(self.label_longest_streak)
        layout.addWidget(self.table_players)
        layout.addWidget(self.button_back)

        self.setLayout(layout)

        # Fetch player data from the database and update the UI
        # self.update_player_data()

    # def update_player_data(self):
    #     # Replace these connection details with your actual database connection details
    #     server = 'your_server'
    #     database = 'your_database'
    #     username = 'your_username'
    #     password = 'your_password'

    #     connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    #     connection = pyodbc.connect(connection_string)
    #     cursor = connection.cursor()

    #     # Example: Retrieve player data from the database
    #     # Replace this query with your actual query to retrieve player data
    #     query = "SELECT player_name, total_play_time, current_streak, longest_streak, score FROM players"
    #     cursor.execute(query)
    #     player_data = cursor.fetchone()

    #     if player_data:
    #         player_name, total_play_time, current_streak, longest_streak, total_score = player_data

    #         self.label_player_name.setText(f'Player Name: {player_name}')
    #         self.label_total_play_time.setText(f'Total Play Time: {total_play_time} hours')
    #         self.label_current_streak.setText(f'Current Streak: {current_streak}')
    #         self.label_longest_streak.setText(f'Longest Streak: {longest_streak}')

    #         # Determine your rank
    #         your_rank = self.determine_rank(connection, total_score)
    #         your_total_score = f'Your Rank: {your_rank} | Your Score: {total_score}'
    #         self.table_players.setRowCount(len(player_scores) + 1)
    #         self.table_players.setItem(len(player_scores), 0, QTableWidgetItem(your_total_score))

    #     # Example: Retrieve a list of players sorted by score
    #     # Replace this query with your actual query to retrieve player scores
    #     query_scores = "SELECT player_name, score FROM players ORDER BY score DESC"
    #     cursor.execute(query_scores)
    #     player_scores = cursor.fetchall()

    #     self.table_players.setRowCount(len(player_scores))
    #     for row, (player, score) in enumerate(player_scores):
    #         self.table_players.setItem(row, 0, QTableWidgetItem(player))
    #         self.table_players.setItem(row, 1, QTableWidgetItem(str(score)))

    #     connection.close()

    def determine_rank(self, connection, your_score):
        # Determine your rank based on your total score
        cursor = connection.cursor()
        query_rank = f"SELECT COUNT(*) + 1 FROM players WHERE score > {your_score}"
        cursor.execute(query_rank)
        your_rank = cursor.fetchone()[0]
        return your_rank

    def back_to_main_menu(self):
        # Implement the logic to go back to the main menu
        print("Going back to the main menu")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player_status_page = PlayerStatusPage()
    player_status_page.show()
    sys.exit(app.exec_())
