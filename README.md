M101P
=====

All my learning material for online class "M101P: MongoDB for Developers" (Sep-Oct)

## Indexes
```javascript
db.students.ensureIndex({class:1, students_id:1});
db.system.indexes.find();   // All existst index in database
db.students.dropIndex({'student_id':1});
db.students.getIndexes();
```

## Multikey
- We can't have more than one multikey index in single collection

```javascript
db.bbb.insert({a:1, b:1})
db.bbb.ensureIndex({a:1, b:1})
db.bbb.insert({a:5, b:[1,2,3]})
db.bbb.insert({a:[1,2,4], b:[1,2,3]})
```
