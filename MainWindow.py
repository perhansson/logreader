#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 08:11:52 2018

Main GUI window for browsing log files. 

@author: phansson
"""

import os
import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 


class MainWindow(QMainWindow):

    # data directory
    __datadir = os.environ['PWD']

    def __init__(self, parent=None, debug=False):
        QMainWindow.__init__(self, parent)

        self.setWindowTitle("Logfile reader")

        self.debug = debug

        # GUI stuff        
        self.create_menu()
        self.create_main_frame()
        #self.create_status_bar()



    def print(str):
        print("[MainWindow]: " + str)
    

    def create_main_frame(self):
        """This is the main widget."""

        self.main_frame = QWidget()

        # main vertical layot
        vbox = QVBoxLayout()

        # add stat box
        #self.create_stat_view(vbox)

        # add control
        #hbox_cntrl = QHBoxLayout()
        #self.acq_button_start = QPushButton("Start")
        #self.connect(self.acq_button_start, SIGNAL('clicked()'), self.on_acq_start)
        #hbox_cntrl.addWidget( self.acq_button_start)
        #self.acq_button_stop = QPushButton("Stop")
        #self.connect(self.acq_button_stop, SIGNAL('clicked()'), self.on_acq_stop)
        #hbox_cntrl.addWidget( self.acq_button_stop)
        #vbox.addLayout( hbox_cntrl )

        # add options
        #self.create_options_view(vbox)

        #self.create_ai_view(vbox)

        #self.create_ao_view(vbox)

        #self.create_do_view(vbox)

        self.create_script_view(vbox)

        
        # add plots
        #self.create_plots_view(vbox)

        hbox_quit = QHBoxLayout()
        self.quit_button = QPushButton("&Quit")
        self.quit_button.clicked.connect(self.on_quit)
        hbox_quit.addStretch(2)
        hbox_quit.addWidget( self.quit_button)                                    
        vbox.addLayout( hbox_quit )

        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)



    def create_menu(self):

        self.file_menu = self.menuBar().addMenu("&File")

        load_file_action = self.create_action("&Save plot",
                                              shortcut="Ctrl+S", slot=self.save_plot, 
                                              tip="Save the plot")

        quit_action = self.create_action("&Quit",
                                         shortcut="Ctrl+Q", slot=self.close, 
                                         tip="Close the application")

        #self.add_actions(self.file_menu, 
        #    (load_file_action, None, quit_action))

        self.add_actions(self.file_menu, (quit_action,load_file_action))

        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About", 
                                          shortcut='F1', slot=self.on_about, 
                                          tip='About this thing')

        self.add_actions(self.help_menu, (about_action,))




    def on_about(self):
        msg = """ Log file reader GUI."""
        QMessageBox.about(self, "About the app", msg.strip())


    def save_plot(self):
        file_choices = "PNG (*.png)|*.png"
        
        path = unicode(QFileDialog.getSaveFileName(self, 
                        'Save file', '', 
                        file_choices))
        if path:
            self.canvas.print_figure(path, dpi=self.dpi)
            self.statusBar().showMessage('Saved to %s' % path, 2000)



    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(  self, text, slot=None, shortcut=None, 
                        icon=None, tip=None, checkable=False, 
                        signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action



    def on_op(self):
        """Attempt to find operating point."""
        # reset QGSET
        logthread('on_op')

    def on_op_quit(self):
        """Attempt to find operating point."""
        # reset QGSET
        logthread('on_op_quit')

    def create_script_view(self, vbox):
        """Creates digital output boxes and buttons."""
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(QLabel('Scripts'))
        hbox_1.addStretch(2)
        vbox.addLayout(hbox_1)

        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(QLabel('Find O.P.'))
        self.op_button = QPushButton("&Find OP")
        self.op_button.clicked.connect(self.on_op)
        hbox_2.addWidget( self.op_button)                                    
        self.op_button_quit = QPushButton("&Quit OP")
        self.op_button_quit.clicked.connect(self.on_op_quit)
        hbox_2.addWidget( self.op_button_quit)                                    
        vbox.addLayout( hbox_2 )

        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(QLabel('Record raw file'))
        self.rec_button = QPushButton("&Start")
        #self.rec_button.clicked.connect(self.on_record)
        hbox_3.addWidget( self.rec_button)                                    
        self.rec_button_quit = QPushButton("&Stop")
        #self.rec_button_quit.clicked.connect(self.on_record_quit)
        hbox_3.addWidget( self.rec_button_quit)                                    
        vbox.addLayout( hbox_3 )

        hbox_dark = QHBoxLayout()
        textbox_dark_file_label = QLabel('Filename:')
        self.textbox_dark_file = QLineEdit()
        self.textbox_dark_file.setMinimumWidth(200)
        self.connect(self.textbox_dark_file, SIGNAL('editingFinished ()'), self.on_dark_file_select)
        self.b_open_dark = QPushButton(self)
        self.b_open_dark.setText('Select file')
        self.b_open_dark.clicked.connect(self.showDarkFileDialog)
        hbox_dark.addWidget(textbox_dark_file_label)
        hbox_dark.addWidget(self.b_open_dark)
        hbox_dark.addWidget(self.textbox_dark_file)
        hbox_dark.addStretch(1)
        vbox.addLayout(hbox_dark)
        


    def showDarkFileDialog(self):
        """Open file dialog to select a file."""
        # select via dialog
        file_name = QFileDialog.getOpenFileName(self,'Open file',self.__datadir)

        # set the textbox
        self.textbox_dark_file.setText(file_name)

        # use the "button" click function to actually apply
        self.on_dark_file_select()
    
        

    def on_dark_file_select(self):
        #if self.debug: 
        self.print('[MainWindow]:  on_dark_file_select')
        t = self.textbox_dark_file.text()
        if t == '':
            self.print('[MainWindow]:  no dark file selected')
            #t = self.fileWriter.filename
        #self.fileWriter.set_filename(str(t))

    def on_quit(self):
        """Quit the main window."""
        print('[MainWindow]: on_quit')        
        print('[MainWindow]: kill thread')        
        self.emit(SIGNAL('quit'))
        #for w in self.plot_widgets:
        #    w.close()
        self.close()
