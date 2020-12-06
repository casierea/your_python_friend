import maya.cmds as cmds
def Renamer(input_string):
    sels = cmds.ls(selection=True)

    input_selection = 1

    for sel in sels:

        collection_count = input_string.count('#')

        tupple_parts = input_string.partition('#' * collection_count)

        numbering_systems = str(input_selection)

        if tupple_parts[1]:
            print 'characters are good.'
            replace_zeroes = numbering_systems.zfill(3)

            cmds.rename(tupple_parts[0] + replace_zeroes + tupple_parts[2])

        else:

            cmds.error('characters are not in order. try again.')
        input_selection += 1


Renamer("L_Arm_###_Jnt")