from kivy.app import App

from kivy.uix.button import  Button

from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

from math import pi

from kivy.uix.pagelayout import PageLayout


Sıralar_Arası = { #Sıralar Arası
"pasa" : 2.5,
"cevher" : 2.8,
"şev" : 1.8,
"rampa" : 2.1
}

Delikler_Arası ={ #Delikler Arası
"pasa" : 2.9,
"cevher" : 3.2,
"şev" : 2,
"rampa" : 2.5
}

türler_kısayol = {
    "p" : "pasa",
    "c" : "cevher",
    "ş" : "şev",
    "r" : "rampa"
}



class PageLayout(PageLayout):
    """
    Define class PageLayout here
    """

    def __init__(self):
        # The super function in Python can be
        # used to gain access to inherited methods
        # which is either from a parent or sibling class.
        super(PageLayout, self).__init__()

        # creating buttons on different pages

        #ilk sayfa

        self.All_box = BoxLayout(orientation='vertical')
        self.box = BoxLayout(orientation='horizontal')

        self.Result = TextInput(hint_text='Result(PF) = kg/m3')
        self.txt = TextInput(hint_text='pasa,cevher,şev,rampa')
        self.delik_sayısı = TextInput(hint_text='delik sayısı')
        self.btn = Button(text='Calculate', on_press=self.Calculate)
        self.clear_btn = Button(text='Clear All', on_press=self.Clear)

        self.sıralar_arası_txt = TextInput(hint_text='sıralar arası')
        self.delikler_arası_txt = TextInput(hint_text='delikler arası')

        self.ort_delik_boyu = TextInput(hint_text='ort delik boyu')
        self.total_patlayıcı_miktarı = TextInput(hint_text='total patlayıcı miktarı')

        self.box1 = BoxLayout(orientation='horizontal')


        self.All_box.add_widget(self.total_patlayıcı_miktarı)

        self.box.add_widget(self.sıralar_arası_txt)
        self.box.add_widget(self.delikler_arası_txt)

        self.box.add_widget(self.delik_sayısı)





        self.box.add_widget(self.ort_delik_boyu)

        self.box1.add_widget(self.Result)
        self.box1.add_widget(self.btn)

        self.bottom_box = BoxLayout(orientation='horizontal')

        self.bottom_box.add_widget(self.txt)
        self.bottom_box.add_widget(self.clear_btn)

        self.All_box.add_widget(self.box1)
        self.All_box.add_widget(self.box)


        self.All_box.add_widget(self.bottom_box)


        self.page1 = BoxLayout(orientation='horizontal')



        self.page1.add_widget(self.All_box)

        #ikinci sayfa


        
        self.All_box2 = BoxLayout(orientation='vertical')
        self.box2 = BoxLayout(orientation='horizontal')

        self.Result2 = TextInput(hint_text='Result(Toplam patlayıcı miktarı) = kg')

        self.txt2 = TextInput(hint_text='pasa,cevher,şev,rampa')
        self.delik_sayısı2 = TextInput(hint_text='delik sayısı')
        self.btn2 = Button(text='Calculate', on_press=self.Calculate2)
        self.clear_btn2 = Button(text='Clear All', on_press=self.Clear2)

        self.patlayıcı_miktarı_m_başına_kg = TextInput(hint_text='patlayıcı miktarı kg/m')

        self.box12 = BoxLayout(orientation='horizontal')

        self.box2.add_widget(self.Result2)


        self.box12.add_widget(self.patlayıcı_miktarı_m_başına_kg)
        self.box12.add_widget(self.delik_sayısı2)

        self.ort_delik_boyu2 = TextInput(hint_text='ort delik boyu')


        self.sıkılama2 = TextInput(hint_text='sıkılama')

        self.delik_çapı2 = TextInput(hint_text='delik çapı(mm)')


        self.box12.add_widget(self.ort_delik_boyu2)


        self.box12.add_widget(self.sıkılama2)


        self.box12.add_widget(self.btn2)

        self.bottom_box2 = BoxLayout(orientation='horizontal')

        self.bottom_box2.add_widget(self.delik_çapı2)
        self.bottom_box2.add_widget(self.txt2)
        self.bottom_box2.add_widget(self.clear_btn2)


        self.All_box2.add_widget(self.box2)
        self.All_box2.add_widget(self.box12)




        self.All_box2.add_widget(self.bottom_box2)

        self.page2 = BoxLayout(orientation='horizontal')

        self.page2.add_widget(self.All_box2)


        
        #üçüncü sayfa

        self.All_box3 = BoxLayout(orientation='vertical')
        self.box3 = BoxLayout(orientation='horizontal')
        self.box13 = BoxLayout(orientation='horizontal')
        self.Result3 = TextInput(hint_text='Result(1m) = kg/m')

        self.txt3 = TextInput(hint_text='pasa,cevher,şev,rampa')

        self.btn3 = Button(text='Calculate', on_press=self.Calculate3)
        self.clear_btn3 = Button(text='Clear All', on_press=self.Clear3)

        self.box3.add_widget(self.Result3)






        self.yoğunluk = TextInput(hint_text='yoğunluk')

        self.delik_çapı = TextInput(hint_text='delik çapı')


        self.box13.add_widget(self.delik_çapı)
        self.box13.add_widget(self.yoğunluk)

        self.box13.add_widget(self.btn3)

        self.All_box3.add_widget(self.box3)
        self.All_box3.add_widget(self.box13)

        self.bottom_box3 = BoxLayout(orientation='horizontal')

        self.bottom_box3.add_widget(self.txt3)
        self.bottom_box3.add_widget(self.clear_btn3)

        self.All_box3.add_widget(self.bottom_box3)

        self.page3 = BoxLayout(orientation='horizontal')

        self.page3.add_widget(self.All_box3)

        #dördüncü sayfa

        self.All_box4 = BoxLayout(orientation='vertical')
        self.box4 = BoxLayout(orientation='horizontal')

        self.Result4 = TextInput(hint_text='Result(Toplam hacim) = m3')
        self.txt4 = TextInput(hint_text='pasa,cevher,şev,rampa')
        self.delik_sayısı4 = TextInput(hint_text='delik sayısı')
        self.btn4 = Button(text='Calculate', on_press=self.Calculate4)
        self.clear_btn4 = Button(text='Clear All', on_press=self.Clear4)

        self.sıralar_arası_txt4 = TextInput(hint_text='sıralar arası')
        self.delikler_arası_txt4 = TextInput(hint_text='delikler arası')

        self.ort_delik_boyu4 = TextInput(hint_text='ort delik boyu')


        self.box14 = BoxLayout(orientation='horizontal')



        self.box4.add_widget(self.sıralar_arası_txt4)
        self.box4.add_widget(self.delikler_arası_txt4)

        self.box4.add_widget(self.delik_sayısı4)

        self.box4.add_widget(self.ort_delik_boyu4)

        self.box14.add_widget(self.Result4)
        self.box14.add_widget(self.btn4)

        self.bottom_box4 = BoxLayout(orientation='horizontal')

        self.bottom_box4.add_widget(self.txt4)
        self.bottom_box4.add_widget(self.clear_btn4)

        self.All_box4.add_widget(self.box14)
        self.All_box4.add_widget(self.box4)

        self.All_box4.add_widget(self.bottom_box4)

        self.page4 = BoxLayout(orientation='horizontal')

        self.page4.add_widget(self.All_box4)

        # adding button on the screen
        # by add widget method

        # 1.sayfa
        self.add_widget(self.page1)


        # 2.sayfa
        self.add_widget(self.page2)

        # 3.sayfa
        self.add_widget(self.page3)

        # 4.sayfa
        self.add_widget(self.page4)


    def Clear(self, instance, *args):
        self.ort_delik_boyu.text =''
        self.Result.text =''
        self.txt.text =''
        self.delik_sayısı.text =''
        self.total_patlayıcı_miktarı.text =''
        self.delikler_arası_txt.text = ''
        self.sıralar_arası_txt.text = ''

    def Clear2(self, instance, *args):
        #kısımlar eklenecek
        self.delik_sayısı2.text=''
        self.ort_delik_boyu2.text=''
        self.sıkılama2.text=''
        self.txt2.text = ''
        self.Result2.text = ''
        self.patlayıcı_miktarı_m_başına_kg.text = ''
        self.delik_çapı2.text=''

    def Clear3(self, instance, *args):
        self.Result3.text = ''
        self.txt3.text = ''
        self.yoğunluk.text = ''
        self.delik_çapı.text = ''

    def Clear4(self, instance, *args):
        self.Result4.text = ''
        self.delikler_arası_txt4.text = ''
        self.sıralar_arası_txt4.text = ''
        self.ort_delik_boyu4.text = ''
        self.delik_sayısı4.text = ''

    def Calculate(self, instance, *args):


        check = ['p', 'c', 'ş', 'r']
        for i in range(4):
            if (self.txt.text.lower() == check[i]):
                self.txt.text = türler_kısayol[self.txt.text.lower()]

        if(self.delik_sayısı.text!='' and self.txt.text!='' and self.ort_delik_boyu.text!='' and self.total_patlayıcı_miktarı.text!=''):
            if(self.sıralar_arası_txt.text==''):
                self.sıralar_arası_txt.text = str(Sıralar_Arası[self.txt.text])
            if(self.delikler_arası_txt.text==''):
                self.delikler_arası_txt.text= str(Delikler_Arası[self.txt.text])
            self.Result.text = str(round((float(self.total_patlayıcı_miktarı.text))/(float(self.sıralar_arası_txt.text)*float(
                self.delikler_arası_txt.text)*int(self.delik_sayısı.text)*float(self.ort_delik_boyu.text)),3))

    def Calculate2(self, instance, *args):
        check = ['p', 'c', 'ş', 'r']
        for i in range(4):
            if (self.txt2.text.lower() == check[i]):
                self.txt2.text = türler_kısayol[self.txt2.text.lower()]

        if (self.delik_çapı2.text == ''):
            if (self.txt2.text == 'pasa'):
                self.delik_çapı2.text = '102'
            else:
                self.delik_çapı2.text = '89'
        if (self.delik_çapı2.text=='102' and self.patlayıcı_miktarı_m_başına_kg.text == ''):
            self.patlayıcı_miktarı_m_başına_kg.text = '6.5'
        if (self.delik_çapı2.text=='89' and self.patlayıcı_miktarı_m_başına_kg.text == ''):
            self.patlayıcı_miktarı_m_başına_kg.text = '5.21'

        if(self.delik_sayısı2.text!='' and self.txt2.text!='' and self.ort_delik_boyu2.text!=''):

            if (self.txt2.text == 'pasa'):
                if (self.sıkılama2.text == ''):
                    self.sıkılama2.text = str(float(self.ort_delik_boyu2.text) * 0.5)
                if (self.patlayıcı_miktarı_m_başına_kg.text==''):
                    self.patlayıcı_miktarı_m_başına_kg.text='6.5'
            if (self.txt2.text=='cevher'):
                if(self.sıkılama2.text==''):
                    self.sıkılama2.text = str(float(self.ort_delik_boyu2.text) * 0.6)
            if (self.patlayıcı_miktarı_m_başına_kg.text=='' and self.txt2.text!= 'pasa'):
                self.patlayıcı_miktarı_m_başına_kg.text='5.21'

            self.Result2.text = str(round(float(self.patlayıcı_miktarı_m_başına_kg.text) * int(self.delik_sayısı2.text) * (
                        float(self.ort_delik_boyu2.text) - float(self.sıkılama2.text)), 3))


    def Calculate3(self, instance, *args):
        check = ['p', 'c', 'ş', 'r']
        for i in range(4):
            if (self.txt3.text.lower() == check[i]):
                self.txt3.text = türler_kısayol[self.txt3.text.lower()]

        if(self.delik_çapı.text==''):
            if(self.txt3.text == 'pasa'):
                self.delik_çapı.text='102'
            else:
                self.delik_çapı.text = '89'

        if(self.yoğunluk.text==''):
            self.yoğunluk.text='850'


        self.Result3.text = str(round(pi*(((float(self.delik_çapı.text))/(2*1000))**2)*float(self.yoğunluk.text),3))

    def Calculate4(self, instance, *args):

        check = ['p', 'c', 'ş', 'r']
        for i in range(4):
            if (self.txt4.text.lower() == check[i]):
                self.txt4.text = türler_kısayol[self.txt4.text.lower()]

        if (self.delik_sayısı4.text != '' and self.txt4.text != '' and self.ort_delik_boyu4.text != ''):
            if (self.sıralar_arası_txt4.text == ''):
                self.sıralar_arası_txt4.text = str(Sıralar_Arası[self.txt4.text])
            if (self.delikler_arası_txt4.text == ''):
                self.delikler_arası_txt4.text = str(Delikler_Arası[self.txt4.text])
            self.Result4.text = str(round((float(self.sıralar_arası_txt4.text)*float(
                self.delikler_arası_txt4.text)*int(self.delik_sayısı4.text)*float(self.ort_delik_boyu4.text)),3))


class Calculate(App):

    def build(self):


        return PageLayout()




Calculate().run()

