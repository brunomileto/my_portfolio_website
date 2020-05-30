import csv
import json
import pyrebase


class Database:
    def __init__(self, data):
        self.data = data

    def write_to_file(self):
        with open('./database_dir/database.txt', 'a') as database_txt:
            email = self.data['email']
            subject = self.data['subject']
            message = self.data['message']
            file = database_txt.write(f'\n{email},{subject},{message}')

    def wrote_to_csv(self):
        with open('./database_dir/database.csv', 'a', newline='') as database_csv:
            email = self.data['email']
            subject = self.data['subject']
            message = self.data['message']
            csv_writer = csv.writer(database_csv)
            csv_writer.writerow([email, subject, message])

    def write_to_json(self):
        with open('./database_dir/database.json', 'a') as database_json:
            file = json.dumps(self.data)
            archive = database_json.write(file)

    def firebase_database_writer(self):
        config = {
            "apiKey": "AIzaSyAhUAL4O_ZdABKC9ge3ddW3XPhssbgOf2E",
            "authDomain": "my-portfolio-website-24481.firebaseapp.com",
            "databaseURL": "https://my-portfolio-website-24481.firebaseio.com/",
            "storageBucket": "my-portfolio-website-24481.appspot.com"
        }
        firebase = pyrebase.initialize_app(config)
        self.firebase_database = firebase.database()
        self.firebase_database.child('users').push(self.data)

    # def firebase_database_retrieve_data(self):
    #     timestamp_keys = self.firebase_database.child('users').shallow().get()
    #     for i in timestamp_keys.val():
    #         data = self.firebase_database.child('users').child(i).get()
    #         print(data.val())
