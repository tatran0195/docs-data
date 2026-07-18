from jupiterutils.Utility import JPT_RUN_LINE, JPT_RUN_CODE
from enum import Enum
class spin(Enum):
    integer = 0
    double = 1
class size_behavior(Enum):
    greedy = 0
    vertical = 1
    horizontal = 4
    fixed = 5
class JDGCreator:
    def __init__(self, title, resizable, validation):
        JPT_RUN_CODE("from pyjdg import *")
        message = "dlg=JDGCreator(title='{}',resizable={},validation={})".format(title, resizable, validation)
        JPT_RUN_CODE(message)

    def activate_selector(self, selector_id):
        r"""
        ## Description
        
        Activate selector by selector id.
        
        ## Syntax
        
        ```psj
        dlg.activate_selector(...)
        ```
        
        ## Inputs
        
        ### `selector_id`
        
        - An _Integer_ specifying the selector id.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {14,17}
        from pyjdg import *
        
        def sampleSelection(dlg):
            select1=[]
            select2=[]
            faces=JPT.GetAllFaces()
            for f in faces:
                if f.id % 2 == 0:
                    select1.append(f.id)
                else:
                    select2.append(f.id)
            JPT.ClearAllSelection()
        
            dlg.activate_selector(selector_id=0)
            for id in select1:
                JPT.SelectionByID(JPT.DItemType.FACE, id, True)
            dlg.activate_selector(selector_id=1)
            for id in select2:
                JPT.SelectionByID(JPT.DItemType.FACE, id, True)
            
        def main():
            dlg=JDGCreator(title="Dialog")
            dlg.add_face_selector(text="Face 1")
            dlg.add_face_selector(text="Face 2")
            dlg.add_label(
                name="Label2",width=200,height=70,
                text="Click Apply button and open the selection list and confirm that " 
                     "selectors with even IDs are selected in Face 1," 
                     "and selectors with odd IDs are selected in Face 2.",
                text_halign="left",text_valign="top",layout="Window")
            
            dlg.generate_window()
            Geometry.Part.Cube()
            dlg.on_dlg_apply(callfunc=sampleSelection)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.activate_selector({})".format(selector_id)
        JPT_RUN_LINE(message)

    def add_1delement_selector(self, text="1D element"):
        r"""
        ## Description
        
        Add "1D element" to the selection list, allowing user to select 1D elements and store the selected 1D elements to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_1delement_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "1D element".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {19}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Length in X",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label7",text="Length in Y",layout="Layout6")
            dlg.add_textbox(name="TextBox8",layout="Layout6")
            dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label10",text="Length in Z",layout="Layout9")
            dlg.add_textbox(name="TextBox11",layout="Layout9")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_1delement_selector(text="1D Element 1")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_1delement_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_2delement_selector(self, text="Element"):
        r"""
        ## Description
        
        Add "Element" to the selection list, allowing user to select 2D elements and store the selected 2D elements to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_2delement_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "Element".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {19}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Length in X",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label7",text="Length in Y",layout="Layout6")
            dlg.add_textbox(name="TextBox8",layout="Layout6")
            dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label10",text="Length in Z",layout="Layout9")
            dlg.add_textbox(name="TextBox11",layout="Layout9")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_2delement_selector(text="2D Element 1")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_2delement_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_3delement_selector(self, text="Solid Element"):
        r"""
        ## Description
        
        Add "Solid element" to the selection list, allowing user to select solid elements and store the selected solid elements to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_3delement_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "Solid Element".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {19}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Length in X",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label7",text="Length in Y",layout="Layout6")
            dlg.add_textbox(name="TextBox8",layout="Layout6")
            dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label10",text="Length in Z",layout="Layout9")
            dlg.add_textbox(name="TextBox11",layout="Layout9")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_3delement_selector(text="3D Element 1")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_3delement_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_barpart_selector(self, text="Bar"):
        r"""
        ## Description
        
        Add "Bar" to the selection list, allowing user to select bar parts and store the selected bar parts to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_barpart_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "Bar".
        
        - A _String_ specifying text which will be displayed as button label.
        - The default value is "Bar".
        Bar
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Mesh Count",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_barpart_selector(text="Bar 1")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_barpart_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_browser(self, name, layout, mode="file", file_filter="", default="", multisel=False):
        r"""
        ## Description
        
        Add a file/folder Browser component to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_browser(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `mode`
        
        - A _String_ specifying the Browser type:
          - "file": allowing user to select a file/files.
          - "folder": allowing user to select a folder/folders.
        - The default value is "file".
        
        ### `file_filter`
        
        - A _String_ specifying the format of the selectable file/files with type (\*.extension).
          - For example: All Files (\*.\*), Abaqus (\*.inp)
        - The default value is "".
        
        ### `default`
        
        - A _String_ specifying the default text which will be shown on the textbox of this component.
        - The default value is "".
        
        ### `multisel`
        
        - A _Boolean_ specifying the possibility of the multiple selection:
          - _True_: allow user to select multiple files/folders at the same time.
          - _False_: allow user to select only one file/folder at a time.
        - The default value is _False_.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7-8}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label3",text="Open",layout="Layout1")
            dlg.add_browser(name="Open File/Folder2",mode="file",file_filter="All Files(*.*)",
              default="C:\\temp",multisel=True,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_browser({},{},{},{},{},{})".format(name,layout,mode,file_filter,default,multisel)
        JPT_RUN_LINE(message)

    def add_button(self, name, layout, text="", width=0, height=0, text_color=0, bk_color=15790320, img="", location="left"):
        r"""
        ## Description
        
        Add a Button to the creating dialog. The Button can be an image Button.
        
        ## Syntax
        
        ```psj
        dlg.add_button(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying text which will be displayed on the Button.
        - The default value is "".
        
        ### `width`
        
        - An _Integer_ specifying the width of the Button.
        - The default value is 0.
        
        ### `height`
        
        - An _Integer_ specifying the height of the Button.
        - The default value is 0.
        
        ### `text_color`
        
        - An _Integer_ specifying the text color.
        - The default value is 0.
        
        ### `bk_color`
        
        - An _Integer_ specifying the background color.
        - The default value is 15790320.
        
        ### `img`
        
        - A _String_ specifying the path of an image to be displayed on the Button.
        - The default value is "".
        
        ### `location`
        
        - A _String_ specifying the location of an image to be displayed on the Button.
        - The default value is "left".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {8,16-17,25-26,34-35}
        from pyjdg import *
        
        TechnoStarImage = JPT.GetProgramPath() + "SampleData/PSJ/PSJ-Utility/Utils/TechnoStar.ico"
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
            dlg.add_button(name="Button3",text="Button",width=60,height=22,layout="Layout2")
            font_Button3=PSJFont()
            font_Button3.size=10
            font_Button3.bold=True
            font_Button3.italic=False
            font_Button3.underline=False
            font_Button3.strikeout=False
            dlg.set_item_font(name="Button3",font=font_Button3)
            dlg.add_button(name="Button4",text="Button",width=60,height=22,bk_color=65535,
                text_color=255,img=TechnoStarImage,location="left",layout="Layout2")
            font_Button4=PSJFont()
            font_Button4.size=10
            font_Button4.bold=False
            font_Button4.italic=True
            font_Button4.underline=False
            font_Button4.strikeout=False
            dlg.set_item_font(name="Button4",font=font_Button4)
            dlg.add_button(name="Button5",text="Button",width=60,height=22,bk_color=65535,
                text_color=255,img=TechnoStarImage,location="right",layout="Layout2")
            font_Button5=PSJFont()
            font_Button5.size=10
            font_Button5.bold=False
            font_Button5.italic=False
            font_Button5.underline=True
            font_Button5.strikeout=False
            dlg.set_item_font(name="Button5",font=font_Button5)
            dlg.add_button(name="Button6",text="Button",width=60,height=22,bk_color=65535,
                text_color=255,img=TechnoStarImage,location="top",layout="Layout2")
            font_Button6=PSJFont()
            font_Button6.size=10
            font_Button6.bold=True
            font_Button6.italic=True
            font_Button6.underline=True
            font_Button6.strikeout=False
            dlg.set_item_font(name="Button6",font=font_Button6)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_button({},{},{},{},{},{},{},{},{})".format(name,layout,text,width,height,text_color,bk_color,img,location)
        JPT_RUN_LINE(message)

    def add_checkbox(self, name, layout, text="", checked=False, lefttext=False, width=0, height=0):
        r"""
        ## Description
        
        Add a CheckBox to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_checkbox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying text which will be displayed next to the CheckBox.
        - The default value is "".
        
        ### `checked`
        
        - A _Boolean_ specifying the default state of this component:
          - _True_: the default state of this component is checked.
          - _False_: the default state of this component is unchecked.
        - The default value is _False_.
        
        ### `lefttext`
        
        - A _Boolean_ specifying the text is on left side of CheckBox:
          - _True_: the text is on left side of the CheckBox.
          - _False_: the text is on right side of the CheckBox.
        - The default value is _False_.
        
        ### `width`
        
        - An _Integer_ specifying the width of the CheckBox.
        - The default value is 0.
        
        ### `height`
        
        - An _Integer_ specifying the height of the CheckBox.
        - The default value is 0.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5,6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_checkbox(name="CheckBox2",text="CheckBox",lefttext=True,checked=True,layout="Window")
            dlg.add_checkbox(name="CheckBox3",text="CheckBox",lefttext=False,checked=True,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_checkbox({},{},{},{},{},{},{})".format(name,layout,text,checked,lefttext,width,height)
        JPT_RUN_LINE(message)

    def add_combobox(self, name, layout, index, options=[], width=0, height=0):
        r"""
        ## Description
        
        Add a ComboBox component to the dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_combobox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `index`
        
        - An _Integer_ specifying the default option to be displayed of the ComboBox.
        - The starting value is 0 (first option -> index=0).
        - This is a required input.
        
        ### `options`
        
        - A _List of String_ specifying the options of the ComboBox.
        - The default value is [].
        
        ### `width`
        
        - An _Integer_ specifying the width of the ComboBox.
        - The default value is 0.
        
        ### `height`
        
        - An _Integer_ specifying the height of the ComboBox.
        - The default value is 0.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4"],index=1,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_combobox({},{},{},{},{},{})".format(name,layout,index,options,width,height)
        JPT_RUN_LINE(message)

    def add_combobox_option(self, name, option_text):
        r"""
        ## Description
        
        Add an option to the ComboBox component.
        
        ## Syntax
        
        ```psj
        dlg.add_combobox_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ### `option_text`
        
        - A _String_ specifying the option added.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4"],layout="Layout1")
            dlg.add_combobox_option(name="ComboBox2",option_text="new_item")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
        
            dlg.generate_window()
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_combobox_option({},{})".format(name,option_text)
        JPT_RUN_LINE(message)

    def add_condition_selector(self, text="Condition"):
        r"""
        ## Description
        
        Add "Condition" to the selection list, allowing user to select condition and store the condition to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_condition_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "Condition".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Value",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_condition_selector(text="Condition 1")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_condition_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_coordinate_selector(self, text="Coordinate"):
        r"""
        ## Description
        
        Add "Coordinate" to the selection list, allowing user to select coordinate and store the coordinate to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_coordinate_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "Coordinate".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Value",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_coordinate_selector(text = "Coordinate 1")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_coordinate_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_edge_selector(self, text="Edge"):
        r"""
        ## Description
        
        Add "Edge" to the selection list, allowing user to select edges and store the selected edges to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_edge_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "Edge".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {19}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Length in X",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label7",text="Length in Y",layout="Layout6")
            dlg.add_textbox(name="TextBox8",layout="Layout6")
            dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label10",text="Length in Z",layout="Layout9")
            dlg.add_textbox(name="TextBox11",layout="Layout9")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_edge_selector(text="Edge 1")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_edge_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_elementedge_selector(self, text="Elem edge"):
        r"""
        ## Description
        
        Add "Elem edge" to the selection list, allowing user to select element edges and store the selected element edges to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_elementedge_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "Elem edge".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {19}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Length in X",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label7",text="Length in Y",layout="Layout6")
            dlg.add_textbox(name="TextBox8",layout="Layout6")
            dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label10",text="Length in Z",layout="Layout9")
            dlg.add_textbox(name="TextBox11",layout="Layout9")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_elementedge_selector(text = "Element edge 1")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_elementedge_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_face_selector(self, text="Face"):
        r"""
        ## Description
        
        Add "Face" to the selection list, allowing user to select faces and store the selected faces to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_face_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "Face".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {19}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Length in X",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label7",text="Length in Y",layout="Layout6")
            dlg.add_textbox(name="TextBox8",layout="Layout6")
            dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label10",text="Length in Z",layout="Layout9")
            dlg.add_textbox(name="TextBox11",layout="Layout9")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_face_selector(text="Face 1")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_face_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_groupbox(self, name, layout, text=""):
        r"""
        ## Description
        
        Add a GroupBox to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_groupbox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying text which will be displayed.
        - The default value is "".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox1",text="Jupiter",layout="Window")
            dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="GroupBox1")
            dlg.add_label(name="Label3",text="Label",layout="Layout2")
            dlg.add_textbox(name="TextBox4",layout="Layout2")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_groupbox({},{},{})".format(name,layout,text)
        JPT_RUN_LINE(message)

    def add_group_selector(self, text="Group"):
        r"""
        ## Description
        
        Add "Group" to the selection list, allowing user to select group and store the group to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_group_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "Group".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Value",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_group_selector(text="Group 1")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_group_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_hlayout(self, name, layout, margin=[]):
        r"""
        ## Description
        
        Add a horizontal Layout to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_hlayout(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `margin`
        
        - A _List_ specifying all the values defining the positions of the creating layout.
          The list of positions is defined in the order of [left,top,right,bottom].
        - The default value is [].
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {8}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Jupiter",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_hlayout(name="footer",margin=[0,10,0,10],layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_hlayout({},{},{})".format(name,layout,margin)
        JPT_RUN_LINE(message)

    def add_imagectrl(self, name, image_file, layout):
        r"""
        ## Description
        
        Add a frame to put an image to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_imagectrl(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `image_file`
        
        - A _String_ specifying the location of an image to display as default.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            image = JPT.GetProgramPath() + \
                r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt_Pics\M30.JPG"
            dlg.add_imagectrl(name="ImageCtrl",image_file=image,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_imagectrl({},{},{})".format(name,image_file,layout)
        JPT_RUN_LINE(message)

    def add_label(self, name, layout, text="", width=0, height=0, text_halign="left", text_valign="top"):
        r"""
        ## Description
        
        Add a Label to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_label(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying text which will be displayed.
        - The default value is "".
        
        ### `width`
        
        - An _Integer_ specifying the width of the Label.
        - The default value is 0.
        
        ### `height`
        
        - An _Integer_ specifying the height of the Label.
        - The default value is 0.
        
        ### `text_halign`
        
        - A _String_ specifying the alignment in horizontal direction:
          - "left": align the showing text to the left in the horizontal direction.
          - "center": align the showing text to the center in the horizontal direction.
          - "right": align the showing text to the right in the horizontal direction.
        - The default value is "left".
        
        ### `text_valign`
        
        - A _String_ specifying the alignment in vertical direction:
          - "top": align the showing text to the top in the vertical direction.
          - "middle": align the showing text to the middle in the vertical direction.
          - "bottom": align the showing text to the bottom in the vertical direction.
        - The default value is "top".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5-6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_label(name="Label2",text="Label",width=30,height=30,
              text_halign="center",text_valign="middle",layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_label({},{},{},{},{},{},{})".format(name,layout,text,width,height,text_halign,text_valign)
        JPT_RUN_LINE(message)

    def add_layout(self, name, layout, orientation, margin=[]):
        r"""
        ## Description
        
        Add a Layout to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_layout(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `orientation`
        
        - An _Orientation object_ specifying the arrangement direction of inside components:
          - _orientation.horizontal_: all components inside are arranged horizontally.
          - _orientation.vertical_: all components inside are arranged vertically.
        - This is a required input.
        
        ### `margin`
        
        - A _List_ specifying all the values defining the positions of the creating Layout.
          The list of positions is defined in the order of [left,top,right,bottom].
        - The default value is [].
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,margin=[0,10,0,10],layout="Window")
            dlg.add_label(name="Label2",text="Jupiter",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_layout({},{},{},{})".format(name,layout,orientation,margin)
        JPT_RUN_LINE(message)

    def add_listbox(self, name, layout, multisel=False, options=[], width=0, height=0):
        r"""
        ## Description
        
        Add a ListBox to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_listbox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `multisel`
        
        - A _Boolean_ specifying the permission that allow user to select multiple values at the same time:
          - _True_: user can select multiple values.
          - _False_: user can select only one value per time.
        - The default value is False.
        
        ### `options`
        
        - A _List of String_ specifying all the options of the ListBox component.
        - The default value is [].
        
        ### `width`
        
        - An _Integer_ specifying the width of the ListBox.
        - The default value is 0.
        
        ### `height`
        
        - An _Integer_ specifying the height of the ListBox.
        - The default value is 0.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5-6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_listbox(name="ListBox3",multisel=True,
              options=["item1","item2","item3"],width=100,height=150,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
        
            dlg.generate_window()
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_listbox({},{},{},{},{},{})".format(name,layout,multisel,options,width,height)
        JPT_RUN_LINE(message)

    def add_listbox_option(self, name, option_text):
        r"""
        ## Description
        
        Add an option to the ListBox component.
        
        ## Syntax
        
        ```psj
        dlg.add_listbox_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component.
        - This is a required input.
        
        ### `option_text`
        
        - A _String_ specifying the option added.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_listbox(name="ListBox3",multisel=True,
              options=["item1","item2","item3"],width=100,height=150,layout="Window")
            dlg.add_listbox_option(name="ListBox3",option_text="new_item")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_listbox_option({},{})".format(name,option_text)
        JPT_RUN_LINE(message)

    def add_node_selector(self, text=""):
        r"""
        ## Description
        
        Add "Node" to the selection list, allowing user to select nodes and store the selected nodes to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_node_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {11}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_listbox(name="ListBox3",multisel=True,options=["item1","item2","item3"],width=100,height=100,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_node_selector()
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_node_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_pageitem(self, name, page_name, page_header, bk_color=16777215, text_color=0):
        r"""
        ## Description
        
        Add a new PageItem to the created/selected PagesCtrl.
        
        ## Syntax
        
        ```psj
        dlg.add_pageitem(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created PagesCtrl component.
        - This is a required input.
        
        ### `page_name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `page_header`
        
        - A _String_ specifying text which will be displayed as PageItem header.
        - This is a required input.
        
        ### `bk_color`
        
        - An _Integer_ specifying the background color.
        - The default value is 16777215.
        
        ### `text_color`
        
        - An _Integer_ specifying the text color.
        - The default value is 0.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_pagesctrl(name="PagesCtrl4",layout="Window")
            dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem5",page_header="Page header 1")
            dlg.add_node_selector()
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_pageitem({},{},{},{},{})".format(name,page_name,page_header,bk_color,text_color)
        JPT_RUN_LINE(message)

    def add_pagesctrl(self, name, layout, show_header=True, current_page=0, sel_color=13158460, show_separator=True, width=0, height=0, text_align="center"):
        r"""
        ## Description
        
        Add a PagesCtrl (wizard type) to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_pagesctrl(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created layout name.
          The created layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `show_header`
        
        - A _Boolean_ specifying the state of the PageItem's header:
          - _True_: PageItem's header will be shown.
          - _False_: PageItem's header will be hidden.
        - The default value is _True_.
        
        ### `current_page`
        
        - An _Integer_ specifying the PageItem shown by default (starts from 0).
        - The default value is 0.
        
        ### `sel_color`
        
        - An _Integer_ specifying the highlight color when selecting a PageItem.
        - The default value is 13158460.
        
        ### `show_separator`
        
        - A _Boolean_ specifying the stage of separator:
          - _True_: Show the separate border.
          - _False_: Do not show the separate border.
        - The default value is _True_.
        
        ### `width`
        
        - An _Integer_ specifying the width of the PagesCtrl.
        - The default value is 0.
        
        ### `height`
        
        - An _Integer_ specifying the height of the PagesCtrl.
        - The default value is 0.
        
        ### `text_align`
        
        - A _String_ specifying the text alignment type (left-center-right) set for PageItem.
        - The default value is "center".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_pagesctrl(name="PagesCtrl4",current_page=2,width=300,height=300,text_align="right",layout="Window")
            dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem5",page_header="PageItem 1")
            dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem6",page_header="PageItem 2")
            dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem7",page_header="PageItem 3")
            dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem8",page_header="PageItem 4")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_pagesctrl({},{},{},{},{},{},{},{},{})".format(name,layout,show_header,current_page,sel_color,show_separator,width,height,text_align)
        JPT_RUN_LINE(message)

    def add_part_selector(self, text=""):
        r"""
        ## Description
        
        Add "Part" to the selection list, allowing user to select parts and store the selected parts to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_part_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {19}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Length in X",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label7",text="Length in Y",layout="Layout6")
            dlg.add_textbox(name="TextBox8",layout="Layout6")
            dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label10",text="Length in Z",layout="Layout9")
            dlg.add_textbox(name="TextBox11",layout="Layout9")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_part_selector()
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_part_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_radiobutton(self, name, layout, text="", width=0, height=0, checked=False, group=False):
        r"""
        ## Description
        
        Add a RadioButton to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_radiobutton(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying text which will be displayed.
        - The default value is "".
        
        ### `width`
        
        - An _Integer_ specifying the width of the RadioButton.
        - The default value is 0.
        
        ### `height`
        
        - An _Integer_ specifying the height of the RadioButton.
        - The default value is 0.
        
        ### `checked`
        
        - A _Boolean_ specifying the default state of this component:
          - _True_: the default state of this component is checked.
          - _False_: the default state of this component is unchecked.
        - The default value is False.
        
        ### `group`
        
        - A _Boolean_ specifying the group in which this RadioButton will be added to:
          - _True_: creating RadioButton will be added separately from the previous RadioButton (different group of button). So, at the time selecting the creating RadioButton, the selected RadioButton will not be deselected.
          - _False_: creating RadioButton will be added to the same group with previous RadioButton. So, at the time selecting the creating RadioButton, the selected RadioButton will be deselected.
        - The default value is False.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_radiobutton(name="RadioButton16",text="RadioButton",layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_radiobutton({},{},{},{},{},{},{})".format(name,layout,text,width,height,checked,group)
        JPT_RUN_LINE(message)

    def add_richeditbox(self, name, layout, text="", width=60, height=22):
        r"""
        ## Description
        
        Add a rich edit box to the dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_richeditbox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying text displayed by default.
        - The default value is "".
        
        ### `width`
        
        - An _Integer_ specifying the width of the rich edit box.
        - The default value is 60.
        
        ### `height`
        
        - An _Integer_ specifying the height of the rich edit box.
        - The default value is 22.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5-6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_richeditbox(name="RichEditBox17",text="RichEditBox content",
                width=200,height=200,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_richeditbox({},{},{},{},{})".format(name,layout,text,width,height)
        JPT_RUN_LINE(message)

    def add_separator(self, name, layout):
        r"""
        ## Description
        
        Add a Separator to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_separator(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout18",orientation=orientation.vertical,layout="Window")
            dlg.add_label(name="Label19",text="Label",text_valign="top",layout="Layout18")
            dlg.add_separator(name="Separator20",layout="Layout18")
            dlg.add_textbox(name="TextBox21",layout="Layout18")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_separator({},{})".format(name,layout)
        JPT_RUN_LINE(message)

    def add_slider(self, name, layout, width=60, height=22, min=0, max=100, pos=0, vertical=False, show_ticks=True, show_border=False, show_bothticks=False):
        r"""
        ## Description
        
        Add a SliderBar to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_slider(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `width`
        
        - An _Integer_ specifying the width of the SliderBar.
        - The default value is 60.
        
        ### `height`
        
        - An _Integer_ specifying the height of the SliderBar.
        - The default value is 22.
        
        ### `min`
        
        - An _Integer_ specifying the minimum value of the SliderBar.
        - The default value is 0.
        
        ### `max`
        
        - An _Integer_ specifying the maximum value of the SliderBar.
        - The default value is 100.
        
        ### `pos`
        
        - An _Integer_ specifying the initial position of the scroller.
        - The default value is 0.
        
        ### `vertical`
        
        - A _Boolean_ specifying the direction of the SliderBar:
          - _True_: creating SliderBar will be put in the vertical direction.
          - _False_: creating SliderBar will be put in the horizontal direction.
        - The default value is _False_.
        
        ### `show_ticks`
        
        - A _Boolean_ specifying the state of the slider's tick mark:
          - _True_: show all the tick mark.
          - _False_: hide all the tick mark.
        - The default value is _True_.
        
        ### `show_border`
        
        - A _Boolean_ specifying the state of the slider's border:
          - _True_: show outside border of the creating SliderBar.
          - _False_: hide outside border of the creating SliderBar.
        - The default value is _False_.
        
        ### `show_bothticks`
        
        - A _Boolean_ specifying the way to display tick mark:
          - _True_: show tick mark on both side of the SliderBar.
          - _False_: show tick mark on one side only of the SliderBar.
        - The default value is _False_.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5-6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_slider(name="Slider21",width=100,height=100,min=0,max=100,pos=4,
              vertical=True,show_bothticks=True,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_slider({},{},{},{},{},{},{},{},{},{},{})".format(name,layout,width,height,min,max,pos,vertical,show_ticks,show_border,show_bothticks)
        JPT_RUN_LINE(message)

    def add_space(self, layout, name="", orientation="", size=0):
        r"""
        ## Description
        
        Add a space between the created components.
        
        ## Syntax
        
        ```psj
        dlg.add_space(...)
        ```
        
        ## Inputs
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - The default value is "".
        
        ### `orientation`
        
        - A _String_ specifying the direction to add a space component between 2 components:
          - "horizontal": Add a space component on the horizontal direction.
          - "vertical": Add a space component on the vertical direction.
        - The default value is "".
        
        ### `size`
        
        - An _Integer_ specifying the size of space.
        - The default value is 0.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {8,16,19}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Field 1",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_space(orientation="vertical",size=2,layout="Window")
            dlg.add_layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label6",text="Field 2",layout="Layout5")
            dlg.add_textbox(name="TextBox7",layout="Layout5")
            dlg.add_layout(name="Layout8",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label9",text="Field 3",layout="Layout8")
            dlg.add_textbox(name="TextBox10",layout="Layout8")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_space({},{},{},{})".format(layout,name,orientation,size)
        JPT_RUN_LINE(message)

    def add_spin(self, name, min, max, pos, increment, layout, type=spin.integer, precision=1):
        r"""
        ## Description
        
        Add a Spin to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_spin(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `min`
        
        - An _Double_ specifying the minimum value of the Spin range.
          If `type` is _spin.double_, the value will be rounded up.
        - This is a required input.
        
        ### `max`
        
        - An _Double_ specifying the maximum value of the Spin range.
          If `type` is _spin.double_, the value will be rounded up.
        - This is a required input.
        
        ### `pos`
        
        - An _Double_ specifying the initial value (starting position) of the Spin range.
          If `type` is _spin.double_, the value will be rounded up.
        - This is a required input.
        
        ### `increment`
        
        - An _Double_ specifying the increment step of the Spin.
          If `type` is _spin.double_, the value will be rounded up.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `type`
        
        - An _Enum_ specifying type of Spin:
          - spin.integer: Integer type
          - spin.double: Double type
        - The default value is spin.integer.
        
        ### `precision`
        
        - An _Integer_ specifying the precision (number of digits after zero) of the input value.
          If `type` is _spin.integer_, this input will be ignored.
        - The default value is 1.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5-7}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_spin(name="Spin2",min=1,max=100,pos=2,increment=2,layout="Window")
            dlg.add_spin(name="Spin3",type=spin.double,min=0.000000,max=50.000000,pos=1.500000,
                increment=1.500000,precision=3,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_spin({},{},{},{},{},{},{},{})".format(name,min,max,pos,increment,layout,type,precision)
        JPT_RUN_LINE(message)

    def add_table(self, rows, columns, layout, name="", menus=[], width=260, height=260, show_grid_line=True, show_row_number=True, show_col_header=True):
        r"""
        ## Description
        
        Add a Table to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_table(...)
        ```
        
        ## Inputs
        
        ### `rows`
        
        - An _Integer_ specifying the number of rows.
        - This is a required input.
        
        ### `columns`
        
        - A _List of String_ specifying the number of columns and heading name of each column or a _[TableColumnInfoVector](../data-type/psj-gui/TableColumnInfoVector)_ object specifying the information of columns in Table.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - The default value is "".
        
        ### `menus`
        
        - A _List of String_ specifying the context menu options (right mouse click):
          - "clear": clear all the existing data.
          - "cut": cut the content of the selected cell.
          - "copy": copy the content of the selected cell.
          - "paste": paste a value/values which has been copied/cut to a selected cell/select cells.
          - "insert row": insert a single row to the bottom of the selected cell.
          - "delete row": delete a selected row/selected rows.
          - "from file": load the data from csv file into the Table.
          - "to file": export the data from the Table to a specific csv file.
        - The default value is [].
        
        ### `width`
        
        - An _Integer_ specifying the width of the Table.
        - The default value is 260.
        
        ### `height`
        
        - An _Integer_ specifying the height of the Table.
        - The default value is 260.
        
        ### `show_grid_line`
        
        - A _Boolean_ specifying the display state of grid lines:
          - _True_: show Table grid lines.
          - _False_: hide Table grid lines.
        - The default value is _True_.
        
        ### `show_row_number`
        
        - A _Boolean_ specifying the state of showing/hiding row header:
          - _True_: show row header.
          - _False_: hide row header.
        - The default value is _True_.
        
        ### `show_col_header`
        
        - A _Boolean_ specifying the state of showing/hiding column header:
          - _True_: show column header.
          - _False_: hide column header.
        - The default value is _True_.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5-11}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",rows=6,
                columns=["Heading1","Heading2","Heading3"],layout="Window",
                menus=["clear","cut","copy",
                        "paste","insert row",
                        "delete row","from file","to file"],
                width=200,height=200,
                show_grid_line=False,show_row_number=True,show_col_header=True)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_table({},{},{},{},{},{},{},{},{},{})".format(rows,columns,layout,name,menus,width,height,show_grid_line,show_row_number,show_col_header)
        JPT_RUN_LINE(message)

    def add_table_right_menu(self, name, menus):
        r"""
        ## Description
        
        Add options to the context menu (Right click event) of Table.
        
        ## Syntax
        
        ```psj
        dlg.add_table_right_menu(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `menus`
        
        - A _List of String_ specifying the menus which will be appeared after executing the right click button event on the Table.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13-17}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",
                menus=["Set Cell Color",
                    "Set Text Color",
                    "Set Column Width",
                    "Custom Menu"])
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_table_right_menu({},{})".format(name,menus)
        JPT_RUN_LINE(message)

    def add_table_sel_option(self, name, row, col, cell, index, options=[]):
        r"""
        ## Description
        
        Set combobox cell in the Table.
        
        ## Syntax
        
        ```psj
        dlg.add_table_sel_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `row`
        
        - A _Integer_ specifying the position in the horizontal direction of the cell (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - A _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table. This argument is only used when _row_ and _col_ are not specified.
          - TableCellID(row,col) defines a cell object
          - TableCellID.row_number returns row number of the cell
          - TableCellID.col_number returns column number of the cell
        - This is a required input.
        
        ### `index`
        
        - An _Integer_ specifying the default option to be displayed of the ComboBox.
        - The starting value is 0 (first option -> index=0).
        - This is a required input.
        
        ### `options`
        
        - A _List of String_ specifying the options of the ComboBox.
        - The default value is [].
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6-7}
        from pyjdg import *
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_table(name="Table2",width=260,height=160,columns=["Heading1","Heading2"],rows=5,layout="Window")
            dlg.generate_window()
            dlg.add_table_cell_option(name="Table2",cell=TableCellID(0,0),options=["0","2"],index=1)
            dlg.add_table_cell_option(name="Table2",row=0,col=1,options=["0","2"],index=1)
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_table_sel_option({},{},{},{},{},{})".format(name,row,col,cell,index,options)
        JPT_RUN_LINE(message)

    def add_tabwnd(self, name, layout, width=60, height=22):
        r"""
        ## Description
        
        Add a TabWnd (tab window) to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_tabwnd(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the tab window component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `width`
        
        - An _Integer_ specifying the width of the tab window.
        - The default value is 60.
        
        ### `height`
        
        - An _Integer_ specifying the height of the tab window.
        - The default value is 22.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_tabwnd(name="TabWnd1",width=200,height=200,layout="Window")
            dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem2",page_text="TabItem",page_orientation="horizontal")
            dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem3",page_text="TabItem")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_tabwnd({},{},{},{})".format(name,layout,width,height)
        JPT_RUN_LINE(message)

    def add_tabwnd_page(self, name, page_name, page_text="", page_orientation="vertical"):
        r"""
        ## Description
        
        Add a TabItem (page) to the TabWnd component.
        
        ## Syntax
        
        ```psj
        dlg.add_tabwnd_page(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the TabWnd component in which the creating TabItem will be put added to.
        - This is a required input.
        
        ### `page_name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `page_text`
        
        - A _String_ specifying text which will be displayed as a title.
        - The default value is "".
        
        ### `page_orientation`
        
        - A _String_ specifying the orientation of the creating tab page. It has 2 options:
          - "vertical": aligning all the inside components in the vertical direction.
          - "horizontal": aligning all the inside components in the horizontal direction.
        - The default value is "vertical".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6,9}
        
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_tabwnd(name="TabWnd2",width=200,height=200,layout="Window")
            dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem3",page_text="TabItem",page_orientation="vertical")
            dlg.add_label(name="Label5",text="Label",text_halign="left",text_valign="top",layout="TabItem3")
            dlg.add_textbox(name="TextBox6",layout="TabItem3")
            dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem4",page_text="TabItem",page_orientation="horizontal")
            dlg.add_label(name="Label7",text="Label",text_halign="left",text_valign="top",layout="TabItem4")
            dlg.add_textbox(name="TextBox8",layout="TabItem4")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_tabwnd_page({},{},{},{})".format(name,page_name,page_text,page_orientation)
        JPT_RUN_LINE(message)

    def add_textbox(self, name, layout, text="", readonly=False, text_color=0, bk_color=16777215, width=0, height=0, text_align="Left", type="string"):
        r"""
        ## Description
        
        Add a Textbox to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_textbox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying text which will be displayed.
        - The default value is "".
        
        ### `readonly`
        
        - A _Boolean_ specifying the read-only state of Textbox is used or not.
          - _True_: The text is read-only state. It can't be editable.
          - _False_: The text can be edited manually.
        - The default value is _False_.
        
        ### `text_color`
        
        - An _Integer_ specifying the text color.
        - The default value is 0.
        
        ### `bk_color`
        
        - An _Integer_ specifying the background color.
        - The default value is 16777215.
        
        ### `width`
        
        - An _Integer_ specifying the width of the Textbox.
        - The default value is 0.
        
        ### `height`
        
        - An _Integer_ specifying the height of the Textbox.
        - The default value is 0.
        
        ### `text_align`
        
        - A _String_ specifying the text position which will be displayed.
          - "Left": align text to left side.
          - "Center": center text to the middle.
          - "Right": align text to right side.
        - The default value is "Left".
        
        ### `type`
        
        - A _String_ specifying the data type for the Textbox:
          - "string": input values are in the _String_ format.
          - "double": input values are in the _Double_ format.
          - "integer": input values are in the _Integer_ format.
        - The default value is "string".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7-8,11-12,15-16,19-20,30-31,34-35}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label3",text="String Type",width=100,text_halign="left",text_valign="top",layout="Layout2")
            dlg.add_textbox(name="TextBox4",width=150,height=25,readonly=True,
                text="TechnoStar",type="string",text_align="left",layout="Layout2")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label7",text="String Type",width=100,text_halign="left",text_valign="top",layout="Layout6")
            dlg.add_textbox(name="TextBox8",width=150,height=25,readonly=False,
                text="12345",type="string",bk_color=16711168,text_color=255,text_align="left",layout="Layout6")
            dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label10",text="Integer Type",width=100,text_halign="left",text_valign="top",layout="Layout9")
            dlg.add_textbox(name="TextBox11",width=150,height=25,readonly=False,
                text="TechnoStar",type="integer",text_align="center",layout="Layout9")
            dlg.add_layout(name="Layout12",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label13",text="Integer Type",width=100,text_halign="left",text_valign="top",layout="Layout12")
            dlg.add_textbox(name="TextBox14",width=150,height=25,readonly=True,
                text="12345",bk_color=65535,text_color=255,type="integer",text_align="center",layout="Layout12")
            font_TextBox14=PSJFont()
            font_TextBox14.size=12
            font_TextBox14.bold=True
            font_TextBox14.italic=False
            font_TextBox14.underline=True
            font_TextBox14.strikeout=False
            dlg.set_item_font(name="TextBox14",font=font_TextBox14)
            dlg.add_layout(name="Layout15",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label16",text="Double Type",width=100,text_halign="left",text_valign="top",layout="Layout15")
            dlg.add_textbox(name="TextBox17",width=150,height=25,readonly=False,
                text="TechnoStar",type="double",text_align="right",layout="Layout15")
            dlg.add_layout(name="Layout18",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label19",text="Double Type",width=100,text_halign="left",text_valign="top",layout="Layout18")
            dlg.add_textbox(name="TextBox20",width=150,height=25,readonly=True,
                text="12345.123",type="double",text_align="right",layout="Layout18")
            font_TextBox20=PSJFont()
            font_TextBox20.size=12
            font_TextBox20.bold=False
            font_TextBox20.italic=True
            font_TextBox20.underline=True
            font_TextBox20.strikeout=False
            dlg.set_item_font(name="TextBox20",font=font_TextBox20)
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_textbox({},{},{},{},{},{},{},{},{},{})".format(name,layout,text,readonly,text_color,bk_color,width,height,text_align,type)
        JPT_RUN_LINE(message)

    def add_vertex_selector(self, text=""):
        r"""
        ## Description
        
        Add "Vertex" to the selection list, allowing user to select vertexes and store the selected vertexes to the selection list.
        
        ## Syntax
        
        ```psj
        dlg.add_vertex_selector(...)
        ```
        
        ## Inputs
        
        ### `text`
        
        - A _String_ specifying the title of selector.
        - The default value is "".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {10}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_vertex_selector()
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_vertex_selector({})".format(text)
        JPT_RUN_LINE(message)

    def add_vlayout(self, name, layout, margin=[]):
        r"""
        ## Description
        
        Add a vertical Layout to the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.add_vlayout(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the created component.
        - This is a required input.
        
        ### `layout`
        
        - A _String_ specifying the created Layout name.
          The created Layout can be a GroupBox component, Layout component, etc.
        - This is a required input.
        
        ### `margin`
        
        - A _List_ specifying all the value defining the positions of the creating layout.
          The list of positions is defined in the order of [left,top,right,bottom].
        - The default value is [].
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_vertex_selector()
            dlg.add_vlayout(name="footer",margin=[0,0,0,20],layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.add_vlayout({},{},{})".format(name,layout,margin)
        JPT_RUN_LINE(message)

    def all_table_sel_option(self, name, row, col, cell, options=[], index=None):
        r"""
        ## Description
        
        Set combobox cell in the Table.
        
        ## Syntax
        
        ```psj
        dlg.add_table_sel_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `row`
        
        - A _Integer_ specifying the position in the horizontal direction of the cell (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - A _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table. This argument is only used when _row_ and _col_ are not specified.
          - TableCellID(row,col) defines a cell object
          - TableCellID.row_number returns row number of the cell
          - TableCellID.col_number returns column number of the cell
        - This is a required input.
        
        ### `options`
        
        - A _List of String_ specifying the options of the ComboBox.
        - The default value is [].
        
        ### `index`
        
        - An _Integer_ specifying the default option to be displayed of the ComboBox.
        - The starting value is 0 (first option -> index=0).
        - This is a required input.
        
        ## Return Code
        
        - A _[TableCellRangeVector](../data-type/psj-gui/TableCellRangeVector)_ object or _List of [TableCellRange](../data-type/psj-gui/TableCellRange)_ specifying the methods of ranges.
        
        ## Sample Code
        
        ```psj {6}
        from pyjdg import *
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_table(name="Table2",width=260,height=160,columns=["Heading1","Heading2"],rows=5,layout="Window")
            dlg.generate_window()
            dlg.add_table_cell_option(name="Table2",cell=TableCellID(0,0),options=["0","2"],index=1)
            dlg.add_table_cell_option(name="Table2",row=0,col=1,options=["0","2"],index=1)
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.all_table_sel_option({},{},{},{},{},{})".format(name,row,col,cell,options,index)
        JPT_RUN_LINE(message)

    def clear_combobox(self, name):
        r"""
        ## Description
        
        Clear all options of a specified ComboBox.
        
        ## Syntax
        
        ```psj
        dlg.clear_combobox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def on_button_clicked (dlg):
            dlg.clear_combobox(name="ComboBox2")
            print("All ComboBox options are cleared")
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4"],index=1,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Button3",text="Clear ComboBox",width=100,height=30,bk_color=15790320,layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_button_clicked(name="Button3",callfunc=on_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.clear_combobox({})".format(name)
        JPT_RUN_LINE(message)

    def clear_listbox(self, name):
        r"""
        ## Description
        
        Clear all options of a specified ListBox.
        
        ## Syntax
        
        ```psj
        dlg.clear_listbox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def on_button_clicked (dlg):
            dlg.clear_listbox(name="ListBox2")
            print("All ListBox options are cleared")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_listbox(name="ListBox2",multisel=True,
              options=["item1","item2","item3"],width=100,height=150,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Button3",text="Clear ListBox",width=100,height=30,bk_color=15790320,layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_button_clicked(name="Button3",callfunc=on_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.clear_listbox({})".format(name)
        JPT_RUN_LINE(message)

    def clear_table_all(self, name):
        r"""
        ## Description
        
        Clear all content of the Table.
        
        ## Syntax
        
        ```psj
        dlg.clear_table_all(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def on_click_clear_all(dlg):
            dlg.clear_table_all(name="Table1")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=14,
                columns=["Heading1","Heading2","Heading3","Heading4","Heading5"],
                layout="Window",width=560,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Clear",text="Clear Value",
                width=80,height=30,layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            for i in range(14):
                for j in range(5):
                    dlg.set_cell_value(name="Table1",row=i,col=j,value=str(i+j))
            dlg.on_command(name="Clear",callfunc=on_click_clear_all)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.clear_table_all({})".format(name)
        JPT_RUN_LINE(message)

    def clear_table_cell(self, name, row, col, text=[]):
        r"""
        ## Description
        
        Clear content of a specific cell of Table.
        
        ## Syntax
        
        ```psj
        dlg.clear_table_cell(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `row`
        
        - An _Integer_ specifying the position in the horizontal direction of the cell (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying the new content of the cleared cell (if needed).
        - The default value is [].
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {11-14}
        from pyjdg import *
        
        # Clear a specific cell by using right-click > Clear Cell
        # The content of specific cell will be cleared
        # Text Change's data will be new content of cleared cell if it is entered  
        def set_table_read_from_file(dlg,name,menu):
            table_cell = dlg.get_table_sel_cell(name)
            if table_cell.size()>0:
                text_change=dlg.get_item_text(name="Textbox4")
                if menu == "Clear Cell":
                    dlg.clear_table_cell(name,
                        row=table_cell[0].row_number,
                        col=table_cell[0].col_number,
                        text=text_change)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",
                orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label3",text="Text Change",layout="Layout1")
            dlg.add_textbox(name="Textbox4",layout="Layout1")
            dlg.add_table(name="Table1",rows=5,
                columns=["String","Integer","Double"],
                layout="Window",width=360,height=260)
            dlg.set_table_column_data_type(name="Table1",
                col=0,data_type="String")
            dlg.set_table_column_data_type(name="Table1",
                col=1,data_type="Integer")
            dlg.set_table_column_data_type(name="Table1",
                col=2,data_type="Double",precision=5)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")  
            dlg.add_table_right_menu(name="Table1",
                menus=["Clear Cell"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=set_table_read_from_file)
            dlg.set_table_cell_checkbox(name="Table1",row=0,col=0,text="Checkbox",
                checked=True)
            dlg.set_cell_value(name="Table1",
                row=1,col=0,value=["Option2","Option3"])
            dlg.set_cell_value(name="Table1",row=0,col=1,value="1")
            dlg.set_cell_value(name="Table1",row=1,col=1,value=[2,3])
            dlg.set_table_cell_button(name="Table1",row=0,col=2,text="Button")
            dlg.set_cell_value(name="Table1",row=1,col=2,value=[2.5,3.5]) 
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.clear_table_cell({},{},{},{})".format(name,row,col,text)
        JPT_RUN_LINE(message)

    def clear_table_range(self, name, cell_range):
        r"""
        ## Description
        
        Clear content of the specific range by position in the Table.
        
        ## Syntax
        
        ```psj
        dlg.clear_table_range(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `cell_range`
        
        - A _[TableCellRange](../data-type/psj-gui/TableCellRange)_ object specifying the information of a specific range (multi cells).
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {8-9}
        from pyjdg import *
        
        def on_click_clear(dlg):
            left=int(dlg.get_item_text(name="TextBox5"))
            top=int(dlg.get_item_text(name="TextBox7"))
            right=int(dlg.get_item_text(name="TextBox9"))
            bottom=int(dlg.get_item_text(name="TextBox11"))
            dlg.clear_table_range(name="Table1",
                cell_range=TableCellRange(left=left,top=top,right=right,bottom=bottom))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=14,
                columns=["Heading1","Heading2","Heading3","Heading4","Heading5"],
                layout="Window",width=560,height=260)
            dlg.add_groupbox(name="GroupBox2",text="Position",layout="Window")
            dlg.add_layout(name="Layout3",orientation=orientation.horizontal,
                layout="GroupBox2")
            dlg.add_label(name="Label4",text="Left",layout="Layout3")
            dlg.add_textbox(name="TextBox5",layout="Layout3")
            dlg.add_label(name="Label6",text="Top",layout="Layout3")
            dlg.add_textbox(name="TextBox7",layout="Layout3")
            dlg.add_label(name="Label8",text="Right",layout="Layout3")
            dlg.add_textbox(name="TextBox9",layout="Layout3")
            dlg.add_label(name="Label10",text="Bottom",layout="Layout3")
            dlg.add_textbox(name="TextBox11",layout="Layout3")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Clear",text="Clear Value",
                width=80,height=30,layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            for i in range(14):
                for j in range(5):
                    dlg.set_cell_value(name="Table1",row=i,col=j,value=str(i+j))
            dlg.on_command(name="Clear",callfunc=on_click_clear)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.clear_table_range({},{})".format(name,cell_range)
        JPT_RUN_LINE(message)

    def close(self):
        r"""
        ## Description
        
        Close the dialog.
        
        ## Syntax
        
        ```psj
        dlg.close(...)
        ```
        
        ## Inputs
        
        This function does not require any input value.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def on_button_clicked(dlg):
            dlg.close()
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,
                layout="Window")
            dlg.add_label(name="Label2",
                text="Click any button to close this dialog!",layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_button_clicked(name="ButtonApply",callfunc=on_button_clicked)
            dlg.on_button_clicked(name="ButtonOk",callfunc=on_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.close({})".format('')
        JPT_RUN_LINE(message)

    def delete_table_column(self, name, position):
        r"""
        ## Description
        
        Delete column at a specific position in the Table.
        
        ## Syntax
        
        ```psj
        dlg.delete_table_column(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `position`
        
        - An _Integer_ specifying the position of column to be deleted.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {8}
        from pyjdg import *
        
        def on_menu(dlg,name,menu):
            sel_ranges=dlg.get_table_sel_range(name="Table1")
            if sel_ranges.size()>0:
                position=sel_ranges[0].left
            dlg.delete_table_column(name="Table1",position=position)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2","Heading3"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",menus=["Delete Column"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_menu)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.delete_table_column({},{})".format(name,position)
        JPT_RUN_LINE(message)

    def delete_table_row(self, name, position):
        r"""
        ## Description
        
        Delete row at a specific position in the Table.
        
        ## Syntax
        
        ```psj
        dlg.delete_table_row(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `position`
        
        - An _Integer_ specifying the position of row to be deleted.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        
        def on_menu(dlg,name,menu):
            sel_ranges=dlg.get_table_sel_range(name="Table1")
            if sel_ranges.size()>0:
                position=sel_ranges[0].top
            dlg.delete_table_row(name="Table1",position=position)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2","Heading3"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",menus=["Delete Row"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_menu)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.delete_table_row({},{})".format(name,position)
        JPT_RUN_LINE(message)

    def disable_item(self, name):
        r"""
        ## Description
        
        Change the "Enable" option of an inputted component to off (Disabled).
        
        ## Syntax
        
        ```psj
        dlg.disable_item(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {14}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_label(name="Label1",text="Label",layout="Window")
            dlg.add_textbox(name="TextBox2",layout="Window")
            dlg.add_textbox(name="TextBox3",layout="Window")
            dlg.add_textbox(name="TextBox4",layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.disable_item(name="TextBox3")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.disable_item({})".format(name)
        JPT_RUN_LINE(message)

    def do_modal(self):
        r"""
        ## Description
        
        Execute the created dialog (show the dialog with all the created functions) with Modal mode.
        
        ## Syntax
        
        ```psj
        dlg.do_modal(...)
        ```
        
        ## Inputs
        
        This function does not require any input value.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {15}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_label(name="Label1",text="Label",layout="Window")
            dlg.add_textbox(name="TextBox2",layout="Window")
            dlg.add_textbox(name="TextBox3",layout="Window")
            dlg.add_textbox(name="TextBox4",layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.disable_item(name="TextBox3")
            dlg.do_modal()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.do_modal({})".format('')
        JPT_RUN_LINE(message)

    def enable_drag_table_row(self, name, enable):
        r"""
        ## Description
        
        Enable to drag table rows to upward/downward.
        
        ## Syntax
        
        ```psj
        dlg.enable_drag_table_row(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Table component.
        - This is a required input.
        
        ### `enable`
        
        - A _Boolean_ specifying the state of dragging table row (upward/downward).
          - _True_: enable to drag the table row
          - _False_: disable to drag the table row
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {22}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,columns=["String","Integer","Double"],
                        layout="Window",width=360,height=260)
            dlg.set_table_column_data_type(name="Table1",col=0,data_type="String")
            dlg.set_table_column_data_type(name="Table1",col=1,data_type="Integer")
            dlg.set_table_column_data_type(name="Table1",col=2,data_type="Double",precision=5)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")   
            dlg.generate_window()
            dlg.set_cell_value(name="Table1",row=0,col=0,value="Option1")
            dlg.set_cell_value(name="Table1",row=1,col=0,value=["Option2","Option3"])
            dlg.set_cell_value(name="Table1",row=0,col=1,value="1")
            dlg.set_cell_value(name="Table1",row=1,col=1,value=[2,3])
            dlg.set_cell_value(name="Table1",row=0,col=2,value="1.5")
            dlg.set_cell_value(name="Table1",row=1,col=2,value=[2.5,3.5])
            dlg.enable_drag_table_row(name="Table1",enable=True)
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.enable_drag_table_row({},{})".format(name,enable)
        JPT_RUN_LINE(message)

    def enable_item(self, name):
        r"""
        ## Description
        
        Change the "Enable" option of an inputted component to on (Enabled).
        
        ## Syntax
        
        ```psj
        dlg.enable_item(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {15}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_label(name="Label1",text="Label",layout="Window")
            dlg.add_textbox(name="TextBox2",layout="Window")
            dlg.add_textbox(name="TextBox3",layout="Window")
            dlg.add_textbox(name="TextBox4",layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.disable_item(name="TextBox3")
            dlg.enable_item(name="TextBox3")
            dlg.generate_window()
            
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.enable_item({})".format(name)
        JPT_RUN_LINE(message)

    def enable_table_cell(self, name, row, col, cell, enable):
        r"""
        ## Description
        
        Set to enable/disable the cell in the table.
        
        ## Syntax
        
        ```psj
        dlg.enable_table_cell(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Table.
        - This is a required input.
        
        ### `row`
        
        - A _Integer_ specifying the position in the horizontal direction of the cell (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - A _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table. This argument is only used when _row_ and _col_ are not specified.
          - TableCellID(row,col) defines a cell object
          - TableCellID.row_number returns row number of the cell
          - TableCellID.col_number returns column number of the cell
        - This is a required input.
        
        ### `enable`
        
        - A _Boolean_ specifying whether to enable/disable cell:
          - _True_: Enable to cell.
          - _False_: Disable to cell.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7,10}
        from pyjdg import *
        
        def on_menu(dlg,name,menu):
            table_cell = dlg.get_table_sel_cell(name)
            if menu == "Disable Cells":
                for cell in table_cell:
                    dlg.enable_table_cell(name="Table1",cell=cell,enable=False)
            elif menu == "Enable Cells":
                for cell in table_cell:
                    dlg.enable_table_cell(name="Table1",cell=cell,enable=True)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",
                menus=["Disable Cells","Enable Cells"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_menu)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.enable_table_cell({},{},{},{},{})".format(name,row,col,cell,enable)
        JPT_RUN_LINE(message)

    def enable_table_column_filter(self, name, col, enable):
        r"""
        ## Description
        
        Add filter option of column of Table.
        
        ## Syntax
        
        ```psj
        dlg.enable_table_column_filter(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the order of the column (starts from 0).
        - This is a required input.
        
        ### `enable`
        
        - A _Boolean_ specifying the state of filter mode of column of Table.
          - _True_: filter mode will be shown
          - _False_: filter mode will be hidden
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {14}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.enable_table_column_filter(name="Table2",col=0,enable=True)
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.enable_table_column_filter({},{},{})".format(name,col,enable)
        JPT_RUN_LINE(message)

    def enable_tabwnd_swap_tab(self, name, enable):
        r"""
        ## Description
        
        Set to enable/disable swap the tab items in a tabwnd.
        
        ## Syntax
        
        ```psj
        dlg.dlg.set_item_visible(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the TabWnd.
        - This is a required input.
        
        ### `enable`
        
        - A _Boolean_ specifying whether to enable/disable swap the tab items:
          - _True_: Enable to swap.
          - _False_: Disable to swap.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_tabwnd(name="TabWnd10",width=200,height=200,layout="Window")
            dlg.enable_tabwnd_swap_tab(name="TabWnd10", enable=False)
            dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem11",page_text="TabItem1")
            dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem12",page_text="TabItem2")
            dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem13",page_text="TabItem3")
            dlg.generate_window()
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.enable_tabwnd_swap_tab({},{})".format(name,enable)
        JPT_RUN_LINE(message)

    def fill_table_by_file(self, name, file, delimiter=","):
        r"""
        ## Description
        
        Write data to Table by CSV file.
        
        ## Syntax
        
        ```psj
        dlg.fill_table_by_file(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `file`
        
        - A _String_ specifying the path link to CSV file.
        - This is a required input.
        
        ### `delimiter`
        
        - A _String_ specifying the character used to separate values (or fields) in the CSV file.
        - The default value is ",".
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        
        def on_command(dlg):
            filePath=dlg.get_item_text(name="Browser3")
            dlg.fill_table_by_file(name="Table5",file=filePath)
        
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_layout(name="Layout2",orientation=orientation.vertical,layout="Window")
            samplePath = JPT.GetProgramPath() + \
                "SampleData\\PSJ\\PSJ-GUI\\RenumberID\\RenumberID_Sample\\RenumberID.csv"
            dlg.add_browser(name="Browser3",mode="file",file_filter=".csv",default=samplePath,layout="Layout2")
            dlg.add_button(name="Button4",text="Fill Table Data",width=80,height=22,bk_color=15790320,layout="Layout2")
            dlg.add_table(name="Table5",width=350,height=250,columns=["Heading1","Heading2","Heading3"],
                rows=10,layout="Layout2")
            dlg.add_label(name="Label6",text="Specify a CSV file and click Fill Table Data button to fill data to Table",
                width=350,text_halign="left",text_valign="top",layout="Window")
            dlg.generate_window()
            dlg.on_button_clicked(name="Button4",callfunc=on_command)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.fill_table_by_file({},{},{})".format(name,file,delimiter)
        JPT_RUN_LINE(message)

    def generate_window(self):
        r"""
        ## Description
        
        Execute the created dialog (show the dialog with all the created functions).
        
        ## Syntax
        
        ```psj
        dlg.generate_window(...)
        ```
        
        ## Inputs
        
        This function does not require any input value.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {15}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_label(name="Label1",text="Label",layout="Window")
            dlg.add_textbox(name="TextBox2",layout="Window")
            dlg.add_textbox(name="TextBox3",layout="Window")
            dlg.add_textbox(name="TextBox4",layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.disable_item(name="TextBox3")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.generate_window({})".format('')
        JPT_RUN_LINE(message)

    def get_cell_label(self, name, row, column):
        r"""
        ## Description
        
        Get label of a button cell, checkbox cell or combobox cell in the Table.
        
        ## Syntax
        
        ```psj
        dlg.get_cell_label(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Table component.
        - This is a required input.
        
        ### `row`
        
        - An _Integer_ specifying the position in the horizontal direction of the cell (starts from 0).
        - This is a required input.
        
        ### `column`
        
        - An _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
        - This is a required input.
        
        ## Return Code
        
        - A _String_ specifying the label of the inputted cell.
        
        ## Sample Code
        
        ```psj {8-9,12-13,16-17}
        from pyjdg import *
        
        def on_cell_button_clicked(dlg,name,cell):
            JPT.ClearLog()
            cellvector=dlg.get_table_sel_cell(name="Table2")
            if cellvector.size() > 0:
                if dlg.is_table_cell_combobox(name="Table2",cell=cellvector[0]):
                    combobox_label= dlg.get_cell_label(name="Table2",
                        row=cellvector[0].row_number,col=cellvector[0].col_number)
                    print("The label of the selected combobox is: " + combobox_label)
                elif dlg.is_table_cell_button(name="Table2",cell=cellvector[0]):
                    button_label= dlg.get_cell_label(name="Table2",
                        row=cellvector[0].row_number,col=cellvector[0].col_number)
                    print("The label of the selected button is: " + button_label)
                elif dlg.is_table_cell_checkbox(name="Table2",cell=cellvector[0]):
                    checkbox_label= dlg.get_cell_label(name="Table2",
                        row=cellvector[0].row_number,col=cellvector[0].col_number)
                    print("The label of the selected checkbox is: " + checkbox_label)
                else:
                    print("Selected cell do not have label")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",width=260,height=260,
                columns=["Heading1","Heading2"],
                rows=5,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",
                layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_cell_value(name="Table2",
                row=0,col=0,
                value=["Option1","Option2","Option3"])
            dlg.set_table_cell_button(name="Table2",
                row=0,col=1,text="Button")
            dlg.set_table_cell_checkbox(name="Table2",row=1,
                col=0,text="Checkbox",checked=True)
            dlg.on_table_sel_changed(name="Table2",
                callfunc=on_cell_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_cell_label({},{},{})".format(name,row,column)
        JPT_RUN_LINE(message)

    def get_cell_value(self, name, row, col, option=-1):
        r"""
        ## Description
        
        Get value of a specific cell of Table.
        
        ## Syntax
        
        ```psj
        dlg.get_cell_value(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Table component.
        - This is a required input.
        
        ### `row`
        
        - An _Integer_ specifying the position in the horizontal direction of the cell (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
        - This is a required input.
        
        ### `option`
        
        - An _Integer_ specifying the index number inside of combobox cell.
        - The default value is -1 (get the displayed content of cell).
        
        ## Return Code
        
        - A _String_ specifying the value of the inputted cell.
        
        ## Sample Code
        
        ```psj {6-8,10-12,14-16}
        from pyjdg import *
        
        def get_table_cell_value(dlg,name,cell):
            cellvector=dlg.get_table_sel_cell(name="Table1")
            if cellvector.size()>0:
                value_cell=dlg.get_cell_value(name="Table1",
                    row=cellvector[0].row_number,
                    col=cellvector[0].col_number)
                dlg.set_item_text(name="Textbox4",text=value_cell)
                value_cell=dlg.get_cell_value(name="Table1",
                    row=cellvector[0].row_number,
                    col=cellvector[0].col_number,option=1)
                dlg.set_item_text(name="Textbox5",text=value_cell)
                value_cell=dlg.get_cell_value(name="Table1",
                    row=cellvector[0].row_number,
                    col=cellvector[0].col_number,option=2)
                dlg.set_item_text(name="Textbox6",text=value_cell)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,200,0],
                orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label3",text="Get Displayed Value",width=100,layout="Layout1")
            dlg.add_textbox(name="Textbox4",layout="Layout1")
            dlg.add_layout(name="Layout2",margin=[0,0,200,0],
                orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label4",text="Get Value option=1",width=100,layout="Layout2")
            dlg.add_textbox(name="Textbox5",layout="Layout2")
            dlg.add_layout(name="Layout3",margin=[0,0,200,0],
                orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label5",text="Get Value option=2",width=100,layout="Layout3")
            dlg.add_textbox(name="Textbox6",layout="Layout3")
            dlg.add_table(name="Table1",rows=5,
                columns=["String","Integer","Double"],
                layout="Window",width=360,height=260)
            dlg.set_table_column_data_type(name="Table1",col=0,data_type="String")
            dlg.set_table_column_data_type(name="Table1",col=1,data_type="Integer")
            dlg.set_table_column_data_type(name="Table1",col=2,data_type="Double",precision=5)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_table_sel_changed(name="Table1",callfunc=get_table_cell_value)
            dlg.set_cell_value(name="Table1",row=0,col=0,
                value=["Option1","Option2","Option3"])
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_cell_value({},{},{},{})".format(name,row,col,option)
        JPT_RUN_LINE(message)

    def get_combobox_option(self, name, index):
        r"""
        ## Description
        
        Get the string value of the being selected ComboBox option.
        
        ## Syntax
        
        ```psj
        dlg.get_combobox_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ### `index`
        
        - A _Integer_ specifying the order of the ComboBox component's values.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the being selected ComboBox option.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_combobox(name="ComboBox1",options=["item1","item2","item3","item4","item5","item6"],layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_combobox_sel(name="ComboBox1",option=2)
            print(dlg.get_combobox_option(name="ComboBox1",index=2))
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_combobox_option({},{})".format(name,index)
        JPT_RUN_LINE(message)

    def get_combobox_sel(self, name):
        r"""
        ## Description
        
        Get the index of the being selected ComboBox option.
        
        ## Syntax
        
        ```psj
        dlg.get_combobox_sel(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the index of the being selected ComboBox option.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_combobox(name="ComboBox1",options=["item1","item2","item3","item4","item5","item6"],layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_combobox_sel(name="ComboBox1",option=3)
            print(dlg.get_combobox_sel(name="ComboBox1"))
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_combobox_sel({})".format(name)
        JPT_RUN_LINE(message)

    def get_dlg_selector_selected_entities(self, selid):
        r"""
        ## Description
        
        Get selected _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ in current Selection List.
        
        ## Syntax
        
        ```psj
        dlg.get_dlg_selector_selected_entities(...)
        ```
        
        ## Inputs
        
        ### `selid`
        
        - A _Integer_ specifying the index of the selector.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object specifying the list of picked items.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        
        def display_selected_entities(dlg):
            str_nodes = ""
            for n in dlg.get_dlg_selector_selected_entities(selid=0):
                str_nodes += 'Selected Node ID: ' + (str(n.id)) + ',\n'
                dlg.set_item_text(name="selected_nodes",text=str_nodes)
        
        def main():
            dlg=JDGCreator(title="Picking Sample",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox1",text="Display all selected nodes",layout="Window")
            dlg.add_label(name="Label2",text="Please select nodes and click Display Nodes button",layout="GroupBox1")
            dlg.add_button(name="display_nodes",text="Display Nodes",layout="GroupBox1")
            dlg.add_richeditbox(name="selected_nodes",text="",width=200,height=200,layout="GroupBox1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_node_selector()
            dlg.add_node_selector()
            dlg.generate_window()
            dlg.on_command(name="display_nodes",callfunc=display_selected_entities)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_dlg_selector_selected_entities({})".format(selid)
        JPT_RUN_LINE(message)

    def get_item_text(self, name):
        r"""
        ## Description
        
        Get text inside the component.
        
        ## Syntax
        
        ```psj
        dlg.get_item_text(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component which user want to get text.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the text inside the component.
        
        ## Sample Code
        
        ```psj {3}
        from pyjdg import *
        def onGetButtonClicked(dlg):
            print(dlg.get_item_text(name="TextBox1"))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_textbox(name="TextBox1",layout="Window")
            dlg.add_button(name="Button2",text="Get text",width=60,height=22,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_command(name="Button2",callfunc=onGetButtonClicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_item_text({})".format(name)
        JPT_RUN_LINE(message)

    def get_len_combobox(self, name):
        r"""
        ## Description
        
        Get the size (number of items) of the ComboBox.
        
        ## Syntax
        
        ```psj
        dlg.get_len_combobox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the size of the ComboBox component.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4","item5"],width=70,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            comboBoxLen=dlg.get_len_combobox(name="ComboBox2")
            print(comboBoxLen)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_len_combobox({})".format(name)
        JPT_RUN_LINE(message)

    def get_len_listbox(self, name):
        r"""
        ## Description
        
        Get the size (number of items) of the ListBox.
        
        ## Syntax
        
        ```psj
        dlg.get_len_listbox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the size of the ListBox component.
        
        ## Sample Code
        
        ```psj {14}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,0,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],
                width=100,height=150,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            listBoxLen=dlg.get_len_listbox(name="ListBox2")
            print(listBoxLen)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_len_listbox({})".format(name)
        JPT_RUN_LINE(message)

    def get_listbox_option(self, name, option_index):
        r"""
        ## Description
        
        Get the string value of the being selected ListBox option.
        
        ## Syntax
        
        ```psj
        dlg.get_listbox_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component.
        - This is a required input.
        
        ### `option_index`
        
        - A _Integer_ specifying the order of the ListBox component's values.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the being selected ListBox option.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_listbox(name="ListBox1",options=["item1","item2","item3","item4","item5","item6"],
                width=100,height=150,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            print(dlg.get_listbox_option(name="ListBox1",option_index=2))
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_listbox_option({},{})".format(name,option_index)
        JPT_RUN_LINE(message)

    def get_listbox_sel(self, name):
        r"""
        ## Description
        
        Get the index of the selecting ListBox option.
        
        ## Syntax
        
        ```psj
        dlg.get_listbox_sel(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the index of the being selected ListBox option.
        
        ## Sample Code
        
        ```psj {15}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,0,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],
                width=100,height=150,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_listbox_sel(name="ListBox2",option=3)
            listBoxPos=dlg.get_listbox_sel(name="ListBox2")
            print(listBoxPos)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_listbox_sel({})".format(name)
        JPT_RUN_LINE(message)

    def get_listbox_sels(self, name):
        r"""
        ## Description
        
        Get the indexes of the selecting ListBox options.
        
        ## Syntax
        
        ```psj
        dlg.get_listbox_sels(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component.
        - This is a required input.
        
        ## Return Code
        
        An _[IntVector](../data-type/psj-utility/pre-utility/built-in-types/IntVector)_ specifying the indexes of the being selected ListBox options.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def onButtonClicked(dlg):
            listBoxPos=dlg.get_listbox_sels(name="ListBox2")
            dlg.set_item_text(name="TextBox4",text=str(list(listBoxPos)))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_listbox(name="ListBox2",multisel=True,
              options=["item1","item2","item3","item4"],width=100,height=150,layout="Window")
            dlg.set_item_size_behavior(name="ListBox2",behavior=size_behavior.fixed)
            dlg.add_layout(name="Layout3",orientation=orientation.horizontal,layout="Window")
            dlg.add_textbox(name="TextBox4",width=150,height=22,layout="Layout3")
            dlg.add_button(name="Button5",text="Get Index",width=60,height=22,bk_color=15790320,layout="Layout3")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_command(name="Button5",callfunc=onButtonClicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_listbox_sels({})".format(name)
        JPT_RUN_LINE(message)

    def get_pagesctrl_current_page(self, name):
        r"""
        ## Description
        
        Get the index order of current selected PageItem of the PagesCtrl.
        
        ## Syntax
        
        ```psj
        dlg.get_pagesctrl_current_page(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of PagesCtrl.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the index order of the current selected PageItem of the PagesCtrl.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def on_pageitem_changed(dlg,name,oldpage):
            current_page=dlg.get_pagesctrl_current_page(name="PagesCtrl1")
            print("Selected page ID:"+str(current_page))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_pagesctrl(name="PagesCtrl1",layout="Window")
            dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem2",
                page_header="PageItem1")
            dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem3",
                page_header="PageItem2")
            dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem4",
                page_header="PageItem3")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Ok",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_pagesctrl_active_page(name="PagesCtrl1",callfunc=on_pageitem_changed)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_pagesctrl_current_page({})".format(name)
        JPT_RUN_LINE(message)

    def get_pagesctrl_page_name(self, name, page_index):
        r"""
        ## Description
        
        Get the name of current selected PageItem of the PagesCtrl.
        
        ## Syntax
        
        ```psj
        dlg.get_pagesctrl_page_name(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of PagesCtrl.
        - This is a required input.
        
        ### `page_index`
        
        - An _Integer_ specifying the index order of current selected PageItem of the PagesCtrl.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the name of PageItem.
        
        ## Sample Code
        
        ```psj {5-6}
        from pyjdg import *
        
        def on_pageitem_changed(dlg,name,oldpage):
            current_page=dlg.get_pagesctrl_current_page(name="PagesCtrl1")
            current_page_name=dlg.get_pagesctrl_page_name(name="PagesCtrl1",
                page_index=current_page)
            print("Selected page name:"+current_page_name)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_pagesctrl(name="PagesCtrl1",layout="Window")
            dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem2",
                page_header="PageItem1")
            dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem3",
                page_header="PageItem2")
            dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem4",
                page_header="PageItem3")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Ok",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_pagesctrl_active_page(name="PagesCtrl1",callfunc=on_pageitem_changed)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_pagesctrl_page_name({},{})".format(name,page_index)
        JPT_RUN_LINE(message)

    def get_table_cell_fill_color(self, name, row, col):
        r"""
        ## Description
        
        Get the fill color of the selected/specified cell.
        
        ## Syntax
        
        ```psj
        dlg.get_table_cell_fill_color(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `row`
        
        - An _Integer_ specifying the position in the horizontal direction of the cell  (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
        - This is a required input.
        
        
        ## Return Code
        
        An _Integer_ specifying color code in Jupiter.
        
        ## Sample Code
        
        ```psj {6-8}
        from pyjdg import *
        
        def on_menu(dlg,name,menu):
            cellvector=dlg.get_table_sel_cell(name="Table1")
            if menu=="Get cell color":
                colorCell = dlg.get_table_cell_fill_color(name="Table1", 
                    row=cellvector[0].row_number,
                    col=cellvector[0].col_number)
                print("The selected cell has the fill color is: " + str(colorCell))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2","Heading3"],
                layout="Window",show_row_number=True,width=350,height=160)
            dlg.add_label(name="Labe2",text="Right-click on the seleted cell then select Get cell color",
                width=350,layout="Window")
            for i in range(3):
                dlg.set_table_column_width("Table2", i, 100)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",
                menus=["Get cell color"])
            dlg.generate_window()
            dlg.set_table_cell_fill_color(name="Table1",
                    cell=TableCellID(row=0,col=0),color=7105764)
            dlg.set_table_cell_fill_color(name="Table1",
                    cell=TableCellID(row=0,col=1),color=255)
            dlg.set_table_cell_fill_color(name="Table1",
                    cell=TableCellID(row=0,col=2),color=0)
            colorValue=JPT.ConvertRGBToJPTColor(255,255,0)
            for i in range(1,3):
                for j in range(0,3):
                    dlg.set_table_cell_fill_color(name="Table1",
                        cell=TableCellID(row=i,col=j),color=colorValue)
                    colorValue+=100000
            dlg.on_table_right_menu(name="Table1",callfunc=on_menu)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_table_cell_fill_color({},{},{})".format(name,row,col)
        JPT_RUN_LINE(message)

    def get_table_column_width(self, name, col):
        r"""
        ## Description
        
        Get the width of the specified column in the Table.
        
        ## Syntax
        
        ```psj
        dlg.get_table_column_width(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the order of the column (starts from 0).
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the width value of the specified cell of the inputted Table.
        
        ## Sample Code
        
        ```psj {12-13}
        from pyjdg import *
        
        def on_menu(dlg,name,menu):
            cellvector=dlg.get_table_sel_cell(name="Table1")
            if menu=="Set Column Width using Dialog":
                dlg.set_table_column_width(name="Table1",
                    col=cellvector[0].col_number)
            if menu=="Set Column Width equal 400":
                dlg.set_table_column_width(name="Table1",
                    col=cellvector[0].col_number,width=400)
            elif menu=="Get Column Width":
                col_width = dlg.get_table_column_width(name="Table1",
                    col=cellvector[0].col_number)
                print("Column "+str(cellvector[0].col_number)+
                    " width is: "+str(col_width))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",
                menus=["Set Column Width using Dialog",
                "Set Column Width equal 400","Get Column Width"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_menu)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_table_column_width({},{})".format(name,col)
        JPT_RUN_LINE(message)

    def get_table_sel_cell(self, name):
        r"""
        ## Description
        
        Get the information and attributes of the selected cells.
        
        ## Syntax
        
        ```psj
        dlg.get_table_sel_cell(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ## Return Code
        
        - A _[TableCellVector](../data-type/psj-gui/TableCellVector)_ object or _List of [TableCellID](../data-type/psj-gui/TableCellID)_ specifying the methods of cells.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def on_context_click(dlg,name,menu):
            cellvector=dlg.get_table_sel_cell(name="Table1")
            for i in range(cellvector.size()):
                print("The cell number {} has information".format(i+1))
                print("Cell's position (row) = "+str(cellvector[0].row_number))
                print("Cell's position (column) = "+str(cellvector[0].col_number))
                print("---------------------------")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",menus=["Check cell info"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_context_click)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_table_sel_cell({})".format(name)
        JPT_RUN_LINE(message)

    def get_table_sel_range(self, name):
        r"""
        ## Description
        
        Get the information and attributes of the selected ranges (multi cells).
        
        ## Syntax
        
        ```psj
        dlg.get_table_sel_range(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ## Return Code
        
        - A _[TableCellRangeVector](../data-type/psj-gui/TableCellRangeVector)_ object or _List of [TableCellRange](../data-type/psj-gui/TableCellRange)_ specifying the methods of ranges.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def on_context_click(dlg,name,menu):
            rangevector=dlg.get_table_sel_range(name="Table1")
            for i in range(rangevector.size()):
                print("The range number {} has information".format(i+1))
                print("Range's position (left) = "+str(rangevector[0].left))
                print("Range's position (top) = "+str(rangevector[0].top))
                print("Range's position (right) = "+str(rangevector[0].right))
                print("Range's position (bottom) = "+str(rangevector[0].bottom))
                print("---------------------------")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=16,
                columns=["Heading1","Heading2","Heading3","Heading4","Heading5"],
                layout="Window",width=550,height=300)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",menus=["Check cell info"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_context_click)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_table_sel_range({})".format(name)
        JPT_RUN_LINE(message)

    def get_tabwnd_current_page(self, name):
        r"""
        ## Description
        
        Get the selecting page of the inputted TabWnd.
        
        ## Syntax
        
        ```psj
        dlg.get_tabwnd_current_page(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the TabWnd component using for getting selected page order.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the order of the selected page of the inputted TabWnd.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def get_current_tab(dlg):
            selected_page = dlg.get_tabwnd_current_page(name="TabWnd1")
            JPT.Debugger(selected_page)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_tabwnd(name="TabWnd1",width=400,height=200,layout="Window")
            dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem2",page_text="TabItem")
            dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem3",page_text="TabItem")
            dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem4",page_text="TabItem")
            dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem5",page_text="TabItem")
            dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem6",page_text="TabItem")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_command(name="ButtonApply",callfunc=get_current_tab)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_tabwnd_current_page({})".format(name)
        JPT_RUN_LINE(message)

    def get_total_column(self, name):
        r"""
        ## Description
        
        Get the total number of columns of the Table.
        
        ## Syntax
        
        ```psj
        dlg.get_total_column(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Table component.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the total number of columns of the Table.
        
        ## Sample Code
        
        ```psj {14}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=14,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            total_cols = dlg.get_total_column(name="Table1")
            JPT.Debugger(total_cols)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_total_column({})".format(name)
        JPT_RUN_LINE(message)

    def get_total_row(self, name):
        r"""
        ## Description
        
        Get the total number of rows of the Table.
        
        ## Syntax
        
        ```psj
        dlg.get_total_row(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Table component.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the total number of rows of the Table.
        
        ## Sample Code
        
        ```psj {14}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=14,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            total_rows = dlg.get_total_row(name="Table1")
            JPT.Debugger(total_rows)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.get_total_row({})".format(name)
        JPT_RUN_LINE(message)

    def hide_layout(self, name):
        r"""
        ## Description
        
        Hide the Layout and all of its children components inside.
        
        ## Syntax
        
        ```psj
        dlg.hide_layout(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Layout component.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {20}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Label",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_layout(name="Layout4",orientation=orientation.horizontal,layout="Window")
            dlg.add_richeditbox(name="RichEditBox8",text="RichEditBox",width=200,height=200,layout="Layout4")
            dlg.add_layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
            dlg.add_textbox(name="TextBox7",layout="Layout5")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox9",layout="Layout6")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.hide_layout(name="Layout5")
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.hide_layout({})".format(name)
        JPT_RUN_LINE(message)

    def insert_combobox_option(self, name, position, option):
        r"""
        ## Description
        
        Insert an option to a specific position of the ComboBox component.
        
        ## Syntax
        
        ```psj
        dlg.insert_combobox_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ### `position`
        
        - An _Integer_ specifying the position in ComboBox to put the new option.
        - This is a required input.
        
        ### `option`
        
        - A _String_ specifying the text which will be used as a ComboBox option.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4","item5"],width=70,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.insert_combobox_option(name="ComboBox2",position=2,option="item_New")
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.insert_combobox_option({},{},{})".format(name,position,option)
        JPT_RUN_LINE(message)

    def insert_combobox_options(self, name, position, options):
        r"""
        ## Description
        
        Insert multiple options to a specific position of the ComboBox component.
        
        ## Syntax
        
        ```psj
        dlg.insert_combobox_options(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ### `position`
        
        - An _Integer_ specifying the position in ComboBox to put the new options.
        - This is a required input.
        
        ### `options`
        
        - A _List of String_ specifying the new options.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4","item5"],width=70,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.insert_combobox_options(name="ComboBox2",position=2,options=["item_New_2","item_New_1"])
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.insert_combobox_options({},{},{})".format(name,position,options)
        JPT_RUN_LINE(message)

    def insert_listbox_option(self, name, position, option):
        r"""
        ## Description
        
        Insert an option to a specific position of the ListBox component.
        
        ## Syntax
        
        ```psj
        dlg.insert_listbox_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component.
        - This is a required input.
        
        ### `position`
        
        - An _Integer_ specifying the position in ListBox to put the new option.
        - This is a required input.
        
        ### `option`
        
        - A _String_ specifying the text which will be used as a ListBox option.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {14}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,0,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],
                width=100,height=150,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.insert_listbox_option(name="ListBox2",position=2,option="item_New")
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.insert_listbox_option({},{},{})".format(name,position,option)
        JPT_RUN_LINE(message)

    def insert_listbox_options(self, name, position, options):
        r"""
        ## Description
        
        Insert multiple options to a specific position of the ListBox component.
        
        ## Syntax
        
        ```psj
        dlg.insert_listbox_options(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component.
        - This is a required input.
        
        ### `position`
        
        - An _Integer_ specifying the position in ListBox to put the new options.
        - This is a required input.
        
        ### `options`
        
        - A _List of String_ specifying the new options.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {14}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,0,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],
                width=100,height=150,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.insert_listbox_options(name="ListBox2",position=2,options=["item_New_2","item_New_1"])
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.insert_listbox_options({},{},{})".format(name,position,options)
        JPT_RUN_LINE(message)

    def insert_table_columns(self, name, columns, position):
        r"""
        ## Description
        
        Insert column(s) at a specific position in the Table.
        
        ## Syntax
        
        ```psj
        dlg.insert_table_columns(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `columns`
        
        - A _[TableColumnInfoVector](../data-type/psj-gui/TableColumnInfoVector)_ object or _List of [TableColumnInfo](../data-type/psj-gui/TableColumnInfo)_ specifying the methods of columns.
        - This is a required input.
        
        ### `position`
        
        - An _Integer_ specifying the position of row to be inserted.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {14-15,22-23}
        from pyjdg import *
        
        def on_click_insert_col(dlg):
            num_col=int(dlg.get_item_text(name="Col"))
            col_header_name=dlg.get_item_text(name="ColHeader")
            sel_ranges=dlg.get_table_sel_range(name="Table1")
            header_vector=TableColumnInfoVector()
            for i in range(num_col):
                if sel_ranges.size()>0:
                    position=sel_ranges[0].left+i
                    header_vector.append(
                        TableColumnInfo(name=col_header_name+"{}".format(i+1),
                        type="Double",precision=2))
                    dlg.insert_table_columns(name="Table1",
                        columns=header_vector,position=position)
                    header_vector.clear()
                else:
                    position=int(dlg.get_total_column(name="Table1"))
                    header_vector.append(
                    TableColumnInfo(name=col_header_name+"{}".format(i+1),
                        type="Double",precision=2))
                    dlg.insert_table_columns(name="Table1",
                        columns=header_vector,position=position)
                    header_vector.clear()
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox1",text="Insert Columns",layout="Window")
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,
                layout="GroupBox1")
            dlg.add_label(name="Label1",text="Number of Col",width=120,layout="Layout1")
            dlg.add_textbox(name="Col",layout="Layout1")
            dlg.add_layout(name="Layout9",orientation=orientation.horizontal,
                layout="GroupBox1")
            dlg.add_label(name="Col_header",text="Column header name",
                width=120,layout="Layout9")
            dlg.add_textbox(name="ColHeader",layout="Layout9")
            dlg.add_button(name="InsertCol",text="Insert Column",
                width=100,height=22,layout="GroupBox1")
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2","Heading3"],
                layout="Window",width=600,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            for i in range(5):
                for j in range(3):
                    dlg.set_cell_value(name="Table1",row=i,col=j,value=str(i+j))
            dlg.on_command(name="InsertCol",callfunc=on_click_insert_col)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.insert_table_columns({},{},{})".format(name,columns,position)
        JPT_RUN_LINE(message)

    def insert_table_rows(self, name, row_num, position):
        r"""
        ## Description
        
        Insert row(s) at a specific position in the Table.
        
        ## Syntax
        
        ```psj
        dlg.insert_table_rows(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `row_num`
        
        - An _Integer_ specifying the number of rows to be inserted.
        - This is a required input.
        
        ### `position`
        
        - An _Integer_ specifying the position of row to be inserted.
          -  If specified, the row will be inserted in front of the inputted position (position-1).
          -  If not specified,the row will be inserted at the end of the table.
        - This is a default input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {10-11,14-15,17}
        from pyjdg import *
        
        def on_click_insert_row(dlg):
            num_row=int(dlg.get_item_text(name="Row"))
            sel_ranges=dlg.get_table_sel_range(name="Table1")
            position=int(dlg.get_total_row(name="Table1"))
            if sel_ranges.size()>0:
                if sel_ranges[0].top == 0:
                    position=sel_ranges[0].top
                    dlg.insert_table_rows(name="Table1",
                        row_num=num_row,position=position)
                elif sel_ranges[0].top > 0:
                    position=sel_ranges[0].top
                    dlg.insert_table_rows(name="Table1",
                        row_num=num_row,position=position)
            else:
                dlg.insert_table_rows(name="Table1",row_num=num_row)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox1",text="Insert Rows",layout="Window")
            dlg.add_layout(name="Layout2",orientation=orientation.horizontal,
                layout="GroupBox1")
            dlg.add_label(name="Label1",text="Number of Rows",layout="Layout2")
            dlg.add_textbox(name="Row",layout="Layout2")
            dlg.add_button(name="InsertRow",text="Insert Row",
                width=100,height=22,layout="GroupBox1")
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2","Heading3"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            for i in range(5):
                for j in range(3):
                    dlg.set_cell_value(name="Table1",row=i,col=j,value=str(i+j))
            dlg.on_command(name="InsertRow",callfunc=on_click_insert_row)
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.insert_table_rows({},{},{})".format(name,row_num,position)
        JPT_RUN_LINE(message)

    def isbutton_checked(self, name):
        r"""
        ## Description
        
        Check the status of the inputted component whether it is checked or not.
        Currently supporting checkbox and radio button components.
        
        ## Syntax
        
        ```psj
        dlg.isbutton_checked(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component using for checking the status of selection.
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the status of the inputted component:
        
        - _True_: The inputted component is checked (Selected).
        - _False_: The inputted component is unchecked (Unselected).
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def check_status(dlg):
            isChecked = dlg.isbutton_checked(name="CheckBox2")
            print(isChecked)
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_checkbox(name="CheckBox2",text="Jupiter",checked=True,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_command(name="CheckBox2",callfunc=check_status)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.isbutton_checked({})".format(name)
        JPT_RUN_LINE(message)

    def is_groupbox_checked(self, name):
        r"""
        ## Description
        
        Check the state of a GroupBox's checkbox.
        
        ## Syntax
        
        ```psj
        dlg.is_groupbox_checked(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of GroupBox.
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the state of groupbox checkbox:
        
        - _True_: The groupbox checkbox is checked.
        - _False_: The groupbox checkbox is unchecked.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        def on_group_checked(dlg,checked):
            if checked :
                print("checked")
            else:
                print("unchecked")
            print("get checked status==", str(dlg.is_groupbox_checked("GroupBox2")))
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_groupbox(name="GroupBox2",text="GroupBox",layout="Window")
            dlg.set_groupbox_checked(name="GroupBox2",checked=False)
            dlg.add_button(name="Button3",text="Button",width=60,height=22,bk_color=15790320,layout="GroupBox2")
            dlg.generate_window()
            dlg.on_groupbox_checked("GroupBox2",on_group_checked)
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.is_groupbox_checked({})".format(name)
        JPT_RUN_LINE(message)

    def is_table_cell_button(self, name, cell):
        r"""
        ## Description
        
        Check the input cell is a button cell or not.
        
        ## Syntax
        
        ```psj
        dlg.is_table_cell_button(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table.
          - TableCellID(row,col) defines a cell object
          - TableCellID.row_number returns row number of the cell
          - TableCellID.col_number returns column number of the cell
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the type of inputted cell:
        
        - _True_: The inputted cell is a button cell.
        - _False_: The inputted cell is not a button cell.
        
        ## Sample Code
        
        ```psj {7-9}
        from pyjdg import *
        
        def on_cell_button_clicked(dlg,name,cell):
            JPT.ClearLog()
            cellvector=dlg.get_table_sel_cell(name="Table2")
            if cellvector.size() > 0:
               check_cell_button = \
                    dlg.is_table_cell_button(name="Table2",
                        cell=cellvector[0])
               print("Is button cell: " + str(check_cell_button))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",width=260,height=260,
                columns=["Heading1","Heading2"],
                rows=5,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",
                layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_table_cell_button(name="Table2",row=0,
                col=0,text="Button")
            dlg.on_table_sel_changed(name="Table2",
                callfunc=on_cell_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.is_table_cell_button({},{})".format(name,cell)
        JPT_RUN_LINE(message)

    def is_table_cell_checkbox(self, name, cell):
        r"""
        ## Description
        
        Check the input cell is a checkbox cell or not.
        
        ## Syntax
        
        ```psj
        dlg.is_table_cell_checkbox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table.
          - TableCellID(row,col) defines a cell object
          - TableCellID.row_number returns row number of the cell
          - TableCellID.col_number returns column number of the cell
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the type of inputted cell:
        
        - _True_: The inputted cell is a checkbox cell.
        - _False_: The inputted cell is not a checkbox cell.
        
        ## Sample Code
        
        ```psj {7-9}
        from pyjdg import *
        
        def on_cell_button_clicked(dlg,name,cell):
            JPT.ClearLog()
            cellvector=dlg.get_table_sel_cell(name="Table2")
            if cellvector.size() > 0:
               check_cell_checkbox = \
                    dlg.is_table_cell_checkbox(name="Table2",
                        cell=cellvector[0])
               print("Is checkbox cell: " + str(check_cell_checkbox))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",width=260,height=260,
                columns=["Heading1","Heading2"],
                rows=5,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",
                layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_table_cell_checkbox(name="Table2",row=0,
                col=0,text="Checkbox",checked=True)
            dlg.on_table_sel_changed(name="Table2",
                callfunc=on_cell_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.is_table_cell_checkbox({},{})".format(name,cell)
        JPT_RUN_LINE(message)

    def is_table_cell_checked(self, name, cell):
        r"""
        ## Description
        
        Check the state of checkbox cell.
        
        ## Syntax
        
        ```psj
        dlg.is_table_cell_checked(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table.
          - TableCellID(row,col) defines a cell object
          - TableCellID.row_number returns row number of the cell
          - TableCellID.col_number returns column number of the cell
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the state of checkbox cell:
        
        - _True_: The checkbox cell is checked.
        - _False_: The checkbox cell is unchecked.
        
        ## Sample Code
        
        ```psj {10-12}
        from pyjdg import *
        
        def on_cell_button_clicked(dlg,name,cell):
            JPT.ClearLog()
            cellvector=dlg.get_table_sel_cell(name="Table2")
            if cellvector.size() > 0:
               check_cell_checkbox = \
                    dlg.is_table_cell_checkbox(name="Table2",
                        cell=cellvector[0])
               check_state_checkbox = \
                    dlg.is_table_cell_checked(name="Table2",
                        cell=cellvector[0])
               print("Is checkbox cell: " + str(check_cell_checkbox))
               print("State of checkbox cell: " + \
                   str(check_state_checkbox))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",width=260,height=260,
                columns=["Heading1","Heading2"],
                rows=5,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",
                layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_table_cell_checkbox(name="Table2",row=0,
                col=0,text="Checkbox",checked=True)
            dlg.on_table_sel_changed(name="Table2",
                callfunc=on_cell_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.is_table_cell_checked({},{})".format(name,cell)
        JPT_RUN_LINE(message)

    def is_table_cell_combobox(self, name, cell):
        r"""
        ## Description
        
        Check the input cell is a combobox cell or not.
        
        ## Syntax
        
        ```psj
        dlg.is_table_cell_combobox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table.
          - TableCellID(row,col) defines a cell object
          - TableCellID.row_number returns row number of the cell
          - TableCellID.col_number returns column number of the cell
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the type of inputted cell:
        
        - _True_: The inputted cell is a combobox cell.
        - _False_: The inputted cell is not a combobox cell.
        
        ## Sample Code
        
        ```psj {7-9}
        from pyjdg import *
        
        def on_cell_button_clicked(dlg,name,cell):
            JPT.ClearLog()
            cellvector=dlg.get_table_sel_cell(name="Table2")
            if cellvector.size() > 0:
               check_cell_combobox = \
                    dlg.is_table_cell_combobox(name="Table2",
                        cell=cellvector[0])
               print("Is combobox cell: " + str(check_cell_combobox))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",width=260,height=260,
                columns=["Heading1","Heading2"],
                rows=5,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",
                layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_cell_value(name="Table2",row=0,col=0,
                value=["Option1","Option2","Option3"])
            dlg.on_table_sel_changed(name="Table2",
                callfunc=on_cell_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.is_table_cell_combobox({},{})".format(name,cell)
        JPT_RUN_LINE(message)

    def on_activate_selector(self, callfunc):
        r"""
        ## Description
        
        Run a created function after a selector is activated.
        
        ## Syntax
        
        ```psj
        dlg.activate_selector(...)
        ```
        
        ## Inputs
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {33}
        from pyjdg import *
        
        def on_node_selector_clicked(dlg):
            dlg.activate_selector(0)
        
        def on_part_selector_clicked(dlg):
            dlg.activate_selector(1)
        
        def on_activate_selector(dlg,selector_id):
            if selector_id==0:
               dlg.set_radiobutton_state("RadioButton3",True)
               dlg.set_radiobutton_state("RadioButton4",False)
            else :
               dlg.set_radiobutton_state("RadioButton4",True)
               dlg.set_radiobutton_state("RadioButton3",False)
        
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_label(
                    name="Label2",width=200,height=80,
                    text="Open the selection list.\n" 
                         "Confirm that selector focus changes when radio buttons are selected,"
                         "and conversely, that radio button selection changes when selectors are focused.",
                    text_halign="left",text_valign="top",layout="Window")
            dlg.add_node_selector()
            dlg.add_part_selector()
            dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
            dlg.add_radiobutton(name="RadioButton3",text="Node",layout="Layout2",checked=True)
            dlg.add_radiobutton(name="RadioButton4",text="Part",layout="Layout2")
            dlg.generate_window()
            dlg.on_button_clicked("RadioButton3",on_node_selector_clicked)
            dlg.on_button_clicked("RadioButton4",on_part_selector_clicked)
            dlg.on_activate_selector(on_activate_selector)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_activate_selector({})".format(callfunc)
        JPT_RUN_LINE(message)

    def on_active_tab_page(self, name, callfunc):
        r"""
        ## Description
        
        Bind a created function after a TabItem is selected.
        
        ## Syntax
        
        ```psj
        dlg.on_active_tab_page(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of TabWnd.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {28}
        from pyjdg import *
        
        def captureTabWndPageChangeMessage(dlg,tabName,newTabPage):
            curPage=dlg.get_tabwnd_current_page(tabName)
            print("TabWnd:  "+ tabName +" changed page to "+ str(newTabPage))
        
        def changeTabPage(dlg):
            dlg.set_tabwnd_current_page(name="TabWnd1",page_index=1)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_tabwnd(name="TabWnd1",width=200,height=200,layout="Window")
            dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem2",page_text="TabItem")
            dlg.add_combobox(name="ComboBox4",layout="TabItem2")
            dlg.add_combobox(name="ComboBox5",layout="TabItem2")
            dlg.add_button(name="Button6",text="Button",width=60,height=22,layout="TabItem2")
            dlg.add_button(name="Button7",text="Button",width=60,height=22,layout="TabItem2")
            dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem3",page_text="TabItem")
            dlg.add_checkbox(name="CheckBox8",text="CheckBox",layout="TabItem3")
            dlg.add_checkbox(name="CheckBox9",text="CheckBox",layout="TabItem3")
            dlg.add_button(name="Button10",text="Click Me to change TabPage",width=260,height=22,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_active_tab_page(name="TabWnd1",callfunc=captureTabWndPageChangeMessage)
            dlg.on_button_clicked(name="Button10",callfunc=changeTabPage)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_active_tab_page({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_browse(self, name, callfunc):
        r"""
        ## Description
        
        Bind a created function to a file/folder Browser component.
        
        ## Syntax
        
        ```psj
        dlg.on_browse(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the file/folder Browser component using for binding a created def function.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {15}
        from pyjdg import *
        
        def on_browse_clicked(dlg,path_list):
            print(path_list[0])
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_browser(name="Browser2",mode="file",file_filter="All Files(*.*)",layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_browse(name="Browser2",callfunc=on_browse_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_browse({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_button_clicked(self, name, callfunc):
        r"""
        ## Description
        
        Bind a created function to a Button/RadioButton/CheckBox.
        
        ## Syntax
        
        ```psj
        dlg.on_button_clicked(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Button/RadioButton/CheckBox using for binding a created def function.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {29-31}
        from pyjdg import *
        
        def on_button_clicked(dlg):
            JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_1", 5357649, 0:0)')
            print("--- Cube created! ---")
        
        def on_checkbox_clicked(dlg):
            print("You clicked on Checkbox!")
        
        def on_radio_buton_clicked(dlg):
            print("You clicked on Radio Button!")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox2",text="GroupBox",layout="Window")
            dlg.add_layout(name="Layout4",orientation=orientation.vertical,layout="GroupBox2")
            dlg.add_label(name="Label8",text="Click on Button!",text_halign="left",text_valign="top",layout="Layout4")
            dlg.add_button(name="Button5",text="Button",width=60,height=22,layout="Layout4")
            dlg.add_label(name="Label9",text="Click on Checkbox!",text_halign="left",text_valign="top",layout="Layout4")
            dlg.add_checkbox(name="CheckBox6",text="CheckBox",layout="Layout4")
            dlg.add_label(name="Label10",text="Click on Radio Button!",text_halign="left",text_valign="top",layout="Layout4")
            dlg.add_radiobutton(name="RadioButton7",text="RadioButton",layout="Layout4")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_button_clicked(name="Button5",callfunc=on_button_clicked)
            dlg.on_button_clicked(name="CheckBox6",callfunc=on_checkbox_clicked)
            dlg.on_button_clicked(name="RadioButton7",callfunc=on_radio_buton_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_button_clicked({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_combobox_sel(self, name, callfunc):
        r"""
        ## Description
        
        Run a created function after a ComboBox item is selected.
        
        ## Syntax
        
        ```psj
        dlg.on_combobox_sel(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component using for binding a created def function.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {21}
        from pyjdg import *
        
        def on_combobox_select(dlg):
            print("Index of selected combobox: {}"
                .format(dlg.get_combobox_sel(name="ComboBox1")))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,100,0],
                orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox1",
                options=["item1","item2","item3","item4","item5"],
                width=70,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_combobox_sel(name="ComboBox1",callfunc=on_combobox_select)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_combobox_sel({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_command(self, name, callfunc):
        r"""
        ## Description
        
        Bind a created function to a component.
        
        ## Syntax
        
        ```psj
        dlg.on_command(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component using for binding a created def function.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {18}
        from pyjdg import *
        
        def onApplyButtonClicked(dlg):
            Geometry.Part.Cube()
            print("--- Cube created! ---")
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[80,0,50,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Click on Apply button!",layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_command(name="ButtonApply",callfunc=onApplyButtonClicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_command({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_dlg_apply(self, callfunc):
        r"""
        ## Description
        
        Execute a created function when Apply button is clicked.
        
        ## Syntax
        
        ```psj
        dlg.on_dlg_apply(...)
        ```
        
        ## Inputs
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {11}
        from pyjdg import *
        
        def on_button_Apply_clicked(dlg):
            print("Apply button is clicked")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True,include_apply=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Please click on Apply button!",layout="Layout1")
            dlg.generate_window()
            dlg.on_dlg_apply(callfunc=on_button_Apply_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_dlg_apply({})".format(callfunc)
        JPT_RUN_LINE(message)

    def on_dlg_cancel(self, callfunc):
        r"""
        ## Description
        
        Execute a created function when Cancel button is clicked.
        
        ## Syntax
        
        ```psj
        dlg.on_dlg_cancel(...)
        ```
        
        ## Inputs
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {11}
        from pyjdg import *
        
        def on_button_Cancel_clicked(dlg):
            print("Cancel button is clicked")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True,include_apply=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Please click on Cancel button!",layout="Layout1")
            dlg.generate_window()
            dlg.on_dlg_cancel(callfunc=on_button_Cancel_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_dlg_cancel({})".format(callfunc)
        JPT_RUN_LINE(message)

    def on_dlg_help(self, callfunc):
        r"""
        ## Description
        
        Execute a created function when Help button is clicked.
        
        ## Syntax
        
        ```psj
        dlg.on_dlg_help(...)
        ```
        
        ## Inputs
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {11}
        from pyjdg import *
        
        def on_button_Help_clicked(dlg):
            print("Help button is clicked")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True,include_apply=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Please click on Help button!",layout="Layout1")
            dlg.generate_window()
            dlg.on_dlg_help(callfunc=on_button_Help_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_dlg_help({})".format(callfunc)
        JPT_RUN_LINE(message)

    def on_dlg_ok(self, callfunc):
        r"""
        ## Description
        
        Execute a created function when OK button is clicked.
        
        ## Syntax
        
        ```psj
        dlg.on_dlg_ok(...)
        ```
        
        ## Inputs
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {11}
        from pyjdg import *
        
        def on_button_OK_clicked(dlg):
            print("OK button is clicked")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True,include_apply=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Please click on OK button!",layout="Layout1")
            dlg.generate_window()
            dlg.on_dlg_ok(callfunc=on_button_OK_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_dlg_ok({})".format(callfunc)
        JPT_RUN_LINE(message)

    def on_dlg_selector_changed(self, callfunc):
        r"""
        ## Description
        
        Run a created function after an item is selected.
        
        ## Syntax
        
        ```psj
        dlg.on_dlg_selector_changed(...)
        ```
        
        ## Inputs
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {26}
        from pyjdg import *
        
        def display_selected_entities(dlg,sel_list):
            str_node=''
            for n in sel_list:
                str_node += 'Node:' + str(n.id) + ', '
            dlg.set_item_text(name="node",text=str_node)
        
        def main():
            dlg=JDGCreator(title="Picking Sample",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox1",text="GroupBox",layout="Window")
            dlg.add_label(name="infor1",text="This sample illustrates that when you pick an item,",layout="GroupBox1")
            dlg.add_label(name="infor2",text="you can receive it right after that by your own function.",layout="GroupBox1")
            dlg.add_label(name="infor3",text="The function must have 2 parameters, "\
                "one is dlg and another is a list that returned by selection; ",layout="GroupBox1")
            dlg.add_label(name="infor4",text="such as : def displaySelectedEntity(dlg,selList):",layout="GroupBox1")
            dlg.add_groupbox(name="GroupBox2",text="Selected node will be shown here",layout="Window")
            dlg.add_richeditbox(name="node",width=100,height=200,layout="GroupBox2")
            dlg.add_node_selector()
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_dlg_selector_changed(callfunc=display_selected_entities)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_dlg_selector_changed({})".format(callfunc)
        JPT_RUN_LINE(message)

    def on_groupbox_checked(self, name, callfunc):
        r"""
        ## Description
        
        Bind a created def function to a GroupBox's CheckBox.
        
        ## Syntax
        
        ```psj
        dlg.on_groupbox_checked(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the GroupBox using for binding a created def function.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {14}
        from pyjdg import *
        def on_group_checked(dlg,checked):
            if checked :
                print("checked")
            else:
                print("unchecked")
            print("get checked status==", str(dlg.is_groupbox_checked("GroupBox2")))
        
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_groupbox(name="GroupBox2",text="GroupBox",layout="Window")
            dlg.set_groupbox_checked(name="GroupBox2",checked=False)
            dlg.add_button(name="Button3",text="Button",width=60,height=22,bk_color=15790320,layout="GroupBox2")
            dlg.generate_window()
            dlg.on_groupbox_checked("GroupBox2",on_group_checked)
        if __name__=='__main__':
            main()```
        
        """
        message = "dlg.on_groupbox_checked({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_listbox_sel(self, name, callfunc):
        r"""
        ## Description
        
        Run a created function after a ListBox item is selected.
        
        ## Syntax
        
        ```psj
        dlg.on_listbox_sel(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component using for binding a created def function.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {20}
        from pyjdg import *
        
        def on_listbox_item_changed(dlg):
            JPT.ClearLog()
            listBoxPos=dlg.get_listbox_sel(name="ListBox2")
            listBoxName=dlg.get_listbox_option(name="ListBox2", option_index=listBoxPos)
            dlg.set_item_text(name="TextBox5", text=listBoxName)
            print('The selected list box item is: ', str(listBoxName))
        
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],width=100,height=120,
                layout="Window")
            dlg.set_item_size_behavior(name="ListBox2",behavior=size_behavior.fixed)
            dlg.add_layout(name="Layout3",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label4",text="Selected Item",width=70,text_halign="left",text_valign="top",
                layout="Layout3")
            dlg.add_textbox(name="TextBox5",width=100,layout="Layout3")
            dlg.generate_window()
            dlg.on_listbox_sel(name="ListBox2", callfunc=on_listbox_item_changed)
        if __name__=='__main__':
            main()
        
        
        ```
        
        """
        message = "dlg.on_listbox_sel({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_pagesctrl_active_page(self, name, callfunc):
        r"""
        ## Description
        
        Set event when selecting a PageItem.
        
        ## Syntax
        
        ```psj
        dlg.on_pagesctrl_active_page(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of PagesCtrl.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {27}
        from pyjdg import *
        
        def on_pageitem_changed(dlg,name,old_page):
            current_page=dlg.get_pagesctrl_current_page(name="PagesCtrl1")
            current_page_name=dlg.get_pagesctrl_page_name(name="PagesCtrl1",
                page_index=current_page)
            old_page_name=dlg.get_pagesctrl_page_name(name="PagesCtrl1",
                page_index=old_page)
            print("Selected page name : "+current_page_name)
            print("Previous selected page : "+old_page_name)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_pagesctrl(name="PagesCtrl1",layout="Window")
            dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem2",
                page_header="PageItem1")
            dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem3",
                page_header="PageItem2")
            dlg.add_pageitem(name="PagesCtrl1",page_name="PageItem4",
                page_header="PageItem3")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Ok",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_pagesctrl_active_page(name="PagesCtrl1",callfunc=on_pageitem_changed)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_pagesctrl_active_page({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_spin_changed(self, name, callfunc):
        r"""
        ## Description
        
        Run a created function after a spin value is changed.
        
        ## Syntax
        
        ```psj
        dlg.on_spin_changed(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Spin component using for binding a created def function.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {3}
        from pyjdg import *
        
        def on_spin_changed(dlg,old_value,new_value):
            total_rows=dlg.get_total_row(name="Table6")
            if new_value is None:
                new_rows=int(dlg.get_item_text(name="Spin4"))
            elif new_value >= 0:
                new_rows=new_value
            if new_rows >= total_rows:
                dlg.insert_table_rows(name="Table6",row_num=int(new_rows-total_rows))
            else:
                if new_rows >= 1:
                    for idx in range (new_rows, total_rows):
                        dlg.delete_table_row(name="Table6",position=new_rows)
            if new_value >= 1:
                print("Current number of rows is: "+ str(new_value))
            else:
                print("Current number of rows is: "+ str(new_value+1))
        
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label3",text="Number of Rows",width=80,
                text_halign="left",text_valign="top",layout="Layout2")
            dlg.add_spin(name="Spin4",min=1,max=10,pos=5,increment=1,layout="Layout2")
            dlg.add_layout(name="Layout5",orientation=orientation.vertical,layout="Window")
            dlg.add_table(name="Table6",width=350,height=300,columns=["Heading1","Heading2","Heading3"],
                rows=5,layout="Layout5")
            dlg.generate_window()
            dlg.on_spin_changed(name="Spin4",callfunc=on_spin_changed)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_spin_changed({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_table_button_clicked(self, name, callfunc):
        r"""
        ## Description
        
        Set event when selecting a button cell. This API will trigger event only if the selected cell is button cell while dlg.on_table_sel_changed() will trigger event with all kinds of cell.
        
        ## Syntax
        
        ```psj
        dlg.on_table_button_clicked(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {22-23}
        from pyjdg import *
        
        def on_cell_button_clicked(dlg,name,cell):
            print(name + " has button cell row = " + str(cell.row_number))
            print(name + " has button cell column = " +
                str(cell.col_number))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",width=260,height=260,
                columns=["Heading1","Heading2"],
                rows=5,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",
                layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")   
            dlg.generate_window()
            dlg.set_table_cell_button(name="Table2",row=0,
                col=0,text="Button")
            dlg.on_table_button_clicked(name="Table2",
                callfunc=on_cell_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_table_button_clicked({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_table_right_menu(self, name, callfunc):
        r"""
        ## Description
        
        Set event when opening/executing context menu.
        
        ## Syntax
        
        ```psj
        dlg.on_table_right_menu(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {30}
        from pyjdg import *
        
        def on_menu(dlg,name,menu):
            print("Table name: "+ name)
            print("Clicked menu: "+ menu)
            table_cell = dlg.get_table_sel_cell(name)
            if menu == "Set Column Width":
                dlg.set_table_column_width(name,table_cell[0].col_number)
            elif menu == "Set Text Color":
                dlg.set_table_cell_text_color(name,table_cell[0])
            elif menu == "Set Cell Color":
                dlg.set_table_cell_fill_color(name)
            elif menu == "Custom Menu":
                print("You can put your function here")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",
                menus=["Set Cell Color","Set Text Color",
                "Set Column Width","Custom Menu"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_menu)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_table_right_menu({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_table_sel_changed(self, name, callfunc):
        r"""
        ## Description
        
        Set event when selecting a cell.
        
        ## Syntax
        
        ```psj
        dlg.on_table_sel_changed(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {22}
        from pyjdg import *
        
        def on_sel_change(dlg,name,cell):
            cellvector=dlg.get_table_sel_cell(name="Table1")
            if cellvector.size() > 0:
               print("Cell's position (row) = "+str(cellvector[0].row_number))
               print("Cell's position (column) = "+str(cellvector[0].col_number))
               print("---------------------------")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",menus=["Check cell info"])
            dlg.generate_window()
            dlg.on_table_sel_changed(name="Table1",callfunc=on_sel_change)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_table_sel_changed({},{})".format(name,callfunc)
        JPT_RUN_LINE(message)

    def on_textbox_input(self, name, callfunc, bool):
        r"""
        ## Description
        
        Bind a created function to a textbox component when its text is changed.
        
        ## Syntax
        
        ```psj
        dlg.on_textbox_input(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the TextBox component using for binding a created def function.
        - This is a required input.
        
        ### `callfunc`
        
        - The name of function wants to be bound to.
        - This is a required input.
        
        ### `bool`
        
        - A _Boolean_ specifying whether to validate the textbox.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        def on_input(dlg):
            text=dlg.get_item_text("TextBox2")
            if text=="1":
                return False
            else :
                print("Hello")
                return True
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_textbox(name="TextBox2",layout="Window")
            dlg.generate_window()
            dlg.on_textbox_input("TextBox2",on_input,True)
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.on_textbox_input({},{},{})".format(name,callfunc,bool)
        JPT_RUN_LINE(message)

    def remove_combobox_option(self, name, position):
        r"""
        ## Description
        
        Remove a specified option in a ComboBox.
        
        ## Syntax
        
        ```psj
        dlg.remove_combobox_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ### `position`
        - An _Integer_ specifying the position of option in ComboBox to be removed.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        from pyjdg import *
        
        def on_button_clicked(dlg):
            option_idx=dlg.get_combobox_sel(name="ComboBox2")
            option_name=dlg.get_combobox_option(name="ComboBox2",index=option_idx)
            dlg.remove_combobox_option(name="ComboBox2",position=option_idx)
            print("The option " + option_name + " is removed")
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4"],width=80,height=25,
                index=0,layout="Layout1")
            dlg.add_button(name="Button3",text="Remove Option",width=90,height=25,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_button_clicked(name="Button3",callfunc=on_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.remove_combobox_option({},{})".format(name,position)
        JPT_RUN_LINE(message)

    def remove_listbox_option(self, name, position):
        r"""
        ## Description
        
        Remove a specified option in a ListBox.
        
        ## Syntax
        
        ```psj
        dlg.remove_listbox_option(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ### `position`
        - An _Integer_ specifying the position of option in ListBox to be removed.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {8}
        from pyjdg import *
        
        def on_button_clicked (dlg):
        # It is possible to remove options one by one or multiple options at the same time
            options_idx=list(dlg.get_listbox_sels(name="ListBox2"))
            for idx in options_idx:
                option_name=dlg.get_listbox_option(name="ListBox2",option_index=options_idx[0])
                dlg.remove_listbox_option(name="ListBox2",position=options_idx[0])
                print("The option " + option_name + " is removed")
        
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_listbox(name="ListBox2",multisel=True,
              options=["item1","item2","item3"],width=100,height=150,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Button3",text="Remove Option",width=100,height=30,bk_color=15790320,layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_button_clicked(name="Button3",callfunc=on_button_clicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.remove_listbox_option({},{})".format(name,position)
        JPT_RUN_LINE(message)

    def select_table_range(self, name, cell_range):
        r"""
        ## Description
        
        Select a specific range by position in the Table.
        
        ## Syntax
        
        ```psj
        dlg.select_table_range(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `cell_range`
        
        - A _[TableCellRange](../data-type/psj-gui/TableCellRange)_ object specifying the information of a specific range (multi cells).
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {8-9}
        from pyjdg import *
        
        def on_click_select(dlg):
            left=int(dlg.get_item_text(name="TextBox5"))
            top=int(dlg.get_item_text(name="TextBox7"))
            right=int(dlg.get_item_text(name="TextBox9"))
            bottom=int(dlg.get_item_text(name="TextBox11"))
            dlg.select_table_range(name="Table1",
                cell_range=TableCellRange(left=left,top=top,right=right,bottom=bottom))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=14,
                columns=["Heading1","Heading2","Heading3","Heading4","Heading5"],
                layout="Window",width=560,height=260)
            dlg.add_groupbox(name="GroupBox2",text="Position",layout="Window")
            dlg.add_layout(name="Layout3",orientation=orientation.horizontal,
                layout="GroupBox2")
            dlg.add_label(name="Label4",text="Left",layout="Layout3")
            dlg.add_textbox(name="TextBox5",layout="Layout3")
            dlg.add_label(name="Label6",text="Top",layout="Layout3")
            dlg.add_textbox(name="TextBox7",layout="Layout3")
            dlg.add_label(name="Label8",text="Right",layout="Layout3")
            dlg.add_textbox(name="TextBox9",layout="Layout3")
            dlg.add_label(name="Label10",text="Bottom",layout="Layout3")
            dlg.add_textbox(name="TextBox11",layout="Layout3")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Select",text="Select",
                width=80,height=30,layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_command(name="Select",callfunc=on_click_select)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.select_table_range({},{})".format(name,cell_range)
        JPT_RUN_LINE(message)

    def set_cell_value(self, name, row, col, cell, index, value):
        r"""
        ## Description
        
        Set value for a specific cell of Table.
        
        ## Syntax
        
        ```psj
        dlg.set_cell_value(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Table component.
        - This is a required input.
        
        ### `row`
        
        - An _Integer_ specifying the position in the horizontal direction of the cell (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table. This argument is only used when _row_ and _col_ are not specified.
          - TableCellID(row,col) defines a cell object
          - TableCellID.row_number returns row number of the cell
          - TableCellID.col_number returns column number of the cell
        - This is a required input.
        
        ### `index`
        
        - An _Integer_ specifying the default option to be displayed of the Combobox. The starting value is 0 (fist option > index = 0)
        - This is a required input.
        
        ### `value`
        
        - A _String_ or *List of String* or *List of Integer* or *List of Double* specifying the content(s) which will be displayed on the selected cell.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {33-39}
        from pyjdg import *
        
        def get_table_cell_value(dlg,name,cell):
            cellvector=dlg.get_table_sel_cell(name="Table1")
            if cellvector.size()>0:
                value_cell=dlg.get_cell_value(name="Table1",
                    row=cellvector[0].row_number,
                    col=cellvector[0].col_number)
                dlg.set_item_text(name="Textbox4",text=value_cell)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",
                orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label3",text="Get Value",layout="Layout1")
            dlg.add_textbox(name="Textbox4",layout="Layout1")
            dlg.add_table(name="Table1",rows=5,
                columns=["String","Integer","Double"],
                layout="Window",width=360,height=260)
            dlg.set_table_column_data_type(name="Table1",
                col=0,data_type="String")
            dlg.set_table_column_data_type(name="Table1",
                col=1,data_type="Integer")
            dlg.set_table_column_data_type(name="Table1",
                col=2,data_type="Double",precision=5)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")   
            dlg.generate_window()
            dlg.on_table_sel_changed(name="Table1",callfunc=get_table_cell_value)
            dlg.set_cell_value(name="Table1",row=0,col=0,value="Option1")
            dlg.set_cell_value(name="Table1",
                row=1,col=0,value=["Option2","Option3"])
            dlg.set_cell_value(name="Table1",row=0,col=1,value="1")
            dlg.set_cell_value(name="Table1",row=1,col=1,value=[2,3])
            dlg.set_cell_value(name="Table1",row=0,col=2,value="1.5")
            dlg.set_cell_value(name="Table1",cell=TableCellID(1,2),value=[2.5,3.5,4.5], index=1) 
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_cell_value({},{},{},{},{},{})".format(name,row,col,cell,index,value)
        JPT_RUN_LINE(message)

    def set_checkbox_state(self, name, checked):
        r"""
        ## Description
        
        Set the state of the CheckBox to checked or unchecked.
        
        ## Syntax
        
        ```psj
        dlg.set_checkbox_state(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component in which will be used for setting the state to checked/unchecked.
        - This is a required input.
        
        ### `checked`
        
        - A _Boolean_ specifying the state of the CheckBox:
          - _True_: The initial state of the CheckBox component is checked.
          - _False_: The initial state of the CheckBox component is unchecked.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_checkbox(name="CheckBox2",text="Jupiter",checked=True,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_checkbox_state(name="CheckBox2",checked=False)
            isChecked = dlg.isbutton_checked(name="CheckBox2")
            print(isChecked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_checkbox_state({},{})".format(name,checked)
        JPT_RUN_LINE(message)

    def set_combobox_sel(self, name, option):
        r"""
        ## Description
        
        Set current selection to the ComboBox component.
        
        ## Syntax
        
        ```psj
        dlg.set_combobox_sel(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ComboBox component.
        - This is a required input.
        
        ### `option`
        
        - An _Integer_ or _String_ specifying the order of the ComboBox component's values or the name of selected item.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4","item5"],width=70,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_combobox_sel(name="ComboBox2",option=3)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_combobox_sel({},{})".format(name,option)
        JPT_RUN_LINE(message)

    def set_groupbox_checked(self, name, checked):
        r"""
        ## Description
        
        Set the initial state of the GroupBox's checkbox to enable/disable GroupBox's components.
        
        ## Syntax
        
        ```psj
        dlg.set_groupbox_checked(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of GroupBox which will be used for setting the state of its checkbox.
        - This is a required input.
        
        ### `checked`
        
        - A _Boolean_ specifying the state of the GroupBox's checkbox:
          - _True_: Enable the checkbox with its state is checked (all components inside are available to use).
          - _False_: Enable the checkbox with its state is unchecked (all components inside are unavailable to use).
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox1",text="GroupBox",layout="Window")
            dlg.set_groupbox_checked(name="GroupBox1",checked=True)
            dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="GroupBox1")
            dlg.add_label(name="Label3",text="Label",layout="Layout2")
            dlg.add_textbox(name="TextBox4",layout="Layout2")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_groupbox_checked({},{})".format(name,checked)
        JPT_RUN_LINE(message)

    def set_groupbox_collapsed(self, name, collapsed):
        r"""
        ## Description
        
        Set the initial state of the GroupBox's collapse feature to show/hide GroupBox's components.
        
        ## Syntax
        
        ```psj
        dlg.set_groupbox_collapsed(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of GroupBox which will be used for setting the state of its collapse feature.
        - This is a required input.
        
        ### `collapsed`
        
        - A _Boolean_ specifying the state of the GroupBox's collapse feature:
          - _True_: Enable the collapse with its state is collapsed (hide all GroupBox's components).
          - _False_: Enable the collapse with its state is expanded (show all GroupBox's components).
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox1",text="GroupBox",layout="Window")
            dlg.set_groupbox_collapsed(name="GroupBox1",collapsed=True)
            dlg.set_groupbox_orientation(name="GroupBox1",orientation="horizontal")
            dlg.add_label(name="Label2",text="Label",layout="GroupBox1")
            dlg.add_textbox(name="TextBox3",layout="GroupBox1")
            dlg.add_label(name="Label4",text="Label",layout="GroupBox1")
            dlg.add_textbox(name="TextBox5",layout="GroupBox1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_groupbox_collapsed({},{})".format(name,collapsed)
        JPT_RUN_LINE(message)

    def set_groupbox_orientation(self, name, orientation):
        r"""
        ## Description
        
        Set the layout of all the components inside the GroupBox component to be aligned in the horizontal or vertical direction.
        
        ## Syntax
        
        ```psj
        dlg.set_groupbox_orientation(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component using for setting the orientation option.
        - This is a required input.
        
        ### `orientation`
        
        - A _String_ specifying the orientation option of the GroupBox:
          - "vertical": align all the inside components in the vertical direction.
          - "horizontal": align all the inside components in the horizontal direction.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox1",text="GroupBox",layout="Window")
            dlg.set_groupbox_orientation(name="GroupBox1",orientation="vertical")
            dlg.add_label(name="Label2",text="Label",layout="GroupBox1")
            dlg.add_textbox(name="TextBox3",layout="GroupBox1")
            dlg.add_label(name="Label4",text="Label",layout="GroupBox1")
            dlg.add_textbox(name="TextBox5",layout="GroupBox1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_groupbox_orientation({},{})".format(name,orientation)
        JPT_RUN_LINE(message)

    def set_icon_file(self, file):
        r"""
        ## Description
        
        Set icon for the creating GUI dialog.
        
        ## Syntax
        
        ```psj
        dlg.set_icon_file(...)
        ```
        
        ## Inputs
        
        ### `file`
        
        - A _String_ specifying the full path of the icon file using to set the icon for the creating GUI dialog.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {8}
        from pyjdg import *
        
        def main():
            sel_ico = JPT.GetProgramPath() + \
                r"Lib\site-packages\win32\test\win32rcparser\python.ico"
        
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.set_icon_file(file=sel_ico)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_icon_file({})".format(file)
        JPT_RUN_LINE(message)

    def set_image_file(self, name, image_path):
        r"""
        ## Description
        
        Set an image to the ImageCtrl.
        
        ## Syntax
        
        ```psj
        dlg.set_image_file(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ImageCtrl component.
        - This is a required input.
        
        ### `image_path`
        
        - A _String_ specifying the full path of the image.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        
        def onChangeButtonClicked(dlg):
            new_pic = JPT.GetProgramPath() + r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt_Pics\M4.JPG"
            dlg.set_image_file(name="ImageCtrl",image_path=new_pic)
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            image = JPT.GetProgramPath() + \
                r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt_Pics\M3.JPG"
            dlg.add_imagectrl(name="ImageCtrl",image_file=image,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ChangePic",text="Change",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_command(name="ChangePic",callfunc=onChangeButtonClicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_image_file({},{})".format(name,image_path)
        JPT_RUN_LINE(message)

    def set_item_font(self, name, font):
        r"""
        ## Description
        
        Set font properties to the text inside the component.
        
        ## Syntax
        
        ```psj
        dlg.set_item_font(...)
        ```
        
        ## Inputs
                                                                                                            
        ### `name`
        
        - A _String_ specifying the name of the component which you want to set the font properties.
        - This is a required input.
        
        ### `font`
        
        - A _Class_ of [PSJFont](../data-type/psj-gui/PSJFont) specifying font properties.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {19}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_textbox(name="TextBox2",layout="Window", width=350, 
                height=35, text_color=255)
            font_TextBox2=PSJFont()
            font_TextBox2.size=18
            font_TextBox2.bold=True
            font_TextBox2.italic=True
            font_TextBox2.underline=True
            font_TextBox2.strikeout=False
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_item_font(name="TextBox2",font=font_TextBox2)
            dlg.set_item_text(name="TextBox2", text="This is a sample text")
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_item_font({},{})".format(name,font)
        JPT_RUN_LINE(message)

    def set_item_size_behavior(self, name, behavior=size_behavior.greedy):
        r"""
        ## Description
        
        Set display behavior of TabWnd, ImgCtrl, Table, PagesCtrl.
        
        ## Syntax
        
        ```psj
        dlg.set_item_size_behavior(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying name of the used component.
        - This is a required input.
        
        ### `behavior`
        
        - An _Enum_ specifying display type of the used component:
          - size_behavior.greedy: Set the displaying component based on the user input width and height, allow resizing component size according to dialog size.
          - size_behavior.fixed: Set the displaying component based on the user input width and height, and won't resize component size according to dialog size.
            For ImageCtrl, `fixed` will take original size of the image to display fitfully.
          - size_behavior.horizontal: Set the displaying component with fixing height based on user input and allow resizing component only horizontally.
          - size_behavior.vertical: Set the displaying component with fixing width based on user input and allow resizing component only vertically.
        - The default value is size_behavior.greedy.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        <Tabs>
        <TabItem value="TabWnd" label="TabWnd" default>
        
        ```psj {6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog")
            dlg.add_tabwnd(name="TabWnd2",width=400,height=300,layout="Window")
            dlg.set_item_size_behavior(name="TabWnd2",behavior=size_behavior.greedy)
            dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem3",page_text="TabItem")
            dlg.add_label(name="Label4",text="Label",text_halign="left",text_valign="top",layout="TabItem3")
            dlg.add_textbox(name="TextBox5",layout="TabItem3")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        </TabItem>
        <TabItem value="ImageCtrl" label="ImageCtrl">
        
        ```psj {7}
        from pyjdg import *
        TechnoStarImage = JPT.GetProgramPath() + "SampleData/PSJ/PSJ-Utility/Utils/TechnoStar.ico"
        
        def main():
            dlg=JDGCreator(title="Dialog")
            dlg.add_imagectrl(name="ImageCtrl2",width=100,height=100,image_file=TechnoStarImage,layout="Window")
            dlg.set_item_size_behavior(name="ImageCtrl2",behavior=size_behavior.fixed)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        </TabItem>
        <TabItem value="Table" label="Table">
        
        ```psj {9}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog")
            dlg.add_table(name="Table2",width=400,height=250,columns=["Heading1","Heading2","Heading3"],rows=5,layout="Window")
            dlg.set_table_column_data_type(name="Table2",col=0,data_type="String")
            dlg.set_table_column_data_type(name="Table2",col=1,data_type="String")
            dlg.set_table_column_data_type(name="Table2",col=2,data_type="String")
            dlg.set_item_size_behavior(name="Table2",behavior=size_behavior.horizontal)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        </TabItem>
        <TabItem value="PagesCtrl" label="PagesCtrl">
        
        ```psj {6}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog")
            dlg.add_pagesctrl(name="PagesCtrl2",width=300,height=250,layout="Window")
            dlg.set_item_size_behavior(name="PagesCtrl2",behavior=size_behavior.vertical)
            dlg.add_pageitem(name="PagesCtrl2",page_name="PageItem3",page_header="PageItem")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        </TabItem>
        
        </Tabs>
        
        """
        message = "dlg.set_item_size_behavior({},{})".format(name,behavior)
        JPT_RUN_LINE(message)

    def set_item_text(self, name, text):
        r"""
        ## Description
        
        Set the text which will be shown inside the component.
        
        ## Syntax
        
        ```psj
        dlg.set_item_text(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component.
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying the content displayed.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {3}
        from pyjdg import *
        def onSetButtonClicked(dlg):
            dlg.set_item_text(name="TextBox1",text="This is sample text")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_textbox(name="TextBox1",layout="Window")
            dlg.add_button(name="Button2",text="Set text",width=60,height=22,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_command(name="Button2",callfunc=onSetButtonClicked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_item_text({},{})".format(name,text)
        JPT_RUN_LINE(message)

    def set_item_visble(self, name, visible):
        r"""
        ## Description
        
        Set the state of the created component as visible or hidden, usable for all ToolBox types.
        
        ## Syntax
        
        ```psj
        dlg.dlg.set_item_visible(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component to be shown or hidden.
        - This is a required input.
        
        ### `visible`
        
        - A _Boolean_ specifying the state of the specified component:
          - _True_: Show the component.
          - _False_: Hide the component.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6-8,10-12}
        from pyjdg import *
        
        def on_combobox_changed(dlg):
            combobox_sel = dlg.get_combobox_sel(name="ComboBox4")
            if combobox_sel == 1:
                dlg.set_item_visible(name="PageItem8",visible=False)
                dlg.set_item_visible(name="PageItem9",visible=False)
                dlg.set_item_visible(name="Table14",visible=False)
            if combobox_sel == 0:
                dlg.set_item_visible(name="PageItem8",visible=True)
                dlg.set_item_visible(name="PageItem9",visible=True)
                dlg.set_item_visible(name="Table14",visible=True)
        
        def main():
            dlg=JDGCreator(title="Dialog",include_apply=False)
            dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label3",text="Select Layout",text_halign="left",text_valign="top",layout="Layout2")
            dlg.add_combobox(name="ComboBox4",options=["Layout1","Layout2"],index=0,layout="Layout2")
            dlg.add_layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
            dlg.add_pagesctrl(name="PagesCtrl6",width=260,height=160,current_page=2,layout="Layout5")
            dlg.add_pageitem(name="PagesCtrl6",page_name="PageItem7",page_header="First page")
            dlg.add_groupbox(name="GroupBox10",text="GroupBox",layout="PageItem7")
            dlg.add_layout(name="Layout11",orientation=orientation.horizontal,layout="GroupBox10")
            dlg.add_label(name="Label12",text="Label",text_halign="left",text_valign="top",layout="Layout11")
            dlg.add_browser(name="Browser13",mode="file",file_filter="All Files(*.*)",layout="Layout11")
            dlg.add_table(name="Table14",width=260,height=160,columns=["Heading1","Heading2"],rows=5,layout="GroupBox10")
            dlg.add_pageitem(name="PagesCtrl6",page_name="PageItem8",page_header="Second page")
            dlg.add_pageitem(name="PagesCtrl6",page_name="PageItem9",page_header="Third page")
            dlg.generate_window()
            dlg.set_pagesctrl_current_page(name="PagesCtrl6",page_index=0)
            dlg.on_combobox_sel(name="ComboBox4",callfunc=on_combobox_changed)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_item_visble({},{})".format(name,visible)
        JPT_RUN_LINE(message)

    def set_listbox_sel(self, name, option):
        r"""
        ## Description
        
        Set current selection to the ListBox component.
        
        ## Syntax
        
        ```psj
        dlg.set_listbox_sel(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the ListBox component.
        - This is a required input.
        
        ### `option`
        
        - An _Integer_ or _String_ specifying the order of the ListBox component's values or the name of selected item.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {14}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,0,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],
                width=100,height=150,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_listbox_sel(name="ListBox2",option=3)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_listbox_sel({},{})".format(name,option)
        JPT_RUN_LINE(message)

    def set_pagesctrl_current_page(self, name, page_index):
        r"""
        ## Description
        
        Set current displayed PageItem in PagesCtrl.
        
        ## Syntax
        
        ```psj
        dlg.set_pagesctrl_current_page(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name the PagesCtrl.
        - This is a required input.
        
        ### `page_index`
        
        - An _Integer_ specifying the index position of the PageItem (starts from 0).
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {5}
        from pyjdg import *
        
        def switch_page(dlg):
            page = dlg.get_combobox_sel(name="switcher")
            dlg.set_pagesctrl_current_page(name='PagesCtrl2',page_index=page)
        
        def main():
        
            dlg=JDGCreator(title="Switch page sample",resizable=True,validation=True)
            dlg.add_groupbox(name="GroupBox1",text="Set current page from combobox",layout="Window")
            dlg.set_groupbox_orientation("GroupBox1","horizontal")
            dlg.add_label(name="Label2",text="Select current page",layout="GroupBox1")
            dlg.add_combobox(name="switcher",options=["First page","Second page","Third page"],layout="GroupBox1")
            dlg.add_groupbox(name="GroupBox2",text="Current page display",layout="Window")
            dlg.set_groupbox_orientation("GroupBox2","horizontal")
            dlg.add_pagesctrl(name="PagesCtrl2",width=260,height=160,layout="GroupBox2")
            dlg.add_pageitem(name="PagesCtrl2",page_name="PageItem3",page_header="First page")
            dlg.add_pageitem(name="PagesCtrl2",page_name="PageItem4",page_header="Second page")
            dlg.add_pageitem(name="PagesCtrl2",page_name="PageItem5",page_header="Third page")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.on_combobox_sel(name="switcher",callfunc=switch_page)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_pagesctrl_current_page({},{})".format(name,page_index)
        JPT_RUN_LINE(message)

    def set_radiobutton_state(self, name, checked):
        r"""
        ## Description
        
        Set the state of the RadioButton to checked or unchecked.
        
        ## Syntax
        
        ```psj
        dlg.set_radiobutton_state(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the component in which will be used for setting the state to selected/unselected.
        - This is a required input.
        
        ### `checked`
        
        - A _Boolean_ specifying the state of the checkbox:
          - _True_: The initial state of the checkbox component is checked.
          - _False_: The initial state of the checkbox component is unchecked.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
            dlg.add_radiobutton(name="RadioButton2",text="Jupiter",checked=True,layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_radiobutton_state(name="RadioButton2",checked=False)
            isChecked = dlg.isbutton_checked(name="RadioButton2")
            print(isChecked)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_radiobutton_state({},{})".format(name,checked)
        JPT_RUN_LINE(message)

    def set_slider_bothtics(self, name, enabled):
        r"""
        ## Description
        
        Show tick marks on both/one side of the SliderBar.
        
        ## Syntax
        
        ```psj
        dlg.set_slider_bothtics(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the SliderBar.
        - This is a required input.
        
        ### `enabled`
        
        - A _Boolean_ specifying the way to display tick mark:
          - _True_: show tick mark on both side of the SliderBar.
          - _False_: show tick mark only on one side of the SliderBar.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_slider(name="Slider3",width=200,height=100,min=0,max=100,pos=0,layout="Layout1")
            dlg.set_slider_bothtics(name="Slider3",enabled=True)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_slider_bothtics({},{})".format(name,enabled)
        JPT_RUN_LINE(message)

    def set_slider_show_border(self, name, enabled):
        r"""
        ## Description
        
        Show border of the SliderBar.
        
        ## Syntax
        
        ```psj
        dlg.set_slider_show_border(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the SliderBar.
        - This is a required input.
        
        ### `enabled`
        
        - A _Boolean_ specifying the state of the slider's border:
          - _True_: show outside border of the creating SliderBar.
          - _False_: hide outside border of the creating SliderBar.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_slider(name="Slider3",width=100,height=30,min=0,max=100,pos=0,layout="Layout1")
            dlg.set_slider_show_border(name="Slider3",enabled=True)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_slider_show_border({},{})".format(name,enabled)
        JPT_RUN_LINE(message)

    def set_slider_show_tics(self, name, enabled):
        r"""
        ## Description
        
        Show tick marks of the SliderBar.
        
        ## Syntax
        
        ```psj
        dlg.set_slider_show_tics(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the SliderBar.
        - This is a required input.
        
        ### `enabled`
        
        - A _Boolean_ specifying the state of the slider's tick mark:
          - _True_: show all the tick mark.
          - _False_: hide all the tick mark.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_slider(name="Slider3",width=100,height=30,min=0,max=100,pos=0,layout="Layout1")
            dlg.set_slider_show_tics(name="Slider3",enabled=False)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_slider_show_tics({},{})".format(name,enabled)
        JPT_RUN_LINE(message)

    def set_slider_vertical(self, name, enabled):
        r"""
        ## Description
        
        Show the SliderBar in the vertical or horizontal direction.
        
        ## Syntax
        
        ```psj
        dlg.set_slider_vertical(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the SliderBar.
        - This is a required input.
        
        ### `enabled`
        
        - A _Boolean_ specifying the direction of the SliderBar:
          - _True_: creating SliderBar will be put in the vertical direction.
          - _False_: creating SliderBar will be put in the horizontal direction.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_slider(name="Slider3",width=100,height=100,min=0,max=100,pos=0,layout="Layout1")
            dlg.set_slider_vertical(name="Slider3",enabled=True)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_slider_vertical({},{})".format(name,enabled)
        JPT_RUN_LINE(message)

    def set_table_cell_alignment(self, name, row, col, alignment):
        r"""
        ## Description
        
        Set text alignment of cell.
        
        ## Syntax
        
        ```psj
        dlg.set_table_cell_alignment(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `row`
        
        - An _Integer_ specifying the order of row (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the order of column (starts from 0).
        - This is a required input.
        
        ### `alignment`
        
        - A _String_ specifying alignment position of content inside a cell.
          - "Left": Align content to the left
          - "Center": Center the content
          - "Right": Align content to the right
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {4-9}
        from pyjdg import *
        
        def on_click_set_alignment(dlg):
            dlg.set_table_cell_alignment(name="Table1",row=0,col=0,
                alignment="Left")
            dlg.set_table_cell_alignment(name="Table1",row=1,col=0,
                alignment="Center")
            dlg.set_table_cell_alignment(name="Table1",row=2,col=0,
                alignment="Right")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=360,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonSetAlignment",width=70,height=30,
                text="Set Alignment",layout="footer")
            dlg.add_button(name="Ok",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_table_column_width(name="Table1",col=0,width=200)
            dlg.set_cell_value(name="Table1",row=0,col=0,
                value="Left Alignment")
            dlg.set_cell_value(name="Table1",row=1,col=0,
                value="Center Alignment")
            dlg.set_cell_value(name="Table1",row=2,col=0,
                value="Right Alignment")
            dlg.on_command(name="ButtonSetAlignment",callfunc=on_click_set_alignment)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_table_cell_alignment({},{},{},{})".format(name,row,col,alignment)
        JPT_RUN_LINE(message)

    def set_table_cell_button(self, name, row, col, text):
        r"""
        ## Description
        
        Set button cell in the Table.
        
        ## Syntax
        
        ```psj
        dlg.set_table_cell_button(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Table component.
        - This is a required input.
        
        ### `row`
        
        - An _Integer_ specifying the order of row (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the order of column (starts from 0).
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying text which will be displayed on the button.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {15-16}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",width=260,height=260,
                columns=["Heading1","Heading2"],
                rows=5,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",
                layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_table_cell_button(name="Table2",row=0,
                col=0,text="Button")
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_table_cell_button({},{},{},{})".format(name,row,col,text)
        JPT_RUN_LINE(message)

    def set_table_cell_checkbox(self, name, row, col, text, checked=False):
        r"""
        ## Description
        
        Set checkbox cell in the Table.
        
        ## Syntax
        
        ```psj
        dlg.set_table_cell_checkbox(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Table component.
        - This is a required input.
        
        ### `row`
        
        - An _Integer_ specifying the order of row (starts from 0).
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the order of column (starts from 0).
        - This is a required input.
        
        ### `text`
        
        - A _String_ specifying text which will be displayed next to the checkbox.
        - This is a required input.
        
        ### `checked`
        
        - A _Boolean_ specifying the state of checkbox.
          - _True_: the checkbox is checked.
          - _False_: the checkbox is unchecked.
        - The default value is _False_.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {15-16}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table2",width=260,height=260,
                columns=["Heading1","Heading2"],
                rows=5,layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",
                layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_table_cell_checkbox(name="Table2",row=0,
                col=0,text="Checkbox",checked=True)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_table_cell_checkbox({},{},{},{},{})".format(name,row,col,text,checked)
        JPT_RUN_LINE(message)

    def set_table_cell_fill_color(self, name, cell, color):
        r"""
        ## Description
        
        Set fill color to the selected/specified cells.
        
        ## Syntax
        
        ```psj
        dlg.set_table_cell_fill_color(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table.
        - If not specified, all the selected cells will be used.
        
        ### `color`
        
        - An _Integer_ specifying the color.
        - If not specified, a color picker dialog is opened for user to select.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6,8-9,11-12,14-15,17-19}
        from pyjdg import *
        
        def on_menu(dlg,name,menu):
            cellvector=dlg.get_table_sel_cell(name="Table1")
            if menu=="Set Fill Color for all selected cells using color picker":
                dlg.set_table_cell_fill_color(name="Table1")
            elif menu=="Set Fill Color only for a selected cell using color picker":
                 dlg.set_table_cell_fill_color(name="Table1",
                    cell=cellvector[0])
            elif menu=="Set Fill Color only for a selected cell with red color":
                dlg.set_table_cell_fill_color(name="Table1",
                    cell=cellvector[0],color=7105764)
            elif menu=="Set Fill Color only for the first cell with red color":
                dlg.set_table_cell_fill_color(name="Table1",
                    cell=TableCellID(row=0,col=0),color=7105764)
            elif menu=="Set Fill Color only for the first 2x2 cells with red color":
                [[dlg.set_table_cell_fill_color(name="Table1",
                    cell=TableCellID(row=i,col=j),color=7105764)
                    for i in (0,1)] for j in (0,1)]
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",
                menus=["Set Fill Color for all selected cells using color picker",
                "Set Fill Color only for a selected cell using color picker",
                "Set Fill Color only for a selected cell with red color",
                "Set Fill Color only for the first cell with red color",
                "Set Fill Color only for the first 2x2 cells with red color"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_menu)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_table_cell_fill_color({},{},{})".format(name,cell,color)
        JPT_RUN_LINE(message)

    def set_table_cell_text_color(self, name, cell, color):
        r"""
        ## Description
        
        Set color to text in the selected/specified cells.
        
        ## Syntax
        
        ```psj
        dlg.set_table_cell_text_color(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `cell`
        
        - A _[TableCellID](../data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table.
        - If not specified, all the selected cells will be used.
        
        ### `color`
        
        - An _Integer_ specifying the color.
        - If not specified, a color picker dialog is opened for user to select.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6,8-9,11-12,14-15,17-19}
        from pyjdg import *
        
        def on_menu(dlg,name,menu):
            cellvector=dlg.get_table_sel_cell(name)
            if menu=="Set Text Color for all selected cells using color picker":
                dlg.set_table_cell_text_color(name="Table1")
            elif menu=="Set Text Color only for a selected cell using color picker":
                 dlg.set_table_cell_text_color(name="Table1",
                    cell=cellvector[0])
            elif menu=="Set Text Color only for a selected cell with red color":
                dlg.set_table_cell_text_color(name="Table1",
                    cell=cellvector[0],color=7105764)
            elif menu=="Set Text Color only for the first cell with red color":
                dlg.set_table_cell_text_color(name="Table1",
                    cell=TableCellID(row=0,col=0),color=7105764)
            elif menu=="Set Text Color only for the first 2x2 cells with red color":
                [[dlg.set_table_cell_text_color(name="Table1",
                    cell=TableCellID(row=i,col=j),color=7105764)
                    for i in (0,1)] for j in (0,1)]
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",
                menus=["Set Text Color for all selected cells using color picker",
                "Set Text Color only for a selected cell using color picker",
                "Set Text Color only for a selected cell with red color",
                "Set Text Color only for the first cell with red color",
                "Set Text Color only for the first 2x2 cells with red color"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_menu)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_table_cell_text_color({},{},{})".format(name,cell,color)
        JPT_RUN_LINE(message)

    def set_table_column_data_type(self, name, col, data_type, precision=2):
        r"""
        ## Description
        
        Set data type validation of cell of Table.
        
        ## Syntax
        
        ```psj
        dlg.set_table_column_data_type(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the order of column (starts from 0).
        - This is a required input.
        
        ### `data_type`
        
        - A _String_ specifying the data type validation for the column of Table.
        - Support 3 types: "String", "Integer" and "Double"
        - This is a required input.
        
        ### `precision`
        
        - An _Integer_ specifying number of digits after floating point displayed inside a Double column.
        - The default value is 2.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {8-13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["String","Integer","Double"],
                layout="Window",width=260,height=260)    
            dlg.set_table_column_data_type(name="Table1",
                col=0,data_type="String")
            dlg.set_table_column_data_type(name="Table1",
                col=1,data_type="Integer")
            dlg.set_table_column_data_type(name="Table1",
                col=2,data_type="Double",precision=5)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="Ok",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_table_column_data_type({},{},{},{})".format(name,col,data_type,precision)
        JPT_RUN_LINE(message)

    def set_table_column_width(self, name, col, width):
        r"""
        ## Description
        
        Set the width of the specified column in the Table.
        
        ## Syntax
        
        ```psj
        dlg.set_table_column_width(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of Table.
        - This is a required input.
        
        ### `col`
        
        - An _Integer_ specifying the order of the column where its width will be changed (starts from 0).
        - This is a required input.
        
        ### `width`
        
        - An _Integer_ specifying the column width.
        - If not specified, a dialog is opened for user to enter a value.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {6-7,9-10}
        from pyjdg import *
        
        def on_menu(dlg,name,menu):
            cellvector=dlg.get_table_sel_cell(name)
            if menu=="Set Column Width using Dialog":
                dlg.set_table_column_width(name="Table1",
                    col=cellvector[0].col_number)
            if menu=="Set Column Width equal 400":
                dlg.set_table_column_width(name="Table1",
                    col=cellvector[0].col_number,width=400)
            elif menu=="Get Column Width":
                col_width = dlg.get_table_column_width(name="Table1",
                    col=cellvector[0].col_number)
                print("Column "+str(cellvector[0].col_number)+
                    " width is: "+str(col_width))
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_table(name="Table1",rows=5,
                columns=["Heading1","Heading2"],
                layout="Window",width=260,height=260)
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_table_right_menu(name="Table1",
                menus=["Set Column Width using Dialog",
                "Set Column Width equal 400","Get Column Width"])
            dlg.generate_window()
            dlg.on_table_right_menu(name="Table1",callfunc=on_menu)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_table_column_width({},{},{})".format(name,col,width)
        JPT_RUN_LINE(message)

    def set_tabwnd_current_page(self, name, page_index):
        r"""
        ## Description
        
        Set the current page of the TabWnd to a specific TabItem order.
        
        ## Syntax
        
        ```psj
        dlg.set_tabwnd_current_page(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the TabWnd component using for setting the current page.
        - This is a required input.
        
        ### `page_index`
        
        - An _Integer_ specifying the tab order.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {23}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_tabwnd(name="TabWnd2",width=300,height=300,layout="Layout1")
            dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem3",page_text="Jupiter-Pre",page_orientation="horizontal")
            dlg.add_label(name="Label7",text="Label",layout="TabItem3")
            dlg.add_textbox(name="TextBox8",layout="TabItem3")
            dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem4",page_text="Jupiter-Post")
            dlg.add_radiobutton(name="RadioButton9",text="RadioButton",layout="TabItem4")
            dlg.add_radiobutton(name="RadioButton10",text="RadioButton",layout="TabItem4")
            dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem5",page_text="Sunshine")
            dlg.add_slider(name="Slider11",width=100,height=30,min=0,max=100,pos=0,layout="TabItem5")
            dlg.add_tabwnd_page(name="TabWnd2",page_name="TabItem6",page_text="PSJ")
            dlg.add_listbox(name="ListBox12",width=100,height=100,layout="TabItem6")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.set_tabwnd_current_page(name="TabWnd2",page_index=2)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.set_tabwnd_current_page({},{})".format(name,page_index)
        JPT_RUN_LINE(message)

    def show_dlg_help_button(self, shown):
        r"""
        ## Description
        
        Show or hide the help button in the creating dialog.
        
        ## Syntax
        
        ```psj
        dlg.show_dlg_help_button(...)
        ```
        
        ## Inputs
        
        ### `shown`
        
        - A _Boolean_ specifying the visibility of the help button:
          - _True_: show the help button
          - _False_: hide the help button
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Label",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.show_dlg_help_button(shown=False)
            dlg.generate_window()
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.show_dlg_help_button({})".format(shown)
        JPT_RUN_LINE(message)

    def show_layout(self, name):
        r"""
        ## Description
        
        Show the Layout and all the children components inside.
        
        ## Syntax
        
        ```psj
        dlg.show_layout(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying the name of the Layout component using for showing along with all of its inside components.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {4}
        from pyjdg import *
        
        def show_layout(dlg):
            dlg.show_layout(name="Layout5")
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
            dlg.add_label(name="Label2",text="Label",layout="Layout1")
            dlg.add_textbox(name="TextBox3",layout="Layout1")
            dlg.add_layout(name="Layout4",orientation=orientation.horizontal,layout="Window")
            dlg.add_richeditbox(name="RichEditBox8",text="RichEditBox",width=200,height=200,layout="Layout4")
            dlg.add_layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
            dlg.add_textbox(name="TextBox7",layout="Layout5")
            dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
            dlg.add_combobox(name="ComboBox9",layout="Layout6")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.hide_layout(name="Layout5")
            dlg.on_command(name="ButtonApply",callfunc=show_layout)
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.show_layout({})".format(name)
        JPT_RUN_LINE(message)

    def show_tooltip(self, name, tip):
        r"""
        ## Description
        
        Show tooltip when user hovers the mouse to a UI component.
        
        ## Syntax
        
        ```psj
        dlg.show_tooltip(...)
        ```
        
        ## Inputs
        
        ### `name`
        
        - A _String_ specifying name of the UI component.
        - This is a required input.
        
        ### `tip`
        
        - A _String_ specifying text appears when mouse hovers.
        - This is a required input.
        
        ## Return Code
        
        This function does not have output value.
        
        ## Sample Code
        
        ```psj {24-32}
        from pyjdg import *
        
        def main():
            dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
            dlg.add_label(name="Label1",text="Label",layout="Window")
            dlg.add_textbox(name="TextBox2",layout="Window")
            dlg.add_richeditbox(name="RichEditBox3",text="RichEditBox",
                width=200,height=200,layout="Window")
            dlg.add_combobox(name="ComboBox4",layout="Window")
            dlg.add_checkbox(name="CheckBox5",text="CheckBox",layout="Window")
            dlg.add_radiobutton(name="RadioButton6",text="RadioButton",
                layout="Window")
            dlg.add_button(name="Button7",text="Button",width=60,height=22,
                layout="Window")
            dlg.add_spin(name="Spin8",layout="Window")
            dlg.add_slider(name="Slider9",width=100,height=30,min=0,max=100,pos=0,
                layout="Window")
            dlg.add_hlayout(name="footer",layout="Window")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
            dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
            dlg.add_space(orientation="horizontal",layout="footer")
            dlg.generate_window()
            dlg.show_tooltip(name="Label1",tip="Tooltip for Label1")
            dlg.show_tooltip(name="TextBox2",tip="Tooltip for TextBox2")
            dlg.show_tooltip(name="RichEditBox3",tip="Tooltip for RichEditBox3")
            dlg.show_tooltip(name="ComboBox4",tip="Tooltip for ComboBox4")
            dlg.show_tooltip(name="CheckBox5",tip="Tooltip for CheckBox5")
            dlg.show_tooltip(name="RadioButton6",tip="Tooltip for RadioButton6")
            dlg.show_tooltip(name="Button7",tip="Tooltip for Button7")
            dlg.show_tooltip(name="Spin8",tip="Tooltip for Spin8")
            dlg.show_tooltip(name="Slider9",tip="Tooltip for Slider9")
        
        if __name__=='__main__':
            main()
        ```
        
        """
        message = "dlg.show_tooltip({},{})".format(name,tip)
        JPT_RUN_LINE(message)

