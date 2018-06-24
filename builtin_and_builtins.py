# -*- coding:utf-8 -*-
# !/usr/bin/env python

import __builtin__

print 'Module name:', __name__

print '*==test __builtin__ and __builtins__==*'
print '__builtin__ == __builtins__', __builtin__ == __builtins__
print '__builtin__ is __builtins__', __builtin__ is __builtins__
print 'id(__builtin__)', id(__builtin__)
print 'id(__builtins__)', id(__builtins__)

print '=' * 50

print '*==test __builtin__.__dict__ and __builtins__==*'
print '__builtin__.__dict__ == __builtins__', __builtin__.__dict__ == __builtins__
print '__builtin__ is __builtins__', __builtin__.__dict__ is __builtins__
print 'id(__builtin__)', id(__builtin__.__dict__)
print 'id(__builtins__)', id(__builtins__)