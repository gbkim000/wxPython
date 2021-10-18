# %% wxPython Grid
# 패키지설치 : pip install -U wxPython
# 참고사이트 : https://wxpython.org/pages/presentations/
# 참고사이트 : https://zetcode.com/wxpython/

# [Programming Examples]
# https://codeloop.org/python-gui-creating-tables-in-wxpython/
import wx
import wx.grid as grid

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title =title, size = (800,600))
 
        self.panel = MyPanel(self)
 
class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
 
        mygrid = grid.Grid(self)
        mygrid.CreateGrid( 26, 9)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(mygrid, 1, wx.EXPAND)
        self.SetSizer(sizer)
 
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Grid In WxPython")
        self.frame.Show()
        return True
# 방법(1)
app = MyApp()
app.MainLoop()

# 방법(2)       
# app = wx.PySimpleApp()
# frame = MyFrame(parent=None, title="Grid In WxPython")
# frame.Show()
# app.MainLoop()

# %% Python Customizing Grid Or TablePython
# https://codeloop.org/python-gui-customizing-table-in-wxpython/

import wx
import wx.grid as grid

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title =title, size = (800,600))
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        mygrid = grid.Grid(self)
        mygrid.CreateGrid(26,9)

        mygrid.SetCellValue(1,1, "Hello")
        mygrid.SetCellFont(1,1, wx.Font(15, wx.ROMAN, wx.ITALIC, wx.NORMAL))


        mygrid.SetCellValue(5,5,"Green Color")
        mygrid.SetCellBackgroundColour(5,5, wx.RED)
        mygrid.SetCellTextColour(5,5,wx.WHITE)


        mygrid.SetCellValue(8,3, "Read Only")
        mygrid.SetReadOnly(8,3,True)

        mygrid.SetCellEditor(6, 0, grid.GridCellNumberEditor(1, 20))
        mygrid.SetCellValue(6, 0, "2")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(mygrid, 1, wx.EXPAND)
        self.SetSizer(sizer)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Grid Or Tables Part Two")
        self.frame.Show()
        return True

app = MyApp()
app.MainLoop()

# %% wxPython
# https://codingshiksha.com/python/python-3-wxpython-accelerator-table-control-widget-using-gridsizer-layout-in-gui-desktop-app-full-project-for-beginners/

import wx
import wx.grid

class TestFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, title="Grid Attributes", size=(600,300))
        grid = wx.grid.Grid(self)
        grid.CreateGrid(10,6)
        for row in range(10):
            for col in range(6):
                grid.SetCellValue(row, col, "(%s,%s)" % (row, col))
         
        grid.SetCellTextColour(1, 1, "red")
        grid.SetCellFont(1,1, wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        grid.SetCellBackgroundColour(2, 2, "light blue")
        
        attr = wx.grid.GridCellAttr()
        attr.SetTextColour("navyblue")
        attr.SetBackgroundColour("pink")
        attr.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

        grid.SetAttr(4, 0, attr)
        grid.SetAttr(5, 1, attr)
        grid.SetRowAttr(8, attr)


app = wx.PySimpleApp()
frame = TestFrame()
frame.Show()
app.MainLoop()

# %% wxPython Grid
# https://stackoverflow.com/questions/53461038/wxpython-gridtable-how-to-update
# 이 프로그램은 모듈이 없어서 인지 실행되지 않음

import wx
import wx.grid as gridlib
# from YahooDij import Dij_history (모듈 설치 못함)
import pandas as pd
import matplotlib.pyplot as plt
import os

class MyDataTable(gridlib.GridTableBase):
    def __init__(self, data=None):
        gridlib.GridTableBase.__init__(self)
        self.headerRows = 0
        if data is None:
            data = pd.DataFrame()

        self.data = data

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data.columns) + 1

    def GetValue(self, row, col):
        if col == 0:
            return self.data.index[row]
        return self.data.iloc[row, col-1]

    def SetValue(self, row, col, value):
        pass


    def GetColLabelValue(self, col):
        if col == 0:
            return 'Index' if self.data.index.name is None else self.data.index.name

        return self.data.columns[col-1]

    def GetTypeName(self, row, col):
        return wx.grid.GRID_VALUE_STRING

    def GetAttr(self, row, col, prop):
        attr = gridlib.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour("#CCE6FF")
        return attr

