import uno
import msgbox

document = XSCRIPTCONTEXT.getDocument()
header = True

def toMarkdown():
    smgr = XSCRIPTCONTEXT.getComponentContext().getServiceManager()
    dp = smgr.createInstanceWithContext("com.sun.star.awt.DialogProvider", XSCRIPTCONTEXT.getComponentContext())
    controller = document.CurrentController
    active_sheet = controller.ActiveSheet
    selection = controller.getSelection()
    data = selection.getDataArray()
    dlg = dp.createDialog("vnd.sun.star.script:calc2md.markdown?location=application")
    text = dlg.getControl("MarkdownOutput")
    dataString = ""
    if header:
        chars = []
        dataString += "| "
        for column in data[0]:
            dataString += str(column)
            chars.append(len(str(column)))
            dataString += " | "
        dataString += '\n'
        for i in range(0,len(data[0])):
            dataString += "| "
            for i in range(0,chars[i]):
                dataString += "-"
            dataString += " "
            
        dataString += "|\n"
        data = data[1:]

    for row in data:
        dataString += "| "
        for column in row:
            dataString += str(column)
            dataString += " | "

        dataString += '\n'
    text.Model.Text = dataString
    dlg.Model.Title = "Markdown Table"
    dlg.execute()
    dlg.dispose()
