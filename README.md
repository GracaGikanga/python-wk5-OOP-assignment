# 🐍 Python OOP Activities

This project showcases basic Object-Oriented Programming (OOP) concepts in Python through two simple activities: **Inheritance** and **Polymorphism**.

---

## 📘 Activity 1: Inheritance

This activity demonstrates how a subclass can inherit properties from a parent class.

### Classes:
- `student`: A base class with attributes `name` and `age`.
- `marks`: A subclass of `student` that inherits all attributes and methods without adding new ones.

### Example:
```python
student1 = student("Alice", 20)
print(student1.name, student1.age)  # Output: Alice 20