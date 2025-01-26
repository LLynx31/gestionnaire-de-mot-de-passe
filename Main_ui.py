from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLayout,
                               QLineEdit, QMainWindow, QPushButton, QScrollArea,
                               QSizePolicy, QStackedWidget, QVBoxLayout, QWidget, QSpacerItem)
from PySide6.QtCore import Signal
from Dialog_ui import *
from modelsData import *
from functools import partial

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadData()
        self.branchementSlots()


    def setupUi(self):
        self.resize(949, 633)
        self.setFixedSize(QSize(949, 633))
        self.setAutoFillBackground(False)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")

        self.StackPage = QStackedWidget(self.centralwidget)
        self.StackPage.setObjectName(u"StackPage")
        self.StackPage.setGeometry(QRect(-1, -1, 951, 631))

        self.pageAuthentification = QWidget()
        self.pageAuthentification.setObjectName(u"pageAuthentification")
        self.framePageAuthentification = QFrame(self.pageAuthentification)
        self.framePageAuthentification.setObjectName(u"framePageAuthentification")
        self.framePageAuthentification.setGeometry(QRect(-1, 9, 951, 621))
        self.framePageAuthentification.setStyleSheet(u"background-color : rgb(241, 241, 241)")
        self.framePageAuthentification.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePageAuthentification.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidgetAuthentification = QStackedWidget(self.framePageAuthentification)
        self.stackedWidgetAuthentification.setObjectName(u"stackedWidgetAuthentification")
        self.stackedWidgetAuthentification.setGeometry(QRect(500, 20, 421, 571))

        self.pageConnexion = QWidget()
        self.pageConnexion.setObjectName(u"pageConnexion")
        self.titreFrameLabel = QLabel(self.pageConnexion)
        self.titreFrameLabel.setObjectName(u"titreFrameLabel")
        self.titreFrameLabel.setGeometry(QRect(30, 40, 391, 41))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(241, 241, 241, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)

        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)

        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)

        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)

        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)

        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)

        self.titreFrameLabel.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        self.titreFrameLabel.setFont(font)
        self.titreFrameLabel.setStyleSheet(u"color : black")
        self.titreFrameLabel.setWordWrap(True)
        self.verticalLayoutWidget = QWidget(self.pageConnexion)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 150, 291, 71))
        self.usernameVerticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.usernameVerticalLayout.setObjectName(u"usernameVerticalLayout")
        self.usernameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.usernameLabel = QLabel(self.verticalLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setStyleSheet(u"color: black")

        self.usernameVerticalLayout.addWidget(self.usernameLabel)

        self.usernamelineEdit = QLineEdit(self.verticalLayoutWidget)
        self.usernamelineEdit.setObjectName(u"usernamelineEdit")
        self.usernamelineEdit.setStyleSheet(u"border: 1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"color: black;\n"
"background-color:rgb(248, 248, 248)")

        self.usernameVerticalLayout.addWidget(self.usernamelineEdit)

        self.verticalLayoutWidget_2 = QWidget(self.pageConnexion)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(70, 230, 291, 71))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.passwordLabel = QLabel(self.verticalLayoutWidget_2)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setStyleSheet(u"color:black")

        self.verticalLayout_2.addWidget(self.passwordLabel)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"border: 1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"color: black;\n"
