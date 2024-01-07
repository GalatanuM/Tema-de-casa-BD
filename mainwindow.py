# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from ui_form import Ui_mainWindow
import hashlib
import datetime
import sqlite3

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.current_user_id = None  # Initialize the current_user_id attribute

        # Connect signals to slots or add additional setup logic here
        self.ui.pushButton.clicked.connect(self.register_user)
        self.ui.pushButton_2.clicked.connect(self.loginButtonClicked)
        self.ui.pushButton_3.clicked.connect(self.checkAvailabilityButtonClicked)
        self.ui.pushButton_4.clicked.connect(self.reserveParkingButtonClicked)
        self.ui.pushButton_5.clicked.connect(self.goBackFromReservations)
        self.ui.pushButton_6.clicked.connect(self.deleteReservation)
        self.ui.pushButton_7.clicked.connect(self.logoutButtonClicked)
        self.ui.pushButton_8.clicked.connect(self.myReservationsButtonClicked)

    def loginButtonClicked(self):
        username = self.ui.lineEdit_2.text()

        # Hash the entered password
        hashed_password = self.hash_password(self.ui.lineEdit.text())

        # Check if the user is registered and if the password is correct
        login_result = self.is_valid_login(username, hashed_password)

        if login_result == "success":
            # Successful login, set the current_user_id
            self.current_user_id = self.get_user_id(username)
            # Switch to the next window
            self.ui.stackedWidget.setCurrentIndex(1)
        elif login_result == "user_not_found":
            # Username not recognized, show a pop-up message
            QMessageBox.warning(self, "Login Failed", "Invalid username. Please register.")
        elif login_result == "incorrect_password":
            # Incorrect password, show a pop-up message
            QMessageBox.warning(self, "Login Failed", "Incorrect password. Please try again.")
        elif login_result == "not_registered":
            # User is not registered, show a pop-up message
            QMessageBox.warning(self, "Login Failed", "You are not registered. Please register before logging in.")

    def get_user(self, username, password):
        conn = sqlite3.connect("parking.db")
        cursor = conn.cursor()

        # Check if the username and password match a record in the 'users' table
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        conn.close()

        return user

    def logoutButtonClicked(self):
        # Switch back to the login screen
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        self.ui.stackedWidget.setCurrentIndex(0)

    def is_valid_login(self, username, hashed_password):
        conn = sqlite3.connect("parking.db")
        cursor = conn.cursor()

        # Check if the username is registered
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        if user:
            # Username found, check if the password is correct
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
            user_with_password = cursor.fetchone()

            if user_with_password:
                # Password is correct
                conn.close()
                self.ui.lineEdit.clear()
                return "success"
            else:
                # Incorrect password
                conn.close()
                self.ui.lineEdit.clear()
                return "incorrect_password"
        else:
            # Username not found
            conn.close()
            self.ui.lineEdit.clear()
            return "not_registered"

    def get_user_id(self, username):
        conn = sqlite3.connect("parking.db")
        cursor = conn.cursor()

        # Get the user ID based on the username
        cursor.execute("SELECT id FROM users WHERE username=?", (username,))
        user_id = cursor.fetchone()[0]  # Assuming the user ID is the first column

        conn.close()

        return user_id

    def register_user(self):
        conn = sqlite3.connect("parking.db")
        cursor = conn.cursor()
        username = self.ui.lineEdit_2.text()

        # Hash the entered password before storing
        hashed_password = self.hash_password(self.ui.lineEdit.text())

        if hashed_password is None or not hashed_password.strip():
            QMessageBox.warning(self, "Registration Failed", "Password cannot be blank.")
            conn.close()
            return

        try:
            # Insert the new user into the 'users' table with hashed password
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            QMessageBox.information(self, "Registration", "Registration successful. You can now log in.")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Registration Failed", "Username already exists. Please choose another.")
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit.clear()

        conn.close()

    def checkAvailabilityButtonClicked(self):
        # Get the selected check-in and check-out date and time
        checkin_date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        checkin_hour = self.ui.timeEdit.time().toString("hh:mm:ss")
        checkout_date = self.ui.calendarWidget_2.selectedDate().toString("yyyy-MM-dd")
        checkout_hour = self.ui.timeEdit_2.time().toString("hh:mm:ss")

        # Format the selected date and time for comparison
        selected_checkin = f"{checkin_date} {checkin_hour}"
        selected_checkout = f"{checkout_date} {checkout_hour}"

        # Query the reservations table to find overlapping reservations
        conn = sqlite3.connect("parking.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT parking_no
            FROM parking
            WHERE parking_no NOT IN (
                SELECT DISTINCT r.parking_number
                FROM reservations r
                WHERE (
                    (r.checkin_date < ? AND r.checkout_date > ?) OR
                    (r.checkin_date = ? AND r.checkin_hour < ? AND r.checkout_date > ?) OR
                    (r.checkout_date = ? AND r.checkout_hour > ? AND r.checkin_date < ?) OR
                    (r.checkin_date = ? AND r.checkout_date = ? AND r.checkin_hour < ? AND r.checkout_hour > ?)
                )
            )
        """, (selected_checkout, selected_checkin, checkin_date, checkin_hour, checkout_date,
              checkout_date, checkout_hour, checkin_date, checkin_date, checkout_date,
              checkin_hour, checkout_hour))

        available_parking_spots = cursor.fetchall()

        conn.close()

        # Clear existing items in the listWidget
        self.ui.listWidget.clear()

        if available_parking_spots:
            # Add available parking spots as new items in the listWidget
            for parking_spot in available_parking_spots:
                item = QListWidgetItem(f"Parking Spot: {parking_spot[0]}")
                self.ui.listWidget.addItem(item)
        else:
            QMessageBox.information(self, "Availability", "No available parking spots for the selected period.")

    def reserveParkingButtonClicked(self):
        # Get the selected parking spot from the listWidget
        selected_item = self.ui.listWidget.currentItem()

        if selected_item:
            # Extract the parking spot number from the selected item text
            parking_spot = int(selected_item.text().split(":")[1].strip())

            # Get the user ID and selected date and time
            user_id = self.current_user_id
            checkin_date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
            checkin_hour = self.ui.timeEdit.time().toString("hh:mm:ss")
            checkout_date = self.ui.calendarWidget_2.selectedDate().toString("yyyy-MM-dd")
            checkout_hour = self.ui.timeEdit_2.time().toString("hh:mm:ss")

            conn = sqlite3.connect("parking.db")
            cursor = conn.cursor()

            try:
                # Begin the transaction
                conn.execute("BEGIN")

                # Insert the reservation into the 'reservations' table
                cursor.execute("""
                        INSERT INTO reservations (user_id, parking_number, checkin_date, checkin_hour, checkout_date, checkout_hour)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (user_id, parking_spot, checkin_date, checkin_hour, checkout_date, checkout_hour))

                # Get the current date and time for the history entry

                reservation_date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Insert the reservation into the 'history' table
                cursor.execute("""
                                        INSERT INTO history (reservation_date_and_time, user_id, check_in_date, check_in_hour, check_out_date, check_out_hour)
                                        VALUES (?, ?, ?, ?, ?, ?)
                                    """, (
                reservation_date_and_time, user_id, checkin_date, checkin_hour, checkout_date, checkout_hour))

                # Commit the transaction
                conn.execute("COMMIT")

                QMessageBox.information(self, "Reservation", "Parking spot reserved successfully.")
            except sqlite3.IntegrityError as e:
                # Extract the error message raised by the database
                error_message = str(e)

                # Rollback the transaction in case of an error
                conn.execute("ROLLBACK")

                # Display the error message in a QMessageBox
                QMessageBox.warning(self, "Reservation Failed", error_message)
            finally:
                conn.close()
        else:
            QMessageBox.warning(self, "Reservation Failed", "Please select a parking spot from the list.")

    def myReservationsButtonClicked(self):
        # Switch to the "My Reservations" page
        self.ui.stackedWidget.setCurrentIndex(2)

        # Fetch reservations for the current user
        reservations = self.get_user_reservations(self.current_user_id)

        # Clear the existing items in the listWidget
        self.ui.listWidget_2.clear()
        self.ui.listWidget.clear()

        # Populate the listWidget with reservations
        for reservation in reservations:
            parking_no = reservation [2]
            checkin_date = reservation[3]
            checkin_hour = reservation[4]
            checkout_date = reservation[5]
            checkout_hour = reservation[6]

            # Format the reservation information as a string
            reservation_info = f"Parking {parking_no} from {checkin_date} {checkin_hour} to {checkout_date} {checkout_hour}"

            # Add the reservation info to the listWidget
            item = QListWidgetItem(reservation_info)
            self.ui.listWidget_2.addItem(item)

    def get_user_reservations(self, user_id):
        conn = sqlite3.connect("parking.db")
        cursor = conn.cursor()

        # Fetch reservations for the current user
        cursor.execute("""
                SELECT * FROM reservations
                WHERE user_id = ?
            """, (user_id,))

        reservations = cursor.fetchall()

        conn.close()

        return reservations

    def goBackFromReservations(self):
        # Switch to the parking reservation screen (index 1)
        self.ui.stackedWidget.setCurrentIndex(1)

        # Clear the existing items in the listWidget_2
        self.ui.listWidget_2.clear()

    def deleteReservation(self):
        # Get the selected reservation item from the listWidget_2
        selected_item = self.ui.listWidget_2.currentItem()

        if selected_item:
            # Extract reservation details from the selected item text
            reservation_details = selected_item.text().split(" ")
            parking_no = int(reservation_details[1])
            checkin_date = reservation_details[3]
            checkin_hour = reservation_details[4]

            conn = sqlite3.connect("parking.db")
            cursor = conn.cursor()

            try:
                # Delete the reservation based on parking_number, checkin_date, and checkin_hour
                cursor.execute("""
                    DELETE FROM reservations
                    WHERE user_id = ? AND parking_number = ? AND checkin_date = ? AND checkin_hour = ?
                """, (self.current_user_id, parking_no, checkin_date, checkin_hour))

                conn.commit()

                # Check if any rows were affected (reservation was deleted)
                if cursor.rowcount > 0:
                    QMessageBox.information(self, "Reservation Deleted", "Reservation deleted successfully.")
                    self.ui.listWidget_2.takeItem(self.ui.listWidget_2.row(selected_item))
                else:
                    QMessageBox.warning(self, "Deletion Failed", "Reservation not found for deletion.")
            except sqlite3.Error as e:
                error_message = str(e)
                QMessageBox.warning(self, "Deletion Failed", f"Error deleting reservation: {error_message}")
            finally:
                conn.close()
        else:
            QMessageBox.warning(self, "Deletion Failed", "Please select a reservation to delete.")

    def hash_password(self, password):
        # Use SHA-256 for password hashing
        if(password):
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            return hashed_password
        else:
            return None




