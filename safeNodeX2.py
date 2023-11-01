# Chris Glew Ltd. www.chrisglew.com
# V 1.0
#   August 2017 
# V 1.1
#   September 2018 - works with Nuke 10 & Nuke 11
# V 1.2
#   June 2019 - works with Linux

import nuke

try:
    nuke.NUKE_VERSION_MAJOR < 11
    import PySide.QtGui as QtGui
except:
    nuke.NUKE_VERSION_MAJOR >= 11
    import PySide2.QtWidgets as QtGui



def AsciFi():
    
    clipboard = QtGui.QApplication.clipboard()
    originalClipboard = clipboard.text()


    for node in nuke.selectedNodes():

        for selectedNode in nuke.selectedNodes():
            selectedNode.knob('selected').setValue(True)
            nuke.nodeCopy('%clipboard%')

        node.knob('selected').setValue(True)

        noOpNode = nuke.createNode("NoOp")

        textKnob = nuke.Multiline_Eval_String_Knob('input', 'text')
        restoreKnob = nuke.PyScript_Knob('Restore')
        restoreKnob.setCommand("import nuke\n\ntry:\n    nuke.NUKE_VERSION_MAJOR < 11\n    import PySide.QtGui as QtGui\nexcept:\n    nuke.NUKE_VERSION_MAJOR >= 11\n    import PySide2.QtWidgets as QtGui\n\nclipboard = QtGui.QApplication.clipboard()\noriginalClipboard = clipboard.text()\n\nfor i in nuke.selectedNodes():\n\ttextKnob = i ['input'].getValue()\n\tfirstInput = i.input(0)\n\tXpos = i.xpos()\n\tYpos = i.ypos()\n\tclipboard.setText(textKnob)\n\tnuke.nodePaste(\"%clipboard%\")\n\tnuke.delete(i)\n\tfor a in nuke.selectedNodes():\n\t\ta.setXpos(Xpos)\n\t\ta.setYpos(Ypos)\n\t\ta.setInput(0, firstInput)")
        restoreKnob.setName('Restore the original Class Type for this Node')
        restoreKnob.setLabel('Restore Node')
        noOpNode.addKnob(textKnob)
        noOpNode.addKnob(restoreKnob)
        textKnob.setVisible(False)

        textKnob.setValue(clipboard.text())
        
        name = node.name()
        noOpNode.setXpos(node.xpos())
        noOpNode.setYpos(node.ypos())
        nuke.delete(node)
        noOpNode.setName(name)
    
        clipboard.setText(originalClipboard)

#AsciFi()