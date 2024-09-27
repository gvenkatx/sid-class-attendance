# importing libraries
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject
import sys

class SimpleForm(QWidget):
    # Define a custom signal to emit the selected value
    selected_value = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()

        # Create a label
        self.label = QLabel("Please select a class for AI Attendance:")
        layout.addWidget(self.label)

        # Create a combo box
        self.comboBox = QComboBox()
        self.comboBox.addItems(["CS101", "CS201", "CS301"])
        layout.addWidget(self.comboBox)

        # Create a button
        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.on_submit)
        layout.addWidget(self.button)

        # Set the layout to the window
        self.setLayout(layout)

        # Set window title and size
        self.setWindowTitle("AI Attendance")
        self.setGeometry(300, 300, 300, 150)
        
        
    def on_submit(self):
        # Get the current text from the combo box
        selected_option = self.comboBox.currentText()
        # Emit the signal with the selected option
        self.selected_value.emit(selected_option)
        # Optionally update the label or perform other actions
        self.label.setText(f"You selected: {selected_option}")
        
        self.close()
    
    
# Main function to run the application
def main():
    app = QApplication(sys.argv)
    
    # Create the form
    form = SimpleForm()

    # Define a slot to handle the selected value
    def handle_selected_value(value):
        print(f"Selected value received: {value}")
        # You can use the selected value here as needed

    # Connect the form's signal to the slot
    form.selected_value.connect(handle_selected_value)
    
    form.show()
    
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()