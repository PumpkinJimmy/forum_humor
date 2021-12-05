```
qs = session.select(Model, cond)
obj = qs.one()
objs = qs.all()
session.insert(obj)
session.update(obj)
session.delete(obj)
session.raw(SQL)
```