import sys
import rclpy
from std_msgs.msg import String
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QMessageBox

class ShapeSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shape Selector Example")
        self.setGeometry(100, 100, 400, 150)

        # Create a label to trigger shape selection
        self.label = QLabel("Select Shape", self)
        self.label.setStyleSheet("border: 1px solid gray; padding: 5px; cursor: pointer;")
        self.label.mousePressEvent = self.show_shape_selection

        # Create a combo box for shape selection (initially hidden)
        self.combo_box = QComboBox(self)
        self.combo_box.hide()
        self.combo_box.addItem("Rose - Rhodonea")
        self.combo_box.addItem("Spiral Curve")
        self.combo_box.addItem("Flower Shape")
        self.combo_box.addItem("Rounded gear")
        self.combo_box.addItem("Butterfly")
        self.combo_box.addItem("circle")
        self.combo_box.currentIndexChanged.connect(self.on_shape_selected)

        # Create a layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combo_box)
        self.setLayout(layout)
        
        # Create a ROS2 publisher
        self.node = rclpy.create_node('shapeNode')  # Create a separate node
        self.publisher = self.node.create_publisher(String, 'shape_selection', 10)

    def show_shape_selection(self, event):
        self.combo_box.show()

    def on_shape_selected(self, index):
        selected_shape = self.combo_box.currentText()
        msg = String()
        msg.data = selected_shape
        self.publisher.publish(msg)
        QMessageBox.information(self, "Selection", f"Selected shape: {selected_shape}")
        self.combo_box.hide()

def main():
    rclpy.init()
    app = QApplication(sys.argv)
    window = ShapeSelector()
    window.show()
    #rclpy.shutdown()
    sys.exit(app.exec_())
    

if __name__ == "__main__":

    main()
  