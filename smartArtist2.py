## Smart Artist - Copyright (c) Chris Glew Ltd - chrisglew.com
## Version 1.0.0
## Version 1.0.5 - updated for latest verion of Nuke (first and last frame info needed)
## Want to create SmartVectors and Vector Distorts but have no Nuke X Licence? No problem! Create a Vector Distort with whatever reference frame and output type you want and a Smart Vector node with vector detail 1
## Note - you will need to publish this through Shotgun to render the SmartVector 

import nuke
import os
import sys

try:
    nuke.NUKE_VERSION_MAJOR < 11
    import PySide.QtGui as QtGui
except:
    nuke.NUKE_VERSION_MAJOR >= 11
    import PySide2.QtWidgets as QtGui

def smartArtist():
    clipboard = QtGui.QApplication.clipboard()
    firstF = nuke.root().firstFrame()
    lastF = nuke.root().lastFrame()
    midF = (firstF+lastF)/2
    Flabel = '"[value reference_frame]"'

    p = nuke.Panel('CreateVectorDistort')
    p.addEnumerationPulldown('Output Mode', 'STMap STMap_Inverse WarpedSrc')
    p.addBooleanCheckBox('Create smartVectors?', False)
    p.addSingleLineInput('reference frame', midF)
    p.show()

    reFrame = p.value('reference frame')

    if p.value('Output Mode') == 'STMap':
        Omode = "st-map"
    elif p.value('Output Mode') == 'STMap_Inverse':
        Omode = '"st-map inverse"'
    elif p.value('Output Mode') == 'WarpedSrc':
        Omode = '"warped src"'
    
    copyT = "set cut_paste_input [stack 0]\nversion 11.1 v6\npush $cut_paste_input\nVectorDistort {\n reference_frame "+str(reFrame)+"\n reference_frame_set true\n output_mode "+Omode+"\n label "+Flabel+"\n selected true\n}"
    copyD = "set cut_paste_input [stack 0]\nversion 11.1 v6\npush $cut_paste_input\nVectorDistort {\n reference_frame "+str(reFrame)+"\n reference_frame_set true\n output_mode "+Omode+"\n label "+Flabel+"\n selected true\n}\nset cut_paste_input [stack 0]\nversion 11.1 v6\npush $cut_paste_input\nSmartVector {\n file.first_frame "+str(firstF)+"\n file.last_frame "+str(lastF)+"\n vectorDetailReg 1\n name smartVectors\n selected true\n}"

    if p.value('Create smartVectors?') == True:
        clipboard.setText(copyD)
    else:
        clipboard.setText(copyT)

    nuke.nodePaste("%clipboard%")

# smartArtist()