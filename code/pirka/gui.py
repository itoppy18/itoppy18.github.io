#!/usr/bin/python3
#coding:utf-8
#kanto kor pirka nociw AI system ver.1.0.0.0 source code
#made by @itoppy18

import sys
import data
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, qApp, QApplication, QLabel, QHBoxLayout, QFrame, QSplitter, QStyleFactory

class Pirka(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		newAction = QAction("新規作成", self)
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
		fileMenu = menubar.addMenu("ファイル")
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
		log = QLabel(self)
		log.move(0,0)
		avatar = QLabel(self)
		avatar.move(400, 0)
		#avatar.setPixmap(QPixmap("itoppy.png"))
		graph = QLabel(self)
		graph.move(400, 250)
		"""
		hbox = QHBoxLayout(self)
		topleft = QFrame(self)
		topleft.setFrameShape(QFrame.StyledPanel)
		topright = QFrame(self)
		topright.setFrameShape(QFrame.StyledPanel)
		bottom = QFrame(self)
		bottom.setFrameShape(QFrame.StyledPanel)
		splitter1 = QSplitter(Qt.Horizontal)
		splitter1.addWidget(topleft)
		splitter1.addWidget(topright)
		splitter2 = QSplitter(Qt.Vertical)
		splitter2.addWidget(splitter1)
		splitter2.addWidget(bottom)
		hbox.addWidget(splitter2)
		self.setLayout(hbox)
		pixmap = QPixmap("itoppy.png")
		hbox.addWidget()
		self.setLayout(hbox)
		"""
		self.setGeometry(100, 100, 800, 500)
		self.setMaximumHeight(500)
		self.setMaximumWidth(800)
		self.setMinimumHeight(500)
		self.setMinimumWidth(800)
		self.setWindowTitle(data.Pirka.version)
		self.setWindowIcon(QIcon("itoppy.png"))        
		self.show()

app = QApplication(sys.argv)
ex = Pirka()
sys.exit(app.exec_())
