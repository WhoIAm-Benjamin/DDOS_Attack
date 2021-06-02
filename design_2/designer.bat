@ECHO OFF
pyuic5 ".ui & .qrc files/design.ui" -o design.py
echo "design.py complete"
pyuic5 ".ui & .qrc files/dialog_design.ui" -o dialog_design.py
echo "dialog_design.py complete"
pyrcc5 ".ui & .qrc files/picture.qrc" -o picture_rc.py
echo "picture_rc.py complete"
set/p "cho=>"