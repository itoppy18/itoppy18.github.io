#!/usr/bin/python3
#coding:utf-8
#kanto kor pirka nociw AI system ver.1.0.0.0 "polaris" source code
#gui.py:GUIを生成
#made by @itoppy18

import sys
import data
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QTextEdit, QGridLayout, QAction, qApp, QApplication, QLabel, QHBoxLayout, QFrame, QSplitter, QStyleFactory

class Pirka(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		hbox = QHBoxLayout(self)
		pixmap = QPixmap("background.png")
		lb1 = QLabel(self)
		lb1.setPixmap(pixmap)
		hbox.addWidget(lb1)
		self.setLayout(hbox)
		self.move(0, 0)
		newAction = QAction("新規作成", self)	#アクションを作る
		newAction.setShortcut("Ctrl+N")
		#newAction.triggered.connect(pass)
		saveAction = QAction("保存", self)
		saveAction.setShortcut("Ctrl+S")
		#saveAction.triggered.connect(pass)
		exitAction = QAction("終了", self)
		exitAction.setShortcut("Ctrl+Q")
		exitAction.triggered.connect(qApp.quit)
		self.statusBar()
		menubar = self.menuBar()
		fileMenu = menubar.addMenu("ファイル")	#メニューを作る
		fileMenu.addAction(newAction)
		fileMenu.addAction(exitAction)
		configAction = QAction("設定",self)
		configAction.setShortcut("Ctrl+C")
		#importAction.triggered.connect(pass)
		importAction = QAction("設定の読み込み", self)
		importAction.setShortcut("Ctrl+I")
		#configAction.triggered.connect(pass)
		configMenu = menubar.addMenu("設定")
		configMenu.addAction(configAction)
		configMenu.addAction(importAction)
		debugAction = QAction("デバッグモード", self)
		debugAction.setShortcut("Ctrl+Alt+D")
		#debugAction.triggered.connect(pass)
		cuiAction = QAction("CUIモード", self)
		cuiAction.setShortcut("Ctrl+Alt+C")
		#cuiAction.triggered.connect(pass)
		objectAction = QAction("オブジェクト一覧", self)
		objectAction.setShortcut("Ctrl+Alt+O")
		#objectAction.triggered.connect(pass)
		hackerMenu = menubar.addMenu("開発者ツール")
		hackerMenu.addAction(debugAction)
		hackerMenu.addAction(cuiAction)
		hackerMenu.addAction(objectAction)
		helpAction = QAction("ヘルプ", self)
		helpAction.setShortcut("Ctrl+H")
		#helpAction.triggered.connect()
		refarenceAction = QAction("リファレンス", self)
		refarenceAction.setShortcut("Ctrl+R")
		#refarenceAction.triggered.connect()
		helpMenu  = menubar.addMenu("ヘルプ")
		helpMenu.addAction(helpAction)
		helpMenu.addAction(refarenceAction)
		self.setGeometry(100, 100, 800, 500)
		self.setMaximumHeight(500)
		self.setMaximumWidth(800)
		self.setMinimumHeight(500)
		self.setMinimumWidth(800)
		self.setWindowTitle(data.Data.version)
		self.setWindowIcon(QIcon("itoppy.png"))        
		self.show()

app = QApplication(sys.argv)
ex = Pirka()
sys.exit(app.exec_())