if __name__ == "__main__":
    # Database setup
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_details (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email_address TEXT NOT NULL
            )
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reservation_date_and_time DATETIME,
                user_id INTEGER,
                check_in_date DATE,
                check_in_hour TIME,
                check_out_date DATE,
                check_out_hour TIME
            )
        """)

    # Check if the 'parking' table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='parking'")
    parking_table_exists = cursor.fetchone()

    if not parking_table_exists:
        # Create the 'parking' table
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS parking (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            parking_no INTEGER
                        )
                    """)
        # Insert 100 parking spots
        cursor.executemany("INSERT INTO parking (parking_no) VALUES (?)", [(i + 1,) for i in range(100)])

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            parking_number INTEGER,
            checkin_date DATE,
            checkin_hour TIME,
            checkout_date DATE,
            checkout_hour TIME,
            UNIQUE (user_id, parking_number, checkin_date, checkin_hour),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (parking_number) REFERENCES parking(parking_no)
        )
    """)

    # Create a trigger to check the checkin_date constraint
    cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS checkin_date_constraint
            BEFORE INSERT ON reservations
            FOR EACH ROW
            WHEN NEW.checkin_date < DATE('now')
            BEGIN
                SELECT RAISE(FAIL, 'Check-in date must be greater than or equal to the current date');
            END;
        """)

    # Create triggers for additional constraints
    cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS checkout_date_constraint
            BEFORE INSERT ON reservations
            FOR EACH ROW
            WHEN NEW.checkout_date < NEW.checkin_date
            BEGIN
                SELECT RAISE(FAIL, 'Check-out date must be greater than or equal to check-in date');
            END;
        """)

    cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS checkout_hour_constraint
            BEFORE INSERT ON reservations
            FOR EACH ROW
            WHEN (NEW.checkin_date = NEW.checkout_date) AND (NEW.checkout_hour <= NEW.checkin_hour)
            BEGIN
                SELECT RAISE(FAIL, 'Check-out hour must be greater than check-in hour');
            END;
        """)

    cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS checkin_hour_constraint
            BEFORE INSERT ON reservations
            FOR EACH ROW
            WHEN (NEW.checkin_date = DATE('now')) AND (NEW.checkin_hour <= TIME('now'))
            BEGIN
                SELECT RAISE(FAIL, 'Check-in hour must be greater than current hour');
            END;
        """)

    cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS check_overlap_constraint
        BEFORE INSERT ON reservations
        FOR EACH ROW
        WHEN EXISTS (
            SELECT 1
            FROM reservations
            WHERE parking_number = NEW.parking_number
              AND user_id = NEW.user_id
              AND (
                (checkin_date <= NEW.checkin_date AND checkout_date >= NEW.checkin_date)
                OR (checkin_date <= NEW.checkout_date AND checkout_date >= NEW.checkout_date)
                OR (checkin_date >= NEW.checkin_date AND checkout_date <= NEW.checkout_date)
              )
        )
        BEGIN
            SELECT RAISE(FAIL, 'Overlapping reservations are not allowed');
        END;
    """)

    conn.commit()
    conn.close()

    # Run the application
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
