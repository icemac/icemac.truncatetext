Truncate text
=============

Intelligent truncation of text means that truncation does not take
place inside a word but only between words. So the given length is
only an approximation. The result text might be a bit longer than the
given length value:

  >>> from icemac.truncatetext import truncate
  >>> 'I was here.'[:4]
  'I wa'
  >>> truncate('I was here.', 4)
  'I was ...'

Only instances of basestring can be truncated:

  >>> truncate(3, 3)
  Traceback (most recent call last):
  ValueError: 3 is no instance of basestring or None
  >>> truncate(u'Lorem ipsum', 5)
  u'Lorem ...'

``None`` a parameter is handled nicely:

  >>> truncate(None, 4)
  ''

Always at least one word is returned:

  >>> truncate('Lorem ipsum', 1)
  'Lorem ...'

If the text is shorter than the ``length``parameter it is returned
without the ellipsis:

  >>> truncate('Lorem ipsum', 11)
  'Lorem ipsum'

If the text contains only of one word which is longer the the wished
lenght it is returned but without the ellipsis:

  >>> truncate('The-really-long-word', 5)
  'The-really-long-word'

Truncation also takes place at tabs, linebreaks:

  >>> truncate("I was here.\nNow I'm away", 11)
  'I was here. ...'
  >>> truncate("I was here.\rNow I'm away", 12)
  'I was here.\rNow ...'
  >>> truncate("I was here.\tNow I'm away", 11)
  'I was here. ...'
