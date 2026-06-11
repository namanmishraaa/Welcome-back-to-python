# 03-oop_basics — Object-Oriented Programming

Master OOP fundamentals: designing classes, inheritance, polymorphism, and writing maintainable code.

## 📚 Topics Covered

### 1. Class Fundamentals
- **Classes and objects** — Blueprints and instances
- **`__init__` method** — Constructor, initializing attributes
- **Instance variables** — Data specific to each object
- **Instance methods** — Functions that operate on instances
- **`self` parameter** — Reference to the instance
- **`__str__` and `__repr__`** — String representations

### 2. Attributes and Methods
- **Class variables** — Shared across all instances
- **Instance variables** — Specific to each instance
- **Instance methods** — Operating on instance data
- **Class methods** — `@classmethod`, alternative constructors
- **Static methods** — `@staticmethod`, utility functions
- **`@property`** — Controlled attribute access with getters/setters

### 3. Encapsulation
- **Public attributes** — No prefix
- **Protected attributes** — `_attribute`, convention only
- **Private attributes** — `__attribute`, name mangling
- **Properties** — Pythonic getter/setter pattern
- **Validation in `__init__`** — Ensuring valid object state

### 4. Inheritance
- **Parent and child classes** — Code reuse through hierarchy
- **`super()`** — Calling parent methods correctly
- **Method Resolution Order (MRO)** — `__mro__`, C3 linearization
- **Multiple inheritance** — Inheriting from multiple parents
- **`isinstance()` and `issubclass()`** — Type checking

### 5. Polymorphism
- **Duck typing** — "If it quacks like a duck..."
- **Method overriding** — Different behaviour in subclasses
- **Operator overloading** — `__add__`, `__lt__`, `__eq__`, etc.
- **Abstract base classes** — `abc.ABC`, `@abstractmethod`

### 6. Magic Methods (Dunder Methods)
- **`__init__`** — Constructor
- **`__str__` vs `__repr__`** — Display representations
- **`__eq__`, `__lt__`, `__le__`** — Comparison operators
- **`__add__`, `__sub__`** — Arithmetic operators
- **`__getitem__`, `__setitem__`, `__len__`** — Container behaviour
- **`__call__`** — Making objects callable
- **`__enter__`, `__exit__`** — Context managers

### 7. Design Principles
- **SOLID principles** — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **Composition over inheritance** — When to favour each
- **Common design patterns** — Singleton, Factory, Observer
- **Mixins** — Adding functionality via multiple inheritance

## 💡 Learning Objectives

By the end of this section, you should be able to:
- ✅ Design and implement well-structured classes
- ✅ Use inheritance and `super()` correctly
- ✅ Implement polymorphism and duck typing
- ✅ Use magic methods for Pythonic interfaces
- ✅ Apply encapsulation with `@property`
- ✅ Understand and apply SOLID principles
- ✅ Choose between composition and inheritance

## 📝 Files in This Section

1. **class_basics.py** — Classes, `__init__`, instance variables/methods, `__str__`/`__repr__`
2. **attributes_and_methods.py** — Class/instance attributes, `@classmethod`, `@staticmethod`, `@property`
3. **encapsulation.py** — Public/protected/private, property validation
4. **inheritance.py** — Parent/child classes, `super()`, MRO, multiple inheritance
5. **polymorphism.py** — Duck typing, method overriding, abstract classes
6. **magic_methods.py** — Dunder methods, operator overloading
7. **design_patterns.py** — Singleton, Factory, Observer patterns
8. **solid_principles.py** — SOLID principles in practice
9. **exercises.py** — Practice problems on OOP

## 🎯 Interview Tips

**Common Questions:**
- What's the difference between `__str__` and `__repr__`?
- Explain MRO and the C3 linearisation algorithm
- What's the difference between class and instance variables?
- When would you use composition over inheritance?
- Explain the SOLID principles with examples
- How does Python implement abstract classes?
- How does name mangling work with `__private`?

**Key Points to Master:**
- `self` is explicit in Python — understand why
- `@classmethod` vs `@staticmethod` vs instance method differences
- How `super()` works in multiple inheritance
- Duck typing is more idiomatic than `isinstance()` checks
- `@property` is the Pythonic way to do getters/setters
- Understand MRO to debug multiple-inheritance issues

## 🚀 Next Steps

After mastering OOP:
1. Build the intermediate projects applying OOP
2. Move to `03-advanced/` for decorators (which use OOP concepts heavily)
3. Study design patterns in depth

---

**Difficulty: ⭐⭐⭐ Critical for professional Python development**