"background-color:rgb(248, 248, 248)")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.seConnecterPushButton = QPushButton(self.pageConnexion)
        self.seConnecterPushButton.setObjectName(u"seConnecterPushButton")
        self.seConnecterPushButton.setGeometry(QRect(70, 330, 291, 41))
        self.seConnecterPushButton.setStyleSheet(u"QPushButton {\n"
"        background-color: #4CAF50; /* Vert moderne */\n"
"        border: none;\n"
"        color: white;\n"
"        padding: 10px 25px;\n"
"        text-align: center;\n"
"        text-decoration: none;\n"
"        display: inline-block;\n"
"        font-size: 16px;\n"
"        font-weight: bold;\n"
"        border-radius: 5px; /* Coins arrondis */\n"
"        transition: background-color 0.3s ease, transform 0.2s ease;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #45a049; /* Vert plus fonc\u00e9 pour hover */\n"
"        transform: scale(1.05); /* Agrandir l\u00e9g\u00e8rement */\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #3e8e41; /* Vert encore plus fonc\u00e9 pour clic */\n"
"        transform: scale(0.95); /* R\u00e9duction l\u00e9g\u00e8re \u00e0 l'appui */\n"
"    }")
        self.seConnecterPushButton.setCheckable(True)
        self.sinscrirelabel = QPushButton(self.pageConnexion)
        self.sinscrirelabel.setObjectName(u"sinscrirelabel")
        self.sinscrirelabel.setGeometry(QRect(70, 390, 291, 20))
        self.sinscrirelabel.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.stackedWidgetAuthentification.addWidget(self.pageConnexion)


        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.titreFrameCompte = QLabel(self.page_3)
        self.titreFrameCompte.setObjectName(u"titreFrameCompte")
        self.titreFrameCompte.setGeometry(QRect(30, 0, 391, 41))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)

        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)

        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)

        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)

        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)

        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)

        self.titreFrameCompte.setPalette(palette1)
        self.titreFrameCompte.setFont(font)
        self.titreFrameCompte.setStyleSheet(u"color : black")
        self.titreFrameCompte.setWordWrap(True)
        self.verticalLayoutWidget_3 = QWidget(self.page_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(60, 60, 291, 71))
        self.verticalLayoutNom = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayoutNom.setObjectName(u"verticalLayoutNom")
        self.verticalLayoutNom.setContentsMargins(0, 0, 0, 0)
        self.labelNom = QLabel(self.verticalLayoutWidget_3)
        self.labelNom.setObjectName(u"labelNom")
        self.labelNom.setStyleSheet(u"color: black")

        self.verticalLayoutNom.addWidget(self.labelNom)

        self.lineEditNom = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEditNom.setObjectName(u"lineEditNom")
        self.lineEditNom.setStyleSheet(u"border: 1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"color: black;\n"
"background-color:rgb(248, 248, 248)")

        self.verticalLayoutNom.addWidget(self.lineEditNom)

        self.verticalLayoutWidget_4 = QWidget(self.page_3)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(60, 140, 291, 71))
        self.verticalLayoutPrenom = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayoutPrenom.setObjectName(u"verticalLayoutPrenom")
        self.verticalLayoutPrenom.setContentsMargins(0, 0, 0, 0)
        self.labelPrenom = QLabel(self.verticalLayoutWidget_4)
        self.labelPrenom.setObjectName(u"labelPrenom")
        self.labelPrenom.setStyleSheet(u"color: black")

        self.verticalLayoutPrenom.addWidget(self.labelPrenom)

        self.lineEditPrenom = QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditPrenom.setObjectName(u"lineEditPrenom")
        self.lineEditPrenom.setStyleSheet(u"border: 1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"color: black;\n"
"background-color:rgb(248, 248, 248)")

        self.verticalLayoutPrenom.addWidget(self.lineEditPrenom)

        self.verticalLayoutWidget_5 = QWidget(self.page_3)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(60, 220, 291, 71))
        self.verticalLayoutEmail = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayoutEmail.setObjectName(u"verticalLayoutEmail")
        self.verticalLayoutEmail.setContentsMargins(0, 0, 0, 0)
        self.labelEmail = QLabel(self.verticalLayoutWidget_5)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setStyleSheet(u"color: black")

        self.verticalLayoutEmail.addWidget(self.labelEmail)

        self.lineEditEmail = QLineEdit(self.verticalLayoutWidget_5)
        self.lineEditEmail.setObjectName(u"lineEditEmail")
        self.lineEditEmail.setStyleSheet(u"border: 1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"color: black;\n"
"background-color:rgb(248, 248, 248)")

        self.verticalLayoutEmail.addWidget(self.lineEditEmail)

        self.verticalLayoutWidget_6 = QWidget(self.page_3)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(60, 380, 291, 71))
        self.verticalLayoutNum = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayoutNum.setObjectName(u"verticalLayoutNum")
        self.verticalLayoutNum.setContentsMargins(0, 0, 0, 0)
        self.labelNum = QLabel(self.verticalLayoutWidget_6)
        self.labelNum.setObjectName(u"labelNum")
        self.labelNum.setStyleSheet(u"color: black")

        self.verticalLayoutNum.addWidget(self.labelNum)

        self.lineEditNum = QLineEdit(self.verticalLayoutWidget_6)
        self.lineEditNum.setObjectName(u"lineEditNum")
        self.lineEditNum.setStyleSheet(u"border: 1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"color: black;\n"
"background-color:rgb(248, 248, 248)")

        self.verticalLayoutNum.addWidget(self.lineEditNum)

        self.verticalLayoutWidget_7 = QWidget(self.page_3)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(60, 300, 291, 71))
        self.verticalLayoutPassword = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayoutPassword.setObjectName(u"verticalLayoutPassword")
        self.verticalLayoutPassword.setContentsMargins(0, 0, 0, 0)
        self.labelPassword = QLabel(self.verticalLayoutWidget_7)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setStyleSheet(u"color: black")

        self.verticalLayoutPassword.addWidget(self.labelPassword)

        self.lineEditPassword = QLineEdit(self.verticalLayoutWidget_7)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setStyleSheet(u"border: 1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"padding: 3px;\n"
"color: black;\n"
"background-color:rgb(248, 248, 248)")

        self.verticalLayoutPassword.addWidget(self.lineEditPassword)

        self.pushButtonSinscrire = QPushButton(self.page_3)
        self.pushButtonSinscrire.setObjectName(u"pushButtonSinscrire")
        self.pushButtonSinscrire.setGeometry(QRect(60, 470, 291, 41))
        self.pushButtonSinscrire.setStyleSheet(u"QPushButton {\n"
"        background-color: #4CAF50; /* Vert moderne */\n"
"        border: none;\n"
"        color: white;\n"
"        padding: 10px 25px;\n"
"        text-align: center;\n"
"        text-decoration: none;\n"
"        display: inline-block;\n"
"        font-size: 16px;\n"
"        font-weight: bold;\n"
"        border-radius: 5px; /* Coins arrondis */\n"
"        transition: background-color 0.3s ease, transform 0.2s ease;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #45a049; /* Vert plus fonc\u00e9 pour hover */\n"
"        transform: scale(1.05); /* Agrandir l\u00e9g\u00e8rement */\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #3e8e41; /* Vert encore plus fonc\u00e9 pour clic */\n"
"        transform: scale(0.95); /* R\u00e9duction l\u00e9g\u00e8re \u00e0 l'appui */\n"
"    }")
        self.pushButtonSinscrire.setCheckable(True)
        self.seconnecterlabel = QPushButton(self.page_3)
        self.seconnecterlabel.setObjectName(u"sinscrirelabel")
        self.seconnecterlabel.setGeometry(QRect(60, 530, 291, 20))
        self.seconnecterlabel.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.stackedWidgetAuthentification.addWidget(self.page_3)


        self.stackedWidgetAuthentification.addWidget(self.page_3)

        self.label = QLabel(self.framePageAuthentification)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(7, 8, 491, 611))
        self.label.setPixmap(QPixmap(u"thumbnail_800x480px-122710.jpg"))
        self.label.setScaledContents(True)
        self.StackPage.addWidget(self.pageAuthentification)

        self.pageDashbord = QWidget()
        self.pageDashbord.setObjectName(u"pageDashbord")
        self.frameMenuDashboard = QFrame(self.pageDashbord)
        self.frameMenuDashboard.setObjectName(u"frameMenuDashboard")
        self.frameMenuDashboard.setGeometry(QRect(0, 0, 255, 631))
        self.frameMenuDashboard.setStyleSheet(u"/* Style g\u00e9n\u00e9ral de la frame */\n"
"QFrame {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
#"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    border: 2px solid #34495E; /* Bordure fine et \u00e9l\u00e9gante */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}\n"
"\n"
"/* Style des boutons \u00e0 l'int\u00e9rieur de la frame */\n"
"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les boutons */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet hover pour les boutons */\n"
"QPushButton:hover {\n"
"    backg"
                        "round-color: #16A085; /* Couleur plus fonc\u00e9e au survol */\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"/* Style des labels */\n"
"QLabel {\n"
"    color: #ECF0F1; /* Couleur blanche/gris clair */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    margin-bottom: 10px; /* Espacement sous le label */\n"
"}\n"
"")

        self.frameMenuDashboard.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameMenuDashboard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_8 = QWidget(self.frameMenuDashboard)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 160, 221, 306))
        self.verticalLayoutMenuDashbord = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayoutMenuDashbord.setSpacing(0)
        self.verticalLayoutMenuDashbord.setObjectName(u"verticalLayoutMenuDashbord")
        self.verticalLayoutMenuDashbord.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayoutMenuDashbord.addWidget(self.pushButton)

        self.pushButtonCB = QPushButton(self.verticalLayoutWidget_8)
        self.pushButtonCB.setObjectName(u"pushButtonCB")

        self.verticalLayoutMenuDashbord.addWidget(self.pushButtonCB)

        self.pushButtonDoc = QPushButton(self.verticalLayoutWidget_8)
        self.pushButtonDoc.setObjectName(u"pushButtonDoc")

        self.verticalLayoutMenuDashbord.addWidget(self.pushButtonDoc)

        self.pushButtonNote = QPushButton(self.verticalLayoutWidget_8)
        self.pushButtonNote.setObjectName(u"pushButtonNote")

        self.verticalLayoutMenuDashbord.addWidget(self.pushButtonNote)

        self.pushButtonGenPass = QPushButton(self.frameMenuDashboard)
        self.pushButtonGenPass.setObjectName(u"pushButtonGenPass")
        self.pushButtonGenPass.setGeometry(QRect(10, 500, 219, 51))
        self.pushButtonDeconnexion = QPushButton(self.frameMenuDashboard)
        self.pushButtonDeconnexion.setObjectName(u"pushButtonDeconnexion")
        self.pushButtonDeconnexion.setGeometry(QRect(20, 560, 201, 51))
        self.pushButtonDeconnexion.setStyleSheet(u"/* Style g\u00e9n\u00e9ral du bouton */\n"
"QPushButton {\n"
"    background-color: #E74C3C; /* Rouge vif */\n"
"    color: white; /* Texte en blanc */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 10px 20px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    font-family: Arial, sans-serif; /* Police moderne */\n"
"    transition: background-color 0.3s ease; /* Transition fluide pour les interactions */\n"
"}\n"
"\n"
"/* Effet au survol */\n"
"QPushButton:hover {\n"
"    background-color: #C0392B; /* Rouge plus fonc\u00e9 au survol */\n"
"}\n"
"\n"
"/* Effet au clic */\n"
"QPushButton:pressed {\n"
"    background-color: #A93226; /* Rouge encore plus fonc\u00e9 */\n"
"    padding-left: 22px; /* L\u00e9g\u00e8re modification pour l'effet d'appui */\n"
"}\n"
"\n"
"/* Bouton d\u00e9sactiv\u00e9 (facultatif) */\n"
"QPushButton:disabled {\n"
"    b"
                        "ackground-color: #E6B0AA; /* Rouge p\u00e2le pour l'\u00e9tat d\u00e9sactiv\u00e9 */\n"
"    color: #FDEDEC; /* Couleur de texte plus douce */\n"
"    border: none; /* Pas de bordure */\n"
"}\n"
"")
        self.labelCompte = ClickableLabel(self.frameMenuDashboard)
        self.labelCompte.setObjectName(u"labelCompte")
        self.labelCompte.setGeometry(QRect(80, 10, 81, 91))
        self.labelCompte.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.labelCompte.setPixmap(QPixmap(u"iconeCompte.png"))
        self.labelCompte.setScaledContents(True)
        self.label_3 = QLabel(self.frameMenuDashboard)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 100, 121, 51))

        self.stackedWidget = QStackedWidget(self.pageDashbord)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(250, 0, 701, 651))

        self.pageApplication = QWidget()
        self.pageApplication.setObjectName(u"pageApplication")
        self.frameApplication = QFrame(self.pageApplication)
        self.frameApplication.setObjectName(u"frameApplication")
        self.frameApplication.setGeometry(QRect(0, 0, 701, 651))
        self.frameApplication.setStyleSheet(u"/* Style g\u00e9n\u00e9ral de la frame */\n"
"QFrame {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    border: 2px solid #34495E; /* Bordure fine et \u00e9l\u00e9gante */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")
        self.frameApplication.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameApplication.setFrameShadow(QFrame.Shadow.Raised)
        self.frameAddApplication = QFrame(self.frameApplication)
        self.frameAddApplication.setObjectName(u"frameAddApplication")
        self.frameAddApplication.setGeometry(QRect(10, 10, 681, 81))
        self.frameAddApplication.setStyleSheet(u"QFrame {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    border: 2px solid #34495E; /* Bordure fine et \u00e9l\u00e9gante */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")
        self.frameAddApplication.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAddApplication.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButtonAddapplication = QPushButton(self.frameAddApplication)
        self.pushButtonAddapplication.setObjectName(u"pushButtonAddapplication")
        self.pushButtonAddapplication.setGeometry(QRect(20, 10, 219, 51))
        self.pushButtonAddapplication.setStyleSheet(u"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les boutons */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"/* Style des labels */\n"
"QLabel {\n"
"    color: #ECF0F1; /* Couleur blanche/gris clair */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    margin-bottom: 10px; /* Espacement sous le label */\n"
"}\n"
"")
        self.scrollAreaApplication = QScrollArea(self.frameApplication)
        self.scrollAreaApplication.setObjectName(u"scrollAreaApplication")
        self.scrollAreaApplication.setGeometry(QRect(9, 99, 681, 531))
        self.scrollAreaApplication.setStyleSheet(u"")
        self.scrollAreaApplication.setWidgetResizable(True)

        self.scrollAreaWidgetContentsApp = QWidget()
        self.scrollAreaWidgetContentsApp.setObjectName(u"scrollAreaWidgetContentsApp")
        self.scrollAreaWidgetContentsApp.setStyleSheet(u"/* Style g\u00e9n\u00e9ral de la frame */\n"
"QWidget {\n"
"    background-color: #2C3E50;\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")

        self.verticalLayoutApp = QVBoxLayout(self.scrollAreaWidgetContentsApp)
        self.verticalLayoutApp.setObjectName(u"verticalLayoutApp")
        self.verticalLayoutApp.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayoutApp.setContentsMargins(5, 5, 5, 5)

        self.label_4 = ClickableLabel(self.scrollAreaWidgetContentsApp)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 80))
        self.label_4.setMaximumSize(QSize(16777215, 80))

        self.verticalLayoutApp.addWidget(self.label_4)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayoutApp.addItem(spacer)

        self.scrollAreaApplication.setWidget(self.scrollAreaWidgetContentsApp)
        self.stackedWidget.addWidget(self.pageApplication)
        self.scrollAreaWidgetContentsApp.adjustSize()

        self.pageCarteBancaire = QWidget()
        self.pageCarteBancaire.setObjectName(u"pageCarteBancaire")
        self.frameCarteBancaire = QFrame(self.pageCarteBancaire)
        self.frameCarteBancaire.setObjectName(u"frameCarteBancaire")
        self.frameCarteBancaire.setGeometry(QRect(0, 0, 701, 651))
        self.frameCarteBancaire.setStyleSheet(u"/* Style g\u00e9n\u00e9ral de la frame */\n"
"QFrame {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    border: 2px solid #34495E; /* Bordure fine et \u00e9l\u00e9gante */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")
        self.frameCarteBancaire.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameCarteBancaire.setFrameShadow(QFrame.Shadow.Raised)
        self.frameAddCarteBancaire = QFrame(self.frameCarteBancaire)
        self.frameAddCarteBancaire.setObjectName(u"frameAddCarteBancaire")
        self.frameAddCarteBancaire.setGeometry(QRect(10, 10, 681, 81))
        self.frameAddCarteBancaire.setStyleSheet(u"QFrame {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    border: 2px solid #34495E; /* Bordure fine et \u00e9l\u00e9gante */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")
        self.frameAddCarteBancaire.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAddCarteBancaire.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButtonAddCarteBancaire = QPushButton(self.frameAddCarteBancaire)
        self.pushButtonAddCarteBancaire.setObjectName(u"pushButtonAddCarteBancaire")
        self.pushButtonAddCarteBancaire.setGeometry(QRect(20, 10, 219, 51))
        self.pushButtonAddCarteBancaire.setStyleSheet(u"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les boutons */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"/* Style des labels */\n"
"QLabel {\n"
"    color: #ECF0F1; /* Couleur blanche/gris clair */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    margin-bottom: 10px; /* Espacement sous le label */\n"
"}\n"
"")
        self.scrollAreaCarteBancaire = QScrollArea(self.frameCarteBancaire)
        self.scrollAreaCarteBancaire.setObjectName(u"scrollAreaCarteBancaire")
        self.scrollAreaCarteBancaire.setGeometry(QRect(9, 99, 681, 531))
        self.scrollAreaCarteBancaire.setStyleSheet(u"")
        self.scrollAreaCarteBancaire.setWidgetResizable(True)

        self.scrollAreaWidgetContentsCB = QWidget()
        self.scrollAreaWidgetContentsCB.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContentsCB.setStyleSheet(u"/* Style g\u00e9n\u00e9ral de la frame */\n"
"QWidget {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")

        self.verticalLayoutCarteBancaire = QVBoxLayout(self.scrollAreaWidgetContentsCB)
        self.verticalLayoutCarteBancaire.setObjectName(u"verticalLayoutCarteBancaire")
        self.verticalLayoutCarteBancaire.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayoutCarteBancaire.setContentsMargins(0, 0, 0, 0)

        self.label_5 = QLabel(self.scrollAreaWidgetContentsCB)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 80))
        self.label_5.setMaximumSize(QSize(16777215, 80))

        self.verticalLayoutCarteBancaire.addWidget(self.label_5)

        self.verticalLayoutCarteBancaire.addItem(spacer)

        self.scrollAreaCarteBancaire.setWidget(self.scrollAreaWidgetContentsCB)
        self.stackedWidget.addWidget(self.pageCarteBancaire)
        self.scrollAreaWidgetContentsCB.adjustSize()

        self.pageDocument = QWidget()
        self.pageDocument.setObjectName(u"pageDocument")
        self.frameDocument = QFrame(self.pageDocument)
        self.frameDocument.setObjectName(u"frameDocument")
        self.frameDocument.setGeometry(QRect(0, 0, 701, 651))
        self.frameDocument.setStyleSheet(u"/* Style g\u00e9n\u00e9ral de la frame */\n"
"QFrame {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    border: 2px solid #34495E; /* Bordure fine et \u00e9l\u00e9gante */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")
        self.frameDocument.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameDocument.setFrameShadow(QFrame.Shadow.Raised)
        self.frameAddDocument = QFrame(self.frameDocument)
        self.frameAddDocument.setObjectName(u"frameAddNote")
        self.frameAddDocument.setGeometry(QRect(10, 10, 681, 81))
        self.frameAddDocument.setStyleSheet(u"QFrame {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    border: 2px solid #34495E; /* Bordure fine et \u00e9l\u00e9gante */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")
        self.frameAddDocument.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAddDocument.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButtonAddDocument = QPushButton(self.frameAddDocument)
        self.pushButtonAddDocument.setObjectName(u"pushButtonAddNote")
        self.pushButtonAddDocument.setGeometry(QRect(20, 10, 219, 51))
        self.pushButtonAddDocument.setStyleSheet(u"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les boutons */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"/* Style des labels */\n"
"QLabel {\n"
"    color: #ECF0F1; /* Couleur blanche/gris clair */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    margin-bottom: 10px; /* Espacement sous le label */\n"
"}\n"
"")
        self.scrollAreaDocument = QScrollArea(self.frameDocument)
        self.scrollAreaDocument.setObjectName(u"scrollAreaDocument")
        self.scrollAreaDocument.setGeometry(QRect(9, 99, 681, 531))
        self.scrollAreaDocument.setStyleSheet(u"")
        self.scrollAreaDocument.setWidgetResizable(True)

        self.scrollAreaWidgetContentsDoc = QWidget()
        self.scrollAreaWidgetContentsDoc.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContentsDoc.setStyleSheet(u"/* Style g\u00e9n\u00e9ral de la frame */\n"
"QWidget {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")

        self.verticalLayoutDocument = QVBoxLayout(self.scrollAreaWidgetContentsDoc)
        self.verticalLayoutDocument.setObjectName(u"verticalLayoutDocument")
        self.verticalLayoutDocument.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayoutDocument.setContentsMargins(0, 0, 0, 0)

        self.label_6 = QLabel(self.scrollAreaWidgetContentsDoc)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 80))
        self.label_6.setMaximumSize(QSize(16777215, 80))

        self.verticalLayoutDocument.addWidget(self.label_6)

        self.verticalLayoutDocument.addItem(spacer)

        self.scrollAreaDocument.setWidget(self.scrollAreaWidgetContentsDoc)
        self.stackedWidget.addWidget(self.pageDocument)
        self.scrollAreaWidgetContentsDoc.adjustSize()

        self.pageNote = QWidget()
        self.pageNote.setObjectName(u"pageNote")
        self.frameNote = QFrame(self.pageNote)
        self.frameNote.setObjectName(u"frameNote")
        self.frameNote.setGeometry(QRect(0, 0, 701, 651))
        self.frameNote.setStyleSheet(u"/* Style g\u00e9n\u00e9ral de la frame */\n"
"QFrame {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    border: 2px solid #34495E; /* Bordure fine et \u00e9l\u00e9gante */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")
        self.frameNote.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameNote.setFrameShadow(QFrame.Shadow.Raised)
        self.frameAddNote = QFrame(self.frameNote)
        self.frameAddNote.setObjectName(u"frameAddCarteBancaire_3")
        self.frameAddNote.setGeometry(QRect(10, 10, 681, 81))
        self.frameAddNote.setStyleSheet(u"QFrame {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    border: 2px solid #34495E; /* Bordure fine et \u00e9l\u00e9gante */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")
        self.frameAddNote.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameAddNote.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButtonAddNote = QPushButton(self.frameAddNote)
        self.pushButtonAddNote.setObjectName(u"pushButtonAddCarteBancaire_3")
        self.pushButtonAddNote.setGeometry(QRect(20, 10, 219, 51))
        self.pushButtonAddNote.setStyleSheet(u"QPushButton {\n"
"    background-color: #1ABC9C; /* Couleur verte pour les boutons */\n"
"    color: white; /* Couleur du texte */\n"
"    border: none; /* Pas de bordure */\n"
"    border-radius: 5px; /* Coins l\u00e9g\u00e8rement arrondis */\n"
"    padding: 8px 15px; /* Espacement int\u00e9rieur */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    margin: 5px 0; /* Espacement entre les boutons */\n"
"	height : 25px\n"
"}\n"
"\n"
"/* Effet clic pour les boutons */\n"
"QPushButton:pressed {\n"
"    background-color: #149174; /* Couleur encore plus fonc\u00e9e quand cliqu\u00e9 */\n"
"}\n"
"\n"
"/* Style des labels */\n"
"QLabel {\n"
"    color: #ECF0F1; /* Couleur blanche/gris clair */\n"
"    font-size: 14px; /* Taille de la police */\n"
"    margin-bottom: 10px; /* Espacement sous le label */\n"
"}\n"
"")
        self.scrollAreaNote = QScrollArea(self.frameNote)
        self.scrollAreaNote.setObjectName(u"scrollAreaNote")
        self.scrollAreaNote.setGeometry(QRect(9, 99, 681, 531))
        self.scrollAreaNote.setStyleSheet(u"")
        self.scrollAreaNote.setWidgetResizable(True)

        self.scrollAreaWidgetContentsNote = QWidget()
        self.scrollAreaWidgetContentsNote.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContentsNote.setStyleSheet(u"/* Style g\u00e9n\u00e9ral de la frame */\n"
"QWidget {\n"
"    background-color: #2C3E50; /* Couleur de fond sombre */\n"
"    padding: 10px; /* Espacement int\u00e9rieur */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Ombre l\u00e9g\u00e8re */\n"
"}")

        self.verticalLayoutNote = QVBoxLayout(self.scrollAreaWidgetContentsNote)
        self.verticalLayoutNote.setObjectName(u"verticalLayoutNote")
        self.verticalLayoutNote.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayoutNote.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.scrollAreaWidgetContentsNote)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 80))
        self.label_7.setMaximumSize(QSize(16777215, 80))

        self.verticalLayoutNote.addWidget(self.label_7)

        self.verticalLayoutNote.addItem(spacer)

        self.scrollAreaNote.setWidget(self.scrollAreaWidgetContentsNote)
        self.stackedWidget.addWidget(self.pageNote)
        self.scrollAreaWidgetContentsNote.adjustSize()

        self.StackPage.addWidget(self.pageDashbord)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)

        self.StackPage.setCurrentIndex(0)
        self.stackedWidgetAuthentification.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titreFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Ce coffre-fort num\u00e9rique est v\u00e9rouill\u00e9. Saississez votre mot de passe principal.", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Nom d'utilisateur", None))
        self.usernamelineEdit.setText("")
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.lineEdit_2.setText("")
        self.seConnecterPushButton.setText(QCoreApplication.translate("MainWindow", u"Se connecter", None))
        self.sinscrirelabel.setText(QCoreApplication.translate("MainWindow", u"Vous n'avez pas de compte ? inscrivez vous", None))
        self.seconnecterlabel.setText(QCoreApplication.translate("MainWindow", u"Vous avez déjà un compte ? se connecter", None))
        self.titreFrameCompte.setText(QCoreApplication.translate("MainWindow", u"Bienvenu, s\u00e9curis\u00e9 vos informations confidentielles. Inscrivez vous.", None))
        self.labelNom.setText(QCoreApplication.translate("MainWindow", u"Nom ", None))
        self.lineEditNom.setText("")
        self.labelPrenom.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom", None))
        self.lineEditPrenom.setText("")
        self.labelEmail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEditEmail.setText("")
        self.labelNum.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro de t\u00e9l\u00e9phone", None))
        self.lineEditNum.setText("")
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.lineEditPassword.setText("")
        self.pushButtonSinscrire.setText(QCoreApplication.translate("MainWindow", u"S'inscrire", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Application", None))
        self.pushButtonCB.setText(QCoreApplication.translate("MainWindow", u"Cartes bancaires", None))
        self.pushButtonDoc.setText(QCoreApplication.translate("MainWindow", u"Documents", None))
        self.pushButtonNote.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.pushButtonGenPass.setText(QCoreApplication.translate("MainWindow", u"G\u00e9n\u00e9rer un mot de passe", None))
        self.pushButtonDeconnexion.setText(QCoreApplication.translate("MainWindow", u"Deconnexion", None))
        self.labelCompte.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bonjours Ad\u00e8le", None))
        self.pushButtonAddapplication.setText(QCoreApplication.translate("MainWindow", u"Ajouter une application", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Netflix.com", None))
        self.pushButtonAddCarteBancaire.setText(QCoreApplication.translate("MainWindow", u"Ajouter une carte bancaire", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Carte visa 1", None))
        self.pushButtonAddDocument.setText(QCoreApplication.translate("MainWindow", u"Ajouter un document", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Document1", None))
        self.pushButtonAddNote.setText(QCoreApplication.translate("MainWindow", u"Ajouter une note", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Note1", None))
    # retranslateUi

    def lauchPageInscription(self):
        self.stackedWidgetAuthentification.setCurrentIndex(1)

    def lauchPageConnexion(self):
        self.stackedWidgetAuthentification.setCurrentIndex(0)

    def lauchDashboardApp(self):
        self.stackedWidget.setCurrentIndex(0)

    def lauchDashboardCB(self):
        self.stackedWidget.setCurrentIndex(1)

    def lauchDashboardDoc(self):
        self.stackedWidget.setCurrentIndex(2)

    def lauchDashboardNote(self):
        self.stackedWidget.setCurrentIndex(3)

    def lauchDashboard(self):
        self.StackPage.setCurrentIndex(1)

    def lauchConnexion(self):
        self.StackPage.setCurrentIndex(0)
        self.stackedWidgetAuthentification.setCurrentIndex(0)

    def lauchDialogAddApp(self):
        self.dialog = Ui_DialogAjoutApp(self.verticalLayoutApp)

    def lauchDialogModApp(self,id_,nomApp,password):
        self.dialog = Ui_DialogModApp(id_,nomApp,password)

    def lauchDialogAddCB(self):
        self.dialog = Ui_DialogAjoutCB(self.verticalLayoutCarteBancaire)

    def lauchDialogModCB(self,id_,titulaire,num,cvv,date):
        self.dialog = Ui_DialogModCB(id_,cvv,date,titulaire,num)

    def lauchDialogAddDoc(self):
        self.dialog = Ui_DialogAjoutDoc()

    def lauchDialogModDoc(self):
        self.dialog = Ui_DialogModDoc()

    def lauchDialogAddNote(self):
        self.dialog = Ui_DialogAjoutNot(self.verticalLayoutNote)

    def lauchDialogModNote(self,id_,text):
        self.dialog = Ui_DialogModNote(id_,text)

    def lauchDialogModCompte(self,id_,nom,prenoms,email,num,password):
        self.dialog = Ui_DialogModCompte(id_,nom,prenoms,email,num,password)

    def lauchDialogSucces(self):
        self.dialog = Ui_DialogSucces()

    def lauchDialogFailed(self):
        self.dialog = Ui_DialogFailed()

    def lauchDialogGenPass(self):
        self.dialog = Ui_DialogGenPassword()

    def branchementSlots(self):
        self.seConnecterPushButton.clicked.connect(self.lauchDashboard)
        self.pushButtonDeconnexion.clicked.connect(self.lauchConnexion)

        self.pushButton.clicked.connect(self.lauchDashboardApp)
        self.pushButtonCB.clicked.connect(self.lauchDashboardCB)
        self.pushButtonNote.clicked.connect(self.lauchDashboardNote)
        self.pushButtonDoc.clicked.connect(self.lauchDashboardDoc)
        self.sinscrirelabel.clicked.connect(self.lauchPageInscription)
        self.seconnecterlabel.clicked.connect(self.lauchConnexion)

        self.pushButtonAddapplication.clicked.connect(self.lauchDialogAddApp)
        self.pushButtonAddCarteBancaire.clicked.connect(self.lauchDialogAddCB)
        self.pushButtonAddDocument.clicked.connect(self.lauchDialogAddDoc)
        self.pushButtonAddNote.clicked.connect(self.lauchDialogAddNote)
        self.pushButtonGenPass.clicked.connect(self.lauchDialogGenPass)

        self.labelCompte.clicked.connect(partial(self.lauchDialogModCompte,self.id_,self.nom,self.prenoms,self.email,self.num,self.password))

    def loadMyPasswordApp(self, vbox:QVBoxLayout):
        dataApp = ["b","o","n","j","o","u","r"]
        for data in dataApp:
            objet = dataAppPass(1,data,"bonjour")
            objet.clicked.connect(partial(self.lauchDialogModApp,objet.id_,objet.nomAppOrSite,objet.password))
            vbox.insertWidget(vbox.count()-1,objet)

    def loadDataCBs(self, vbox:QVBoxLayout):
        dataApp = ["b","o","n","j","o","u","r"]
        for data in dataApp:
            objet = dataCB(1,data,"Numéro de carte: " + "1558489489498489","012","27/08/2025")
            objet.clicked.connect(partial(self.lauchDialogModCB,objet.id_,objet.cbTitulaire,objet.numCB,objet.cvvCB,objet.dateCB))
            vbox.insertWidget(vbox.count()-1,objet)

    def loadDataNotes(self, vbox:QVBoxLayout):
        dataApp = ["b","o","n","j","o","u","r"]
        for data in dataApp:
            objet = dataNotePass(1,"bonjour")
            objet.clicked.connect(partial(self.lauchDialogModNote,objet.id_,objet.noteText))
            vbox.insertWidget(vbox.count()-1,objet)

    def loadMDataDoc(self, vbox:QVBoxLayout):
        dataApp = ["b","o","n","j","o","u","r"]
        for data in dataApp:
            objet = dataAppPass(1,data,"bonjour")
            objet.clicked.connect(partial(self.lauchDialogModDoc,objet.id_,objet.nomAppOrSite,objet.password))
            vbox.insertWidget(vbox.count()-1,objet)

    def loadDataCompte(self):
        self.id_ = "1"
        self.nom = "Coulibaly"
        self.prenoms = "Adèle"
        self.email = "adele.coulibaly@inphb.ci"
        self.password = "********"
        self.num = "0758058585"


    def loadData(self):
        self.loadMyPasswordApp(self.verticalLayoutApp)
        self.loadDataCBs(self.verticalLayoutCarteBancaire)
        self.loadDataNotes(self.verticalLayoutNote)
        self.loadDataCompte()

class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, parent=None, titre=None):
        super().__init__(parent)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        if titre :
            self.setText(titre)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

