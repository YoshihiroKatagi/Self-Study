package junit.example.ch07;

public class Book {

    String title;
    int price;
    Author author;

    public String getTitle() { return title; }

    public void setTitle(String title) { this.title = title; }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public Author getAuthor() {
        return author;
    }

    public void setAuthor(Author author) {
        this.author = author;
    }
}
