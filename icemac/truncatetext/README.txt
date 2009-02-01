Nicely truncate text
====================

Intelligent truncation of text means that truncation does not take
place inside a word but only between words. So the required length is
only an approximation. The result text might be a bit longer than the
required length:

  >>> from icemac.truncatetext import truncate
  >>> 'I was here.'[:3]
  'I w'
  >>> truncate('I was here.', 3)
  'I was ...'

Only instances of basestring can be truncated:

  >>> truncate(3, 3)
  Traceback (most recent call last):
  ValueError: 3 is no instance of basestring or None
  >>> truncate(u'Lorem ipsum', 5)
  u'Lorem ...'

``None`` is handled nicely:

  >>> truncate(None, 4)
  ''

Always at least one word is returned even when it is longer than the
required length:

  >>> truncate('Lorem ipsum', 1)
  'Lorem ...'

If the text contains only of one word which is longer than the desired
length it is returned without an ellipsis:

  >>> truncate('The-really-long-word', 5)
  'The-really-long-word'

If the text is shorter than the desired length it is returned without
the ellipsis, too:

  >>> truncate('Lorem ipsum', 11)
  'Lorem ipsum'

Truncation also takes place at tabs and linebreaks:

  >>> truncate("I was here.\nNow I'm away", 11)
  'I was here. ...'
  >>> truncate("I was here.\rNow I'm away", 12)
  'I was here.\rNow ...'
  >>> truncate("I was here.\tNow I'm away", 11)
  'I was here. ...'
