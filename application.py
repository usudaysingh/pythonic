import wx

"""
app = wx.App()
frame = wx.Frame(None, -1, 'Hello Baby', pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE)
frame.Show()

app.MainLoop()
"""
class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        smenu = wx.Menu()
        mum = wx.Menu()

        # create toolbar
        toolbar = self.CreateToolBar()
        tundo = toolbar.AddLabelTool(wx.ID_UNDO, '', wx.Bitmap('/home/rajputs/Desktop/undo.png'))
        tredo = toolbar.AddLabelTool(wx.ID_REDO, '', wx.Bitmap('/home/rajputs/Desktop/redo.png'))
        toolbar.Realize()

        #create menu item
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        fileMenu.Append(wx.ID_ANY, 'Import Newsfeed list...')
        fileMenu.Append(wx.ID_ANY, 'Import bookmarks...')
        fileMenu.Append(wx.ID_ANY, 'Import mail...')
        fileMenu.AppendSeparator()  # Append separator
        mum.Append(wx.ID_ANY, 'Under Menu')
        fileMenu.AppendMenu(wx.ID_ANY, 'UnderMenu', mum)
        menubar.Append(fileMenu, '&File')
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem) # to bind with onquit method

        menubar.Append(smenu, '&Commit')
        self.SetMenuBar(menubar)

        # font size
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        #V box
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        """
        # create Panel
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')

        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#ededed')

        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vbox)

        # Set string
        st1 = wx.StaticText(midPan, label='Class Name')
        st1.SetFont(font)
        strbox = wx.BoxSizer(wx.HORIZONTAL)
        strbox.Add(st1, 1, wx.EXPAND|wx.ALL, 10)
        vbox.Add(strbox)

        # set textbox
        textbox = wx.BoxSizer(wx.HORIZONTAL)
        tc = wx.TextCtrl(midPan)
        textbox.Add(st1, 1, wx.EXPAND | wx.ALL, 20)
        vbox.Add(textbox)
        """
        display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border = 10)

        hbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion=1, flag=wx.EXPAND)
        but = wx.Button(self, label="here i am")
        hbox.Add(but, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border = 5)
        # grid sizer
        gs = wx.GridSizer(5, 4, 5, 5)
        gs.AddMany( [(wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Bck'), 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.Button(self, label='Close'), 0, wx.EXPAND),
            (wx.Button(self, label='7'), 0, wx.EXPAND),
            (wx.Button(self, label='8'), 0, wx.EXPAND),
            (wx.Button(self, label='9'), 0, wx.EXPAND),
            (wx.Button(self, label='/'), 0, wx.EXPAND),
            (wx.Button(self, label='4'), 0, wx.EXPAND),
            (wx.Button(self, label='5'), 0, wx.EXPAND),
            (wx.Button(self, label='6'), 0, wx.EXPAND),
            (wx.Button(self, label='*'), 0, wx.EXPAND),
            (wx.Button(self, label='1'), 0, wx.EXPAND),
            (wx.Button(self, label='2'), 0, wx.EXPAND),
            (wx.Button(self, label='3'), 0, wx.EXPAND),
            (wx.Button(self, label='-'), 0, wx.EXPAND),
            (wx.Button(self, label='0'), 0, wx.EXPAND),
            (wx.Button(self, label='.'), 0, wx.EXPAND),
            (wx.Button(self, label='='), 0, wx.EXPAND),
            (wx.Button(self, label='+'), 0, wx.EXPAND) ])
        hbox.Add(gs, proportion=1, flag=wx.EXPAND)

        # flex grid sizer
        panel = wx.Panel(self)
        title = wx.StaticText(panel, label="Title")
        author = wx.StaticText(panel, label="Author")
        review = wx.StaticText(panel, label="Review")

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        fbox = wx.BoxSizer(wx.VERTICAL)
        fgrid = wx.FlexGridSizer(3, 2, 9, 25)
        fbox.Add(fgrid, proportion=1, flag=wx.EXPAND|wx.BOTTOM|wx.TOP, border=10)
        fgrid.AddMany([(title), (tc1, 1, wx.EXPAND), (author),
            (tc2, 1, wx.EXPAND), (review, 1, wx.EXPAND), (tc3, 1, wx.EXPAND)])

        fgrid.AddGrowableRow(2, 1)
        fgrid.AddGrowableCol(1, 1)
        fbox.Add(fgrid)
        vbox.Add(fbox)

        self.SetSizer(vbox)

        def OnUndo(self, e):
            '''
            Undo method for undo toolbar
            '''
            if self.count > 1 and self.count <= 5:
                self.count = self.count - 1

            if self.count == 1:
                self.toolbar.EnableTool(wx.ID_UNDO, False)

            if self.count == 4:
                self.toolbar.EnableTool(wx.ID_REDO, True)


        def OnRedo(self, e):
            '''
            Redo method for toolbar
            '''
            if self.count < 5 and self.count >= 1:
                self.count = self.count + 1

            if self.count == 5:
                self.toolbar.EnableTool(wx.ID_REDO, False)

            if self.count == 2:
                self.toolbar.EnableTool(wx.ID_UNDO, True)

        self.SetSize((300, 200))
        self.SetTitle('Application')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        '''
        To quit the toolbar
        '''
        self.close()

def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()

if  __name__ == '__main__':
    main()