class MyFrame(wx.Frame):
    """Frame class that display data"""
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (1000,2000))

        self.InitUI()

    def InitUI(self):

        # PANEL
        self.panel = wx.Panel(self, -1) # set id = -1
        self.panel.SetBackgroundColour('White')

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()

        openMenuItem = menu1.Append(wx.ID_OPEN, '&Open', 'Open a file in a dialog')
        menu1.AppendSeparator() # add a separator
        closeMenuItem = menu1.Append(wx.ID_EXIT, '&Quit', 'Close the dialog')
        menuBar.Append(menu1, '&File')
        self.SetMenuBar(menuBar)

        # input widgets
        label_text = wx.StaticText(self.panel, -1, 'Company Code:', pos=(0, 5))
        self.text_enter = wx.TextCtrl(self.panel, -1, "", pos=(110, 1), style=wx.TE_PROCESS_TAB | wx.TE_CENTER | wx.TE_PROCESS_ENTER)
        self.checkBox1 = wx.CheckBox(self.panel, -1, "Open Price", (0,50))
        self.checkBox2 = wx.CheckBox(self.panel, -1, "Highest Price", (100,50))
        self.checkBox3 = wx.CheckBox(self.panel, -1, "Lowest Price", (220,50))
        self.checkBox4 = wx.CheckBox(self.panel, -1, "Close Price", (340,50))
        self.checkBox5 = wx.CheckBox(self.panel, -1, "Volume", (450,50))
        plot_button = wx.Button(self.panel, -1, "Plot", pos=(550, 50))

        self.Bind(wx.EVT_MENU, self.onOpen, openMenuItem)
        self.Bind(wx.EVT_MENU, self.onClose, closeMenuItem)
        self.Bind(wx.EVT_TEXT_ENTER, self.onEnter, self.text_enter)
        #self.Bind(wx.EVT_BUTTON, self.onClick, plot_button)

    def onOpen(self, event):
        filepath = None
        openFileDialog = wx.FileDialog(self, "Open CSV File", "", "", "csv files(*.csv) |*.csv", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        filepath = openFileDialog.GetPath() # path
        #make a grid table
        panel2 = wx.Panel(self.panel, id=2, pos=(0, 100), size = (800, 500))
        self.df = pd.read_csv(filepath, header=0)
        self.table = MyDataTable(self.df)
        grid = gridlib.Grid(self, 2, pos=(0, 100), size=(self.table.GetNumberRows(), self.table.GetNumberCols()))
        grid.SetRowLabelSize(0)
        grid.SetColLabelSize(30)
        grid.SetTable(self.table)
        grid.AutoSize()
        grid.AutoSizeColumns(True)

        openFileDialog.Destroy()

    def onClose(self, event):
        self.Destroy()
        
    def onEnter(self, event):
        df2 = self.df[self.df['Codes'] == self.text_enter]
        self.table = MyDataTable(df2)
        grid = gridlib.Grid(self, 2, pos=(0, 100), size=(self.table.GetNumberRows(), self.table.GetNumberCols()))
        grid.SetRowLabelSize(0)
        grid.SetColLabelSize(30)
        grid.SetTable(self.table)
        grid.AutoSize()
        grid.AutoSizeColumns(True)

class MyApp(wx.App):

    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Yahoo Finance")
        self.frame.Show()

        return True

def main():
    app = MyApp()
    app.MainLoop()

  
if __name__ == "__main__":
    main()

# ===========================================================================
# [wxPython 참고 사이트] : https://www.blog.pythonlibrary.org/
#
# [wxPython 카테고리] : https://www.blog.pythonlibrary.org/category/wxpython/
#
# [wxPython: Grid Tips and Tricks] :
#   https://www.blog.pythonlibrary.org/2010/04/04/wxpython-grid-tips-and-tricks/
#   https://www.blog.pythonlibrary.org/2010/04/
#
# [Second Window Open]
#   https://www.blog.pythonlibrary.org/2018/10/19/wxpython-how-to-open-a-second-window-frame/
#
# ===========================================================================

# %% pop up 메뉴 띄우기
import wx
import wx.grid as  gridlib
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Grid with Popup Menu")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(panel)
        self.grid.CreateGrid(25,8)
        self.grid.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK,
                       self.showPopupMenu)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)
        
    #----------------------------------------------------------------------
    def showPopupMenu(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            # make a menu
        
        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,"One")
        menu.AppendItem(item)
        menu.Append(self.popupID2, "Two")
        menu.Append(self.popupID3, "Three")
        
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
    
