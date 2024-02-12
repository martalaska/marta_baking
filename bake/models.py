from django.db import models
#from django.contrib.postgres.fields import ArrayField


class Ingredients(models.Model):
    title = models.CharField(max_length = 100, default = "Ingredients", primary_key = True)
    #for i in range(20):
    for i in range(40):
        exec(f"{"pair_"+str(i)} = models.CharField(max_length = 100, default = '', blank = True)")
    # image = models.URLField(blank = True)
    # strawberry = models.FloatField()
    # apricot = models.FloatField()
    # cointerau = models.FloatField()
    # almond = models.FloatField()
    # milk_chocolate = models.FloatField()
    # vanilla = models.FloatField()
    # grapefruit = models.FloatField()
    matches = models.CharField(max_length = 2000, default = "")
    #m = ArrayField(models.CharField(max_length = 100), default = make_list())

#print(list(Ingredients.objects.values_list("title", flat = True)))
add_to_model = {}
for j in Ingredients.objects.all():
    for q in range(40):
        pair = getattr(j, "pair_"+str(q)) 
        all_titles = list(Ingredients.objects.values_list("title", flat = True))
        if pair not in all_titles:
            if pair not in add_to_model:
                add_to_model[pair] = [getattr(j, "title")]
            else:
                add_to_model[pair].append(getattr(j, "title"))

for ing in add_to_model:
    Ingredients.objects.create(title = ing)
    attribute_list = add_to_model[ing]
    
    for s in range(len(attribute_list)):
        exec("Ingredients.objects.filter(title = ing).update("+f"{'pair_'+str(s)} = attribute_list["+str(s)+"])")

#         print(attribute_list[s])
#         setattr(Ingredients.objects.filter(title = "Rhubarb"), "pair_"+str(s), attribute_list[s])
#         #print(getattr(o, "pair_"+str(s)))
#         print(Ingredients.objects.filter(title = ing)[0])
#         print(getattr(Ingredients.objects.filter(title = ing)[0], "pair_0"))
# Ingredients.objects.filter(title = "Rhubarb").__setattr__("pair_0", "Vanilla")
# print(getattr(Ingredients.objects.filter(title = "Rhubarb")[0], "pair_0"))
  
#print(getattr(Ingredients.objects.filter(title = "Rhubarb")[0], "pair_0"))

    #if search in getattr(i, "matches"):
    #    pairing.append(getattr())


class Ingredients_Recipe(models.Model):
    title = models.CharField(max_length = 100, primary_key = True)
    water = models.FloatField(default = 0)
    fat = models.FloatField(default = 0)
    sugar = models.FloatField(default = 0)
    dry = models.FloatField(default = 0)


# class Node:
#     def __init__(self, name1, name2):
#         self.name1 = name1
#         self.name2 = name2
#         self.next = None


# class LinkedList():
#     def __init__(self):
#         self.head = Node("", "")
#         self.current = Node("", "")
#         self.head = self.current
#         self.current.next = None

#     def addNode(self, name1, name2):
#         self.current.name1 = name1
#         self.current.name2 = name2
#         newNode = Node("", "")
#         self.current.next = newNode
#         self.current = newNode


# class Ingredients_LinkedLists():
#     def __init__(self):
#         self.model = {}

#     def add_Pair(self, name, pair):
#         if name not in self.model:
#             self.model[name] = LinkedList()
#         self.model[name].addNode(name, pair)
#         if pair not in self.model:
#             self.model[pair] = LinkedList()
#         self.model[pair].head = self.model[name].current
#         self.model[pair].head.next = Node("", "")

#     def add_List(self, name, pairs_list):
#         if name not in self.model:
#             self.model[name] = LinkedList()
#         for p in pairs_list:
#             self.add_Pair(name, p)
        

# data = Ingredients_LinkedLists()

# data.add_List("Grapefruit", ["Vanilla", "Cointerau", "Pistachio"])

# Create your models here.
