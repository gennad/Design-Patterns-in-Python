Holder: object O has subobject S as an
attribute (may be a property), that's all

self.S.method or O.S.method


Wrapper: holder (often via a private
attribute) plus delegation (use O.method)
• explicit: def method(self,*a,**k):
return self._S.method(*a,**k)
• automatic (typically via __getattr__)...:
def __getattr__(self, name):
return getattr(self._S, name)

