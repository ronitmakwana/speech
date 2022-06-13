# from test_microphone import show
# import tkinter as tk
#                             # filedialog is used in this case to save the file path selected by the user
# from tkinter import filedialog
# print('yoooo this is working')
# for i in range(5):
#     print(i*'*')

# x = show()

# if x == 'okay':
# # def go(show):
#     #     if show == 'okay':
#     root = tk.Tk()
#     file_path = ""

#     def open_and_prep():
#         # global is needed to interact with variables in the global name space
#         global file_path
#         # askopefilename is used to retrieve the file path and file name.
#         file_path = filedialog.askopenfilename()
#     def process_open_file():
#         global file_path
#             # do what you want with the file here.
#         if file_path != "":
#                                         # opens file from file path and prints each line.
#             with open(file_path,"r") as testr:
#                 for line in testr:
#                     print (line)

#                         # create Button that link to methods used to get file path.
#     tk.Button(root, text="Open file", command=open_and_prep).pack()
#     # create Button that link to methods used to process said file.
#     tk.Button(root, text="Print Content", command=process_open_file).pack()
#     root.mainloop()
    
#         # x = show()
        
#         # go(x)

import sys
import io
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication
from speak import lati
from speak import listen

"""
Folium in PyQt5

"""
start = True
while start:
    y = listen()
    print(y,'--=====')
    if y == 'oh':
        start=False
        x = lati()
        class MyApp(QWidget):
            def __init__(self):
                super().__init__()
                self.setWindowTitle('Folium in PyQt Example')
                self.window_width, self.window_height = 1600, 1200
                self.setMinimumSize(self.window_width, self.window_height)

                layout = QVBoxLayout()
                self.setLayout(layout)
            
                loc = (x)
                coordinate = (loc)
                m = folium.Map(
                    tiles='Stamen Terrain',
                    zoom_start=13,
                    location=coordinate
                
                )
                folium.Marker(location=loc,icon = folium.Icon(color='blue')).add_to(m)

                # save map data to data object
                data = io.BytesIO()
                m.save(data, close_file=False)

                webView = QWebEngineView()
                webView.setHtml(data.getvalue().decode())
                layout.addWidget(webView)


        if __name__ == '__main__':
            app = QApplication(sys.argv)
            app.setStyleSheet('''
                QWidget {
                    font-size: 35px;
                    color: #b1b1b1;
                    background-color: #323232;
                }
            ''')
            
            myApp = MyApp()
            myApp.show()
            while True:
                d = listen()
                if d == 'stop':   
                    
                    try:
                        sys.exit(app.exec_())
                    except SystemExit:
                        print('Closing Window...')

            
    # else:
    #     listen()