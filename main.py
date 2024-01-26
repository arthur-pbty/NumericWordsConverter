nombre = input("Entrez un nombre : ")

res = ""

if nombre == "0":
   res = "zéro"

def lettre(n):
   res = ""
   
   if len(n) == 3:
      if n[0] == "1":
         res = "cent "
      elif n[0] == "2":
         res = "deux cent "
      elif n[0] == "3":
         res = "trois cent "
      elif n[0] == "4":
         res = "quatre cent "
      elif n[0] == "5":
         res = "cinq cent "
      elif n[0] == "6":
         res = "six cent "
      elif n[0] == "7":
         res = "sept cent "
      elif n[0] == "8":
         res = "huit cent "
      elif n[0] == "9":
         res = "neuf cent "
   
   if len(n) >= 2:
      if n[-2] == "1":
         if n[-1] == "0":
            res += "dix "
         elif n[-1] == "1":
            res += "onze "
         elif n[-1] == "2":
            res += "douze "
         elif n[-1] == "3":
            res += "treize "
         elif n[-1] == "4":
            res += "quatorze "
         elif n[-1] == "5":
            res += "quinze "
         elif n[-1] == "6":
            res += "seize "
         elif n[-1] == "7":
            res += "dix-sept "
         elif n[-1] == "8":
            res += "dix-huit "
         elif n[-1] == "9":
            res += "dix-neuf "
      elif n[-2] == "2":
         res += "vingt "
      elif n[-2] == "3":
         res += "trente "
      elif n[-2] == "4":
         res += "quarante "
      elif n[-2] == "5":
         res += "cinquante "
      elif n[-2] == "6":
         res += "soixante "
      elif n[-2] == "7":
         res += "soixante-dix "
      elif n[-2] == "8":
         res += "quatre-vingt "
      elif n[-2] == "9":
         res += "quatre-vingt-dix "

   if len(n) >= 1:
      if n[-1] != 0:
         if len(n) >= 2:
            if n[-2] == "2" or n[-2] == "3" or n[-2] == "4" or n[-2] == "5" or n[-2] == "6":
               if n[-1] == "1":
                  res += "et un "
               elif n[-1] == "2":
                  res += "deux "
               elif n[-1] == "3":
                  res += "trois "
               elif n[-1] == "4":
                  res += "quatre "
               elif n[-1] == "5":
                  res += "cinq "
               elif n[-1] == "6":
                  res += "six "
               elif n[-1] == "7":
                  res += "sept "
               elif n[-1] == "8":
                  res += "huit "
               elif n[-1] == "9":
                  res += "neuf "

            elif n[-2] == "7" or n[-2] == "9":
               if n[-1] == "1":
                  res += "onze "
               if n[-1] == "2":
                  res += "douze "
               if n[-1] == "3":
                  res += "treize "
               if n[-1] == "4":
                  res += "quatorze "
               if n[-1] == "5":
                  res += "quinze "
               if n[-1] == "6":
                  res += "seize "
               if n[-1] == "7":
                  res += "dix-sept "
               if n[-1] == "8":
                  res += "dix-huit "
               if n[-1] == "9":
                  res += "dix-neuf "
            
            elif n[-2] == "8":
               if n[-1] == "1":
                  res += "un "
               elif n[-1] == "2":
                  res += "deux "
               elif n[-1] == "3":
                  res += "trois "
               elif n[-1] == "4":
                  res += "quatre "
               elif n[-1] == "5":
                  res += "cinq "
               elif n[-1] == "6":
                  res += "six "
               elif n[-1] == "7":
                  res += "sept "
               elif n[-1] == "8":
                  res += "huit "
               elif n[-1] == "9":
                  res += "neuf "
            
            else:
               if n[-1] == "1":
                  res += "un "
               elif n[-1] == "2":
                  res += "deux "
               elif n[-1] == "3":
                  res += "trois "
               elif n[-1] == "4":
                  res += "quatre "
               elif n[-1] == "5":
                  res += "cinq "
               elif n[-1] == "6":
                  res += "six "
               elif n[-1] == "7":
                  res += "sept "
               elif n[-1] == "8":
                  res += "huit "
               elif n[-1] == "9":
                  res += "neuf "

         else:
            if n[-1] == "1":
               res += "un "
            elif n[-1] == "2":
               res += "deux "
            elif n[-1] == "3":
               res += "trois "
            elif n[-1] == "4":
               res += "quatre "
            elif n[-1] == "5":
               res += "cinq "
            elif n[-1] == "6":
               res += "six "
            elif n[-1] == "7":
               res += "sept "
            elif n[-1] == "8":
               res += "huit "
            elif n[-1] == "9":
               res += "neuf "

   return res


listNombre = []
while nombre != "":
   listNombre.append(nombre[-3:])
   nombre = nombre[:-3]

select = 0
for part in listNombre:
   select += 1
   if select == 2:
      res = lettre(part) + "mille "  + res
   elif select == 3:
      res = lettre(part) + "million " + res
   elif select == 4:
      res = lettre(part) + "milliard " + res
   elif select == 5:
      res = lettre(part) + "billion " + res
   elif select == 6:
      res = lettre(part) + "billiard " + res
   elif select == 7:
      res = lettre(part) + "trillion " + res
   elif select == 8:
      res = lettre(part) + "trilliard " + res
   elif select == 9:
      res = lettre(part) + "quadrillion " + res
   elif select == 10:
      res = lettre(part) + "quadrilliard " + res
   elif select == 11:
      res = lettre(part) + "quintillion " + res
   elif select == 12:
      res = lettre(part) + "quintilliard " + res
   elif select == 13:
      res = lettre(part) + "sextillion " + res
   elif select == 14:
      res = lettre(part) + "sextilliard " + res
   elif select == 15:
      res = lettre(part) + "septillion " + res
   elif select == 16:
      res = lettre(part) + "septilliard " + res
   elif select == 17:
      res = lettre(part) + "octillion " + res
   elif select == 18:
      res = lettre(part) + "octilliard " + res
   elif select == 19:
      res = lettre(part) + "nonillion " + res
   elif select == 20:
      res = lettre(part) + "nonilliard " + res
   elif select == 21:
      res = lettre(part) + "décillion " + res
   elif select == 22:
      res = lettre(part) + "décilliard " + res
   elif select == 23:
      res = lettre(part) + "undécillion " + res
   elif select == 24:
      res = lettre(part) + "undécilliard " + res
   elif select == 25:
      res = lettre(part) + "duodécillion " + res
   elif select == 26:
      res = lettre(part) + "duodécilliard " + res
   elif select == 27:
      res = lettre(part) + "tridécillion " + res
   elif select == 28:
      res = lettre(part) + "tridécilliard " + res
   elif select == 29:
      res = lettre(part) + "quattuordécillion " + res
   elif select == 30:
      res = lettre(part) + "quattuordécilliard " + res
   
   else:
      res = lettre(part) + res

print(res)