# %% 마우스 우측 버튼 클릭 위치 출력
import wx
import wx.grid as gridlib

########################################################################
class MyForm(wx.Frame):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Getting the Row/Col")
        panel = wx.Panel(self)
 
        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(12, 8)
        self.myGrid = myGrid
        self.myGrid.GetGridWindow().Bind(wx.EVT_RIGHT_DOWN, self.onRightClick)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)
        
    #----------------------------------------------------------------------
    def onRightClick(self, event):
        """"""
        x, y = self.myGrid.CalcUnscrolledPosition(event.GetX(),
                                                  event.GetY())
        row, col = self.myGrid.XYToCell(x, y)
        print(row, col)
        
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()
  
# %% Grids and Tooltips
import wx
import wx.grid as  gridlib
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Grid Tooltips")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        
        self.grid = gridlib.Grid(panel)
        self.grid.CreateGrid(25,8)
        
        # put a tooltip on the cells in a column
        self.grid.GetGridWindow().Bind(wx.EVT_MOTION, self.onMouseOver)
        # the following is equivalent to the above mouse binding
##        for child in self.grid.GetChildren():
##             if child.GetName() == 'grid window':
##                 child.Bind(wx.EVT_MOTION, self.onMouseOver)
        
        # put a tooltip on a column label
        self.grid.GetGridColLabelWindow().Bind(wx.EVT_MOTION, 
                                               self.onMouseOverColLabel)
        # put a tooltip on a row label
        self.grid.GetGridRowLabelWindow().Bind(wx.EVT_MOTION, 
                                               self.onMouseOverRowLabel)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)
        
    #----------------------------------------------------------------------
    def onMouseOver(self, event):
        """
        Displays a tooltip over any cell in a certain column
        """
        # Use CalcUnscrolledPosition() to get the mouse position within the 
        # entire grid including what's offscreen
        # This method was suggested by none other than Robin Dunn
        x, y = self.grid.CalcUnscrolledPosition(event.GetX(),event.GetY())
        coords = self.grid.XYToCell(x, y)
        col = coords[1]
        row = coords[0]
        
        # Note: This only sets the tooltip for the cells in the column
        if col == 1:
            msg = "This is Row %s, Column %s!" % (row, col)
            event.GetEventObject().SetToolTipString(msg)
        else:
            event.GetEventObject().SetToolTipString('')

    #----------------------------------------------------------------------
    def onMouseOverColLabel(self, event):
        """
        Displays a tooltip when mousing over certain column labels
        """
        x = event.GetX()
        y = event.GetY()
        col = self.grid.XToCol(x, y)
        
        if col == 0:
            self.grid.GetGridColLabelWindow().SetToolTipString('Column One')
        elif col == 1:
            self.grid.GetGridColLabelWindow().SetToolTipString('Column Two')
        else:
            self.grid.GetGridColLabelWindow().SetToolTipString('')
        event.Skip()
        
    #----------------------------------------------------------------------
    def onMouseOverRowLabel(self, event):
        """
        Displays a tooltip on a row label
        """
        x = event.GetX()
        y = event.GetY()
        row = self.grid.YToRow(y)
        print(row)
        if row == 0:
            self.grid.GetGridRowLabelWindow().SetToolTipString("Row One")
        elif row == 1:
            self.grid.GetGridRowLabelWindow().SetToolTipString('Row Two')
        else:
            self.grid.GetGridRowLabelWindow().SetToolTipString("")
        event.Skip()
        
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()

# %% Using Arrow Keys to Navigate Out of a Cell Edit
# 셀편집 후 방향키 눌러졌는지 감지

import wx
import wx.grid as  gridlib
class MyForm(wx.Frame):
    
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Navigating out of a cell")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(panel)
        self.grid.CreateGrid(25,8)
        
        self.grid.Bind(gridlib.EVT_GRID_EDITOR_CREATED, self.onCellEdit)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)
        
    #----------------------------------------------------------------------
    def onCellEdit(self, event):
        '''
        When cell is edited, get a handle on the editor widget
        and bind it to EVT_KEY_DOWN
        '''        
        editor = event.GetControl()        
        editor.Bind(wx.EVT_KEY_DOWN, self.onEditorKey)
        event.Skip()
    
    #----------------------------------------------------------------------
    def onEditorKey(self, event):
        '''
        Handler for the wx.grid's cell editor widget's keystrokes. Checks for specific
        keystrokes, such as arrow up or arrow down, and responds accordingly. Allows
        all other key strokes to pass through the handler.
        '''
        keycode = event.GetKeyCode() 
        if keycode == wx.WXK_UP:
            print('you pressed the UP key!')
            self.grid.MoveCursorUp(False)
        elif keycode == wx.WXK_DOWN:
            print('you pressed the down key!')
            self.grid.MoveCursorDown(False)
        elif keycode == wx.WXK_LEFT:
            print('you pressed the left key!')
            self.grid.MoveCursorLeft(False)
        elif keycode == wx.WXK_RIGHT:
            print('you pressed the right key')
            self.grid.MoveCursorRight(False)
        else:
            pass
        event.Skip()
        
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()


