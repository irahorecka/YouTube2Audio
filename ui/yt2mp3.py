# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/yt2mp3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 664)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(340, 10, 270, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("")
        self.title_label.setText("YouTube to Audio")
        self.title_label.setObjectName("title_label")
        self.enter_playlist_url_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_playlist_url_label.setGeometry(QtCore.QRect(140, 450, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.enter_playlist_url_label.setFont(font)
        self.enter_playlist_url_label.setObjectName("enter_playlist_url_label")
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(140, 471, 550, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.url_input.setFont(font)
        self.url_input.setStyleSheet("color: rgb(240, 240, 240)")
        self.url_input.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.url_input.setObjectName("url_input")
        self.url_load_button = QtWidgets.QPushButton(self.centralwidget)
        self.url_load_button.setGeometry(QtCore.QRect(40, 470, 90, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.url_load_button.setFont(font)
        self.url_load_button.setObjectName("url_load_button")
        self.remove_from_table_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_from_table_button.setGeometry(QtCore.QRect(760, 370, 150, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.remove_from_table_button.setFont(font)
        self.remove_from_table_button.setObjectName("remove_from_table_button")
        self.url_error_label = QtWidgets.QLabel(self.centralwidget)
        self.url_error_label.setGeometry(QtCore.QRect(525, 452, 170, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.url_error_label.setFont(font)
        self.url_error_label.setObjectName("url_error_label")
        self.url_fetching_data_label = QtWidgets.QLabel(self.centralwidget)
        self.url_fetching_data_label.setGeometry(QtCore.QRect(630, 450, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.url_fetching_data_label.setFont(font)
        self.url_fetching_data_label.setObjectName("url_fetching_data_label")
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(40, 594, 110, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.download_button.setFont(font)
        self.download_button.setObjectName("download_button")
        self.download_path = QtWidgets.QPushButton(self.centralwidget)
        self.download_path.setGeometry(QtCore.QRect(40, 524, 90, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.download_path.setFont(font)
        self.download_path.setAutoDefault(False)
        self.download_path.setObjectName("download_path")
        self.download_folder_select = QtWidgets.QLabel(self.centralwidget)
        self.download_folder_select.setGeometry(QtCore.QRect(140, 528, 430, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.download_folder_select.setFont(font)
        self.download_folder_select.setStyleSheet("border-color: rgb(255, 255, 255)")
        self.download_folder_select.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.download_folder_select.setFrameShadow(QtWidgets.QFrame.Plain)
        self.download_folder_select.setObjectName("download_folder_select")
        self.video_table = QtWidgets.QTableWidget(self.centralwidget)
        self.video_table.setGeometry(QtCore.QRect(40, 70, 871, 284))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.video_table.setFont(font)
        self.video_table.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.video_table.setStyleSheet("color: rgb(240, 240, 240)")
        self.video_table.setMidLineWidth(0)
        self.video_table.setRowCount(250)
        self.video_table.setColumnCount(5)
        self.video_table.setObjectName("video_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        item.setFont(font)
        self.video_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        item.setFont(font)
        self.video_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        item.setFont(font)
        self.video_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        item.setFont(font)
        self.video_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        item.setFont(font)
        self.video_table.setHorizontalHeaderItem(4, item)
        self.video_table.horizontalHeader().setVisible(True)
        self.video_table.horizontalHeader().setCascadingSectionResizes(False)
        self.video_table.horizontalHeader().setDefaultSectionSize(164)
        self.video_table.horizontalHeader().setMinimumSectionSize(19)
        self.video_table.verticalHeader().setDefaultSectionSize(34)
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(160, 594, 110, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.download_folder_label = QtWidgets.QLabel(self.centralwidget)
        self.download_folder_label.setGeometry(QtCore.QRect(140, 507, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.download_folder_label.setFont(font)
        self.download_folder_label.setObjectName("download_folder_label")
        self.video_info_input = QtWidgets.QLineEdit(self.centralwidget)
        self.video_info_input.setGeometry(QtCore.QRect(180, 370, 510, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.video_info_input.setFont(font)
        self.video_info_input.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.video_info_input.setStyleSheet("color: rgb(240, 240, 240)")
        self.video_info_input.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.video_info_input.setObjectName("video_info_input")
        self.itunes_annotate = QtWidgets.QPushButton(self.centralwidget)
        self.itunes_annotate.setGeometry(QtCore.QRect(40, 370, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.itunes_annotate.setFont(font)
        self.itunes_annotate.setObjectName("itunes_annotate")
        self.revert_annotate = QtWidgets.QPushButton(self.centralwidget)
        self.revert_annotate.setGeometry(QtCore.QRect(40, 370, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.revert_annotate.setFont(font)
        self.revert_annotate.setObjectName("revert_annotate")
        self.album_artwork = QtWidgets.QLabel(self.centralwidget)
        self.album_artwork.setGeometry(QtCore.QRect(710, 416, 201, 201))
        self.album_artwork.setStyleSheet("background-color: rgb(82, 95, 106)")
        self.album_artwork.setFrameShape(QtWidgets.QFrame.Panel)
        self.album_artwork.setFrameShadow(QtWidgets.QFrame.Plain)
        self.album_artwork.setText("")
        self.album_artwork.setPixmap(QtGui.QPixmap("ui/../img/default_artwork.png"))
        self.album_artwork.setScaledContents(True)
        self.album_artwork.setAlignment(QtCore.Qt.AlignCenter)
        self.album_artwork.setObjectName("album_artwork")
        self.change_video_info_input = QtWidgets.QPushButton(self.centralwidget)
        self.change_video_info_input.setGeometry(QtCore.QRect(490, 400, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.change_video_info_input.setFont(font)
        self.change_video_info_input.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.change_video_info_input.setObjectName("change_video_info_input")
        self.download_status = QtWidgets.QLabel(self.centralwidget)
        self.download_status.setGeometry(QtCore.QRect(290, 594, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.download_status.setFont(font)
        self.download_status.setText("")
        self.download_status.setObjectName("download_status")
        self.change_video_info_input_all = QtWidgets.QPushButton(self.centralwidget)
        self.change_video_info_input_all.setGeometry(QtCore.QRect(580, 400, 110, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.change_video_info_input_all.setFont(font)
        self.change_video_info_input_all.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.change_video_info_input_all.setObjectName("change_video_info_input_all")
        self.credit_url = QtWidgets.QLabel(self.centralwidget)
        self.credit_url.setGeometry(QtCore.QRect(836, 48, 80, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.credit_url.setFont(font)
        self.credit_url.setObjectName("credit_url")
        self.save_as_mp4_box = QtWidgets.QCheckBox(self.centralwidget)
        self.save_as_mp4_box.setGeometry(QtCore.QRect(638, 528, 60, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.save_as_mp4_box.setFont(font)
        self.save_as_mp4_box.setObjectName("save_as_mp4_box")
        self.save_as_mp3_box = QtWidgets.QCheckBox(self.centralwidget)
        self.save_as_mp3_box.setGeometry(QtCore.QRect(582, 528, 54, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.save_as_mp3_box.setFont(font)
        self.save_as_mp3_box.setObjectName("save_as_mp3_box")
        self.save_filetype = QtWidgets.QLabel(self.centralwidget)
        self.save_filetype.setGeometry(QtCore.QRect(582, 507, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.save_filetype.setFont(font)
        self.save_filetype.setObjectName("save_filetype")
        self.url_reattempt_load_label = QtWidgets.QLabel(self.centralwidget)
        self.url_reattempt_load_label.setGeometry(QtCore.QRect(576, 450, 120, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.url_reattempt_load_label.setFont(font)
        self.url_reattempt_load_label.setObjectName("url_reattempt_load_label")
        self.url_poor_connection = QtWidgets.QLabel(self.centralwidget)
        self.url_poor_connection.setGeometry(QtCore.QRect(550, 450, 140, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.url_poor_connection.setFont(font)
        self.url_poor_connection.setObjectName("url_poor_connection")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube to Audio"))
        self.enter_playlist_url_label.setText(
            _translate("MainWindow", "Playlist or video URL")
        )
        self.url_load_button.setText(_translate("MainWindow", "Load"))
        self.remove_from_table_button.setText(_translate("MainWindow", "Remove video"))
        self.url_error_label.setText(
            _translate("MainWindow", "Could not get URL. Try again.")
        )
        self.url_fetching_data_label.setText(_translate("MainWindow", "Loading..."))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.download_path.setText(_translate("MainWindow", "Select"))
        self.download_folder_select.setText(_translate("MainWindow", "Folder: "))
        self.video_table.setSortingEnabled(False)
        item = self.video_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "song"))
        item = self.video_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "album"))
        item = self.video_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "artist"))
        item = self.video_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "genre"))
        item = self.video_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "artwork"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.download_folder_label.setText(_translate("MainWindow", "Download folder"))
        self.itunes_annotate.setText(_translate("MainWindow", "Ask butler"))
        self.revert_annotate.setText(_translate("MainWindow", "Go back"))
        self.change_video_info_input.setText(_translate("MainWindow", "Replace"))
        self.change_video_info_input_all.setText(
            _translate("MainWindow", "Replace all")
        )
        self.credit_url.setText(_translate("MainWindow", "source code"))
        self.save_as_mp4_box.setText(_translate("MainWindow", "MP4"))
        self.save_as_mp3_box.setText(_translate("MainWindow", "MP3"))
        self.save_filetype.setText(_translate("MainWindow", "Save as:"))
        self.url_reattempt_load_label.setText(
            _translate("MainWindow", "Reattempting load...")
        )
        self.url_poor_connection.setText(
            _translate("MainWindow", "Poor internet connection.")
        )
