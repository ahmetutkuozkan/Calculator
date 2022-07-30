from kivy.app import App

from kivy.uix.button import  Button

from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

from math import pi



türler ={
"pasa" : 7.25,
"cevher" : 8.96,
"şev" : 3.6,
"rampa" : 5.25}
türler_kısayol = {
    "p" : "pasa",
    "c" : "cevher",
    "ş" : "şev",
    "r" : "rampa"
}

patlayıcı_miktarı_delik_89mm = 5.21
patlayıcı_miktarı_delik_102mm = 6.5

class Calculate(App):

    def build(self):

        self.All_box = BoxLayout(orientation='vertical')
        self.box = BoxLayout(orientation='horizontal')

        self.Result = TextInput(hint_text='Result = kg/m3,kg,kg/m')
        self.txt1 = TextInput(hint_text='PF,TOTAL,1M')
        self.txt = TextInput(hint_text='pasa,cevher,şev,rampa')
        self.delik_sayısı = TextInput(hint_text='delik sayısı')
        self.btn = Button(text='Calculate', on_press=self.Calculate)
        self.clear_btn = Button(text='Clear All', on_press=self.Clear)



        self.box.add_widget(self.Result)



        self.box.add_widget(self.txt1)
        self.box.add_widget(self.txt)
        self.box.add_widget(self.delik_sayısı)


        self.ort_delik_boyu = TextInput(hint_text='ort delik boyu')
        self.total_patlayıcı_miktarı = TextInput(hint_text='total patlayıcı miktarı')
        self.sıkılama = TextInput(hint_text='sıkılama')
        self.yoğunluk = TextInput(hint_text='yoğunluk')
        self.box1 = BoxLayout(orientation='horizontal')

        self.box1.add_widget(self.ort_delik_boyu)
        self.box1.add_widget(self.total_patlayıcı_miktarı)
        self.box1.add_widget(self.sıkılama)
        self.box1.add_widget(self.yoğunluk)
        self.box1.add_widget(self.btn)


        self.All_box.add_widget(self.box)
        self.All_box.add_widget(self.box1)
        self.All_box.add_widget(self.clear_btn)


        return self.All_box

    def Clear(self, instance, *args):
        self.ort_delik_boyu.text =''
        self.Result.text =''
        self.txt1.text =''
        self.txt.text =''
        self.sıkılama.text =''
        self.delik_sayısı.text =''
        self.total_patlayıcı_miktarı.text =''
        self.yoğunluk.text =''

    def Calculate(self, instance, *args):

        self.txt1.text = self.txt1.text.upper()
        check = ['p', 'c', 'ş', 'r']
        for i in range(4):
            if (self.txt.text.lower() == check[i]):
                self.txt.text = türler_kısayol[self.txt.text.lower()]

        if(self.txt1.text=='PF' or self.txt1.text=='P'):
            self.txt1.text = 'PF'
            if(self.delik_sayısı.text=='' or self.txt.text=='' or self.ort_delik_boyu.text==''):
                instance.Result
            else:
                if(self.total_patlayıcı_miktarı.text==''):
                    self.total_patlayıcı_miktarı.text='850'
                self.Result.text = str(round((float(self.total_patlayıcı_miktarı.text))/(float(türler[self.txt.text])*int(self.delik_sayısı.text)*float(self.ort_delik_boyu.text)),3))

        elif(self.txt1.text=='T' or self.txt1.text=='TOTAL'):
            self.txt1.text = 'TOTAL'
            if(self.txt.text=='pasa'):
                if(self.sıkılama.text==''):
                    self.sıkılama.text = str(float(self.ort_delik_boyu.text)*0.5)
                self.Result.text = str(round(patlayıcı_miktarı_delik_102mm*int(self.delik_sayısı.text)*(float(self.ort_delik_boyu.text)-float(self.sıkılama.text)),3))
            else:
                if (self.sıkılama.text == ''):
                    self.sıkılama.text = str(3)
                self.Result.text = str(round(patlayıcı_miktarı_delik_89mm*int(self.delik_sayısı.text)*(float(self.ort_delik_boyu.text)-float(self.sıkılama.text)),3))

        elif(self.txt1.text=='1M' or self.txt1.text=='1'):
            self.txt1.text = '1M'
            if(self.yoğunluk.text==''):
                self.yoğunluk.text='850'
            if (self.txt.text == 'pasa'):
                self.Result.text = str(round(pi*(((102)/(2*1000))**2)*float(self.yoğunluk.text),3))
            else:
                self.Result.text = str(round(pi*(((89)/(2*1000))**2)*float(self.yoğunluk.text),3))


#PF,cevher,81,4.4,700




Calculate().run()

