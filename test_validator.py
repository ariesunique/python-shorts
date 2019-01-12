from validator import is_valid


def test_null_or_empty_input():
  assert is_valid("") == False
  assert is_valid(None) == False
  assert is_valid("     ") == False


def test_no_tags():
  assert is_valid("not valid") == False
  assert is_valid("This <is> not </is> valid") == False


def test_tag_is_invalid():
  assert is_valid("<nor is this></nor is this>") == False

  assert is_valid("<<p>bad tag</p>") == False

  assert is_valid("<p*>no specials chars</p*>") == False

  assert is_valid("<>empty tag</>") == False

  assert is_valid("<  >another empty tag</  >") == False

  assert is_valid("<p>this ends with a slash</") == False

  assert is_valid("<") == False

  assert is_valid("</") == False

  assert is_valid("/") == False

  assert is_valid("</closing_tag>") == False


def test_single_tag():
  assert is_valid("<tag>this is valid</tag>") == True


def test_tag_with_underscore():
  assert is_valid("<tag_with_underscore></tag_with_underscore>") == True


def test_several_tags():
  str3 = "<table><tr><td>item</td></tr></table>"
  assert is_valid(str3) == True


def test_bad_nesting():
  str4 = "<head><title>this is bad</head></title>"
  assert is_valid(str4) == False


def test_special_chars():
  str5 = "<p>4 \< 5</p>"
  assert is_valid(str5) == True

  str6 = "<p>1\<2</p>"
  assert is_valid(str6) == True

  str7 = "<p>\<not a tag\></p>"
  assert is_valid(str7) == True

  str8 = "<p>\\\<\></p>"
  assert is_valid(str8) == True

  str9 = "<p><not a tag></p>"
  assert is_valid(str9) == False


def test_full_doc():
  str7 = """
<html>
  <head><title>Here's the title</title></head>
  <body>
    <p>Here's some stuff in the body</p>
  </body>
</html>
"""
  assert is_valid(str7) == True
