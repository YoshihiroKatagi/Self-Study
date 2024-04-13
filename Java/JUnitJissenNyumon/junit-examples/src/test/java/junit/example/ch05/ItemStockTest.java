package junit.example.ch05;

import org.junit.Before;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

@RunWith(Enclosed.class)
public class ItemStockTest {

    public static class InCaseOfEmpty {
        ItemStock sut;

        @Before
        public void setUp() throws Exception {
            sut = new ItemStock();
        }

        @Test
        public void size_A_returns_0() throws Exception {
            assertThat(sut.size("A"), is(0));
        }

        @Test
        public void contains_A_returns_false() throws Exception {
            assertThat(sut.contains("A"), is(false));
        }
    }

    public static class InCaseItContainsProductA {
        ItemStock sut;

        @Before
        public void setUp() throws Exception {
            sut = new ItemStock();
            sut.add("A", 1);
        }

        @Test
        public void size_returns_1() throws Exception {
            assertThat(sut.size("A"), is(1));
        }

        @Test
        public void contains_A_returns_true() throws Exception {
            assertThat(sut.contains("A"), is(true));
        }
    }
}
