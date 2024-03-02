package junit.example.ch07;

import org.junit.Test;

import static junit.example.ch07.BookStoreTestHelper.CreateBookObject_MartinFowlerIsRefactoring;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class BookStoreTest {

    @Test
    public void getTotalPrice() throws Exception {
        // SetUp
        BookStore sut = new BookStore();
        Book book = CreateBookObject_MartinFowlerIsRefactoring();
        sut.addToCart(book, 1);
        // Exercise & Verify
        assertThat(sut.getTotalPrice(), is(4500));
    }

    @Test
    public void get_0() throws Exception {
        // SetUp
        BookStore sut = new BookStore();
        Book book = CreateBookObject_MartinFowlerIsRefactoring();
        sut.addToCart(book, 1);
        // Exercise & Verify
        assertThat(sut.get(0), is(sameInstance(book)));
    }
}
