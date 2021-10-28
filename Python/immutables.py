#!/usr/bin/python
mutable_non_empty_attributes = ["primaryEmail", "username"]
immutable_non_empty_attributes = ("primaryEmail", "username")
immutable_non_empty_attributes2 = ('password')
mutable_empty_attributes = []
immutable_empty_attributes = ()

for i in mutable_non_empty_attributes:
  if i is None:
    print("Found empty attribute: {}".format(i))

for i in immutable_non_empty_attributes:
  if i is None:
    print("Found empty attribute: {}".format(i))

for i in mutable_empty_attributes:
  if i is None:
    print("Found empty attribute: {}".format(i))

for i in immutable_empty_attributes:
  if i is None:
    print("Found empty attribute: {}".format(i))

if mutable_non_empty_attributes is None:
    print("Found empty attribute: {}".format(mutable_non_empty_attributes))

if immutable_non_empty_attributes is None:
    print("Found empty attribute: {}".format(immutable_non_empty_attributes))

if mutable_empty_attributes is None:
    print("Found empty attribute: {}".format(mutable_empty_attributes))

if immutable_empty_attributes is None:
    print("Found empty attribute: {}".format(immutable_empty_attributes))

print("mutable_non_empty_attributes: {}".format(mutable_non_empty_attributes))
print("immutable_non_empty_attributes: {}".format(immutable_non_empty_attributes))
print("mutable_empty_attributes: {}".format(mutable_empty_attributes))
print("immutable_empty_attributes: {}".format(immutable_empty_attributes))
print("mutable_non_empty_to_immutable: {}".format(tuple(mutable_non_empty_attributes)))
print("immutable_non_empty_to_mutable: {}".format(list(immutable_non_empty_attributes)))
print("immutable_non_empty_to_mutable2: {}".format(immutable_non_empty_attributes2))

