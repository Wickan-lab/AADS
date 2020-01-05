from treenode import TreeNode

#TEST 1
dile = TreeNode("Dile")
edo = TreeNode("Edo")
raffo = TreeNode("Raffo", [dile, edo])
cami = TreeNode("Cami")
stella = TreeNode("Stella", [TreeNode("Jess")])
gabry = TreeNode("Gabry", [TreeNode("Saba"), TreeNode("Luca"), stella])
ale = TreeNode("Ale", [TreeNode("Dave"), gabry, TreeNode("Greg")])
enzo = TreeNode("Enzo", [TreeNode("Diodato")])
fra = TreeNode("Fra", [enzo])
fede = TreeNode("Fede", [ale, fra])

cami.add_child(raffo)
cami.add_child(fede)
peppe = TreeNode("Peppe", [TreeNode("Marco"), TreeNode("Gio"), TreeNode("Marghe")])
cami.add_child(peppe)
print(cami)
print("\n")

print(cami.give_software())

#TEST 2
tredici = TreeNode("13", [TreeNode("16"), TreeNode("17")])
otto = TreeNode("8", [TreeNode("12"), tredici, TreeNode("14")])
quattro = TreeNode("4", [TreeNode("9"), TreeNode("10")])
sette = TreeNode("7", [TreeNode("11", [TreeNode("15")])])
tre = TreeNode("3")
tre.add_child(sette)
tre.add_child(otto)
due = TreeNode("2", [TreeNode("5"), TreeNode("6")])

uno = TreeNode("1", [due, tre, quattro])
print(uno)
print(uno.give_software())

#TEST 3
a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c", [TreeNode("d", [TreeNode("e", [TreeNode("f", [TreeNode("g")]), TreeNode("h", [TreeNode("i"), TreeNode("l")])])])])

b.add_child(c)
a.add_child(b)
print(a)
print(a.give_software())