# %% How to Hide Row and Column Labels
import wx
import wx.grid as  gridlib
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Changing Row/Col Labels")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        grid = gridlib.Grid(panel)
        grid.CreateGrid(25,8)
        
        # http://bit.ly/aXbeNF - link to FAQ
        grid.SetRowLabelSize(0) # hide the rows
        grid.SetColLabelSize(0) # hide the columns
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
    
# %% Display Something (Dialog/Frame/Whatever) When the User Clicks on a Row Label
import wx
import wx.grid as gridlib
class MyForm(wx.Frame):
    
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "Show Dialog on Row Label Click")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(panel)
        self.grid.CreateGrid(25,8)
        
        self.grid.Bind(gridlib.EVT_GRID_LABEL_LEFT_CLICK, self.onRowClick)
        # self.grid.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.onRowClick)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)
        
    #----------------------------------------------------------------------
    def onRowClick(self, event):
        """
        Displays a message dialog to the user which displays which row
        label the user clicked on
        """
        # Note that rows are zero-based
        row = event.GetRow()
        dlg = wx.MessageDialog(None, "You clicked on Row Label %s" %row,
                               "Notice",
                               wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
    
# %% How to Change Column/Row Labels
import wx
import wx.grid as  gridlib
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Hiding Rows and Columns")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        grid = gridlib.Grid(panel)
        grid.CreateGrid(25,8)
        
        # change a couple column labels
        grid.SetColLabelValue(0, "Name")
        grid.SetColLabelValue(1, "Phone")
        
        # change the row labels
        for row in range(25):
            rowNum = row + 1
            grid.SetRowLabelValue(row, "Row %s" % rowNum)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
    
# %%
# stacked_buttons.py

import wx
class MyPanel(wx.Panel):
    
    def __init__(self, parent):
        super().__init__(parent)
        button1 = wx.Button(self, label='Press Me')
        button2 = wx.Button(self, label='Press Me too')
        button3 = wx.Button(self, label='Another button')
        
class MyFrame(wx.Frame):
    
    def __init__(self):
        #super().__init__(None, title='Hello World')
        wx.Frame.__init__(self, None, wx.ID_ANY, title='Hello World')
        panel = MyPanel(self)
        self.Show()
        
if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MyFrame()
    app.MainLoop()
    
# %% How to Open a Second Window / Frame
# https://www.blog.pythonlibrary.org/2018/10/19/wxpython-how-to-open-a-second-window-frame/

import wx
class OtherFrame(wx.Frame):
    """
    Class used for creating frames other than the main one
    """
    
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.Show()
class MyPanel(wx.Panel):
    
    # def __init__(self, parent):
    #     wx.Panel.__init__(self, parent)
        
    #     btn = wx.Button(self, label='Create New Frame')
    #     btn.Bind(wx.EVT_BUTTON, self.on_new_frame)
    #     self.frame_number = 1
        
    # def on_new_frame(self, event):
    #     title = 'SubFrame {}'.format(self.frame_number)
    #     frame = OtherFrame(title=title)
    #     self.frame_number += 1

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        btn = wx.Button(self, label='Create New Frame')
        btn.Bind(wx.EVT_BUTTON, self.on_new_frame)
        self.frame_number = 1
        self.parent = parent
    def on_new_frame(self, event):
        title = 'SubFrame {}'.format(self.frame_number)
        frame = OtherFrame(title=title, parent=self.parent)
        self.frame_number += 1
        
class MainFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, title='Main Frame', size=(800, 600))
        panel = MyPanel(self)
        self.Show()
        
if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

# %% wxPython tutorial 
# 
# https://zetcode.com/wxpython/
#
#!/usr/bin/env python
 
# simple.py

import wx

app = wx.App()

frame = wx.Frame(None, title='Simple application')
frame.Show()

app.MainLoop()


