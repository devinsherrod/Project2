from PyQt6.QtWidgets import QApplication, QMainWindow
from Project2GUI import Ui_MainWindow
from Project2Logic import Scores
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scores = Scores()

        self.ui.Submit_button.clicked.connect(self.submit_scores)
        self.ui.Num_of_students_label_2.textChanged.connect(self.update_boxes)

        self.score_boxes = [(self.ui.Score1_input, self.ui.Score1_label),
                            (self.ui.Score2_input, self.ui.Score2_label),
                            (self.ui.Score3_input, self.ui.Score3_label),
                            (self.ui.Score4_input, self.ui.Score4_label)]

        self.update_boxes()
        self.ui.Feedback_label.setStyleSheet('font-size: 20pt;')

    def update_boxes(self):
        """
        shows and hides boxes based on how many scores they have
        """
        try:
            num = int(self.ui.Num_of_students_label_2.text())
            for x, (box, label) in enumerate(self.score_boxes):
                should_show = x < num
                box.setVisible(should_show)
                label.setVisible(should_show)
        except ValueError:
            for box, label in self.score_boxes:
                box.setVisible(False)
                label.setVisible(False)

    def submit_scores(self):
        """
        Handles the process when the submit button is clicked
        """
        name = self.ui.StudentName_input.text().strip()
        attempts = self.ui.Num_of_students_label_2.text().strip()
        scores = [box.text() for box, _ in self.score_boxes]

        result, success = self.scores.save_scores(name, attempts, scores)

        color = 'green' if success else 'red'
        self.ui.Feedback_label.setStyleSheet(f'color: {color};')
        self.ui.Feedback_label.setText(result)

        if success:
            self.clear_inputs()

    def clear_inputs(self):
        """
        Clears all the boxes from the user input that has been put in
        """
        self.ui.StudentName_input.clear()
        self.ui.Num_of_students_label_2.clear()
        for box, _ in self.score_boxes:
            box.clear()
        self.update_boxes()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
