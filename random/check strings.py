txt = "Lorem ipsum dolor sit amet"
print(("free" in txt))
print(("Lorem" in txt))


if "free" in txt:
  print("tem free")
if "Lorem" in txt:
  print("tem Lorem")
  print("Lorem" in txt)
  
if "free" not in txt:
  print("não tem free")
  print("free" not in txt) 
if "Lorem" not in txt:
  print("não tem Lorem")
  