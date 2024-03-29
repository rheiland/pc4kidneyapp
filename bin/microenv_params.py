 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class MicroenvTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}


        menv_var1 = Button(description='oxygen', disabled=True, layout=name_button_layout)
        menv_var1.style.button_color = 'tan'

        param_name1 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.oxygen_diffusion_coefficient = FloatText(value=100000.0,
          step=10000,style=style, layout=widget_layout)

        param_name2 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.oxygen_decay_rate = FloatText(value=10,
          step=1,style=style, layout=widget_layout)
        param_name3 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.oxygen_initial_condition = FloatText(value=38,style=style, layout=widget_layout)
        param_name4 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.oxygen_Dirichlet_boundary_condition = FloatText(value=38,style=style, layout=widget_layout)
        self.oxygen_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)
        self.oxygen_Dirichlet_boundary_condition_toggle_ymin = Checkbox(description='ymin', disabled=False,style=style, layout=widget_layout)

        self.oxygen_Dirichlet_boundary_condition_value_ymin = FloatText(value=24,style=style, layout=widget2_layout)
        self.oxygen_Dirichlet_boundary_condition_toggle_ymax = Checkbox(description='ymax', disabled=False,style=style, layout=widget_layout)

        self.oxygen_Dirichlet_boundary_condition_value_ymax = FloatText(value=6,style=style, layout=widget2_layout)
        self.oxygen_Dirichlet_boundary_condition_toggle_xmin = Checkbox(description='xmin', disabled=False,style=style, layout=widget_layout)

        self.oxygen_Dirichlet_boundary_condition_value_xmin = FloatText(value=38,style=style, layout=widget2_layout)
        self.oxygen_Dirichlet_boundary_condition_toggle_xmax = Checkbox(description='xmax', disabled=False,style=style, layout=widget_layout)

        self.oxygen_Dirichlet_boundary_condition_value_xmax = FloatText(value=10,style=style, layout=widget2_layout)
        self.oxygen_Dirichlet_boundary_condition_toggle_zmin = Checkbox(description='zmin', disabled=False,style=style, layout=widget_layout)

        self.oxygen_Dirichlet_boundary_condition_value_zmin = FloatText(value=38,style=style, layout=widget2_layout)
        self.oxygen_Dirichlet_boundary_condition_toggle_zmax = Checkbox(description='zmax', disabled=False,style=style, layout=widget_layout)

        self.oxygen_Dirichlet_boundary_condition_value_zmax = FloatText(value=10,style=style, layout=widget2_layout)

        menv_var2 = Button(description='blood_vessel_distance', disabled=True, layout=name_button_layout)
        menv_var2.style.button_color = 'lightgreen'

        param_name5 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.blood_vessel_distance_diffusion_coefficient = FloatText(value=0.0,
          step=0.01,style=style, layout=widget_layout)

        param_name6 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.blood_vessel_distance_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name7 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.blood_vessel_distance_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name8 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.blood_vessel_distance_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.blood_vessel_distance_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var3 = Button(description='pbm_gbm_distance', disabled=True, layout=name_button_layout)
        menv_var3.style.button_color = 'tan'

        param_name9 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.pbm_gbm_distance_diffusion_coefficient = FloatText(value=0.0,
          step=0.01,style=style, layout=widget_layout)

        param_name10 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.pbm_gbm_distance_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name11 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.pbm_gbm_distance_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name12 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.pbm_gbm_distance_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.pbm_gbm_distance_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)
        self.calculate_gradient = Checkbox(description='calculate_gradients', disabled=False, layout=desc_button_layout)
        self.track_internal = Checkbox(description='track_in_agents', disabled=False, layout=desc_button_layout)


         #  ------- micronenv info
        menv_units_button1 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button2 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button3 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button4 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button5 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button7 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button8 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button9 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button11 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button12 = Button(description='mmHg', disabled=True, layout=units_button_layout) 




        row_oxygen = [menv_var1,  ] 
        row1 = [param_name1, self.oxygen_diffusion_coefficient, menv_units_button1]
        row2 = [param_name2, self.oxygen_decay_rate, menv_units_button2]
        row3 = [param_name3, self.oxygen_initial_condition, menv_units_button3]
        row4 = [param_name4, self.oxygen_Dirichlet_boundary_condition, menv_units_button4, self.oxygen_Dirichlet_boundary_condition_toggle]
        row5 = [self.oxygen_Dirichlet_boundary_condition_toggle_ymin, self.oxygen_Dirichlet_boundary_condition_value_ymin,]
        row6 = [self.oxygen_Dirichlet_boundary_condition_toggle_ymax, self.oxygen_Dirichlet_boundary_condition_value_ymax,]
        row7 = [self.oxygen_Dirichlet_boundary_condition_toggle_xmin, self.oxygen_Dirichlet_boundary_condition_value_xmin,]
        row8 = [self.oxygen_Dirichlet_boundary_condition_toggle_xmax, self.oxygen_Dirichlet_boundary_condition_value_xmax,]
        row9 = [self.oxygen_Dirichlet_boundary_condition_toggle_zmin, self.oxygen_Dirichlet_boundary_condition_value_zmin,]
        row10 = [self.oxygen_Dirichlet_boundary_condition_toggle_zmax, self.oxygen_Dirichlet_boundary_condition_value_zmax,]
        row_blood_vessel_distance = [menv_var2,  ] 
        row11 = [param_name5, self.blood_vessel_distance_diffusion_coefficient, menv_units_button5]
        row12 = [param_name6, self.blood_vessel_distance_decay_rate, menv_units_button6]
        row13 = [param_name7, self.blood_vessel_distance_initial_condition, menv_units_button7]
        row14 = [param_name8, self.blood_vessel_distance_Dirichlet_boundary_condition, menv_units_button8, self.blood_vessel_distance_Dirichlet_boundary_condition_toggle]
        row_pbm_gbm_distance = [menv_var3,  ] 
        row15 = [param_name9, self.pbm_gbm_distance_diffusion_coefficient, menv_units_button9]
        row16 = [param_name10, self.pbm_gbm_distance_decay_rate, menv_units_button10]
        row17 = [param_name11, self.pbm_gbm_distance_initial_condition, menv_units_button11]
        row18 = [param_name12, self.pbm_gbm_distance_Dirichlet_boundary_condition, menv_units_button12, self.pbm_gbm_distance_Dirichlet_boundary_condition_toggle]
        row19 = [self.calculate_gradient,]
        row20 = [self.track_internal,]


        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box_oxygen = Box(children=row_oxygen, layout=box_layout)
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box_blood_vessel_distance = Box(children=row_blood_vessel_distance, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box_pbm_gbm_distance = Box(children=row_pbm_gbm_distance, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)

        self.tab = VBox([
          box_oxygen,
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box_blood_vessel_distance,
          box11,
          box12,
          box13,
          box14,
          box_pbm_gbm_distance,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point

        self.oxygen_diffusion_coefficient.value = float(vp[0].find('.//diffusion_coefficient').text)
        self.oxygen_decay_rate.value = float(vp[0].find('.//decay_rate').text)
        self.oxygen_initial_condition.value = float(vp[0].find('.//initial_condition').text)
        self.oxygen_Dirichlet_boundary_condition.value = float(vp[0].find('.//Dirichlet_boundary_condition').text)
        if vp[0].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.oxygen_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.oxygen_Dirichlet_boundary_condition_toggle.value = False
        if vp[0].find('.//boundary_value[1]').attrib['enabled'].lower() == 'true':
          self.oxygen_Dirichlet_boundary_condition_toggle_ymin.value = True
        else:
          self.oxygen_Dirichlet_boundary_condition_toggle_ymin.value = False
        self.oxygen_Dirichlet_boundary_condition_value_ymin.value = float(vp[0].find('.//Dirichlet_options//boundary_value[1]').text)
        if vp[0].find('.//boundary_value[2]').attrib['enabled'].lower() == 'true':
          self.oxygen_Dirichlet_boundary_condition_toggle_ymax.value = True
        else:
          self.oxygen_Dirichlet_boundary_condition_toggle_ymax.value = False
        self.oxygen_Dirichlet_boundary_condition_value_ymax.value = float(vp[0].find('.//Dirichlet_options//boundary_value[2]').text)
        if vp[0].find('.//boundary_value[3]').attrib['enabled'].lower() == 'true':
          self.oxygen_Dirichlet_boundary_condition_toggle_xmin.value = True
        else:
          self.oxygen_Dirichlet_boundary_condition_toggle_xmin.value = False
        self.oxygen_Dirichlet_boundary_condition_value_xmin.value = float(vp[0].find('.//Dirichlet_options//boundary_value[3]').text)
        if vp[0].find('.//boundary_value[4]').attrib['enabled'].lower() == 'true':
          self.oxygen_Dirichlet_boundary_condition_toggle_xmax.value = True
        else:
          self.oxygen_Dirichlet_boundary_condition_toggle_xmax.value = False
        self.oxygen_Dirichlet_boundary_condition_value_xmax.value = float(vp[0].find('.//Dirichlet_options//boundary_value[4]').text)
        if vp[0].find('.//boundary_value[5]').attrib['enabled'].lower() == 'true':
          self.oxygen_Dirichlet_boundary_condition_toggle_zmin.value = True
        else:
          self.oxygen_Dirichlet_boundary_condition_toggle_zmin.value = False
        self.oxygen_Dirichlet_boundary_condition_value_zmin.value = float(vp[0].find('.//Dirichlet_options//boundary_value[5]').text)
        if vp[0].find('.//boundary_value[6]').attrib['enabled'].lower() == 'true':
          self.oxygen_Dirichlet_boundary_condition_toggle_zmax.value = True
        else:
          self.oxygen_Dirichlet_boundary_condition_toggle_zmax.value = False
        self.oxygen_Dirichlet_boundary_condition_value_zmax.value = float(vp[0].find('.//Dirichlet_options//boundary_value[6]').text)

        self.blood_vessel_distance_diffusion_coefficient.value = float(vp[1].find('.//diffusion_coefficient').text)
        self.blood_vessel_distance_decay_rate.value = float(vp[1].find('.//decay_rate').text)
        self.blood_vessel_distance_initial_condition.value = float(vp[1].find('.//initial_condition').text)
        self.blood_vessel_distance_Dirichlet_boundary_condition.value = float(vp[1].find('.//Dirichlet_boundary_condition').text)
        if vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.blood_vessel_distance_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.blood_vessel_distance_Dirichlet_boundary_condition_toggle.value = False

        self.pbm_gbm_distance_diffusion_coefficient.value = float(vp[2].find('.//diffusion_coefficient').text)
        self.pbm_gbm_distance_decay_rate.value = float(vp[2].find('.//decay_rate').text)
        self.pbm_gbm_distance_initial_condition.value = float(vp[2].find('.//initial_condition').text)
        self.pbm_gbm_distance_Dirichlet_boundary_condition.value = float(vp[2].find('.//Dirichlet_boundary_condition').text)
        if vp[2].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.pbm_gbm_distance_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.pbm_gbm_distance_Dirichlet_boundary_condition_toggle.value = False

        if uep.find('.//options//calculate_gradients').text.lower() == 'true':
          self.calculate_gradient.value = True
        else:
          self.calculate_gradient.value = False
        if uep.find('.//options//track_internalized_substrates_in_each_agent').text.lower() == 'true':
          self.track_internal.value = True
        else:
          self.track_internal.value = False
        


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp[0].find('.//diffusion_coefficient').text = str(self.oxygen_diffusion_coefficient.value)
        vp[0].find('.//decay_rate').text = str(self.oxygen_decay_rate.value)
        vp[0].find('.//initial_condition').text = str(self.oxygen_initial_condition.value)
        vp[0].find('.//Dirichlet_boundary_condition').text = str(self.oxygen_Dirichlet_boundary_condition.value)
        vp[0].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.oxygen_Dirichlet_boundary_condition_toggle.value).lower()

        vp[0].find('.//Dirichlet_options//boundary_value[1]').text = str(self.oxygen_Dirichlet_boundary_condition_value_ymin.value)
        vp[0].find('.//Dirichlet_options//boundary_value[1]').attrib['enabled'] = str(self.oxygen_Dirichlet_boundary_condition_toggle_ymin.value).lower()

        vp[0].find('.//Dirichlet_options//boundary_value[2]').text = str(self.oxygen_Dirichlet_boundary_condition_value_ymax.value)
        vp[0].find('.//Dirichlet_options//boundary_value[2]').attrib['enabled'] = str(self.oxygen_Dirichlet_boundary_condition_toggle_ymax.value).lower()

        vp[0].find('.//Dirichlet_options//boundary_value[3]').text = str(self.oxygen_Dirichlet_boundary_condition_value_xmin.value)
        vp[0].find('.//Dirichlet_options//boundary_value[3]').attrib['enabled'] = str(self.oxygen_Dirichlet_boundary_condition_toggle_xmin.value).lower()

        vp[0].find('.//Dirichlet_options//boundary_value[4]').text = str(self.oxygen_Dirichlet_boundary_condition_value_xmax.value)
        vp[0].find('.//Dirichlet_options//boundary_value[4]').attrib['enabled'] = str(self.oxygen_Dirichlet_boundary_condition_toggle_xmax.value).lower()

        vp[0].find('.//Dirichlet_options//boundary_value[5]').text = str(self.oxygen_Dirichlet_boundary_condition_value_zmin.value)
        vp[0].find('.//Dirichlet_options//boundary_value[5]').attrib['enabled'] = str(self.oxygen_Dirichlet_boundary_condition_toggle_zmin.value).lower()

        vp[0].find('.//Dirichlet_options//boundary_value[6]').text = str(self.oxygen_Dirichlet_boundary_condition_value_zmax.value)
        vp[0].find('.//Dirichlet_options//boundary_value[6]').attrib['enabled'] = str(self.oxygen_Dirichlet_boundary_condition_toggle_zmax.value).lower()

        vp[1].find('.//diffusion_coefficient').text = str(self.blood_vessel_distance_diffusion_coefficient.value)
        vp[1].find('.//decay_rate').text = str(self.blood_vessel_distance_decay_rate.value)
        vp[1].find('.//initial_condition').text = str(self.blood_vessel_distance_initial_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').text = str(self.blood_vessel_distance_Dirichlet_boundary_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.blood_vessel_distance_Dirichlet_boundary_condition_toggle.value).lower()

        vp[2].find('.//diffusion_coefficient').text = str(self.pbm_gbm_distance_diffusion_coefficient.value)
        vp[2].find('.//decay_rate').text = str(self.pbm_gbm_distance_decay_rate.value)
        vp[2].find('.//initial_condition').text = str(self.pbm_gbm_distance_initial_condition.value)
        vp[2].find('.//Dirichlet_boundary_condition').text = str(self.pbm_gbm_distance_Dirichlet_boundary_condition.value)
        vp[2].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.pbm_gbm_distance_Dirichlet_boundary_condition_toggle.value).lower()


        uep.find('.//options//calculate_gradients').text = str(self.calculate_gradient.value)
        uep.find('.//options//track_internalized_substrates_in_each_agent').text = str(self.track_internal.value)
