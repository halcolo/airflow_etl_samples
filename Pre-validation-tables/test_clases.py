class P:

     def p1(self):
         print('Start')

     def p2(self):
         print('Help')

     def ps(self):
         print('Settings')

     def d(self):
         print('Default function')

     myDict = {
         "start": p1,
         "help": p2,
         "settings": ps
     }

     def call_it(self, name):
         f = lambda self, x : self.myDict.get(x, lambda x : self.d())(self)
         f(self, name)


p = P()
p.call_it('starts')