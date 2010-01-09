# -*- coding: utf-8 -*-
# Copyright (c) 2009-2010 Michael Howitz
# See also LICENSE.txt
# $Id$

def truncate(text, length, ellipsis='...'):
    if text is None:
        text = ''
    if not isinstance(text, basestring):
        raise ValueError("%r is no instance of basestring or None" % text)

    # thread other whitespaces as word break
    content = text.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
    # make sure to have at least one space for finding spaces later on
    content += ' '

    if len(content) > length:
        # find the next space after max_len chars (do not break inside a word)
        pos = length + content[length:].find(' ')
        if pos != (len(content) - 1):
            # if the found whitespace is not the last one add an ellipsis
            text = text[:pos].strip() + ' ' + ellipsis

    return text
