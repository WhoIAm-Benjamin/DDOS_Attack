@ECHO OFF
pyuic5 ".ui & .qrc files/design.ui" -o design.py
echo "design.py complete"
pyuic5 ".ui & .qrc files/dialog_design.ui" -o dialog_design.pyw
echo "dialog_design.py complete"
pyrcc5 ".ui & .qrc files/picture.qrc" -o picture_rc.pyw
echo "picture_rc.py complete"
pyuic5 ".ui & .qrc files/error.ui" -o error.pyw
echo "error.pyw complete"
pyrcc5 ".ui & .qrc files/error_resource.qrc" -o error_resource_rc.pyw
echo "error_resource_rc.pyw complete"
set/p "cho=>"