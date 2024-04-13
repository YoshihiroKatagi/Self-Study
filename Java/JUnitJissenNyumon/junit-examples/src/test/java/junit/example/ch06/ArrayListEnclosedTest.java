package junit.example.ch06;

import org.junit.Before;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

import java.util.ArrayList;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

@RunWith(Enclosed.class)
public class ArrayListEnclosedTest {

    public static class InCaseListIsAdded1Data {
        private ArrayList<String> sut;

        @Before
        public void setUp() throws Exception {
            sut = new ArrayList<String>();
            sut.add("A");
        }

        @Test
        public void size_returns_1() throws Exception {
            int actual = sut.size();
            assertThat(actual, is(1));
        }
    }

    public static class InCaseListIsAdded2Data {
        private ArrayList<String> sut;

        @Before
        public void setUp() throws Exception {
            sut = new ArrayList<String>();
            sut.add("A");
            sut.add("B");
        }

        @Test
        public void size_returns_2() throws Exception {
            int actual = sut.size();
            assertThat(actual, is(2));
        }
    }
}
