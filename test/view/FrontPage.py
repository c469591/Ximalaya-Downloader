# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrontPage.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_frontPageFrame(object):
    def setupUi(self, frontPageFrame):
        if not frontPageFrame.objectName():
            frontPageFrame.setObjectName(u"frontPageFrame")
        frontPageFrame.resize(850, 650)
        frontPageFrame.setStyleSheet(u"background-color: rgb(249, 249, 249);")
        self.horizontalLayout = QHBoxLayout(frontPageFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(frontPageFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(frontPageFrame)

        QMetaObject.connectSlotsByName(frontPageFrame)
    # setupUi

    def retranslateUi(self, frontPageFrame):
        frontPageFrame.setWindowTitle(QCoreApplication.translate("frontPageFrame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("frontPageFrame", u"\u9996\u9875", None))
    # retranslateUi

