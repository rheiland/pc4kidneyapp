
python flatten_cell_def_xml.py <hierarchical.xml>
python flatten_cell_def_xml.py test0.xml
--> tmp2.xml

python flatten_cell_def_xml.py <hierarchical.xml flattened.xml>
python recurse_xml.py test0.xml 
python recurse_xml.py test0.xml tmp2.xml
