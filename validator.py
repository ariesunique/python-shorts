import string

def is_valid(doc):
  # doc should not be empty
  if doc == None or doc.strip() == "":
    return False

  doc = doc.replace("\n", "")

  # doc should start with an open tag
  if not doc.startswith("<"):
    return False

  LT = "<"
  GT = ">"
  BACKSLASH = "\\"
  FORWARDSLASH = "/"
  
  # this will maintain the found tags
  stk = []

  # this is the tag currently being processed
  curr_tag = []

  # indicates if the current char is part of a tag
  inside_tag = False
  
  # iterate over each char in the doc, building the tags along the way;
  #    store each tag that is found in a stack;
  #    when we find an ending tag, pop the stack;
  #    compare the end tag with the popped tag, if not the same, doc is not valid
  for i, ch in enumerate(doc):

    # the FORWARDSLASH is processed along with the char that came in front of it, so we can skip this
    if ch == FORWARDSLASH:
      continue

    # if the prev char was a backslash, then we ignore the current char
    if doc[i-1] == BACKSLASH:
      continue 

    # if we find a "less than" char and we are not yet inside a tag, 
    #   then this is the beginning of a tag; store the char and set the inside_tag flag 
    #   check to see if the next char is a forward slash so we know if this is an end tag
    if ch == LT and not inside_tag:
      curr_tag.append(ch)
      inside_tag = True
      if i+1 < len(doc) and doc[i+1] == FORWARDSLASH:
        curr_tag.append(FORWARDSLASH)

    # else if we find a "greater than" char and the inside_tag flag was previously set, 
    #    then this must be the end of the tag; 
    #    turn off the inside_tag flag and reset the list storing the chars for this tag
    elif ch == GT and inside_tag:
      curr_tag.append(ch)
      inside_tag = False
      tag = "".join(curr_tag)
      curr_tag = []

      # if this is a closing tag, pop stack and compare the current tag with the popped tag
      #    if they are not the same, the doc is not valid
      if tag.startswith("</"):
        # we hit an ending tag, but there was nothing on the stack yet => not valid; return False
        if not stk:
          return False

        prevtag = stk.pop().strip(GT).strip(LT).strip(FORWARDSLASH).strip()
        tag = tag.strip(GT).strip(LT).strip(FORWARDSLASH).strip()
        if not tag or prevtag != tag:
          return False
      # if this was not a closing tag (ie just another opening tag) append it to the stack
      else:  
        stk.append(tag)

    # else if the inside_tag flag is set, then this char is part of the tag;
    #    since we have already processed the special chars (LT, GT, FORWARDSLASH, BACKSLASH), 
    #    the only other chars in the tag should be ascii chars or underscore; return False if otherwise
    elif inside_tag:
      if ch not in string.ascii_lowercase and ch != "_":
        return False
      curr_tag.append(ch)

  # at this point we have processed all the chars in the doc
  # if the doc is well-formed (aka valid) the stack should be empty and the start_tag flag 
  #    should be False
  if stk or inside_tag:
    return False

  # if all else checks out, the doc is valid
  return True
