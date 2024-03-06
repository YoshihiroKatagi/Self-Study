package ch18;

import org.junit.Before;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

@RunWith(Enclosed.class)
public class ItemStockTest {
    public static class InitialCase {
        ItemStock sut;
        Item book;

        @Before
        public void setUp() throws Exception {
            book = new Item("book", 3800);
            sut = new ItemStock();
        }

        @Test
        public void getNum_returns_0() {
            assertThat(sut.getNum(book), is(0));
        }

        @Test
        public void getNum_returns_1() throws Exception {
            sut.add(book);
            assertThat(sut.getNum(book), is(1));
        }
    }

    public static class book_is_added {
        ItemStock sut;
        Item book;

        @Before
        public void setUp() throws Exception {
            book = new Item("book", 3800);
            sut = new ItemStock();
            sut.add(book);
        }

        @Test
        public void getNum_returns_1() throws Exception {
            assertThat(sut.getNum(book), is(1));
        }

        @Test
        public void getNum_returns_2() throws Exception {
            sut.add(book);
            assertThat(sut.getNum(book), is(2));
        }

        @Test
        public void getNum_return_1_with_book_and_bike() throws Exception {
            Item bike = new Item("bike", 57000);
            sut.add(bike);
            assertThat(sut.getNum(book), is(1));
            assertThat(sut.getNum(bike), is(1));

        }
    }
}
