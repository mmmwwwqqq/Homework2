def Artek(s, n):
    Astud=[]
    s = s.split(',')
    for i in range (len(s)):
         if '5' in s[i]:
              Astud.append(s[i])
    Astud.sort()
    for i in range(n):
         print(Astud[i].split()[0])

Artek('Сидоров 3, Смирнова 5, Самойкин 4, Емельянов 2, Кац 5, Вдовиченко 5, Северин 4, Субботкин 5', 3)
