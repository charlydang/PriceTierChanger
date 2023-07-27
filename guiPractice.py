from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont, QIcon
from PyQt5.QtCore import Qt, pyqtSlot, QSize
from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QCheckBox, QPushButton, QHBoxLayout, QApplication, QStatusBar
import configparser
import sys
import os

#Global Variables
config = configparser.ConfigParser()
config.read("config.ini")



class lineEditDemo(QWidget):
        
        def __init__(self,parent=None):
                super().__init__(parent)

                
                         
                self.e3 = QLineEdit()
                self.e3.setValidator(QIntValidator())
                self.e3.setMaxLength(4)
                #self.e3.setText(config['SectionOne']['itemnumber'])

                self.e2 = QLineEdit()
                self.e2.setEchoMode(QLineEdit.Password)

                self.e1 = QLineEdit()
                #self.e1.setText(config['SectionOne']['UserName'])

                self.tier1 = QLineEdit()
                #self.tier1.setText(config['Prices']['price1'])

                self.tier2 = QLineEdit()
                #self.tier2.setText(config['Prices']['price2'])

                self.tier3 = QLineEdit()
                #self.tier3.setText(config['Prices']['price3'])

                self.tier4 = QLineEdit()
                #self.tier4.setText(config['Prices']['price4'])

                self.tier5 = QLineEdit()
                #self.tier5.setText(config['Prices']['price5'])

                self.tier6 = QLineEdit()
                #self.tier6.setText(config['Prices']['price6'])

                self.tier7 = QLineEdit()
                #self.tier7.setText(config['Prices']['price7'])

                self.tier8 = QLineEdit()
                #self.tier8.setText(config['Prices']['price8'])

                self.tier9 = QLineEdit()
                #self.tier9.setText(config['Prices']['price9'])

                #Add the Layouts to the Gui        
                flo = QFormLayout()
                flo.addRow("Username",self.e1)
                flo.addRow("Password",self.e2)
                flo.addRow("ItemNumber",self.e3)


                widget = QWidget()
                removeButton = QPushButton(widget)
                removeButton.setText("Remove Price Tiers")
                removeButton.clicked.connect(self.on_click_remove)
                flo.addRow(removeButton)

                checkBoxButton = QPushButton(widget)
                checkBoxButton.setText("Location CheckBoxes")
                checkBoxButton.clicked.connect(self.on_click_checkbox)
                flo.addRow(checkBoxButton)
                
                #Price Tier 1
                layout1 = QHBoxLayout()
                self.priceTier1Checkbox = QCheckBox()
                Tier1CheckboxLabel = QLabel("Edit?")
                Tier1FieldLabel = QLabel("Tier 1:")
                layout1.addWidget(Tier1FieldLabel)
                layout1.addWidget(self.tier1)
                layout1.addWidget(Tier1CheckboxLabel)
                layout1.addWidget(self.priceTier1Checkbox)
                
                priceTier1Line = QWidget()
                priceTier1Line.setLayout(layout1)
                flo.addRow(priceTier1Line)

                #Price Tier 2
                layout2 = QHBoxLayout()
                self.priceTier2Checkbox = QCheckBox()
                Tier2CheckboxLabel = QLabel("Edit?")
                Tier2FieldLabel = QLabel("Tier 2:")
                layout2.addWidget(Tier2FieldLabel)
                layout2.addWidget(self.tier2)
                layout2.addWidget(Tier2CheckboxLabel)
                layout2.addWidget(self.priceTier2Checkbox)
                
                priceTier2Line = QWidget()
                priceTier2Line.setLayout(layout2)
                flo.addRow(priceTier2Line)

                #Price Tier 3
                layout3 = QHBoxLayout()
                self.priceTier3Checkbox = QCheckBox()
                Tier3CheckboxLabel = QLabel("Edit?")
                Tier3FieldLabel = QLabel("Tier 3:")
                layout3.addWidget(Tier3FieldLabel)
                layout3.addWidget(self.tier3)
                layout3.addWidget(Tier3CheckboxLabel)
                layout3.addWidget(self.priceTier3Checkbox)

                priceTier3Line = QWidget()
                priceTier3Line.setLayout(layout3)
                flo.addRow(priceTier3Line)

                #Price Tier 4
                layout4 = QHBoxLayout()
                self.priceTier4Checkbox = QCheckBox()
                Tier4CheckboxLabel = QLabel("Edit?")
                Tier4FieldLabel = QLabel("Tier 4:")
                layout4.addWidget(Tier4FieldLabel)
                layout4.addWidget(self.tier4)
                layout4.addWidget(Tier4CheckboxLabel)
                layout4.addWidget(self.priceTier4Checkbox)
                
                priceTier4Line = QWidget()
                priceTier4Line.setLayout(layout4)
                flo.addRow(priceTier4Line)

                #Price Tier 5
                layout5 = QHBoxLayout()
                self.priceTier5Checkbox = QCheckBox()
                Tier5CheckboxLabel = QLabel("Edit?")
                Tier5FieldLabel = QLabel("Tier 5:")
                layout5.addWidget(Tier5FieldLabel)
                layout5.addWidget(self.tier5)
                layout5.addWidget(Tier5CheckboxLabel)
                layout5.addWidget(self.priceTier5Checkbox)
                
                priceTier5Line = QWidget()
                priceTier5Line.setLayout(layout5)
                flo.addRow(priceTier5Line)                

                #Price Tier 6
                layout6 = QHBoxLayout()
                self.priceTier6Checkbox = QCheckBox()
                Tier6CheckboxLabel = QLabel("Edit?")
                Tier6FieldLabel = QLabel("Tier 6:")
                layout6.addWidget(Tier6FieldLabel)
                layout6.addWidget(self.tier6)
                layout6.addWidget(Tier6CheckboxLabel)
                layout6.addWidget(self.priceTier6Checkbox)
                
                priceTier6Line = QWidget()
                priceTier6Line.setLayout(layout6)
                flo.addRow(priceTier6Line)

                #Price Tier 7
                layout7 = QHBoxLayout()
                self.priceTier7Checkbox = QCheckBox()
                Tier7CheckboxLabel = QLabel("Edit?")
                Tier7FieldLabel = QLabel("Tier 7:")
                layout7.addWidget(Tier7FieldLabel)
                layout7.addWidget(self.tier7)
                layout7.addWidget(Tier7CheckboxLabel)
                layout7.addWidget(self.priceTier7Checkbox)
                
                priceTier7Line = QWidget()
                priceTier7Line.setLayout(layout7)
                flo.addRow(priceTier7Line)

                #Price Tier 8
                layout8 = QHBoxLayout()
                self.priceTier8Checkbox = QCheckBox()
                Tier8CheckboxLabel = QLabel("Edit?")
                Tier8FieldLabel = QLabel("Tier 8:")
                layout8.addWidget(Tier8FieldLabel)
                layout8.addWidget(self.tier8)
                layout8.addWidget(Tier8CheckboxLabel)
                layout8.addWidget(self.priceTier8Checkbox)
                
                priceTier8Line = QWidget()
                priceTier8Line.setLayout(layout8)
                flo.addRow(priceTier8Line)

                #Price Tier 9
                layout9 = QHBoxLayout()
                self.priceTier9Checkbox = QCheckBox()
                Tier9CheckboxLabel = QLabel("Edit?")
                Tier9FieldLabel = QLabel("Tier 9:")
                layout9.addWidget(Tier9FieldLabel)
                layout9.addWidget(self.tier9)
                layout9.addWidget(Tier9CheckboxLabel)
                layout9.addWidget(self.priceTier9Checkbox)
                
                priceTier9Line = QWidget()
                priceTier9Line.setLayout(layout9)
                flo.addRow(priceTier9Line)             

                priceTierChanger = QPushButton(widget)
                priceTierChanger.setText("Change Price Tiers")
                priceTierChanger.clicked.connect(self.on_price_changer)
                flo.addRow(priceTierChanger)

                self.atrributeID = QLineEdit()
                self.atrributeID.setText(config['SectionOne']['AttributeID'])
                flo.addRow("Attribute ID", self.atrributeID)

                self.sideItemNumber = QLineEdit()
                self.sideItemNumber.setText(config['SectionOne']['sideitemnumber'])
                flo.addRow("Side Item Number", self.sideItemNumber)

                sidePricing = QPushButton(widget)
                sidePricing.setText("Change Side Priceing")
                sidePricing.clicked.connect(self.on_side_price_changer)
                flo.addRow(sidePricing)

                self.statusBar = QStatusBar()  
                flo.addRow(self.statusBar)

                self.setLayout(flo)
                self.setWindowTitle("Price Changer!")




        def on_price_changer(self):
                if not self.e2.text() == "":
                        config['SectionOne']['UserName'] = self.e1.text()
                        config['SectionOne']['Password'] = self.e2.text()
                        config['Prices']['price1'] = self.tier1.text()
                        config['Prices']['price2'] = self.tier2.text()
                        config['Prices']['price3'] = self.tier3.text()
                        config['Prices']['price4'] = self.tier4.text()
                        config['Prices']['price5'] = self.tier5.text()
                        config['Prices']['price6'] = self.tier6.text()
                        config['Prices']['price7'] = self.tier7.text()
                        config['Prices']['price8'] = self.tier8.text()
                        config['Prices']['price9'] = self.tier9.text()

                        if self.priceTier1Checkbox.isChecked():
                                config['EditTiers']['tier1'] = "true"
                        else:
                                config['EditTiers']['tier1'] = "false"
                        if self.priceTier2Checkbox.isChecked():
                                config['EditTiers']['tier2'] = "true"
                        else:
                                config['EditTiers']['tier2'] = "false"
                        if self.priceTier3Checkbox.isChecked():
                                config['EditTiers']['tier3'] = "true"
                        else:
                                config['EditTiers']['tier3'] = "false"
                        if self.priceTier4Checkbox.isChecked():
                                config['EditTiers']['tier4'] = "true"
                        else:
                                config['EditTiers']['tier4'] = "false"
                        if self.priceTier5Checkbox.isChecked():
                                config['EditTiers']['tier5'] = "true"
                        else:
                                config['EditTiers']['tier5'] = "false"
                        if self.priceTier6Checkbox.isChecked():
                                config['EditTiers']['tier6'] = "true"
                        else:
                                config['EditTiers']['tier6'] = "false"
                        if self.priceTier7Checkbox.isChecked():
                                config['EditTiers']['tier7'] = "true"
                        else:
                                config['EditTiers']['tier7'] = "false"
                        if self.priceTier8Checkbox.isChecked():
                                config['EditTiers']['tier8'] = "true"
                        else:
                                config['EditTiers']['tier8'] = "false"
                        if self.priceTier9Checkbox.isChecked():
                                config['EditTiers']['tier9'] = "true"
                        else:
                                config['EditTiers']['tier9'] = "false"

                        with open('config.ini', 'w') as configfile:    # save
                            config.write(configfile)
                        os.system('python EditPriceTierMain.py')
                else:
                       print("You did not enter your password!")

        def on_side_price_changer(self):
                if not self.e2.text() == "":
                        config['SectionOne']['UserName'] = self.e1.text()
                        config['SectionOne']['Password'] = self.e2.text()
                        config['SectionOne']['attributeID'] = self.atrributeID
                        config['SectionOne']['SideItemNumber'] = self.sideItemNumber 
                        with open('config.ini', 'w') as configfile:    # save
                                config.write(configfile)
                        os.system('python EditSidePricing.py')

        def on_click_remove(self):
                if not self.e2.text() == "":
                        config['SectionOne']['UserName'] = self.e1.text()
                        config['SectionOne']['Password'] = self.e2.text()
                        with open('config.ini', 'w') as configfile:    # save
                                config.write(configfile)
                        os.system('python PriceTierRemover.py')

                

        def on_click_checkbox(self):
                if not self.e2.text() == "":
                        config['SectionOne']['UserName'] = self.e1.text()
                        config['SectionOne']['Password'] = self.e2.text()
                        with open('config.ini', 'w') as configfile:    # save
                                config.write(configfile)        
                        os.system('python LocationCheckbox.py')

       

if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = lineEditDemo()
        

        win.show()
        sys.exit(app.exec_())