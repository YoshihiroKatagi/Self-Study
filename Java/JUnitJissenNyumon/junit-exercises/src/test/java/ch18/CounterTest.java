package ch18;

import org.junit.Before;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

@RunWith(Enclosed.class)
public class CounterTest {
    public static class InitialCase {
        Counter sut;

        @Before
        public void setUp() { sut = new Counter(); }

        @Test
        public void get_1() {
            assertThat(sut.increment(), is(1));
        }
    }

    public static class increment_once {
        Counter sut;

        @Before
        public void setUp() {
            sut = new Counter();
            sut.increment();
        }

        @Test
        public void  get_2() {
            assertThat(sut.increment(), is(2));
        }
    }

    public static class increment_50_times {
        Counter sut;

        @Before
        public void setUp() {
            sut = new Counter();
            for (int i = 0; i < 50; i++) sut.increment();
        }

        @Test
        public void get_51() {
            assertThat(sut.increment(), is(51));
        }
    }
}
