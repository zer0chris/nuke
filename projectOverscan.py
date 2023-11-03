# Overscan 3D projection - 03/2020 chrisglew ltd.

import nuke

def projectOverscan():
	for i in nuke.selectedNodes():
		nodeClasses = ['Camera','Camera2']
		# turn off read from file
		if i.Class() == 'Camera2':
			i['read_from_file'].setValue(0)
		if i.Class() in nodeClasses:
			aA = i['translate'].toScript()
			bB = i['rotate'].toScript()
			cC = i['focal'].toScript()
			dD = i['haperture'].toScript()
			eE = i['vaperture'].toScript()
			fF = i['label'].toScript()
		else:
			nuke.message('Please Select a Camera')

	c = nuke.createNode('Camera')
	r = nuke.createNode('Reformat')

	# create overscan
	r['label'].setValue('REFORMAT_OVERSCAN\n(Put above Project3D)')
	r['resize'].setValue('none')
	r['type'].setValue('scale')
	r['scale'].setValue(2)

	Rname = r['name'].getValue()

	eXp = '1/'+str(Rname)+'.scale*curve'
	#copy settings to new camera


	c['translate'].fromScript(aA)
	c['rotate'].fromScript(bB)
	c['focal'].fromScript(cC)
	c['haperture'].fromScript(dD)
	c['vaperture'].fromScript(eE)
	c['label'].fromScript(fF)

	c['focal'].setExpression(eXp)

	# c.setInput(0, None)

	# turn on read from file
	if i.Class() == 'Camera2':
			i['read_from_file'].setValue(1)
	else:
		pass
# projectOverscan()