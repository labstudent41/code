// Abstract class
abstract class Shape {
    // Abstract method (no implementation)
    abstract double calculateArea();

    // Concrete method
    void display() {
        System.out.println("This is a shape.");
    }
}

// Concrete subclass 1
class Circle extends Shape {
    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    // Implementing the abstract method
    @Override
    double calculateArea() {
        return Math.PI * radius * radius;
    }

    @Override
    void display() {
        System.out.println("This is a circle with radius " + radius);
    }
}

// Concrete subclass 2
class Rectangle extends Shape {
    double length;
    double width;

    Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    // Implementing the abstract method
    @Override
    double calculateArea() {
        return length * width;
    }

    @Override
    void display() {
        System.out.println("This is a rectangle with length " + length + " and width " + width);
    }
}

public class Abstract {
    public static void main(String[] args) {
        // Create instances of Circle and Rectangle
        Circle circle = new Circle(5.0);
        Rectangle rectangle = new Rectangle(4.0, 6.0);

        // Call abstract method and concrete method on objects
        System.out.println("Circle Area: " + circle.calculateArea());
        circle.display();

        System.out.println("Rectangle Area: " + rectangle.calculateArea());
        rectangle.display();
    }
}
